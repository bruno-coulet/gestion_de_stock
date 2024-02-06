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
    
    def addProduct(self, idProduct, idCategory):
        query = f'UPDATE product SET category_id=%s WHERE id=%s'
        params = (idCategory, idProduct)
        self.db.executeQuery(query, params)
    
    def removeProduct(self, idProduct):
        query = f'UPDATE product SET category_id=NULL WHERE id=%s'
        params = (idProduct,)
        self.db.executeQuery(query, params)
