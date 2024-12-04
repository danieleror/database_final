import input_validation as inpt
import pandas as pd
import numpy as np
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
        response = inpt.get_integer_input('Please enter a value 1-4:')
        while not 1 <= response <= 4:
            print('ERROR: Response out of range!')
            response = inpt.get_integer_input('Please enter a value 1-4:')

        # sales menu
        if response == 1:
            print('1) View all sales\n'
                  '2) Modify sale\n'
                  '3) Delete sale\n'
                  '4) Exit to main menu')

            # gets choice from user
            response = inpt.get_integer_input('Please enter a value 1-4:')
            while not (1 <= response <= 4):
                print('ERROR: Input out of range!')
                response = inpt.get_integer_input('Please enter a value 1-4:')

            if response == 1:  # view all sales
                # retrieves all database info and stores it into variable
                sales = pd.read_sql('SELECT * FROM (sale_info CROSS JOIN sale_orders USING(sale_id)) '
                                    'CROSS JOIN products USING(product_sku) '
                                    'CROSS JOIN customers USING(customer_id);', connection).values

                sale_ids_printed = []
                for sale in sales:
                    if not sale[0] in sale_ids_printed:
                        # prints header for sale
                        sale_ids_printed.append(sale[0])
                        print(f'-------------------------------------------------\n'
                              f'Sale ID: {sale[0]}\n'
                              f'Total Amount: ${sale[1]}\n'
                              f'Date ordered: {sale[2]}\n'
                              f'Status: {sale[3]}\n'
                              f'CUSTOMER INFO:\n'
                              f'    ID: {sale[4]}\n'
                              f'    Name: {sale[10]}\n'
                              f'    Phone: {sale[11]}\n'
                              f'    Email: {sale[12]}\n'
                              f'    Address: {sale[13]}\n'
                              f'ORDER CONTENTS:')

                    # prints each product order in sale
                    print(f'    {sale[7]:8<} - {sale[6]:4<}x {sale[8]:<20} @ ${sale[9]}')

                print('-------------------------------------------------')
            elif response == 2:  # modify sale

                print()
            elif response == 3:  # delete sale
                print()

            # no else, program automatically returns to main menu
        # customer menu
        elif response == 2:
            print('Customers currently in system:')

            # displays customers to user
            customers = pd.read_sql('SELECT * FROM customers;', connection).values
            print('ID  Name            Phone         Email                    Address')
            for customer in customers:
                print(f'{customer[0]:<4}{customer[1]:16}{customer[2]:14}{customer[3]:25}{customer[4]}')

            # gives user option to add/modify or go back to main menu
            print('Options:\n'
                  '1) Add new customer\n'
                  '2) Edit existing customer info\n'
                  '3) Delete Customer\n'
                  '4) Show customer order history\n'
                  '5) Exit to main menu')
            response = inpt.get_integer_input('Please enter a value 1-4:')
            if not (1 <= response <= 5):
                print('ERROR: Response out of range!')
                response = inpt.get_integer_input('Please enter a value 1-4:')
            if response == 1:  # user wants to add new customer
                new_customer_id = customers[len(customers) - 1][0] + 1  # new id is 1 more than current highest

                # gets  customer name from user
                new_customer_name = input('Please enter the new customer\'s name:')
                while len(new_customer_name) < 5 or '"' in new_customer_name:
                    # informs user to enter a longer name and to avoid quotes as
                    # they can cause issues when executing the sql script
                    new_customer_name = input('Name must be at least 5 characters, and must not include quotes:')

                # gets customer's phone number from user
                new_customer_phone = inpt.get_phone_number_input('Please enter customer\'s phone number (XXX-XXX-XXXX):')

                # gets customer's email from user
                new_customer_email = inpt.get_email_input('Please enter customer\'s email (xxx@xxx.xxx):')

                # gets customer's address from user
                new_customer_address = input('Please enter customer\'s address:')
                while len(new_customer_address) == 0:
                    new_customer_address = input('ERROR: No entry given. Please enter customer\'s address:')

                # inserts data into new record
                cursor.execute('''INSERT INTO customers VALUES(''' + str(new_customer_id) + ''', "'''
                               + new_customer_name + '''", "'''
                               + str(new_customer_phone) + '''", "'''
                               + new_customer_email + '''", "'''
                               + new_customer_address + '''");''')
                print('New customer successfully saved!')
            elif response == 2:  # user wants to modify existing customer's info
                # gets id of customer info to modify
                id_to_modify = inpt.get_integer_input('Please enter the ID of the customer who\'s info you\'d like'
                                                      'to modify:')
                while not 1 <= id_to_modify <= len(customers):
                    print('ERROR: Customer-ID not found!')
                    id_to_modify = inpt.get_integer_input('Please enter the ID of the customer who\'s info you\'d like'
                                                          'to modify:')

                # gets new value for customer's name (may not change)
                new_name = customers[id_to_modify - 1][1]
                if inpt.get_yes_no_input('Would you like to change the customer\'s name? (y/n)'):
                    new_name = input('Please enter customer\'s new name:')
                    while len(new_name) < 5 or '"' in new_name:
                        new_name = input('Name must be at least 5 characters, and must not include quotes:')

                # gets new value for customer's phone number (may not change)
                new_number = customers[id_to_modify - 1][2]
                if inpt.get_yes_no_input('Would you like to change the customer\'s phone number? (y/n)'):
                    new_number = inpt.get_phone_number_input('What would you like the new number to be?')

                # gets new value for customer's email (may not change)
                new_email = customers[id_to_modify - 1][3]
                if inpt.get_yes_no_input('Would you like to change the customer\'s email? (y/n)'):
                    new_price = inpt.get_float_input('Please enter new email:')

                # gets new value for customer's address (may not change)
                new_address = customers[id_to_modify - 1][4]
                if inpt.get_yes_no_input('Would you like to change the customer\'s address? (y/n)'):
                    new_address = input('Please enter new address:')
                    while len(new_address) == 0:
                        new_address = input('ERROR: No entry given. Please enter customer\'s address:')

                # updates record with new information from user
                cursor.execute('''UPDATE customers SET name="''' + new_name + '''", 
                        phone="''' + str(new_number) + '''", 
                        email="''' + new_email + '''", 
                        address="''' + new_address + '''"
                        WHERE customer_id=''' + str(id_to_modify) + ''';''')

            elif response == 3:
                # gets an id that exists from the user
                id_to_delete = inpt.get_integer_input('Enter the ID of the customer you wish to delete:')
                valid_id = False
                while not valid_id:
                    for customer in customers:
                        if id_to_delete == customer[0]:
                            valid_id = True

                    if not valid_id:
                        print('ERROR: Customer-ID not found, please try again...')
                        id_to_delete = inpt.get_integer_input('Enter the ID of the customer you wish to delete:')

                sale_exists = False
                sale_info = pd.read_sql('SELECT * FROM sale_info;', connection).values
                for sale in sale_info:
                    if sale[4] == id_to_delete:
                        sale_exists = True

                if sale_exists:
                    print('ERROR: Unable to complete operation because there is at least 1 sale associated with this\n'
                          'customer. Associated sales must be deleted prior to deleting this customer.')
                else:  # valid sku and no associated sales exist, so product can be deleted
                    cursor.execute('''DELETE FROM customers WHERE customer_id=''' + str(id_to_delete) + ''';''')

            elif response == 4:  # user wants to view all sales for a specific customer
                # gets an id that exists from the user
                customer_id = inpt.get_integer_input('Enter the ID of the customer who\'s sales you\'d like to view:')
                valid_id = False
                while not valid_id:
                    for customer in customers:
                        if customer_id == customer[0]:
                            valid_id = True

                    if not valid_id:
                        print('ERROR: Customer-ID not found, please try again...')
                        id_to_delete = inpt.get_integer_input('Enter the ID of the customer who\'s sales you\'d like '
                                                              'to view:')
                # gets all sales that match this customer
                sales = pd.read_sql('SELECT * FROM (sale_info CROSS JOIN sale_orders USING(sale_id)) '
                                    'CROSS JOIN products USING(product_sku) '
                                    'WHERE customer_id=' + str(customer_id) + ';', connection).values
                if len(sales) == 0:
                    print('Selected customer has no sales in system.')
                else:  # will iterate through each sale
                    sale_ids_used = []
                    for sale in sales:
                        if not sale[0] in sale_ids_used:
                            # adds sale id to used ids and prints header for each individual sale
                            sale_ids_used.append(sale[0])
                            print(f'-------------------------------------------------\n'
                                  f'Sale ID: {sale[0]}\n'
                                  f'Total Amount: ${sale[1]}\n'
                                  f'Date Ordered: {sale[2]}\n'
                                  f'Status: {sale[3]}\n'
                                  f'ORDER CONTENTS:')

                        print(f'    {sale[7]:8<} - {sale[6]:4<}x {sale[8]:<20} @ ${sale[9]}')

                    print('-------------------------------------------------\n'
                          'Total sales found: ' + str(len(sale_ids_used)))

            # no else needed, program automatically returns to main menu

        # products menu
        elif response == 3:
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
                  '3) Delete product\n'
                  '4) Exit to main menu')
            response = inpt.get_integer_input('Please enter a value 1-4:')
            if not (1 <= response <= 4):
                print('ERROR: Response out of range!')
                response = inpt.get_integer_input('Please enter a value 1-4:')
            if response == 1:  # user wants to add new product
                new_product_sku = products[len(products) - 1][0] + 1  # new sku is 1 more than current highest

                # gets new product name from user
                new_product_name = input('Please enter the new product\'s name:')
                while len(new_product_name) < 10 or '"' in new_product_name:
                    # informs user to choose a lengthy name and to avoid quotes as
                    # they can cause issues when executing the sql script
                    new_product_name = input('Name must be at least 10 characters, and must not include quotes:')

                # gets new product price from user, and rounds it to 2 decimal places
                new_product_price = round(inpt.get_float_input('Please enter the new product\'s price:'), 2)

                # inserts data into new record
                cursor.execute('''INSERT INTO products VALUES(''' + str(new_product_sku) + ''', "'''
                                                                  + new_product_name + '''", '''
                                                                  + str(new_product_price) + ''');''')
                print('New product successfully added!')
            elif response == 2:  # user wants to modify existing product
                # gets sku of product to modify
                sku_to_modify = inpt.get_integer_input('Please enter the SKU of the product to modify:')
                while not 1 <= sku_to_modify <= len(products):
                    print('ERROR: SKU not available!')
                    sku_to_modify = inpt.get_integer_input('Please enter the SKU of the product to modify:')

                # gets new value for product name (may not change)
                new_name = products[sku_to_modify-1][1]
                if inpt.get_yes_no_input('Would you like to change the product\'s name? (y/n)'):
                    new_name = input('What would you like the new name to be?')
                    while len(new_name) < 10 or '"' in new_name:
                        new_name = input('Name must be at least 10 characters, and must not include quotes:')

                # gets new value to product price (may not change)
                new_price = products[sku_to_modify-1][2]
                if inpt.get_yes_no_input('Would you like to change the product\'s price? (y/n)'):
                    new_price = inpt.get_float_input('What would you like the new price to be?')

                # updates record with new information from user
                cursor.execute('''UPDATE products SET name="''' + new_name + '''", 
                        price=''' + str(new_price) + ''' WHERE product_sku=''' + str(sku_to_modify) + ''';''')

            elif response == 3:  # delete product
                # gets a sku that exists from the user
                sku_to_delete = inpt.get_integer_input('Enter the SKU of the product you wish to delete:')
                valid_sku = False
                while not valid_sku:
                    for product in products:
                        if sku_to_delete == product[0]:
                            valid_sku = True

                    if not valid_sku:
                        print('ERROR: SKU not found, please try again...')
                        sku_to_delete = inpt.get_integer_input('Enter the SKU of the product you wish to delete:')

                sale_exists = False
                sale_orders = pd.read_sql('SELECT * FROM sale_orders;', connection).values
                for sale in sale_orders:
                    if sale[1] == sku_to_delete:
                        sale_exists = True

                if sale_exists:
                    print('ERROR: Unable to complete operation because there is at least 1 sale associated with this\n'
                          'product. Associated sales must be deleted prior to deleting this product.')
                else:  # valid sku and no associated sales exist, so product can be deleted
                    cursor.execute('''DELETE FROM products WHERE product_sku=''' + str(sku_to_delete) + ''';''')

            # no else needed, program automatically returns to main menu

        # program exit
        else:
            running = False

    print('Program terminating...')
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
