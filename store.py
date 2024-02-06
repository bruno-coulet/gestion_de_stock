from tkinter import *
from tkinter import ttk
from Modifications import Modifications
from Product import Product
from Category import Category
import mysql.connector

modifications = Modifications()
product = Product()
category = Category()

class Store:
    def __init__(self, screen):
        self.screen =screen
        self.screen.geometry('800x600')
        self.screen.title('store - Tableau de bord')
        self.screen['bg'] = 'grey'
        self.screen.resizable(height=False, width=False)

        self.gui()
        self.setup_database()

    def gui(self):
        """Affiche le titre, le sous titre et les boutons"""
        label_Bienvenue = Label(self.screen, text='Bienvenue à la Boutique', font=("impact", 25, "bold"))
        label_Bienvenue.place(x=220,y=50)

        label_Tableau = Label(self.screen, text='Tableau de bord', font=("impact", 25, "bold"))
        label_Tableau.place(x=290,y=100)

        # Bouton pour ouvrir le sous menu d'ajout de produit
        add_button = Button(self.screen, text="Ajouter un produit", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command=self.open_add_product_window)
        add_button.place(x=50,y=250)

        # ouvre le sous menu modification
        modify_button = Button(self.screen, text="Modifier le produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = self.open_modify_product_window)
        modify_button.place(x=50,y=350)

        delete_button = Button(self.screen, text="Supprimer un produit", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = self.open_delete_product_window)
        delete_button.place(x=50,y=450)

    # def delete(self):
    #     """Supprime un produit"""
    #     # Obtenez l'ID du produit à partir de l'interface utilisateur
    #     id_product = input("ID du produit à effacer : ")
    #     # Appelez la méthode deleteProduct de la classe Modifications avec l'ID du produit
    #     modifications.deleteProduct(id_product)

    def open_delete_product_window(self):
        """Ouvre une nouvelle fenêtre pour supprimer un produit"""
        delete_product_window = Toplevel(self.screen)
        delete_product_window.title("Supprimer un produit")
        delete_product_window.geometry("600x400")

        label_id = Label(delete_product_window, text="ID du produit:", font=("helvetica", 15))
        label_id.place(x=50, y=250)
        id_entry = Entry(delete_product_window, font=("helvetica", 15))
        id_entry.place(x=200, y=250)

        delete_button = Button(delete_product_window, text="Supprimer le produit", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command=lambda: modifications.deleteProduct(id_entry.get()))
        delete_button.place(x=150, y=300)



    def open_add_product_window(self):
        """Ouvre une nouvelle fenêtre pour l'ajout de produit"""
        add_product_window = Toplevel(self.screen)
        add_product_window.title("Ajouter un produit")
        add_product_window.geometry("600x400")

        # Champs d'entrée de texte pour le nom, la description, le prix, la quantité et l'ID de la catégorie du produit
        label_name = Label(add_product_window, text="Nom du produit:", font=("helvetica", 15))
        label_name.place(x=50, y=50)
        name_entry = Entry(add_product_window, font=("helvetica", 15))
        name_entry.place(x=200, y=50)

        label_description = Label(add_product_window, text="Description:", font=("helvetica", 15))
        label_description.place(x=50, y=100)
        description_entry = Entry(add_product_window, font=("helvetica", 15))
        description_entry.place(x=200, y=100)

        label_price = Label(add_product_window, text="Prix:", font=("helvetica", 15))
        label_price.place(x=50, y=150)
        price_entry = Entry(add_product_window, font=("helvetica", 15))
        price_entry.place(x=200, y=150)

        label_quantity = Label(add_product_window, text="Quantité:", font=("helvetica", 15))
        label_quantity.place(x=50, y=200)
        quantity_entry = Entry(add_product_window, font=("helvetica", 15))
        quantity_entry.place(x=200, y=200)

        label_category_id = Label(add_product_window, text="ID de la catégorie:", font=("helvetica", 15))
        label_category_id.place(x=50, y=250)
        category_id_entry = Entry(add_product_window, font=("helvetica", 15))
        category_id_entry.place(x=200, y=250)

        # Bouton pour ajouter le produit
        add_button = Button(add_product_window, text="Ajouter le produit", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command=lambda: modifications.createProduct(name_entry.get(), description_entry.get(), price_entry.get(), quantity_entry.get(), category_id_entry.get()))
        add_button.place(x=150, y=300)

    def open_modify_product_window(self):
        """Ouvre une nouvelle fenêtre pour modifier un produit"""
        modify_product_window = Toplevel(self.screen)
        modify_product_window.title("Modifier un produit")
        modify_product_window.geometry("600x400")

        # Champs d'entrée de texte pour le nom, la description, le prix, la quantité et l'ID de la catégorie du produit
        label_name = Label(modify_product_window, text="Nom du produit:", font=("helvetica", 15))
        label_name.place(x=50, y=50)
        name_entry = Entry(modify_product_window, font=("helvetica", 15))
        name_entry.place(x=200, y=50)

        label_description = Label(modify_product_window, text="Description:", font=("helvetica", 15))
        label_description.place(x=50, y=100)
        description_entry = Entry(modify_product_window, font=("helvetica", 15))
        description_entry.place(x=200, y=100)

        label_price = Label(modify_product_window, text="Prix:", font=("helvetica", 15))
        label_price.place(x=50, y=150)
        price_entry = Entry(modify_product_window, font=("helvetica", 15))
        price_entry.place(x=200, y=150)

        label_quantity = Label(modify_product_window, text="Quantité:", font=("helvetica", 15))
        label_quantity.place(x=50, y=200)
        quantity_entry = Entry(modify_product_window, font=("helvetica", 15))
        quantity_entry.place(x=200, y=200)

        label_category_id = Label(modify_product_window, text="ID de la catégorie:", font=("helvetica", 15))
        label_category_id.place(x=50, y=250)
        category_id_entry = Entry(modify_product_window, font=("helvetica", 15))
        category_id_entry.place(x=200, y=250)

        # Bouton pour modifier le produit
        modify_button = Button(modify_product_window, text="Modifier le produit", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command=lambda: modifications.updateProduct(id_entry.get(),name_entry.get(), description_entry.get(), price_entry.get(), quantity_entry.get(), category_id_entry.get()))
        modify_button.place(x=150, y=300)

    def setup_database(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="store",
        )
        self.cursor = self.mydb.cursor()
        self.show_products()

    def show_products(self):
        """Affiche la liste des produits"""
        self.cursor.execute("SELECT * FROM product;")
        products = self.cursor.fetchall()
        for product in products:
            print(f"{product[1]}")

        # Crée un arbre (treeview) pour afficher le nom de la table
        products_list = ttk.Treeview(self.screen, columns=("id","Nom", "Quantité"), show="headings")
        products_list.heading("id", text="id")
        products_list.heading("Nom", text="Produits")
        products_list.heading("Quantité", text="Quantité")

        # Configurer la largeur des colonnes
        products_list.column("id", width=50)
        products_list.column("Nom", width=200)
        products_list.column("Quantité", width=100) 

        # Effacer les anciennes données dans l'arbre
        for item in products_list.get_children():
            products_list.delete(item)

        # Affiche le contenu dans la fenêtre Tkinter
        for row in products:
            products_list.insert('', 'end', values=(row[0],row[1], row[4]))


        # Affiche l'arbre
        products_list.grid(row=0, column=0, padx=300, pady=200, sticky="nsew")



        # Ajoute une barre de défilement verticale
        scrollbar = Scrollbar(self.screen, orient="vertical", command=products_list.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Configurer l'arbre pour utiliser la barre de défilement
        products_list.configure(yscrollcommand=scrollbar.set)


        # Configurer la grille pour que l'arbre prenne toute la place disponible
        # self.screen.grid_rowconfigure(0, weight=1)
        # self.screen.grid_columnconfigure(0, weight=1)
        # self.screen.grid_columnconfigure(1, weight=0)


 
if __name__ == "__main__":
    root = Tk()
    app = Store(root)
    root.mainloop()
        
