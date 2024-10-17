from pyfiglet import Figlet
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os,time
from controllers.algo_brute_force import bruteForce
from controllers.algo_optimise import AlgoOptimise

class RunApp:
    
    def __init__(self):
        self.RED = "\033[31m"
        self.RESET = "\033[0m"
        self.BLUE = "\033[34m"

        f = Figlet(font='graffiti')
        self.figlet_text = f.renderText('Data Analyst')
        print(self.RED + self.figlet_text + self.RESET)

        input(self.BLUE + 'Veuillez choisir le dataset à analyser (press Enter)' + self.RESET)

        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        self.dataPath = askopenfilename(title="Choisir le dataset")  
        root.update()

        # self.moneyInvest = input(BLUE + "Combien voulez-vous investir (euros/€): " + RESET)
        self.moneyInvest = 500
    
    def run(self):
        while True:
            os.system('cls')
            print(self.RED + self.figlet_text + self.RESET)
            print(f"Dataset sélectionné : {self.dataPath}")
            print(f"Montant à investir : {self.moneyInvest} €")
            choix = input("""
                  1 - Brute Force
                  2 - Algorithme Optimise
                  0 - Quitter
                  """)
            if choix == '1':
                ct = time.time()
                algo = bruteForce(self.dataPath, self.moneyInvest)
                algo.main()
                print(f'Temps d\'execution du programme {time.time() - ct} s')
                break
            elif choix == '2':
                ct = time.time()
                algo = AlgoOptimise(self.dataPath, self.moneyInvest)
                algo.main()
                print(f'Temps d\'execution du programme {time.time() - ct} s')
                break
            elif choix == '0':
                print("Tres bien a bientot !")
            