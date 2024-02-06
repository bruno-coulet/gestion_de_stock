from Product import Product
from Category import Category


class Modifications:
    def __init__(self):
        self.product = Product()
        self.category = Category()


    def createProduct(self, name, description, price, quantity, id_category):
        try:
            id_category = int(id_category)
        except ValueError:
            print("ID de categorie invalide. Veuillez entrer un nombre.")

        self.product.create(name, description, price ,quantity ,id_category)


    def updateProduct(self, id, name, description, price, quantity, id_category):
        try:
            id = int(id)
        except ValueError:
            print("L'ID de produit est invalide. Veuillez entrer un nombre.")
            return

        self.product.update(id, name, description, price, quantity, id_category)


    # def deleteProduct(self):
    #     id_product = input("ID du produit à effacer : ")

    #     try:
    #         id_product = int(id_product)
    #     except ValueError:
    #         print("L'ID de produit est invalide. Veuillez entrer un nombre.")

    #     self.product.delete(id_product)
    def deleteProduct(self, id_product):
        """Supprime un produit avec l'ID spécifié"""
        try:
            id_product = int(id_product)
        except ValueError:
            print("L'ID de produit est invalide. Veuillez entrer un nombre.")
            return

        self.product.delete(id_product)



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