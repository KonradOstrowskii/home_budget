import pandas as pd

class Budget:
    def __init__(self, categories):
        self.categories = categories
        self.data = {}
        for category in self.categories:
            self.data[category] = 0
    
    def add(self, category, amount):
        self.data[category] += amount
    
    def remove(self, category, amount):
        self.data[category] -= amount
    
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
        
    def budget_category(self):
        budget_category = ['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Travels', 'Gifts', 'Eating Outside', 'Mortgage']
        for number , category in enumerate(budget_category):
                print(f"{number+1}:{category}")
        