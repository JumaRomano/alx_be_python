# temp_conversion_tool.py

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Check if global conversion factors are defined
def check_conversion_factors():
    if FAHRENHEIT_TO_CELSIUS_FACTOR is None or CELSIUS_TO_FAHRENHEIT_FACTOR is None:
        raise ValueError("Conversion factors are not defined properly.")

# Define the conversion functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User Interaction
def main():
    # Check if conversion factors are defined
    check_conversion_factors()
    
    while True:
        try:
            temperature = input("Enter the temperature to convert (or type 'exit' to quit): ")
            if temperature.lower() == 'exit':
                print("Exiting the temperature conversion tool.")
                break
            
            temperature = float(temperature)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp:.2f}°C")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp:.2f}°F")
            else:
                raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        except ValueError as e:
            print(f"Invalid input. Please enter a numeric value. Error: {e}")

if __name__ == "__main__":
    main()
