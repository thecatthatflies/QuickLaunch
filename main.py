import subprocess, sys
try:
    import ttkbootstrap as ttk
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "ttkbootstrap"])
    import ttkbootstrap

from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.dialogs import Messagebox
import webbrowser, json, os
from tkinter import filedialog

LINKS_FILE = "links.json"
MAX_LINKS = 20
THEMES = ["morph", "darkly", "superhero", "solar", "litera", "cyborg", "pulse", "flatly", "journal", "minty"]

def load_links():
    if os.path.exists(LINKS_FILE):
        with open(LINKS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_links():
    with open(LINKS_FILE, "w") as f:
        json.dump(LINKS, f, indent=2)

LINKS = load_links()
CURRENT_THEME = "morph"
app = ttk.Window(themename=CURRENT_THEME)
app.title("QuickLaunch")
app.geometry("420x670")
app.resizable(True, True)

def open_link(url):
    webbrowser.open(url)

def refresh_buttons():
    for widget in app.winfo_children():
        widget.destroy()

    ttk.Label(app, text="QuickLaunch", font=("Helvetica", 20, "bold")).pack(pady=(25, 15))

    if LINKS:
        for name, url in LINKS.items():
            btn = ttk.Button(app, text=name, bootstyle="info-outline", width=32, command=lambda url=url: open_link(url))
            btn.pack(pady=5)
    else:
        ttk.Label(app, text="✨ No links yet — add some!", font=("Helvetica", 12, "italic")).pack(pady=60)

    ttk.Label(app, text="Press M to open menu", font=("Arial", 10), anchor="center").pack(side="bottom", pady=10)

def open_menu():
    menu = ttk.Toplevel(app)
    menu.title("Settings")
    menu.geometry("390x575")
    menu.resizable(False, False)

    ttk.Label(menu, text="Add New Link", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
    name_entry = ttk.Entry(menu, width=30)
    name_entry.pack(pady=5)
    name_entry.focus()
    url_entry = ttk.Entry(menu, width=30)
    url_entry.pack(pady=5)

    add_btn = ttk.Button(menu, text="Add Link", bootstyle="success-outline")

    def add_link():
        if len(LINKS) >= MAX_LINKS:
            Messagebox.show_info("Max links reached (20).", "Limit reached")
            return

        name = name_entry.get().strip().title()
        url = url_entry.get().strip()
        if name and url:
            LINKS[name] = url
            save_links()
            refresh_buttons()
            name_entry.delete(0, 'end')
            url_entry.delete(0, 'end')
            remove_entry['values'] = list(LINKS.keys())
            Messagebox.ok("Link added!")

    add_btn.config(command=add_link)
    add_btn.pack(pady=6)
    ToolTip(add_btn, text="Adds a new site to your launcher")

    ttk.Label(menu, text="Remove Link", font=("Helvetica", 12, "bold")).pack(pady=(25, 5))
    remove_entry = ttk.Combobox(menu, values=list(LINKS.keys()), width=30)
    remove_entry.pack(pady=5)

    def remove_link():
        name = remove_entry.get().strip()
        if name in LINKS:
            confirm = Messagebox.yesno(f"Remove link: {name}?", "Confirm delete")
            if confirm == "Yes":
                del LINKS[name]
                save_links()
                refresh_buttons()
                remove_entry['values'] = list(LINKS.keys())
                remove_entry.set("")
                Messagebox.ok("Link removed.")

    remove_btn = ttk.Button(menu, text="Remove Selected", bootstyle="danger-outline", command=remove_link)
    remove_btn.pack(pady=6)
    ToolTip(remove_btn, text="Deletes the selected link")

    ttk.Label(menu, text="App Theme", font=("Helvetica", 12, "bold")).pack(pady=(30, 5))
    theme_selector = ttk.Combobox(menu, values=THEMES, width=27)
    theme_selector.set(app.style.theme.name)
    theme_selector.pack(pady=5)

    def change_theme():
        selected = theme_selector.get()
        if selected in THEMES:
            app.style.theme_use(selected)
            Messagebox.ok("Theme applied!")

    ttk.Button(menu, text="Apply Theme", bootstyle="info-outline", command=change_theme).pack(pady=6)

    ttk.Label(menu, text="Import / Export Links (please save as links.json)", font=("Helvetica", 12, "bold")).pack(pady=(25, 5))

    def export_links():
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
        if path:
            with open(path, "w") as f:
                json.dump(LINKS, f, indent=2)
            Messagebox.ok("Links exported!")

    def import_links():
        path = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
        if path:
            with open(path, "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    LINKS.update(data)
                    save_links()
                    refresh_buttons()
                    remove_entry['values'] = list(LINKS.keys())
                    Messagebox.ok("Links imported!")

    ttk.Button(menu, text="Export", bootstyle="secondary", command=export_links).pack(pady=4)
    ttk.Button(menu, text="Import", bootstyle="secondary", command=import_links).pack(pady=4)

    ttk.Label(menu, text="Close this window to return.", font=("Arial", 9)).pack(pady=(25, 10))

def key_handler(event):
    if event.char.lower() == 'm':
        open_menu()

app.bind("<Key>", key_handler)

refresh_buttons()
app.mainloop()
