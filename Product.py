from Db import Db

class Product:
    def __init__(self):
        self.table = 'product'
        self.db = Db(host='localhost', user='root', password='root', database='store')


    def create(self, name, description, price, quantity, id_category):
        query = f'INSERT INTO {self.table} (name, description, price, quantity, id_category ) VALUES (%s, %s, %s, %s, %s)'
        params = (name, description, price, quantity, id_category)
        self.db.executeQuery(query, params)

    def read(self):
        query = f'SELECT * FROM {self.table}'
        return self.db.fetch(query)

    def update(self, id, name, description, price, quantity, id_category):
        query = f'UPDATE {self.table} SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s WHERE id=%s'
        params = (name, description, price, quantity, id_category, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f'DELETE FROM {self.table} WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)

    def find(self, id):
        query = f'SELECT * FROM {self.table} WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)
    
    