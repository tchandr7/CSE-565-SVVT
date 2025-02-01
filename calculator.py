class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        self.result = a / b
        return self.result

    def exponent(self, a, b):
        self.result = a ** b
        return self.result


def main():
    calc = Calculator()

    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            continue

        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if choice == '1':
            print(f"Result: {calc.add(a, b)}")
        elif choice == '2':
            print(f"Result: {calc.subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {calc.multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {calc.divide(a, b)}")
        elif choice == '5':
            print(f"Result: {calc.exponent(a, b)}")


if __name__ == "__main__":
    main()
