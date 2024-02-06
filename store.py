from tkinter import *
from tkinter import ttk
from Modifications import Modifications
from Product import Product
from Category import Category
import mysql.connector

main = Modifications()
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

        # add_button = Button(self.screen, text="Ajouter un produit", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = main.createProduct)
        # Bouton pour ouvrir le sous menu d'ajout de produit
        add_product_button = Button(self.screen, text="Ajouter un produit", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command=self.open_add_product_window)
        add_product_button.place(x=50,y=250)

        modify_button = Button(self.screen, text="Modifier le produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = main.updateProduct)
        modify_button.place(x=50,y=350)

        delete_button = Button(self.screen, text="Supprimer un produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = main.deleteProduct)
        delete_button.place(x=50,y=450)

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
        add_button = Button(add_product_window, text="Ajouter le produit", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command=lambda: main.createProduct(name_entry.get(), description_entry.get(), price_entry.get(), quantity_entry.get(), category_id_entry.get()))
        add_button.place(x=150, y=300)


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
        products_list = ttk.Treeview(self.screen, columns=("Nom",), show="headings")
        products_list.heading("Nom", text="Produits")

        # Effacer les anciennes données dans l'arbre
        for item in products_list.get_children():
            products_list.delete(item)

        # Affiche le contenu dans la fenêtre Tkinter
        for row in products:
            products_list.insert('', 'end', values=(row[1],))

        # Affiche l'arbre
        products_list.grid(row=0, column=0, padx=300, pady=200)

 
if __name__ == "__main__":
    root = Tk()
    app = Store(root)
    root.mainloop()
        
