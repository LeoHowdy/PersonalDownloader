
# 🎥 LEOAMOTA YouTube Downloader

Um aplicativo leve e simples para baixar vídeos do YouTube em alta qualidade, com vídeo e áudio integrados, sem necessidade de instalação do FFmpeg.

## 🚀 Funcionalidades

- Não coleta dados!
- Baixa vídeos com **áudio e vídeo combinados** (sem múltiplos arquivos).
- Interface gráfica intuitiva com **Tkinter**.
- Mostra **barra de progresso**, **tamanho do arquivo** e **velocidade de download**.
- Botão para **colar link da área de transferência**.
- Permite selecionar a **pasta de destino**.
- Já inclui o **FFmpeg embutido**, pronto para uso em qualquer computador com Windows.

## 📦 Download

> ✅ A versão empacotada está disponível em formato `.exe` para Windows.  
> 🧊 FFmpeg já está incluso no executável – **não é necessário instalar separadamente!**

🔗 [Clique aqui para baixar via Google Drive](https://drive.google.com/YOUR_LINK_AQUI)  
*(adicione o link real ao seu Drive)*

---

## 📷 Capturas de tela

[GsrI5uMWEAAQstn](https://github.com/user-attachments/assets/b7ecf2d2-72c5-4a6e-b95b-e4125cfc427a)


## 🛠 Como foi feito

- Linguagem: **Python 3**
- Bibliotecas:
  - [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
  - [`tkinter`](https://docs.python.org/3/library/tkinter.html)
  - [`requests`](https://docs.python-requests.org/)
- Empacotado com: [`PyInstaller`](https://pyinstaller.org/)
- FFmpeg embutido: versão estática localizada na pasta `ffmpeg/bin`

---

## 🧪 Como compilar manualmente

Para desenvolvedores que desejam compilar por conta própria:

1. Instale as dependências:

```bash
pip install yt-dlp requests
```

2. Execute:

```bash
python downloader_gui_max_2.0.py
```

3. Para empacotar em `.exe` (Windows):

```bash
pyinstaller --noconsole --onefile --icon="icone.ico" --add-data "ffmpeg;ffmpeg" downloader_gui_max_2.0.py
```

> ⚠️ Certifique-se de que `ffmpeg` esteja na pasta correta e o caminho do `--add-data` esteja correto (no Windows, use `;`, no Linux/Mac, use `:`)

---

## 🛡️ Segurança

Este aplicativo é seguro e **não coleta nenhum dado**.  
Alguns antivírus podem acusar falsos positivos por ser um executável não assinado digitalmente. Para evitar isso, você pode assinar com certificado digital próprio (opcional).

---

## 👨‍💻 Autor

**LEOAMOTA**  
Desenvolvedor autodidata focado em soluções práticas com Python.  
[GitHub](https://github.com/seuusuario) • [YouTube](https://youtube.com/...) *(opcional)*

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** – sinta-se livre para usar, modificar e distribuir com os devidos créditos.
