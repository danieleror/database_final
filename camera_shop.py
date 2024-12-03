import input_validation as inpt
import pandas as pd
import sqlite3


def main():
    connection = sqlite3.connect('dans_camera_shop.db')
    cursor = connection.cursor()
    print('Welcome to Dan\'s Camera Shop!')
    running = True
    while running:
        print('Main menu options:')
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
            print('Products available:')

            # displays products to user
            products = pd.read_sql('SELECT * FROM products;', connection).values
            print('SKU  ITEM                          PRICE')
            for product in products:
                print(f'{product[0]:<5}{product[1]:30}{product[2]}')

            # gives user option to add/modify or go back to main menu
            print('Options:\n'
                  '1) Add new product\n'
                  '2) Edit existing product\n'
                  '3) Exit to main menu')
            response = inpt.get_numerical_input('Please enter 1, 2, or 3:')
            if not (1 <= response <= 3):
                print('ERROR: Response out of range!')
                response = inpt.get_numerical_input('Please enter 1, 2, or 3:')
            if response == 1:  # user wants to add new product
                # TODO: implement addition of new product
                print('add product here')
            elif response == 2:  # user wants to modify existing product
                # TODO: implement modification of existing product
                print('modify product here')
            # no else, program automatically returns to main menu
        else:  # program exit
            running = False

    print('Program terminating...')
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
