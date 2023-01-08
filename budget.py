import pandas as pd
import os


class Budget:
    def __init__(self, categories):
        self.categories = categories
        self.data = {}
        for category in self.categories:
            self.data[category] = 0
            
    # Features Add  expenses
    def add(self, category, amount):
        self.data[category] = amount
        Budget.save(self,'budget.xlsx')
        
    # Features Remove expenses
    def remove(self, category, amount):
        self.data[category] -= amount
        Budget.save(self,'budget.xlsx')
    
    def save(self, file_name):
        # Load the existing data from the Excel file
        df = pd.read_excel(file_name, engine='openpyxl')

        # Convert the new data to a DataFrame
        new_df = pd.DataFrame([self.data])

        # Combine the existing data with the new data
        df = pd.concat([df, new_df], ignore_index=True)

        # Save the combined data to the Excel file
        df.style.set_caption('Budget') \
            .format({col: '${:,.2f}'.format for col in self.categories}) \
            .hide(axis='index') \
            .to_excel(file_name, index=False)
        # writer = pd.ExcelWriter(file_name, engine='openpyxl')
        # writer.close()
                 
    # Function showing all budget category
    def open(self,file_name) :
        
        path = "/Users/konrad/python_programs/budget.xlsx"
        isExist = os.path.exists(path)
        if isExist == True:
            pass
        if isExist == False:
            print("FileNotFoundError")
            print("Creating New File")
             # Create a DataFrame with the budget data
            df = pd.DataFrame([self.data])
            # Convert the new data to a DataFrame
            new_df = pd.DataFrame([self.data])

            # Combine the existing data with the new data
            df = pd.concat([df, new_df], ignore_index=True)

            # Save the DataFrame to the Excel file
            df.to_excel(file_name, index=False)
            
            # Save the combined data to the Excel file
            writer = pd.ExcelWriter(file_name, engine='openpyxl')
            df.style.set_caption('Budget') \
                .format({col: '${:,.2f}'.format for col in self.categories}) \
                .hide(axis='index') \
                .to_excel(file_name, index=False)
            writer.if_sheet_exists('replace')
            writer.close()
            
    def budget_category(self):
        budget_category = ['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Travels', 'Gifts', 'Eating Outside', 'Mortgage']
        for number , category in enumerate(budget_category):
                print(f"{number+1}:{category}")
    # Function showing transaction history
    def transaction_history(self):
        fd = pd.read_excel('budget.xlsx')
        print(fd)
    # Function counting chosen one by user
    def count(self):
        fd = pd.read_excel('budget.xlsx')
        Budget.budget_category(self)
        try:        
            count= input("What would You like to count? : ").capitalize()
            sum =fd[count].sum()
            print(sum)
        except KeyError as e:
                # This code will be executed if a KeyError occurs
                print("Error: key not found in budget list")
        
