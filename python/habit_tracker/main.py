from datetime import date, timedelta
import json
import os

def get_today():
    return date.today().isoformat()


def get_week_dates():
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    return monday, today


def weekly_report():
    if not habits:
        print("No habits to report yet.")
        return

    start_date, end_date = get_week_dates()

    total_completions = 0
    total_possible = len(habits) * (end_date - start_date).days + len(habits)

    print("\n--- Weekly Progress Report ---")
    print(f"Week starting: {start_date}")
    print(f"Report date: {end_date}")

    results = []

    for habit in habits:
        weekly_dates = {
            date.fromisoformat(day)
            for day in habit["completed_dates"]
            if start_date <= date.fromisoformat(day) <= end_date
        }

        count = len(weekly_dates)
        total_completions += count

        results.append((habit["name"], count))

        print(f"{habit['name']}: {count} completion(s)")

    percentage = (total_completions / total_possible) * 100

    print(f"\nTotal completions: {total_completions}")
    print(f"Weekly completion rate: {percentage:.1f}%")

    most_consistent = max(results, key=lambda item: item[1])
    print(f"Most consistent habit: {most_consistent[0]}")



def calculate_current_streak(habit):

    completed_dates = set(habit["completed_dates"])

    current_day = date.today()

    # If today isn't completed, start checking from yesterday.
    if current_day.isoformat() not in completed_dates:
        current_day -= timedelta(days=1)

    streak = 0

    while current_day.isoformat() in completed_dates:

        streak += 1
        current_day -= timedelta(days=1)

    return streak


def calculate_best_streak(habit):

    completed_dates = sorted(set(habit["completed_dates"]))

    if len(completed_dates) == 0:
        return 0

    best_streak = 1
    current_streak = 1

    for i in range(1, len(completed_dates)):

        previous_day = date.fromisoformat(completed_dates[i - 1])
        current_day = date.fromisoformat(completed_dates[i])

        difference = (current_day - previous_day).days

        if difference == 1:
            current_streak += 1
        else:
            current_streak = 1

        best_streak = max(best_streak, current_streak)

    return best_streak



def save_habits():

    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)

    print("Habits saved successfully!")



def load_habits():

    if os.path.exists("habits.json"):

        try:
            with open("habits.json", "r") as file:
                data = json.load(file)

            for habit in data:
                if "completed_dates" not in habit:

                    # Old data cannot tell us the actual date.
                    # Preserve its current completed status as today.
                    if habit.get("completed", False):
                        habit["completed_dates"] = [get_today()]
                    else:
                        habit["completed_dates"] = []

                    del habit["completed"]

            return data

        except json.JSONDecodeError:
            print("Warning: Your habits file is corrupted!")
            return []

    return []





def add_habit():

    name = input("Enter habit name: ").strip()

    if name == "":
        print("Habit name cannot be empty!")
        return

    habit = {
        "name": name,
        "completed_dates": []
    }

    habits.append(habit)

    save_habits()

    print(f"'{name}' added successfully!")





def view_habits():

    if len(habits) == 0:
        print("You haven't added any habits yet!")
        return

    today = get_today()

    print("\n====== YOUR HABITS ======")

    for index, habit in enumerate(habits, start=1):

        status = (
            "Completed"
            if today in habit["completed_dates"]
            else "Not completed"
        )

        current = calculate_current_streak(habit)
        best = calculate_best_streak(habit)

        print(f"\n{index}. {habit['name']}")
        print(f"   Status: {status}")
        print(f"   Current streak: {current} days")
        print(f"   Best streak: {best} days")



def complete_habit():

    if len(habits) == 0:
        print("No habits available!")
        return

    view_habits()

    try:
        choice = int(input("\nWhich habit did you complete? "))

        if choice < 1 or choice > len(habits):
            print("Invalid habit number!")
            return

        habit = habits[choice - 1]

        today = get_today()

        if today in habit["completed_dates"]:
            print("Already completed today!")
            return

        habit["completed_dates"].append(today)

        save_habits()

        print(f"{habit['name']} completed for today!")

    except ValueError:
        print("Please enter a valid number!")


def delete_habit():

    if len(habits) == 0:
        print("There are no habits to delete!")
        return

    view_habits()

    try:
        choice = int(input("\nEnter habit number to delete: "))

        if choice < 1 or choice > len(habits):
            print("Invalid habit number!")
            return

        habit = habits[choice - 1]
        

        confirm = input(
            f"Are you sure you want to delete '{habit['name']}'? (y/n): "
        ).lower()

        if confirm == "y":
            deleted_habit = habits.pop(choice - 1)
            save_habits()
            print(f"'{deleted_habit['name']}' deleted successfully!")

        elif confirm == "n":
            print("Deletion cancelled!")

        else:
            print("Invalid confirmation!")

    except ValueError:
        print("Please enter a valid number!")



def view_statistics():

    total = len(habits)

    if total == 0:
        print("No habits available for statistics!")
        return

    today = get_today()

    completed = 0

    for habit in habits:
        if today in habit["completed_dates"]:
            completed += 1

    incomplete = total - completed

    percentage = (completed / total) * 100

    print("\n====== HABIT STATISTICS ======")
    print(f"Total habits: {total}")
    print(f"Completed today: {completed}")
    print(f"Not completed: {incomplete}")
    print(f"Completion rate: {percentage:.1f}%")

    print("\n====== STREAK STATISTICS ======")

    for habit in habits:
        current = calculate_current_streak(habit)
        best = calculate_best_streak(habit)

        print(f"\n{habit['name']}")
        print(f"Current streak: {current} days")
        print(f"Best streak: {best} days")



habits = load_habits()


while True:

    print("\n==============================")
    print("       HABIT TRACKER")
    print("==============================")

    print("1. Add a habit")
    print("2. View all habits")
    print("3. Complete a habit")
    print("4. Delete a habit")
    print("5. View statistics")
    print("6. Exit")
    print("7. Weekly Progress Report")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_habit()

    elif choice == "2":
        view_habits()

    elif choice == "3":
           complete_habit()

    elif choice == "4":
          delete_habit()

    elif choice == "5":
            view_statistics()
    elif choice == "6":
        print("Thank you for using Habit Tracker!")
        break
    elif choice == "7":
         weekly_report()

    else:
        print("Invalid choice! Please select 1-6.")
