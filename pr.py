import PyPDF2
from openpyxl import Workbook

pdf_file = open('Prueba1.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
page1 = pdf_reader.getPage(1) # Seleccionar la página a leer
text = page1.extractText() # Extraer el texto de la página

filas = text.split('\n') # Separar el texto en filas
tabla = []
for fila in filas:
    columna = fila.split('\t') # Separar la fila en columnas
    print(columna)
    tabla.append(columna)




