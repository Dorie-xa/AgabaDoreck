#Contact management system 
import sqlite3
import re

#  Database setup
def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect("contacts.db")
    conn.row_factory = sqlite3.Row          
    return conn


def create_table():
    """Create the contacts table if it does not already exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT    NOT NULL,
                phone   TEXT    NOT NULL,
                email   TEXT
            )
        """)


# Validation helpers

def is_valid_phone(phone: str) -> bool:
    """
    Return True when *phone* contains only digits, hyphens, and an
    optional leading '+'.  Examples that pass: +256-701-123456, 0701-123456
    """
    return bool(re.fullmatch(r"[+]?[\d\-]+", phone))


def is_valid_email(email: str) -> bool:
    """
    Return True when *email* contains both '@' and '.'.
    An empty / None value is also accepted (email is optional).
    """
    if not email:
        return True
    return "@" in email and "." in email


def add_contact(name: str, phone: str, email: str = "") -> None:
    """Insert a new contact after validating phone and email."""
    if not is_valid_phone(phone):
        print(
            f"  [ERROR] Invalid phone number '{phone}'.\n"
            "          Only digits, hyphens, and a leading '+' are allowed "
            "(e.g. +256-701-123456)."
        )
        return

    
    if not is_valid_email(email):
        print(
            f"  [ERROR] Invalid email address '{email}'.\n"
            "          An email must contain '@' and '.'."
        )
        return

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email or None),
        )
    print(f"  [OK] Contact '{name}' added successfully.")


def view_contact(contact_id: int) -> None:
    """Print a single contact by its ID."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM contacts WHERE id = ?", (contact_id,)
        ).fetchone()

    if row:
        _print_contact(row)
    else:
        print(f"  [INFO] No contact found with ID {contact_id}.")


def update_contact(
    contact_id: int,
    name: str = None,
    phone: str = None,
    email: str = None,
) -> None:
    """Update one or more fields of an existing contact."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM contacts WHERE id = ?", (contact_id,)
        ).fetchone()

    if not row:
        print(f"  [INFO] No contact found with ID {contact_id}.")
        return

    # Fall back to the stored value when the caller passes nothing
    new_name  = name  if name  is not None else row["name"]
    new_phone = phone if phone is not None else row["phone"]
    new_email = email if email is not None else row["email"]

    # validate phone 
    if not is_valid_phone(new_phone):
        print(
            f"  [ERROR] Invalid phone number '{new_phone}'.\n"
            "          Only digits, hyphens, and a leading '+' are allowed."
        )
        return

    #  validate email 
    if not is_valid_email(new_email):
        print(
            f"  [ERROR] Invalid email address '{new_email}'.\n"
            "          An email must contain '@' and '.'."
        )
        return

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE contacts
               SET name = ?, phone = ?, email = ?
             WHERE id   = ?
            """,
            (new_name, new_phone, new_email, contact_id),
        )
    print(f"  [OK] Contact ID {contact_id} updated successfully.")


def delete_contact(contact_id: int) -> None:
    """Remove a contact by its ID."""
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM contacts WHERE id = ?", (contact_id,)
        )

    if cursor.rowcount:
        print(f"  [OK] Contact ID {contact_id} deleted.")
    else:
        print(f"  [INFO] No contact found with ID {contact_id}.")


def list_all_contacts() -> None:
    """Print every contact in the database."""
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM contacts ORDER BY name").fetchall()

    if not rows:
        print("  [INFO] No contacts found.")
        return

    print(f"\n  {'─'*52}")
    print(f"  {'ID':<5} {'Name':<20} {'Phone':<18} {'Email'}")
    print(f"  {'─'*52}")
    for row in rows:
        print(
            f"  {row['id']:<5} {row['name']:<20} "
            f"{row['phone']:<18} {row['email'] or '—'}"
        )
    print(f"  {'─'*52}")
    print(f"  {len(rows)} contact(s) listed.\n")


#  Advanced search

def search_contacts(query: str) -> None:
    """
    Search contacts by name, phone **or email** (Task 2).
    Results are displayed in a clean, formatted table.
    """
    pattern = f"%{query}%"
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT * FROM contacts
             WHERE name  LIKE ?
                OR phone LIKE ?
                OR email LIKE ?
            ORDER BY name
            """,
            (pattern, pattern, pattern),
        ).fetchall()

    print(f"\n  Search results for '{query}':")
    if not rows:
        print("  No matching contacts found.")
        return

    print(f"  {'─'*52}")
    print(f"  {'ID':<5} {'Name':<20} {'Phone':<18} {'Email'}")
    print(f"  {'─'*52}")
    for row in rows:
        print(
            f"  {row['id']:<5} {row['name']:<20} "
            f"{row['phone']:<18} {row['email'] or '—'}"
        )
    print(f"  {'─'*52}")
    print(f"  {len(rows)} result(s) found.\n")

