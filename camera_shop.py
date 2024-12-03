import input_validation as inpt
import pandas as pd
import sqlite3


def main():
    connection = sqlite3.connect('dans_camera_shop.db')
    cursor = connection.cursor()

    running = True
    while running:
        print('Welcome to Dan\'s Camera Shop! What would you like to do?')
        print('1) Sales')
        print('2) Customers')
        print('3) Products')
        print('4) Exit')
        response = inpt.get_numerical_input('Please enter a value 1-4:')
        while not 1 <= response <= 4:
            print('ERROR: Response out of range!')
            response = inpt.get_numerical_input('Please enter a value 1-4:')

        if response == 1:  # sales menu
            # TODO: implement sales menu
            print('sales menu')
        elif response == 2:  # customers menu
            # TODO: implement customers menu
            print('customers menu')
        elif response == 3:  # products menu
            # TODO: implement products menu
            print('products menu')
        else:  # program exit
            running = False

    print('Program terminating...')
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
