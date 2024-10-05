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


                                                          ft.TextButton(text="Actualizar",
                                        icon = ft.icons.UPDATE,
                                        icon_color= "white",
                                        style= ft.ButtonStyle(color = "white",  bgcolor ="purple"),
                                        on_click=self.update_data,
                                        ),    
                            ft.TextButton(text="Borrar",
                                        icon = ft.icons.DELETE,
                                        icon_color= "white",
                                        style= ft.ButtonStyle(color = "white",  bgcolor ="purple"),
                                        on_click= self.delete_data,
                                        ),                          
                            ]
                        )
                    )
                ]
            )
        )


        self.table = ft.Container(
            bgcolor= "#222222",
            border_radius=10,
            padding= 10,
            col = 8,
            content= ft.Column(   
                expand=True,           
                controls=[
                    ft.Container(
                        padding = 10,
                        content= ft.Row(
                            controls=[
                                self.searh_field,
                                ft.IconButton(
                                    icon= ft.icons.EDIT,
                                    on_click= self.edit_flied_text,
                                    icon_color= "white",
                                ),

                               ft.IconButton(tooltip="Descargar en PDF",
                                            icon = ft.icons.PICTURE_AS_PDF,
                                            icon_color= "white",
                                            on_click= self.save_pdf,
                                            ),     
                                ft.IconButton(tooltip="Descargar en EXCEL",
                                        icon = ft.icons.SAVE_ALT,
                                        icon_color= "white",
                                        on_click= self.save_excel,
                                        ),  
                            ]
                        ),
                    ),

                    
                    ft.Column(
                        expand= True, 
                        scroll="auto",
                        controls=[
                        ft.ResponsiveRow([
                            self.data_table
                            ]),
                        ]
                    )
                ]
            )
        )
        self.conent = ft.ResponsiveRow(
            controls=[
                self.form,
                self.table
            ]
        )

  
    def show_data(self):
        self.data_table.rows = []
        for x in self.data.get_contacts():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed= self.get_index, 
                    cells=[
                        ft.DataCell(ft.Text(x[1])),  
                        ft.DataCell(ft.Text(str(x[2]))),  
                        ft.DataCell(ft.Text(x[3])),
                        ft.DataCell(ft.Text(str(x[4]))),  
                    ]
                )
            )
        self.update()


    def  add_data(self, e):
        name = self.name.value
        age = str(self.age.value)
        email = self.email.value
        phone = str(self.phone.value)
        
        if len(name) and len(age) and len(email) and len(phone) > 0:
            contact_exists = False
            for row in self.data.get_contacts():
                if row[1] == name:
                    contact_exists = True
                    break

            if not contact_exists:
                self.clean_fields()
                self.data.add_contact(name, age, email, phone)
                self.show_data()
            else:
                print("El contacto ya existe en la base de datos.")
        print("Escriba sus datos")
