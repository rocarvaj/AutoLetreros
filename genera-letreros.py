import pandas as pd
from jinja2 import Template
import os
import subprocess

def leer_template_latex(archivo_template):
    # Leer el archivo de plantilla LaTeX externo
    with open(archivo_template, 'r') as file:
        return file.read()


def crear_codigo_latex(nombre_archivo, nombre_archivo_salida, archivo_template):
    # Leer el archivo XLSX
    df = pd.read_excel(nombre_archivo)
    
    # Leer la plantilla LaTeX desde un archivo externo
    latex_template = leer_template_latex(archivo_template)

    # Crear el template con Jinja2
    template = Template(latex_template)

    # Renderizar el código LaTeX
    latex_code = template.render(df=df)

    # Guardar el código LaTeX en un archivo .tex
    with open(f"{nombre_archivo_salida}.tex", "w") as f:
        f.write(latex_code)

def generar_pdf(nombre_archivo_salida):
    # Compilar el archivo .tex a PDF utilizando pdflatex
    subprocess.run(['pdflatex', f"{nombre_archivo_salida}.tex"])

def main():
    # Ruta al archivo de entrada
    nombre_archivo = "V02-RCDI.xlsx"
    nombre_archivo_salida = f"{nombre_archivo.split('.')[0]}-letreros"
    archivo_template = "template-letrero.tex"

    # Crear el archivo LaTeX y generar el PDF
    crear_codigo_latex(nombre_archivo, nombre_archivo_salida, archivo_template)
    generar_pdf(nombre_archivo_salida)

    # Eliminar archivos temporales generados por LaTeX
    os.remove(f"{nombre_archivo_salida}.aux")
    os.remove(f"{nombre_archivo_salida}.log")
    os.remove(f"{nombre_archivo_salida}.tex")

if __name__ == "__main__":
    main()