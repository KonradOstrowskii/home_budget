from budget import Budget 

    
def main():
    
    # Create an instance of the Budget class with the given categories
    budget = Budget(['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Travels', 'Gifts', 'Eating Outside', 'Mortgage'])
    # List of all available category
    category_list = ['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Travels', 'Gifts', 'Eating Outside', 'Mortgage']
    while True:
        # Open budget.xlsx file
        budget.open("budget.xlsx")
        while True:
            # List of all available action
            available_action = ["add","remove","q","history","sum"]
            
            # Get the user's choice
            action = input('Enter "add" to add a category, "remove" to remove "history" to to see history,"sum" to sum value of a row "q" for exit : ')
            # Check if action User chose is available          
            if action not in available_action:
                print("This is not allowed action")
                
            # Add an expense from the budget
            if action == "add":
                # Creating new row for file
                budget.new_row()
                budget.budget_category(category_list) 
                try:
                    for category in category_list :
                        while True:
                            try:
                                # User input for the amount
                                amount = int(input(f'Enter the amount to {category} : '))
                                # Features Add  expenses
                                budget.add(category, amount)
                            except ValueError as e:
                                print("Amount only can be a numbers :")
                                continue
                            break
                except KeyError as e:
                    # This code will be executed if a KeyError occurs
                    print("Error: key not found in budget list")
                break
                    
            # Remove an expense from the budget
            elif action == "remove" :
                # Creating new row for file
                budget.new_row()
                budget.budget_category(category_list)
                try:
                    for category in category_list :
                        while True:
                            try:
                                # User input for the amount
                                amount = int(input(f'Enter the amount to {category} : '))
                                # Features Remove  expenses
                                budget.remove(category, amount)
                            except ValueError as e:
                                print("Amount only can be a numbers :")
                                continue
                            break
                except KeyError as e:
                    # This code will be executed if a KeyError occurs
                    print("Error: key not found in budget list")
                break
            # Function showing transaction history                    
            elif action == "history":
                budget.transaction_history()
            # Function counting chosen one by user    
            elif action == "sum":
                budget.count(budget_to_count=category_list)
            # Exit   
            elif action == "q":
                print("Thank You , see You next time !")
                quit()
                
        


if __name__ == '__main__':
    main()
