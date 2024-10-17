import pandas as pd
import itertools

class bruteForce:
    def __init__(self, datasetpath, money):
        self.datasetpath = datasetpath
        self.money = money
        
    def brute_force(self):
        # Lecture du fichier CSV
        df = pd.read_csv(self.datasetpath)

        # Assurer que le fichier contient bien les colonnes attendues
        if 'name' not in df.columns or 'price' not in df.columns or 'profit' not in df.columns:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'name', 'price' et 'profit'.")

        # Convertir les données en un format plus simple
        actions = df[['name', 'price', 'profit']].to_dict(orient='records')

        budget_max = self.money

        # Algorithme de force brute
        best_profit = 0
        best_combination = []

        # Générer toutes les combinaisons possibles d'actions
        for r in range(1, len(actions) + 1):
            for combination in itertools.combinations(actions, r):
                # Utiliser les colonnes prix et profit par leur nom
                total_price = sum(item['price'] for item in combination)  # Colonne 'price'
                total_profit = sum(item['profit'] for item in combination)  # Colonne 'profit'
                print(combination)
                # Vérifier si le budget est respecté et si le profit est le meilleur
                if total_price <= budget_max and total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = combination
        
        # Affichage des résultats
        print("Algorithme de force brute :")
        print(f"Meilleur profit : {best_profit} %")
        print("Actions sélectionnées :")
        for action in best_combination:
            print(f"{action['name']} - Prix : {action['price']} €, Profit : {action['profit']} %")

    # Correction : Remplacer self.run() par self.brute_force()
    def main(self):
        self.brute_force()