# helper
def _print_contact(row) -> None:
    """Pretty-print a single contact row."""
    print(f"\n  {'─'*36}")
    print(f"  ID    : {row['id']}")
    print(f"  Name  : {row['name']}")
    print(f"  Phone : {row['phone']}")
    print(f"  Email : {row['email'] or '—'}")
    print(f"  {'─'*36}\n")

#CLI Menu
def _prompt(label: str, required: bool = True) -> str:
    """Read a non-empty string from the user."""
    while True:
        value = input(f"  {label}: ").strip()
        if value or not required:
            return value
        print(f"  [ERROR] {label} cannot be empty.")


def _prompt_optional(label: str) -> str:
    """Read an optional string (may be blank)."""
    return input(f"  {label} (optional, press Enter to skip): ").strip()


def _prompt_int(label: str):
    """Read an integer from the user, returning None on invalid input."""
    raw = input(f"  {label}: ").strip()
    try:
        return int(raw)
    except ValueError:
        print(f"  [ERROR] '{raw}' is not a valid number.")
        return None


def main() -> None:
    """Interactive CLI loop for the Contact Manager."""
    create_table()

    menu = """

   === Contact Manager ===   
   1. Add Contact             
   2. View Contact             
   3. Update Contact           
   4. Delete Contact          
   5. Search Contacts          
   6. List All Contacts       
   7. Exit                     
"""

    while True:
        print(menu, flush=True)
        choice = input("  Choose an option (1-7): ").strip()
        print() 

        try:
         if choice == "1":
            print("\n  -- Add Contact --")
            name  = _prompt("Name")
            phone = _prompt("Phone (e.g. +256-701-123456)")
            email = _prompt_optional("Email")
            add_contact(name, phone, email)

         elif choice == "2":
            print("\n  -- View Contact --")
            cid = _prompt_int("Contact ID")
            if cid is not None:
                view_contact(cid)

         elif choice == "3":
            print("\n  -- Update Contact --")
            cid = _prompt_int("Contact ID to update")
            if cid is None:
                continue
            print("  (Press Enter to keep the current value.)")
            name  = input("  New Name  : ").strip() or None
            phone = input("  New Phone : ").strip() or None
            email = input("  New Email : ").strip() or None
            update_contact(cid, name, phone, email)

         elif choice == "4":
            print("\n  -- Delete Contact --")
            cid = _prompt_int("Contact ID to delete")
            if cid is not None:
                confirm = input(
                    f"  Are you sure you want to delete ID {cid}? (y/n): "
                ).strip().lower()
                if confirm == "y":
                    delete_contact(cid)
                else:
                    print("  [INFO] Deletion cancelled.")

         elif choice == "5":
            print("\n  -- Search Contacts --")
            query = _prompt("Search term (name, phone, or email)")
            search_contacts(query)

         elif choice == "6":
            print("\n  -- All Contacts --")
            list_all_contacts()

         elif choice == "7":
            print("\n  Goodbye!\n")
            break

         else:
            print("  [ERROR] Invalid option. Please enter a number from 1 to 7.")

        except Exception as e:
            print(f"\n  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
            print("  Please try again.\n")


if __name__ == "__main__":
    main()