from Product import Product
from Category import Category
import Db

class Gerant:

    def __init__(self) -> None:
        self.product = Product()
        self.category = Category()        
        

    def createProduct(self, name, description, price, quantity, id_category):
        self.product.create(name, description, price, quantity, id_category)

    def readProduct(self):
        return self.product.read()
    
    def updateProduct(self, id, name, description, price, quantity, id_category):
        self.product.update(id, name, description, price, quantity, id_category)
    
    def deleteProduct(self, id):
        self.product.delete(id)
    
    def findProduct(self, id):
        return self.product.find(id)
    
    def createCategory(self, name):
        self.category.create(name)

    def readCategory(self):
        return self.category.read()
    
    def updateCategory(self, id, name):
        self.category.update(id, name)

    def deleteCategory(self, id):
        self.category.delete(id)

    def findCategory(self, id):
        return self.category.find(id)
    
    def addProductToCategory(self, idProduct, idCategory):
        self.category.addProduct(idProduct, idCategory)