# Real World application for loop control statements
# World Cup 2026 winner predictor 

countries = ["Argentina", "Brazil", "France", "Germany", "Spain", "England", "Netherlands"]

print("Welcome to World Cup 2026 Predictor!")
print("=" * 50)

show_help = True
while True:
    if show_help:
        print("\nAvailable commands:")
        print("  'list'  - Show all countries")
        print("  'exit'  - Quit program")
        print("  Or enter a country name to check\n")
        show_help = False
    
    try:
        user_input = input("Enter a country (or command): ").strip()
        
        # Input validation
        if not user_input:
            print("⚠️ Please enter something.")
            continue
        
        if user_input.lower() == "exit":
            print("Thanks for playing!")
            break
        
        elif user_input.lower() == "list":
            print("\nCountries that can win the world cup 2026:")
            for i, country in enumerate(countries, 1): 
                print(f"  {i}. {country}") 
            continue
        
        # Case-insensitive country check
        elif user_input.title() in countries:
            print(f"✅ {user_input.title()} has a chance to win the world cup 2026!")
        
        else:
            print(f"❌ {user_input} is not on the list.")
            print("Tip: Type 'list' to see all countries.")
    
    except KeyboardInterrupt:
        pass  # User pressed Ctrl+C, continue gracefully
        print("\nExiting...")
        break