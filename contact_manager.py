# Autor: Jonathan Hernández
# Fecha: 04 Octubre 2024
# Descripción: CRUD form flet.
# GitHub: https://github.com/Jona163

import sqlite3

class ContactManager:
    def __init__(self):
        self.connection = sqlite3.connect("data.db",check_same_thread=False)

    def add_contact(self, name, age, email, phone):
        query = '''INSERT INTO datos (NOMBRE, EDAD, CORREO, TELEFONO) 
                   VALUES (?, ?, ?, ?)'''
        self.connection.execute(query, (name, age, email, phone))
        self.connection.commit()

    def get_contacts(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM datos"
        cursor.execute(query)
        contacts = cursor.fetchall()
        return contacts
