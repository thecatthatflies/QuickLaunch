import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import webbrowser

app = ttk.Window(themename="darkly")
app.title("MumBot Launcher")
app.geometry("350x575")
app.resizable(False, False)

header = ttk.Label(app, text="Hello, Mama", font=("Helvetica", 18, "bold"), anchor="center")
header.pack(pady=(20, 10))

LINKS = {
    "walmart": "https://www.walmart.com",
    "amazon": "https://www.amazon.com",
    "upwork": "https://www.upwork.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com",
    "linkedin": "https://www.linkedin.com",
    "microsoft news": "https://msn.com",
    "github": "https://github.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com"
}

def open_link(url):
    webbrowser.open(url)

for label, url in LINKS.items():
    btn = ttk.Button(
        app,
        text=label,
        bootstyle="info-outline",  # info color, outlined
        width=25,
        command=lambda url=url: open_link(url)
    )
    btn.pack(pady=10)

app.mainloop()