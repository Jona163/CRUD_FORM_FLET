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

     
        self.data_table =  ft.DataTable(
                            expand= True,
                            border=ft.border.all(2, "purple"),
                            data_row_color = { ft.MaterialState.SELECTED: "purple", ft.MaterialState.PRESSED: "black"},
                            border_radius=10,
                            show_checkbox_column = True,
                            columns=[
                                ft.DataColumn(ft.Text("Nombre", color="purple", weight = "bold")),
                                ft.DataColumn(ft.Text("Edad", color="purple", weight = "bold")),
                                ft.DataColumn(ft.Text("Correo", color="purple", weight = "bold"), numeric=True),
                                ft.DataColumn(ft.Text("Telefono", color="purple", weight = "bold"), numeric=True ),
                            ],
                        )        
        
       
        self.show_data()



        self.form = ft.Container(
            bgcolor="#222222",
            border_radius=10,
            col=4,
            padding= 10,
            content= ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Ingrese sus datos",
                            size=40,
                            text_align="center",
                            font_family = "vivaldi",),
                    self.name,
                    self.age,
                    self.email,
                    self.phone,
                    ft.Container(
                        content= ft.Row(
                            spacing = 5,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls= [
                            ft.TextButton(text="Guardar",
                                        icon = ft.icons.SAVE,
                                        icon_color= "white",
                                        style= ft.ButtonStyle(color = "white",  bgcolor ="purple"),
                                        on_click= self.add_data,
                                        ),
