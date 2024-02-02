from tkinter import *
from tkinter import ttk
from main import Main
import mysql.connector

screen =Tk()
screen.geometry('800x600')
screen.title('store - Tableau de bord')
screen['bg'] = 'grey'
screen.resizable(height=False, width=False)
main = Main()


label_Bienvenue = Label(screen, text='Bienvenue à la Boutique', font=("impact", 25, "bold"))
label_Bienvenue.place(x=220,y=50)

label_Tableau = Label(screen, text='Tableau de bord', font=("impact", 25, "bold"))
label_Tableau.place(x=290,y=100)



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="store",
)
cursor = mydb.cursor()

cursor.execute("SELECT * FROM product;")
products = cursor.fetchall()
# for product in products:
#     print(f"{product[1]}")


# Création d'un arbre (treeview) pour afficher les noms de la table
treeview = ttk.Treeview(screen, columns=("Nom",), show="headings")
treeview.heading("Nom", text="Produits")

# Effacer les anciennes données dans l'arbre
for item in treeview.get_children():
    treeview.delete(item)

# Affichage du contenu dans la fenêtre Tkinter
for row in products:
    treeview.insert('', 'end', values=(row[1],))


# Affichage de l'arbre
treeview.grid(row=0, column=0, padx=300, pady=200)


add_button = Button(screen, text="Ajouter un produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = main.createProduct)
add_button.place(x=50,y=500)

delete_button = Button(screen, text="Supprimer un produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white", command = main.deleteProduct)
delete_button.place(x=300,y=500)

modify_button = Button(screen, text="Modifier le produits", font=("helvetica", 15), bg='black', highlightcolor='orange', fg="white")
modify_button.place(x=550,y=500)


screen.mainloop()
