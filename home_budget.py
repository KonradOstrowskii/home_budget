
from budget import Budget 

    
def main():
    
    # Create an instance of the Budget class with the given categories
    budget = Budget(['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Travels', 'Gifts', 'Eating Outside', 'Mortgage'])

    while True:
        available_action = ["add","remove","q","history","sum"]
        
        # Get the user's choice
        action = input('Enter "add" to add a category, "remove" to remove "history" to to see history,"sum" to sum value of a row "q" for exit : ')
                       
        if action not in available_action:
            print("This is not allowed action")
        # Add an expense from the budget
        if action == "add":
            budget.budget_category()
            try:
                category = input('Enter the category to add : ').capitalize()
                amount = int(input('Enter the amount to add : '))
                budget.add(category, amount)
                budget.save('budget.xlsx')
            except KeyError as e:
                # This code will be executed if a KeyError occurs
                print("Error: key not found in budget list")
        # Remove an expense from the budget
        elif action == "remove" :
            budget.budget_category()
            try:
                category = input('Enter the category to remove : ').capitalize()
                amount = int(input('Enter the amount to remove : '))
                budget.remove(category, amount)
                budget.save('budget.xlsx')
            except KeyError as e:
                # This code will be executed if a KeyError occurs
                print("Error: key not found in budget list")
        # Function showing transaction history                    
        elif action == "history":
            budget.transaction_history()
        # Function counting chosen one by user    
        elif action == "sum":
            budget.count()
        # Exit   
        elif action == "q":
            # Save the updated budget to the Excel file
            budget.save('budget.xlsx')
            break

        


if __name__ == '__main__':
    main()
