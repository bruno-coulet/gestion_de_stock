from tkinter import *
# from main import *

screen =Tk()
screen.geometry('800x600')
screen.title('store - interface graphique')
screen['bg'] = 'grey'
screen.resizable(height=False, width=False)

label = Label(screen, text='Bienvenue à la Boutique', font=("impact", 25, "bold"))
# label.pack(side=LEFT, padx=200)
label.place(x='250',y='100')

button = Button(screen, text="Produits", font=("helvetica", 15), bg='black', fg="white")
button.place(x='250',y='300')


# menu = Menu(screen)
# menu.add_cascade(label="Produits en stock")
# menu.add_cascade(label="Catégories de produits")

# screen.config(menu=menu)

screen.mainloop()
