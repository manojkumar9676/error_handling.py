"""
error_handling.py
Demonstrates error handling in Python using try-except,
multiple exceptions, else, finally, logging, and custom errors.
"""

import logging

# --------------------------------------------------
# 5 & 6. Configure logging and save logs to a file
# --------------------------------------------------
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# Custom Exception
# --------------------------------------------------
class NegativeNumberError(Exception):
    """Raised when a negative number is provided"""
    pass


def divide_numbers(a, b):
    """Function to divide two numbers"""
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error("Division by zero error")
        print("❌ Error: Cannot divide by zero.")
    except TypeError as e:
        logging.error("Invalid data type used")
        print("❌ Error: Please enter numbers only.")
    else:
        print("✅ Division Result:", result)
    finally:
        print("🔁 Division operation completed.\n")


def check_positive(number):
    """Function to check positive number"""
    try:
        if number < 0:
            raise NegativeNumberError("Negative numbers are not allowed")
        print("✅ Number is positive:", number)
    except NegativeNumberError as e:
        logging.error(e)
        print("❌ Custom Error:", e)
    finally:
        print("🔁 Number check completed.\n")


# --------------------------------------------------
# 8. Simulate runtime errors
# --------------------------------------------------
def simulate_errors():
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # IndexError
    except IndexError as e:
        logging.error("Index out of range error")
        print("❌ Error: List index out of range.")
    finally:
        print("🔁 Runtime error simulation completed.\n")


# --------------------------------------------------
# Main Execution
# --------------------------------------------------
if __name__ == "__main__":
    divide_numbers(10, 2)      # Normal execution
    divide_numbers(10, 0)      # ZeroDivisionError
    divide_numbers(10, "a")    # TypeError

    check_positive(5)          # Valid case
    check_positive(-3)         # Custom exception

    simulate_errors()          # Runtime error
