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
