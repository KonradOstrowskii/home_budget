import pandas as pd
import os
import openpyxl


class Budget:
    def __init__(self, categories):
        self.categories = categories
        self.data = {}
        budget_category = ['Rent', 'Utilities', 'Groceries', 'Entertainment', 
                           'Travels', 'Gifts', 'Eating Outside', 'Mortgage']
        for category in self.categories:
            self.data[category] = 0
            
    # Features Add  expenses
    def add(self, category, amount):
        self.data[category] = amount
        Budget.save(self,'budget.xlsx')
        
    # Features Remove expenses
    def remove(self, category, amount):
        self.data[category] = -amount
        Budget.save(self,'budget.xlsx')
    
    def save(self, file_name):
        # Load the existing data from the Excel file
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.active

        # Find the last row of the sheet
        last_row = sheet.max_row

        # Update the values in the existing row
        for i, category in enumerate(self.categories):
            sheet.cell(row=last_row, column=i+1).value = self.data[category]

        # Save the changes to the Excel file
        sheet.insert_rows(sheet.max_row + 1)
        wb.save(file_name)
        
    def new_row(self,file_name="budget.xlsx"):
        # Load the existing data from the Excel file
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.active

        # Find the last row of the sheet
        last_row = sheet.max_row

        # Update the values in the existing row
        for i, category in enumerate(self.categories):
            sheet.cell(row=last_row+1, column=i+1).value = self.data[category]
        wb.save(file_name)
        
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
            df.style.set_caption('Budget') \
                .format({col: '${:,.2f}'.format for col in self.categories}) \
                .hide(axis='index') \
                .to_excel(file_name, index=False)
            
    def budget_category(self):
        budget_category = ['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Travels', 'Gifts', 'Eating Outside', 'Mortgage']
        for number , category in enumerate(budget_category):
                return(f"{number+1}:{category}")
                
    # Function showing transaction history
    def transaction_history(self):
        fd = pd.read_excel('budget.xlsx')
        print(fd)
        
    # Function counting chosen one by user
    def count(self,budget_to_count):
        fd = pd.read_excel('budget.xlsx')
        Budget.budget_category(self)
        try:     
            for number , category in enumerate(budget_to_count):
                print(f"{number+1}:{category}")
                sum =fd[category].sum()
                print(sum)
        except KeyError as e:
                # This code will be executed if a KeyError occurs
                print("Error: key not found in budget list")
