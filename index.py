from tkinter import ttk
from tkinter import *

import sqlite3
from tkinter.tix import COLUMN

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')


        #Creador de frame contenedor
        frame = LabelFrame(self.wind, text= 'Register A new Product')
        frame.grid(row = 0, column = 0, columnspan= 3, pady = 20)

        #Name Input

        Label(frame, text= 'Name: ').grid(row =1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row=1, column = 1)

        #Price input

        Label(frame, text= 'Price: ' ).grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)


        #Button Add Product

        ttk.Button(frame, text= ' save product').grid(row = 3 , columnspan= 2 , sticky= W + E)




if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()