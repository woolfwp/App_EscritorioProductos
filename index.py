from inspect import Parameter
from tkinter import ttk
from tkinter import *

import sqlite3
from wsgiref import validate


class Product:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')


        #Creador de frame contenedor
        frame = LabelFrame(self.wind, text= 'Register A new Product')
        frame.grid(row = 0, column = 0, columnspan= 3, pady = 20)

        #Name Input

        Label(frame, text= 'Name: ').grid(row =1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column = 1)

        #Price input

        Label(frame, text= 'Price: ' ).grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)


        #Button Add Product

        ttk.Button(frame, text= ' save product', command= self.add_product).grid(row = 3 , columnspan= 2 , sticky= W + E)


        #Output menssages

        self.message = Label(text= '', fg = 'red')
        self.message.grid(row=3, column= 0, columnspan= 2, sticky= W +E)

        #Table

        self.tree = ttk.Treeview(height= 10, columns= 2)
        self.tree.grid(row = 4, column = 0, columnspan= 2)
        self.tree.heading('#0' , text= 'Name ', anchor= CENTER)
        self.tree.heading('#1', text=  'Price', anchor= CENTER)

        #buttons, modificar y eliminar

        ttk.Button(text= 'DELETE', command= self.delete_product).grid(row= 5, column = 0, sticky= W + E)
        ttk.Button(text= 'EDIT', command= self.edit_product).grid(row= 5, column = 1, sticky= W + E)

        #Filling the Row
        self.get_products()

    #Funcion para operar con la base de datos
    def run_query(self, query, parameters = ()): 
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):

        #cleaning table
        records = self.tree.get_children() 
        for element in records:
            self.tree.delete(element)
        #quering date
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)

        for row in db_rows:
            #print(db_rows)
            self.tree.insert('' , 0 ,text= row[1], values = row [2])


    #Validacion e ingreso de datos       
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Name and Price are Required'
        self.get_products()

    #eliminacion de productos

    def delete_product(self):
        self.message['text'] = ''

        # seleccion de item
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return

        # Eliminar item seleccionado 
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name= ?'
        self.run_query(query , (name, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.get_products()


    def edit_product(self):
        self.message['text'] = ''

        # seleccion de item
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return
        #Trae los datos 
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]

        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()