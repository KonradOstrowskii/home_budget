Home Budget Tracker
This is a simple program for tracking and managing a home budget. The program allows users to add and remove expenses and view a summary of their budget by category.

Features
Add and remove expenses
View summary of budget by category
Save and load budget data from an Excel file
Requirements
Python 3.6 or higher
pandas library
Usage
To use the program, first create an instance of the Budget class:


budget = Budget()
The Budget class has the following methods:

add_expense(category, amount): Add an expense to the budget. category is the category of the expense (e.g. "Rent", "Utilities", etc.), and amount is the cost of the expense.
remove_expense(category, amount): Remove an expense from the budget. category is the category of the expense, and amount is the cost of the expense.
save(file_name): Save the budget data to an Excel file. file_name is the name of the Excel file to save to (e.g. "budget.xlsx").
open(file_name): Load the budget data from an Excel file. file_name is the name of the Excel file to load from (e.g. "budget.xlsx").
<img width="835" alt="Zrzut ekranu 2023-01-04 o 15 41 06" src="https://user-images.githubusercontent.com/97406457/210580216-bef86104-9418-46e2-8571-c1fed9b6109c.png">
