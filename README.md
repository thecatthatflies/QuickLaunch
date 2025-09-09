QUICKLAUNCH APP – README

Version: 1.0  
Author: thecatthatflies  
Date: July 2025

-------------------------------
ABOUT THE APP
-------------------------------
QuickLaunch is a simple, beautiful launcher that opens your favorite websites instantly — like Gmail, Amazon, Walmart, ChatGPT, LinkedIn, and more.

You can:
- Add or remove your own links
- Change the look of the app with different themes
- Resize it or open a menu by pressing the "M" key
- Save your links for next time

No login, no fluff — just fast access to what matters.

-------------------------------
HOW TO USE
-------------------------------
1. Open the app by double-clicking the .exe (on Windows) or .app (on Mac)
2. Press "M" to open the menu
3. Add or remove links and pick your favorite theme
4. That’s it — everything saves automatically!

-------------------------------
MAC INSTALL INSTRUCTIONS
-------------------------------
1. Make sure Python is installed:
   https://www.python.org/downloads/

2. Open Terminal and run:
   pip3 install pyinstaller ttkbootstrap

3. Go to the "Main Files" folder and run:
   pyinstaller --windowed --onefile --add-data "links.json:." main.py

4. Your app will appear inside the "dist" folder as `main`

-------------------------------
WINDOWS INSTALL INSTRUCTIONS
-------------------------------
1. Open Command Prompt or PowerShell

2. Run:
   pip install pyinstaller ttkbootstrap

3. Navigate to your "Main Files" folder:
   cd path\to\Main Files

4. Run:
   pyinstaller --noconsole --onefile --add-data "links.json;." main.py

5. Your app will appear inside the "dist" folder as `main.exe`

-------------------------------
NOTES
-------------------------------
• You can only save up to 20 links
• Make sure "links.json" stays in the same folder as the app while compiling
• The app does not require internet to open, but does to launch websites

-------------------------------
SUPPORT
-------------------------------
If you run into problems or want to customize this app, contact **aiyan.chowdhury41@gmail.com** for further assistance.

Enjoy!

-------------------------------
DISCLAIMER
-------------------------------
Under any circumstances, unless proven in writing and signed by the owner are you allowed to reproduce, modify, or distribute any piece of content from this repository at all.
