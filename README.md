# project-capstone-modul-1-purwadhika
## Simple mini shop using python program

Documentation for Python Program: Toko Elektronik
Purpose:

This Python program simulates a basic inventory management system for an electronics store. It allows users to view product information, filter and sort products, add products to a shopping cart, and remove products from the cart. The program also allows users to log in as either an administrator or a customer.

Objective Users:

Customers: Can view product information, filter and sort products, add products to a shopping cart, and remove products from the cart.
Administrators: Can perform all of the actions that customers can, as well as add new products to the inventory, update existing product information, and remove products from the inventory.
How to Use:
run main.py

Select your role:

Customer: Choose option 1 to log in as a customer.
Administrator: Choose option 2 to log in as an administrator.
Navigate the menu:
Once you are logged in, you will be presented with a menu of options. Follow the prompts to perform the desired actions.

Additional Information:

The program uses a list of dictionaries to store product information. Each dictionary contains the following keys:

No: A unique identifier for the product
Product Id: A random number generated for each product
Year: The year the product was released
Product Name: The name of the product
Category: The category of the product (e.g., Electronics, Accessories, Wearables, etc.)
Price: The price of the product
Stock: The number of units of the product in stock
Rating: The average rating of the product
Seller: The seller of the product
The program uses a list of dictionaries to store shopping cart information. Each dictionary contains the following keys:

Product Name: The name of the product
Price: The price of the product
Seller: The seller of the product
Jumlah: The quantity of the product in the cart
The program uses a list of dictionaries to store user login information. Each dictionary contains the following keys:

Username: The username of the user
Password: The password of the user
The program uses the tabulate library to print tables of data in a formatted way.

The program uses the random library to generate random numbers for product IDs.

The program uses the input() function to get user input.

The program uses the print() function to display output to the user.
