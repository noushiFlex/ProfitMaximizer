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
        profits = df['profit'].tolist()

        ratio = []
        for i in range(len(prices)):
            if prices[i] > 0:  # Éviter la division par zéro
                ratio.append((profits[i] / prices[i], names[i], prices[i], profits[i]))
            else:
                print(f"Action ignorée (prix nul) : {names[i]} avec un prix de {prices[i]}€")

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
                chosen_profits.append(r[3])  # Profit
                remaining_money -= r[2]
                total_profit += r[3]

        return total_profit, chosen_items, chosen_prices, chosen_profits

    def display_results(self):
        profit, chosen_items, chosen_prices, chosen_profits = self.greedy_algo()

        print("Algorithme glouton :")
        print(f"Profit maximal : {profit:.2f}€")  # Afficher le profit en euros
        print("Actions sélectionnées :")
        for item, price, profit in zip(chosen_items, chosen_prices, chosen_profits):
            print(f"Nom : {item}, Prix : {price:.2f}€, Profit : {profit}")

    def main(self):
        self.display_results()
