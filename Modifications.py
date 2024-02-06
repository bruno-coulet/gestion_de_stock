from Product import Product
from Category import Category


class Modifications:
    def __init__(self):
        self.product = Product()
        self.category = Category()

    # def createProduct(self):
    def createProduct(self, name, description, price, quantity, id_category):
        # name = input("Nom : ")
        # description = (input("Description : "))
        # price = input("Prix : ")
        # quantity = input("Quantité : ")
        # id_category = int(input("ID de la catégorie : "))
        
        try:
            id_category = int(id_category)
        except ValueError:
            print("ID de categorie invalide. Veuillez entrer un nombre.")

        self.product.create(name, description, price ,quantity ,id_category)



    def updateProduct(self):
        id = input("ID du produit : ")
        name = input("Nom : ")
        description = input("Description : ")
        price = input("Prix : ")
        quantity = input("Quantité : ")
        id_category = int(input("ID de la catégorie : "))

        try:
            id = int(id)
        except ValueError:
            print("L'ID de produit est invalide. Veuillez entrer un nombre.")
            # self.menu()

        self.product.update(id, name, description, price, quantity, id_category)
        # self.gerant.updateProduct(id, name, description, price, quantity, id_category)
        # self.menu()

    def deleteProduct(self):
        id_product = input("ID du produit à effacer : ")

        try:
            id_product = int(id_product)
        except ValueError:
            print("L'ID de produit est invalide. Veuillez entrer un nombre.")
            # self.menu()

        self.product.delete(id_product)
        # self.menu()

    def findProduct(self):
        id_product = input("ID du produit : ")

        try:
            id_product = int(id_product)
        except ValueError:
            print("L'ID de produit est invalide. Veuillez entrer un nombre.")
            # self.menu()

        print(self.product.find(id_product))
        # self.menu()

    def createCategory(self):
        name = input("Nom catégorie : ")

        self.category.create(name)
        # self.menu()

    def readCategory(self):
        for category in self.category.readCategory():
            print("Categorie : ")
            print(f"id : {category[0]}")
            print(f"nom de catégorie : {category[1]}")
            print("------------------")
        self.menu()

    def updateCategory(self):
        id_category = input("ID de la categorie : ")
        name = input("Nom de la categorie : ")


        try:
            id_category = int(id_category)
        except ValueError:
            print("ID de categorie ou nombre maximum de produit invalide. Veuillez entrer un nombre.")
            # self.menu()

        self.category.update(id_category, name)
        # self.menu()

    def deleteCategory(self):
        id_category = input("ID de la categorie : ")

        try:
            id_category = int(id_category)
        except ValueError:
            print("ID de categorie invalide. Veuillez entrer un nombre.")
            # self.menu()

        self.category.delete(id_category)
        # self.menu()

    def findCategory(self):
        id_category = input("ID de la categorie : ")

        try:
            id_category = int(id_category)
        except ValueError:
            print("ID de categorie invalide. Veuillez entrer un nombre.")
            # self.menu()

        print(self.category.find(id_category))
        # self.menu()

    def addProductToCategory(self):
        id_product = input("ID du produit : ")
        id_category = input("ID de la categorie : ")

        try:
            id_product = int(id_product)
            id_category = int(id_category)
        except ValueError:
            print("ID de produit ou ID de categorie invalide. Veuillez entrer un nombre.")
            # self.menu()

        self.category.addProduct(id_product, id_category)
        # self.menu()

    def readProduct(self):
        # for product in self.gerant.readProduct():
        for product in self.product.read():
            print("Produit : ")
            print(f"id : {product[0]}")
            print(f"Nom : {product[1]}")
            print(f"Description : {product[2]}")
            print(f"Prix :{product[3]}")
            print(f"Quantité : {product[4]}")
            print(f"Id_catégorie : {product[5]}")
            print("------------------")
        # self.menu()

# Modifications()
        






        # CI DESSOUS C'ETAIT DANS LE INIT (ligne 8)
        # self.menu()

    # def menu(self):
    #     print("1. Créer un produit")
    #     print("2. Lire les produits")
    #     print("3. Modifier un produit")
    #     print("4. Supprimer un produit")
    #     print("5. Trouver un produit")
    #     print("6. Créer une categorie")
    #     print("7. Lire les categories")
    #     print("8. Modifier une categorie")
    #     print("9. Supprimer une categorie")
    #     print("10. Trouver une categorie")
    #     print("11. Ajouter un produit dans une categorie")
    #     print("12. Quitter")
    #     choix = input("Votre choix : ")

    #     try:
    #         choix = int(choix)
    #     except ValueError:
    #         print("Choix invalide. Veuillez entrer un nombre.")
    #         self.menu()

    #     if choix == 1:
    #         self.createProduct()
    #     elif choix == 2:
    #         self.readProduct()
    #     elif choix == 3:
    #         self.updateProduct()
    #     elif choix == 4:
    #         self.deleteProduct()
    #     elif choix == 5:
    #         self.findProduct()
    #     elif choix == 6:
    #         self.createCategory()
    #     elif choix == 7:
    #         self.readCategory()
    #     elif choix == 8:
    #         self.updateCategory()
    #     elif choix == 9:
    #         self.deleteCategory()
    #     elif choix == 10:
    #         self.findCategory()
    #     elif choix == 11:
    #         self.addProductToCategory()
    #     elif choix == 12:
    #         exit()
    #     else:
    #         print("Choix invalide")
    #         self.menu()