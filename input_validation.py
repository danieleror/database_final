"""
Daniel Eror
12/5/2024

Functions to be used when input validation is needed from the command line.
Purpose is to save space in main python file, and to be easily copied and reused in other projects
that take input from the command line.
"""


# gets integer input from user
def get_integer_input(prompt) -> int:
    response = input(prompt)  # receives initial input
    casted_response = 0  # initializes variable to be returned
    valid_input = False
    while not valid_input:  # loops until a valid int input has been given
        try:
            if len(response) > 0:
                casted_response = int(response)  # attempts to cast to int
                valid_input = True
            else:  # if response is empty, inform user and try again
                print('ERROR: Please enter a value!')
                response = input(prompt)
                valid_input = False
        except ValueError:  # if casting to int failed, user is informed to try again
            print('ERROR: Input must be an integer!')
            response = input(prompt)

    return casted_response  # returns value to user


# gets float input from user
def get_float_input(prompt) -> float:
    response = input(prompt)  # receives initial input
    casted_response = 0  # initializes variable to be returned
    valid_input = False
    while not valid_input:  # loops until a valid float input has been given
        try:
            if len(response) > 0:
                casted_response = float(response)  # attempts to cast to float
                valid_input = True
            else:  # if response is empty, inform user and try again
                print('ERROR: Please enter a value!')
                response = input(prompt)
                valid_input = False
        except ValueError:  # if casting to float failed, user is informed to try again
            print('ERROR: Input must be a float!')
            response = input(prompt)

    return casted_response  # returns value to user


# gets date input int the form "MM/DD/YYYY"
def get_date_input(prompt) -> str:
    response = input(prompt)
    valid_input = False
    while not valid_input:  # loops until valid date has been entered
        if len(response) != 10 or response[2] != '/' or response[5] != '/':
            # informs user that their response did not match specified format
            print('ERROR: Date does not follow specified format!')
            response = input(prompt)
            valid_input = False
        else:
            try:
                values = response.split('/')
                month = int(values[0])
                day = int(values[1])
                year = int(values[2])
                if not (1 <= month <= 12 and 1 <= day <= 31 and 2000 <= year <= 3000):
                    # values entered are invalid. user is notified to try again
                    print('ERROR: Invalid date entered, please try again...')
                    response = input(prompt)
                    valid_input = False
                else:  # passed all tests
                    valid_input = True
            except ValueError:
                print('ERROR: Non-numerical value entered. Please try again...')
                response = input(prompt)
                valid_input = False

    return response  # returns validated date
