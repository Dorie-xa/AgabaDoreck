#Task scheduler
import random
import time
from datetime import datetime, timedelta

def generate_mock_tasks(n=100000):
    random.seed(42)
    names = [f"Task_{i}" for i in range(n)]
    priorities = [random.randint(1, 5) for _ in range(n)]
    base = datetime(2026, 6, 19)
    deadlines = [(base + timedelta(days=random.randint(-5, 30))).strftime("%Y-%m-%d") for _ in range(n)]
    return [{"name": n, "priority": p, "deadline": d} for n, p, d in zip(names, priorities, deadlines)]


_index = {}

def build_index(tasks):
    for task in tasks:
        _index[task["name"]] = task
    return _index


def search_task(tasks, keyword):
    if keyword not in _index:
        build_index(tasks)
    return _index.get(keyword)


def sort_tasks_by_priority(tasks):
    for task in tasks:
        task["deadline_dt"] = datetime.strptime(task["deadline"], "%Y-%m-%d")
    return sorted(tasks, key=lambda t: (t["priority"], t["deadline_dt"]))


def due_in_3_days(tasks):
    now = datetime(2026, 6, 19)
    end = now + timedelta(days=3)
    return [t for t in tasks if now <= t.get("deadline_dt", datetime.strptime(t["deadline"], "%Y-%m-%d")) <= end]


def get_time_taken(tasks=None):
    times = {}

    start = time.perf_counter()
    sorted_tasks = sort_tasks_by_priority(tasks)
    times["sort"] = time.perf_counter() - start

    idx = build_index(tasks)

    start = time.perf_counter()
    search_task(tasks, "Task_50000")
    times["search"] = time.perf_counter() - start

    return times


if __name__ == "__main__":
    tasks = generate_mock_tasks()

    build_index(tasks)

    result = search_task(tasks, "Task_50000")
    print(f"Search result: {result}")

    sorted_tasks = sort_tasks_by_priority(tasks)
    print(f"Sorted by priority: {sorted_tasks[0]['name']} (priority {sorted_tasks[0]['priority']})")
    print(f"Sorted by priority: {sorted_tasks[-1]['name']} (priority {sorted_tasks[-1]['priority']})")

    due = due_in_3_days(tasks)
    print(f"Tasks due in 3 days: {len(due)}")

    times = get_time_taken(tasks)
    print(f"Time taken - sort: {times['sort']:.4f}s, search: {times['search']:.4f}s")