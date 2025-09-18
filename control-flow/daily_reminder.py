def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    reminder_message = f"Note: '{task}' is a {priority} priority task."
    match priority:
        case 'high':
            reminder_message = f"Reminder: '{task}' is a high priority task"
            if time_bound == 'yes':
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += ". It should be completed as soon as possible."
        case 'medium':
            if time_bound == 'yes':
                reminder_message += " that should be done today."
            else:
                reminder_message += ". Consider completing it soon."
        case 'low':
            if time_bound == 'yes':
                reminder_message += " that you should get done today."
            else:
                reminder_message += ". Consider completing it when you have free time."
        case _:
            print("Invalid priority entered. Please choose from high, medium, or low.")
            return
    print(reminder_message)
if __name__ == "__main__":
    daily_reminder()
