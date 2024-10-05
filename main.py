# Autor: Jonathan Hernández
# Fecha: 04 Octubre 2024
# Descripción: CRUD form flet.
# GitHub: https://github.com/Jona163

import flet as ft 
from contact_manager import ContactManager
from fpdf import FPDF
import pandas as pd
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Tabla de Datos', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

class FormUi(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page 
        self.data = ContactManager()
        self.selected_row = None

        self.name = ft.TextField(label="Nombre", border_color= "purple")
        self.age = ft.TextField(label="Edad", border_color= "purple", 
                                input_filter=ft.NumbersOnlyInputFilter(),
                                max_length =2)
        self.email =ft.TextField(label="Correo", border_color= "purple")
        self.phone = ft.TextField(label="Telefono", border_color= "purple",
                                  input_filter=ft.NumbersOnlyInputFilter(),
                                  max_length=9)
        
        self.searh_field = ft.TextField(                        
                            suffix_icon = ft.icons.SEARCH,
                            label= "Buscar por el nombre",
                            border= ft.InputBorder.UNDERLINE,
                            border_color= "white",
                            label_style = ft.TextStyle(color= "white"),
                            on_change = self.searh_data,
                        )     
