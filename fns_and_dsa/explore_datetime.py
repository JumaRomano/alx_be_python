from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it as "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a future date
def calculate_future_date(days_to_add):
    current_date = datetime.now()  # Get the current date
    future_date = current_date + timedelta(days=days_to_add)  # Add the specified number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format as "YYYY-MM-DD"
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()

    # Prompt the user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()

