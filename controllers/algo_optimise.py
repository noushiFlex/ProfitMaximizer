import pandas as pd

class AlgoGlouton:
    def __init__(self, datasetpath: str, money: float):
        self.datasetpath = datasetpath
        self.money = money

    def convert_old_format(self, df):
        """Convertit l'ancien format en nouveau format."""
        df['Bénéfice (après 2 ans)'] = df['profit'] / df['price'] * 100  # Convertir le profit en pourcentage
        df['Coût par action (en euros)'] = df['price']  # Assigner le prix
        df['Actions'] = df['name']  # Assigner le nom
        return df[['Actions', 'Coût par action (en euros)', 'Bénéfice (après 2 ans)']]

    def knapsack(self) -> tuple:
        # Lecture du fichier CSV avec un séparateur spécifié
        df = pd.read_csv(self.datasetpath, sep=';', engine='python')

        # Nettoyer les noms de colonnes en supprimant les espaces
        df.columns = df.columns.str.strip()

        # Afficher les colonnes du DataFrame pour débogage
        print("Colonnes détectées :", df.columns.tolist())

        # Vérifier le format du dataset
        if 'Actions' in df.columns and 'Coût par action (en euros)' in df.columns and 'Bénéfice (après 2 ans)' in df.columns:
            # Nouveau format
            print("Nouveau format détecté : Pas de conversion nécessaire.")
            names = df['Actions'].tolist()

            # Convertir les colonnes en types numériques
            df['Coût par action (en euros)'] = pd.to_numeric(df['Coût par action (en euros)'], errors='coerce')
            
            # Nettoyer la colonne de bénéfice et convertir en type numérique
            df['Bénéfice (après 2 ans)'] = df['Bénéfice (après 2 ans)'].str.replace('%', '').astype(float)  # Retirer '%' et convertir en float
            df['Bénéfice (après 2 ans)'] = df['Bénéfice (après 2 ans)'] / 100  # Convertir en pourcentage décimal

            # Vérifier les NaN après conversion
            if df['Coût par action (en euros)'].isnull().any() or df['Bénéfice (après 2 ans)'].isnull().any():
                print("Attention : Il y a des valeurs NaN dans les colonnes de coût ou de bénéfice.")

            prices = [int(price * 100) for price in df['Coût par action (en euros)'].tolist() if pd.notnull(price)]  # Convertir les prix en centimes
            profits = [(df['Bénéfice (après 2 ans)'][i] * df['Coût par action (en euros)'][i]) for i in range(len(df)) if pd.notnull(df['Bénéfice (après 2 ans)'][i]) and pd.notnull(df['Coût par action (en euros)'][i])]  # Calculer les profits

        elif 'name' in df.columns and 'price' in df.columns and 'profit' in df.columns:
            # Ancien format
            print("Ancien format détecté : Conversion nécessaire.")
            df = self.convert_old_format(df)

            # Convertir les colonnes en types numériques
            df['Coût par action (en euros)'] = pd.to_numeric(df['Coût par action (en euros)'], errors='coerce')
            
            # Nettoyer la colonne de bénéfice et convertir en type numérique
            df['Bénéfice (après 2 ans)'] = df['Bénéfice (après 2 ans)'].str.replace('%', '').astype(float)  # Retirer '%' et convertir en float
            df['Bénéfice (après 2 ans)'] = df['Bénéfice (après 2 ans)'] / 100  # Convertir en pourcentage décimal

            # Vérifier les NaN après conversion
            if df['Coût par action (en euros)'].isnull().any() or df['Bénéfice (après 2 ans)'].isnull().any():
                print("Attention : Il y a des valeurs NaN dans les colonnes de coût ou de bénéfice.")

            names = df['Actions'].tolist()
            prices = [int(price * 100) for price in df['Coût par action (en euros)'].tolist() if pd.notnull(price)]  # Convertir les prix en centimes
            profits = [(df['Bénéfice (après 2 ans)'][i] * df['Coût par action (en euros)'][i]) for i in range(len(df)) if pd.notnull(df['Bénéfice (après 2 ans)'][i]) and pd.notnull(df['Coût par action (en euros)'][i])]  # Calculer les profits

        else:
            raise ValueError("Le fichier CSV doit contenir soit le format ancien ('name', 'price', 'profit'), soit le nouveau ('Actions', 'Coût par action (en euros)', 'Bénéfice (après 2 ans)').")

        # Nombre d'actions et budget maximal
        n = len(prices)
        W = int(self.money * 100)  # Convertir le budget en centimes

        # Vérification des tailles
        assert len(prices) == n, "La liste des prix ne correspond pas au nombre d'actions."
        assert len(profits) == n, "La liste des profits ne correspond pas au nombre d'actions."

        # Filtrer les actions avec prix à zéro pour éviter la division par zéro
        ratio = [(profits[i] / prices[i], names[i], prices[i], profits[i]) for i in range(n) if prices[i] > 0]

        # Tri basé sur le ratio profit/prix
        ratio.sort(reverse=True, key=lambda x: x[0])

        # Sélection des actions les plus rentables
        total_profit = 0
        chosen_items = []
        chosen_prices = []
        chosen_profits = []

        for r in ratio:
            if W >= r[2]:  # Si le budget restant permet d'acheter cette action
                W -= r[2]  # Réduire le budget disponible
                total_profit += r[3]  # Ajouter le profit
                chosen_items.append(r[1])
                chosen_prices.append(r[2] / 100)  # Reconvertir en euros
                chosen_profits.append(r[3])

        # Retourner le résultat
        return total_profit, chosen_items, chosen_prices, chosen_profits

    def display_results(self):
        profit, chosen_items, chosen_prices, chosen_profits = self.knapsack()

        print("Algorithme glouton :")
        print(f"Profit maximal : {profit:.2f}€")  # Afficher le profit en euros
        print("Actions sélectionnées :")
        for item, price, profit in zip(chosen_items, chosen_prices, chosen_profits):
            print(f"Nom : {item}, Prix : {price:.2f}€, Profit : {profit:.2f}€")

    def main(self):
        self.display_results()
