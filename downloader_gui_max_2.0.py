import os
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL
import requests

# Função para localizar arquivos mesmo dentro do .exe
def resource_path(relative_path):
    """Retorna o caminho absoluto, mesmo quando empacotado com PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.getcwd(), relative_path)

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LEOMOTA YouTube Video Downloader")

        # URL do vídeo
        self.url_label = tk.Label(root, text="URL do vídeo:")
        self.url_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.url_entry = tk.Entry(root, width=60)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        self.paste_button = tk.Button(root, text="Colar Link", command=self.paste_url)
        self.paste_button.grid(row=0, column=2, padx=5, pady=5)

        # Pasta de destino
        self.path_label = tk.Label(root, text="Pasta de destino:")
        self.path_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.path_entry = tk.Entry(root, width=60)
        self.path_entry.grid(row=1, column=1, padx=5, pady=5)

        self.browse_button = tk.Button(root, text="Escolher Pasta", command=self.select_path)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)

        # Barra de progresso
        self.progress_label = tk.Label(root, text="Progresso:")
        self.progress_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.progress = tk.Label(root, text="0% (0MB de 0MB)")
        self.progress.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # Velocidade
        self.speed_label = tk.Label(root, text="Velocidade: 0 KB/s")
        self.speed_label.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        # Botão de download
        self.download_button = tk.Button(root, text="Baixar", command=self.start_download_thread)
        self.download_button.grid(row=4, column=1, pady=10)

    def paste_url(self):
        try:
            clipboard = self.root.clipboard_get()
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, clipboard)
        except tk.TclError:
            pass

    def select_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)

    def start_download_thread(self):
        thread = threading.Thread(target=self.download_video)
        thread.start()

    def download_video(self):
        url = self.url_entry.get()
        path = self.path_entry.get()

        if not url or not path:
            messagebox.showwarning("Aviso", "Por favor, insira a URL e selecione a pasta de destino.")
            return

        def progress_hook(d):
            if d.get('status') == 'downloading':
                percent = d.get('_percent_str', '').strip()
                downloaded = d.get('_downloaded_bytes_str', '0').strip()
                total = d.get('_total_bytes_str', '0').strip()
                speed = d.get('_speed_str', '0 KB/s').strip()
                self.progress.config(text=f"{percent} ({downloaded} de {total})")
                self.speed_label.config(text=f"Velocidade: {speed}")

        ydl_opts = {
            'ffmpeg_location': resource_path('ffmpeg/bin/ffmpeg.exe'),
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'format': 'bestvideo+bestaudio/best',
            'progress_hooks': [progress_hook],
            'noplaylist': True
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Concluído", "Download concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro durante o download: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()
