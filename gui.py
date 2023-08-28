import tkinter as tk
from tkinter import ttk, filedialog
from pytube import YouTube
import subprocess
from PIL import Image, ImageTk
import os

def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))

def get_image_path(image_filename):
    return os.path.join(get_script_directory(), "logo", image_filename)

def download_video():
    url = url_entry.get()
    quality = quality_combobox.get()
    format_choice = format_combobox.get()
    
    try:
        yt = YouTube(url)
        
        if format_choice == "mp4":
            streams = yt.streams.filter(progressive=True, file_extension="mp4", res=quality)
        elif format_choice == "mp3":
            download_mp3(url)
            return
        
        if streams:
            stream = streams.first()
            download_status_label.config(text="Téléchargement...")
            stream.download(output_path=download_path)
            download_status_label.config(text="Téléchargement fini")
        else:
            download_status_label.config(text="Aucun flux correspondant trouvé")
    except Exception as e:
        download_status_label.config(text="Une Erreur est survenue: " + str(e))

def download_mp3(url):
    download_path = download_path_label["text"][23:]  # Get the previously set download path
    try:
        command = f'youtube-dl -x --audio-format mp3 -o "{download_path}/%(title)s.%(ext)s" {url}'
        subprocess.call(command, shell=True)
        download_status_label.config(text="Téléchargement fini")
    except Exception as e:
        download_status_label.config(text="Une Erreur est survenue: " + str(e))

def set_download_path():
    global download_path
    download_path = filedialog.askdirectory()
    download_path_label.config(text=f"Chemin de téléchargement: {download_path}")

app = tk.Tk()
app.title("Mp4 DownloaderV1")
app.iconbitmap(get_image_path("trou.ico"))  # Chemin d'accès à l'icône

# Chemin d'accès au logo
logo_path = get_image_path("15454.jpg")

# Charger l'image du logo
logo_image = Image.open(logo_path)

# Spécifier la taille souhaitée de l'image du logo en pixels
desired_logo_size = (300, 200)
logo_image = logo_image.resize(desired_logo_size)
logo_image = ImageTk.PhotoImage(logo_image)

# Créer un widget Label pour afficher l'image du logo
logo_label = tk.Label(app, image=logo_image)
logo_label.pack()

# URL Entry
url_label = tk.Label(app, text="URL de la vidéo:")
url_label.pack(pady=10)
url_entry = tk.Entry(app, width=40, highlightthickness=1, highlightbackground="black")
url_entry.pack()

# Download Path
set_path_button = tk.Button(app, text="Définit le chemin de téléchargement", command=set_download_path)
set_path_button.pack(pady=10)
download_path_label = tk.Label(app, text="Chemin de téléchargement : non défini")
download_path_label.pack()

# Format Selection
format_label = tk.Label(app, text="Choisi le format:")
format_label.pack(pady=5)
format_combobox = ttk.Combobox(app, values=["mp4", "mp3"])
format_combobox.pack()

# Quality Selection
quality_label = tk.Label(app, text="Choisi la qualité:")
quality_label.pack(pady=5)
quality_combobox = ttk.Combobox(app, values=["1080p", "720p", "480p", "360p"])
quality_combobox.pack()

# Download Button
download_button = tk.Button(app, text="Télécharger", command=download_video)
download_button.pack(pady=20)

# Download Status Label
download_status_label = tk.Label(app, text="", fg="green")
download_status_label.pack()

# Utilisation de balises HTML pour mettre en gras le titre et contour noir
title_label = tk.Label(app, text="Création de Zxldrok", font=("Helvetica", 10), bd=1, relief="solid")
title_label.pack(pady=12)

app.mainloop()
