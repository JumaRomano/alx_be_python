# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    """Calculate and return a future date based on the number of days to add."""
    current_date = datetime.now()  # Get the current date
    future_date = current_date + timedelta(days=days)  # Calculate future date
    return future_date.strftime("%Y-%m-%d")  # Format the future date

def main():
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Prompt user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = calculate_future_date(days_to_add)
        print(f"Future date: {future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
