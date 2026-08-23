from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        num = float(input("Enter a number: "))
        print(f"Square: {square(num)}")
        print(f"Is Even: {is_even(num)}")
        print(f"Fahrenheit: {celsius_to_fahrenheit(num)}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
