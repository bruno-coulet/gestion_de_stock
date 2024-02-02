from Db import Db

class Category:
    def __init__(self):
        self.table = 'category'
        self.db = Db(host='localhost', user='root', password='root', database='store')

    
    def create(self,name):
        query = f'INSERT INTO {self.table} (name) VALUES (%s)'
        params = (str(name),)
        self.db.executeQuery(query, params)

    def read(self):
        query = f'SELECT * FROM category'
        return self.db.fetch(query)
    
    def update(self, name, id):
        query = f'UPDATE category SET name=%s WHERE id=%s'
        params = (name, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f'DELETE FROM category WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
    
    def find(self, id):
        query = f'SELECT * FROM category WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)
    

    def addProduct(self, idProduct, idCategory):
        query = f'UPDATE product SET category_id=%s WHERE id=%s'
        params = (idCategory, idProduct)
        self.db.executeQuery(query, params)
    
    def removeProduct(self, idProduct):
        query = f'UPDATE product SET category_id=NULL WHERE id=%s'
        params = (idProduct,)
        self.db.executeQuery(query, params)

    def getProducts(self, idCategory):
        query = f'SELECT * FROM product WHERE category_id=%s'
        params = (idCategory,)
        return self.db.fetch(query, params)
    
    def getFreeCategorys(self):
        query = f'SELECT * FROM category WHERE max_products > (SELECT COUNT(*) FROM product WHERE category_id=category.id)'
        return self.db.fetch(query)
    
    def getFullCategorys(self):
        query = f'SELECT * FROM category WHERE max_products <= (SELECT COUNT(*) FROM product WHERE category_id=category.id)'
        return self.db.fetch(query)
    
    def getEmptyCategorys(self):
        query = f'SELECT * FROM category WHERE max_products = 0'
        return self.db.fetch(query)
    
    def getProductsCount(self, idCategory):
        query = f'SELECT COUNT(*) FROM product WHERE category_id=%s'
        params = (idCategory,)
        return self.db.fetch(query, params)
    
    def getProductsCountByType(self, idCategory, type):
        query = f'SELECT COUNT(*) FROM product WHERE category_id=%s AND type=%s'
        params = (idCategory, type)
        return self.db.fetch(query, params)
    

