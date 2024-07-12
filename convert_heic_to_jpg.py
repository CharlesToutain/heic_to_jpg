import os
from tkinter import Tk, filedialog, messagebox
from PIL import Image
import pillow_heif

def convert_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pillow_heif.register_heif_opener()

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        name, ext = os.path.splitext(filename)
        if ext.lower() == ".heic":
            jpg_file_path = os.path.join(output_folder, f"{name}.jpg")

            try:
                image = Image.open(file_path)
                image.save(jpg_file_path, "JPEG")
                print(f"Converted {filename} to {jpg_file_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

    messagebox.showinfo("Conversion terminée", "Toutes les images ont été converties.")

def select_folder():
    input_folder = filedialog.askdirectory(title="Sélectionner le dossier contenant les photos HEIC")
    output_folder = filedialog.askdirectory(title="Sélectionner le dossier de sortie pour les photos JPG")

    if input_folder and output_folder:
        convert_images(input_folder, output_folder)
    else:
        messagebox.showwarning("Sélection de dossier", "Vous devez sélectionner les deux dossiers.")

def main():
    root = Tk()
    root.withdraw()  # Masquer la fenêtre principale
    select_folder()

if __name__ == "__main__":
    main()
