# Final Project - Camera Shop Data System
### by Daniel Eror

## Setup
Be sure that `camera_shop.py`, `input_validation.py`, and `dans_camera_shop.db` are all in the same directory. Then, 
simply run `camera_shop.py` either in an IDE or through the terminal. This program's user interface is entirely through
the terminal, and all directions are given therein. 

___NOTE:___ if you want to save changes to the database, be sure you exit 
the program through the menu options. If you terminate the program by typing CTRL+C or clicking STOP in the IDE, any 
changes you make will not be saved in the database file. 

## Overview
To simplify input validation, I created a python file to store some functions that I knew I would use repeatedly in my 
program. This includes functions that get dates, phone numbers, integers, and more from the user. 

For the main functionality of the program, there are several nested loops, and tons of nested if statements. This all 
combines to create the user interface, which contains several menus, and different options within those menus. I use 
sqlite to perform all database operations, and some pandas/numpy for retrieving information to show to the user. At the 
end of my program, sqlite saves all changes made into the database file, so it is stored long-term. 

All data was fabricated by myself. I actually wrote the majority of the program first, and then killed two birds with 
one stone, by using my program to add data to my database, while debugging/troubleshooting at the same time to find 
issues. My input validation ensured that all data entered into the database is clean. 

I use CROSS JOIN operations throughout my program to combine related data. Also, I prevent the user from deleting any
data that would cause errors with related data. Specifically, if a user tries to delete a product or customer that is 
associated with a sale, the operation is stopped and the program informs the user that they need to delete the 
associated first. When a user deletes a sale, that sale is deleted from the sale_info table, and also all orders with 
that ID are deleted from the sale_orders table. 