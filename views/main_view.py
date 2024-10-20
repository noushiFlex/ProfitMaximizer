from pyfiglet import Figlet
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os,time
from controllers.algo_brute_force import bruteForce
from controllers.algo_optimise import AlgoGlouton

class RunApp:
    
    def __init__(self):
        self.RED = "\033[31m"           
        self.RESET = "\033[0m"       #Bright Red
        self.BYellow = "\033[1;33m"  #Bright Purple
        self.BCyan = "\033[1;36m"    #Bright Cyan


        f = Figlet(font='speed')
        self.figlet_text = f.renderText('shares Maximizer')
        print(self.BCyan + self.figlet_text + self.RESET)

        input(self.BYellow + 'Veuillez choisir le dataset à analyser (press Enter)' )

        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        self.dataPath = askopenfilename(title="Choisir le dataset")  
        root.update()
        
        # self.moneyInvest = input(BLUE + "Combien voulez-vous investir (euros/€): " + RESET)
        while True:
            try:
                self.moneyInvest = float(input("Entrez la somme que vous souhaitez investir : " + self.RESET))
                break
            except:
                print("Veuillez choisir une somme valide .")
    
    def run(self):
        while True:
            os.system('cls')
            print(self.BCyan + self.figlet_text )
            print(f"Dataset sélectionné : {self.dataPath}")
            print(f"Montant à investir : {self.moneyInvest} € " + self.RESET)
            print(self.BYellow)
            choix = input("""
    1 - Brute Force [🐌]
    2 - Algorithme Optimise [☄️]
    0 - Quitter [💥]
                  """ + self.RESET)
            if choix == '1':
                ct = time.time()
                algo = bruteForce(self.dataPath, self.moneyInvest)
                algo.main()
                print(f'Temps d\'execution du programme {time.time() - ct} s')
                break
            elif choix == '2':
                print("Execution de l'algo optimise")
                ct = time.time()
                algo = AlgoGlouton(self.dataPath, self.moneyInvest)
                algo.main()
                print(f'Temps d\'execution du programme {time.time() - ct} s')
                break
            elif choix == '0':
                print( self.BYellow + "Tres bien a bientot !"+self.RESET)
                break