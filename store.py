from tkinter import *
from tkinter import ttk
from main import Main
from Product import Product
from Category import Category
import mysql.connector

main = Main()
product = Product()
category = Category()

class Store:
    def __init__(self, screen):
        self.screen =Tk()
        self.screen.geometry('800x600')
        self.screen.title('store - Tableau de bord')
        self.screen['bg'] = 'grey'
        self.screen.resizable(height=False, width=False)

        self.initialize_gui()
        self.setup_database()


    def initialize_gui(self):
        label_Bienvenue = Label(self.screen, text='Bienvenue à la Boutique', font=("impact", 25, "bold"))
        label_Bienvenue.place(x=220,y=50)

        label_Tableau = Label(self.screen, text='Tableau de bord', font=("impact", 25, "bold"))
        label_Tableau.place(x=290,y=100)

        add_button = Button(self.screen, text="Ajouter un produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = main.createProduct)
        add_button.place(x=50,y=500)

        modify_button = Button(self.screen, text="Modifier le produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = main.updateProduct)
        modify_button.place(x=300,y=500)

        delete_button = Button(self.screen, text="Supprimer un produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = main.deleteProduct)
        delete_button.place(x=550,y=500)

    def setup_database(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="store",
        )
        self.cursor = self.mydb.cursor()
        self.populate_treeview()

    def populate_treeview(self):
        self.cursor.execute("SELECT * FROM product;")
        products = self.cursor.fetchall()
        for product in products:
            print(f"{product[1]}")


        # Création d'un arbre (treeview) pour afficher les noms de la table
        treeview = ttk.Treeview(self.screen, columns=("Nom",), show="headings")
        treeview.heading("Nom", text="Produits")

        # Effacer les anciennes données dans l'arbre
        for item in treeview.get_children():
            treeview.delete(item)

        # Affichage du contenu dans la fenêtre Tkinter
        for row in products:
            treeview.insert('', 'end', values=(row[1],))

        # Affichage de l'arbre
        treeview.grid(row=0, column=0, padx=300, pady=200)

 
if __name__ == "__main__":
    root = Tk()
    app = Store(root)
    root.mainloop()