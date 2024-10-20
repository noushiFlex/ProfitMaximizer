import pandas as pd
import time

class AlgoGlouton:
    def __init__(self, datasetpath: str, money: float):
        self.datasetpath = datasetpath
        self.money = money

    def greedy_algo(self) -> tuple:
        df = pd.read_csv(self.datasetpath)

        if 'name' not in df.columns or 'price' not in df.columns or 'profit' not in df.columns:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'name', 'price' et 'profit'.")

        if df.empty:
            raise ValueError("Le fichier CSV est vide.")

        names = df['name'].tolist()
        prices = df['price'].tolist()
        profits = df['profit'].tolist()  # Profits en pourcentage

        ratio = []
        ignored_count = 0
        for i in range(len(prices)):
            if prices[i] > 0:  # Éviter la division par zéro
                # Calculer le profit en euros (prix * pourcentage / 100)
                profit_euros = prices[i] * (profits[i] / 100)
                ratio.append((profit_euros / prices[i], names[i], prices[i], profit_euros))
            else:
                ignored_count += 1  # Compter les actions ignorées

        if not ratio:
            raise ValueError("Aucune action valide disponible avec un prix supérieur à zéro.")

        # Trier par ratio profit/prix décroissant
        ratio.sort(key=lambda x: x[0], reverse=True)

        total_profit = 0
        chosen_items = []
        chosen_prices = []
        chosen_profits = []
        remaining_money = self.money

        # Sélectionner les actions
        for r in ratio:
            if remaining_money >= r[2]:  # Prix de l'action
                chosen_items.append(r[1])  # Nom
                chosen_prices.append(r[2])  # Prix
                chosen_profits.append(r[3])  # Profit en euros
                remaining_money -= r[2]
                total_profit += r[3]

        return total_profit, chosen_items, chosen_prices, chosen_profits, ignored_count
    
    def display_results(self):
        profit, chosen_items, chosen_prices, chosen_profits, ignored_count = self.greedy_algo()

        # Calculer l'investissement total
        total_investment = sum(chosen_prices)

        # Calcul du retour sur investissement en pourcentage
        roi_percent = (profit / total_investment) * 100 if total_investment > 0 else 0

        print("Algorithme glouton :")
        print(f"Retour sur investissement : {profit:.2f}€")
        print(f"Investissement total : {total_investment:.2f}€")
        # print(f"Retour sur investissement (ROI en %) : {roi_percent:.2f}%")
        print(f"Actions sélectionnées :")
        for item, price, profit in zip(chosen_items, chosen_prices, chosen_profits):
            print(f"Nom : {item}, Prix : {price:.2f}€, Profit : {profit:.2f}%")
        
        if ignored_count > 0:
            print(f"\n{ignored_count} action(s) ignorée(s) en raison d'un prix nul.")

    def main(self):
        self.display_results()

