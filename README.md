
# Home Budget Tracker

This is a simple program for tracking and managing a home budget. The program allows users to add and remove expenses, view a summary of their budget by category, and save and load budget data from an Excel file.

## Features

- Add and remove expenses
- View summary of budget by category
- Save and load budget data from an Excel file
## Usage

Usage
To use the program, first create an instance of the Budget class:

Copy code
budget = Budget(categories)


The Budget class has the following methods:

- add(category, amount): Add an expense to the budget. category is the category of the expense (e.g. "Rent", "Utilities", etc.), and amount is the cost of the expense.
- remove(category, amount): Remove an expense from the budget. category is the category of the expense, and amount is the cost of the expense.
- save(file_name): Save the budget data to an Excel file. file_name is the name of the Excel file to save to (e.g. "budget.xlsx").
- open(file_name): Load the budget data from an Excel file. file_name is the name of the Excel file to load from (e.g. "budget.xlsx").
- transaction_history(): View the transaction history of the budget.
- count(): Count the total expenses in a chosen category.
## Run

- To run the program, call the main() function. This will prompt the user to select an action (add, remove, save, open, transaction history, or count) and then execute the chosen action.
<img width="835" alt="Zrzut ekranu 2023-01-04 o 15 41 06" src="https://user-images.githubusercontent.com/97406457/210580216-bef86104-9418-46e2-8571-c1fed9b6109c.png">
