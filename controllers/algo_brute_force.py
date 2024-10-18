import pandas as pd
import itertools

class bruteForce:
    def __init__(self, datasetpath, money):
        self.datasetpath = datasetpath
        self.money = money
        
    def brute_force(self):
        df = pd.read_csv(self.datasetpath)

        if 'name' not in df.columns or 'price' not in df.columns or 'profit' not in df.columns:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'name', 'price' et 'profit'.")

        actions = df[['name', 'price', 'profit']].to_dict(orient='records')

        budget_max = self.money

        best_profit = 0
        best_combination = []

        for r in range(1, len(actions) + 1):
            for combination in itertools.combinations(actions, r):
                # Utiliser les colonnes prix et profit par leur nom
                total_price = sum(item['price'] for item in combination)  
                total_profit = sum(item['profit'] for item in combination)
                print(combination)
                
                if total_price <= budget_max and total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = combination
        print("Algorithme de force brute :")
        print(f"Meilleur profit : {best_profit} %")
        print("Actions sélectionnées :")
        for action in best_combination:
            print(f"{action['name']} - Prix : {action['price']} €, Profit : {action['profit']} %")

    def main(self):
        self.brute_force()