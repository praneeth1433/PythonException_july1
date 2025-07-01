'''

1. User Input Validation System

Build a script that takes user inputs (name, age, email).
— Handle empty input
— Raise ValueError for invalid age (<0)
— Raise custom exception for invalid email (no ‘@’)
'''
from logging import exception

try:
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    email = input('Enter your email: ')

    if name == '' or age == '' or email == '':
        raise ValueError('input cannot be empty')

    age = int(age)
    if age < 0:
        raise ValueError('age cannot be negative')

    if '@' not in email:
        raise ValueError("Invalid Email: '@' symbol is missing")

    print('Name:', name)
    print('Age:', age)
    print('Email:', email)

except ValueError as e:
    print('ValueError', e)
else:
    print('Success')
finally:
    print('Data Uploaded')

'''
File Reader Tool

Build a function that opens a file and reads its content.
— Handle FileNotFoundError if the file doesn’t exist
— Handle PermissionError for restricted files
— Use finally to always close the file

'''

def readFile(filename):
    try:
        f = open(filename, 'r')
        print(f.read())

    except FileNotFoundError:
        print('File Not Found')

    except PermissionError:
        print('No permission to read this file')
    finally:
        try:
            f.close()
            print('File Closed')
        except:
            print('File not opened')

filenames=input('Enter file name: ')
readFile(filenames)


'''
3. Safe Division Function

Write a safe_divide(a, b) function that:
— Catches ZeroDivisionError
— Catches TypeError if a or b are not numbers
— Logs errors and returns meaningful messages

'''

def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return 'Can not divide by zero'
    except TypeError:
        return 'Inputs must be numbers'

print(safe_division(2,3))
print(safe_division(20,0))

'''
4.API Request Handler (Mock Project)

Simulate an API call using a function.
— Raise exception for invalid endpoint
— Handle timeout with a custom TimeoutError
— Use try-except-finally to manage connection lifecycle

'''

'''
5. Dictionary Data Fetcher

Fetch a value from a dictionary by key.
— Handle KeyError and return a default message
— Log access errors for missing keys
— Raise exception if dictionary is empty
'''

def fetch_value(data,key):
    try:
        if data=={}:
            raise Exception("Dictionary is empty")
        return data[key]

    except KeyError:
        print(f"log: '{key}' not found")
        return "key not found"
    except Exception as e:
        return str(e)

dict = {"name":'praneeth','age':25}

print(fetch_value(dict,'name'))
print(fetch_value(dict,'email'))
print(fetch_value({},'age'))


'''
6.  File Upload Validator

Validate file format and size.
— Raise ValueError for unsupported formats (e.g., .exe)
— Raise custom FileTooLargeException if size > 5MB
— Catch both and return meaningful feedback
'''

def validate_file(file_name,file_size):
    try:
        if file_name.endswith('.exe'):
            raise ValueError('.exe files are not allowed')

        if file_size > 5:
            raise Exception('File size cannot be greater than 5mb')

        return "File is valid"

    except ValueError as e:
        return f"ValueError: {e}"

    except Exception as e:
        return f"Error: {e}"


print(validate_file('demo.py',3))
print(validate_file('demo.py',10))
print(validate_file('demo.exe',3))


'''
7. Student Grade Calculator

Read marks from user, compute grade.
— Handle non-integer input (ValueError)
— Handle marks outside valid range (0–100)
— Raise custom exceptions for invalid scores

'''

def grade_calculator():
    try:
        marks = input('Enter marks out of 100: ')
        marks = int(marks)

        if marks < 0 or marks > 100:
            raise Exception('marks must be between 0 and 100')

        if marks >= 90:
            return "Grade: A"
        if marks >= 70:
            return "Grade: B"
        if marks >= 50:
            return "Grade: C"
        if marks >= 40:
            return "Grade: D"
        else:
            return "Fail"

    except ValueError:
        return "Please enter a numbers"
    except Exception as e:
        return f"Error: {e}"

print(grade_calculator())
print(grade_calculator())
print(grade_calculator())


'''
8. Database Connection Simulator

Simulate a DB connection (no real DB needed).
— If credentials are wrong, raise PermissionError
— If DB not found, raise ConnectionError
— Use finally block to ‘close’ the connection

'''

def connect_db(username,password,db_name):
    try:
        print('Connecting to DB')

        if username != 'praneeth' or password != '9999':
            raise PermissionError('Invalid username or password')

        if db_name == 'demo':
            raise ConnectionError('DB not found')

        print('Successfully connected to DB',db_name)

    except PermissionError as e:
        print("permissionError",e)
    except Exception as ee:
        print("Connection error",ee)
    finally:
        print("Connection closed")

connect_db('praneeth','9999','demo')
connect_db('praneeth','9911','demo')
connect_db('praneeth','9999','dbms')