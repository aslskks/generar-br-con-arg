import barcode
from barcode.ean import EAN13
from barcode.writer import ImageWriter

def calculate_checksum(code):
    """
    Calculate and return the EAN-13 checksum for the given code.
    """
    evensum = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7]) + int(code[9]) + int(code[11])
    oddsum = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]) + int(code[8]) + int(code[10])
    total = oddsum + evensum * 3
    remainder = total % 10
    if remainder == 0:
        return 0
    else:
        return 10 - remainder

def codigos():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--info", type=str, help="ingresa la info")
    parser.add_argument("--nombre", type=str, help="ingresa el nombre del codigo de barras")
    args = parser.parse_args()
    informacion = args.info
    nombre = args.nombre
    """
    if "espacio" in nombre:
        import os
        os.system("pip install pyinstaller")
    """

    generarcodigos(informacion, nombre)

def generarcodigos(info, nombre):
    numeros = info

    # Calculate checksum
    checksum = calculate_checksum(numeros)
    numeros_with_checksum = f"{numeros}{checksum}"

    with open("static" + nombre + ".jpeg", "wb") as file:
        writer = ImageWriter()
        writer.text_distance = 1  # Adjust this value to control the font size indirectly
        EAN13(numeros_with_checksum, writer=writer).write(file)

if __name__ == "__main__":
    try:
        codigos()
    except KeyboardInterrupt:
        import sys
        sys.exit()
    except Exception as e:
        from tkinter.messagebox import showerror
        print(e)
        showerror(title="generador de barras con argparse", message=f"{e}")
        raise ValueError("error por el programa")
        