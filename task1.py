def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Choose the conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    
    choice = int(input("Enter choice: "))
    value = float(input("Enter the temperature value: "))
    
    conversions = {
        1: celsius_to_fahrenheit,
        2: celsius_to_kelvin,
        3: fahrenheit_to_celsius,
        4: fahrenheit_to_kelvin,
        5: kelvin_to_celsius,
        6: kelvin_to_fahrenheit
    }
    
    result = conversions.get(choice, lambda x: "Invalid choice")(value)
    print("Converted Temperature:", result)

if __name__ == "__main__":
    main()
