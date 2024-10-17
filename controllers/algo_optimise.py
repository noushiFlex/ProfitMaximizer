import pandas as pd

class AlgoOptimise:
    def __init__(self, datasetpath: str, money: float):
        self.datasetpath = datasetpath
        self.money = money

    def knapsack(self) -> tuple:
        # Lecture du fichier CSV
        df = pd.read_csv(self.datasetpath)

        # Vérifier les colonnes
        if 'name' not in df.columns or 'price' not in df.columns or 'profit' not in df.columns:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'name', 'price' et 'profit'.")

        # Vérifier si le fichier est vide
        if df.empty:
            raise ValueError("Le fichier CSV est vide.")

        # Extraire les prix et bénéfices
        names = df['name'].tolist()
        try:
            prices = [int(price * 100) for price in df['price'].tolist()]  # Convertir les prix en centimes
            profits = df['profit'].tolist()
        except ValueError:
            raise ValueError("Les colonnes 'price' et 'profit' doivent contenir des valeurs numériques.")

        # Nombre d'actions et budget maximal
        n = len(prices)
        W = int(self.money * 100)  # Convertir le budget en centimes

        # Vérification des tailles
        assert len(prices) == n, "La liste des prix ne correspond pas au nombre d'actions."
        assert len(profits) == n, "La liste des profits ne correspond pas au nombre d'actions."

        # Table de programmation dynamique
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # Algorithme de sac à dos dynamique
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if prices[i - 1] <= w:
                    # Ensure we do not access invalid indices
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - prices[i - 1]] + profits[i - 1])
                else:
                    dp[i][w] = dp[i - 1][w]

        # Résultat optimal
        result = dp[n][W]
        w = W
        chosen_items = []
        chosen_prices = []
        chosen_profits = []

        # Retracer les actions sélectionnées
        for i in range(n, 0, -1):
            if result <= 0:
                break
            if result == dp[i - 1][w]:
                continue
            else:
                chosen_items.append(names[i - 1])
                chosen_prices.append(prices[i - 1] / 100)  # Convertir les prix en euros
                chosen_profits.append(profits[i - 1])
                result -= profits[i - 1]
                w -= prices[i - 1]

        # Retourner le résultat
        return dp[n][W], chosen_items, chosen_prices, chosen_profits

    def display_results(self):
        profit, chosen_items, chosen_prices, chosen_profits = self.knapsack()

        print("Algorithme optimisé (sac à dos dynamique) :")
        print(f"Profit maximal : {profit / 100:.2f}€")  # Afficher le profit en euros
        print("Actions sélectionnées :")
        for item, price, profit in zip(chosen_items, chosen_prices, chosen_profits):
            print(f"Nom : {item}, Prix : {price:.2f}€, Profit : {profit}")

    def main(self):
        self.display_results()
