📘 Error Handling in Python – README
📂 File Name

error_handling.py

🎯 Objective

This program demonstrates error handling in Python using:

try-except blocks

Multiple exception handling

else and finally blocks

Logging errors to a file

Custom exceptions

Runtime error simulation

🛠️ Modules Used

logging – to record error messages into a log file

📌 Features Explained
1. Try-Except Blocks

Used to catch runtime errors and prevent program crashes.

2. Multiple Exception Handling

Handles different errors such as:

ZeroDivisionError

TypeError

IndexError

3. Else Block

Executes when no exception occurs.

4. Finally Block

Executes every time, whether an error occurs or not.

5. Logging Errors

Errors are logged using the logging module for debugging.

6. Log File Creation

All errors are saved in:

error_log.txt

7. Custom Exception

A user-defined exception NegativeNumberError is created to handle negative input values.

8. Runtime Error Simulation

An IndexError is intentionally generated to show how runtime errors are handled.

▶️ How to Run the Program
python error_handling.py

📄 Output

Displays error messages on the console

Stores error details with timestamps in error_log.txt
