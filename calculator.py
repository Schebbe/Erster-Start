import tkinter as tk
from tkinter import messagebox

# Hauptfenster einrichten im Cyberpunk-Stil
root = tk.Tk()
root.title("CyberCalc v1.0 // Cyberpunk")
root.geometry("350x520")
root.configure(bg="#0c0714")  # Tiefes Cyber-Dunkelviolett
root.resizable(False, False)

# Globale Variable für den Rechenausdruck
expression = ""

# Funktion, um Zahlen/Operatoren hinzuzufügen
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Funktion für das Endergebnis (=)
def equalpress():
    global expression
    try:
        # eval berechnet den String-Ausdruck automatisch
        total = str(eval(expression.replace('×', '*').replace('÷', '/')))
        equation.set(total)
        expression = total  # Ergebnis für Folgeberechnungen speichern
    except ZeroDivisionError:
        equation.set("SYS_ERR: / 0")
        expression = ""
    except:
        equation.set("SYS_ERR")
        expression = ""

# Funktion zum kompletten Löschen (C)
def clear():
    global expression
    expression = ""
    equation.set("0")

# Funktion für Backspace (Letztes Zeichen löschen)
def backspace():
    global expression
    expression = expression[:-1]
    if expression == "":
        equation.set("0")
    else:
        equation.set(expression)

# Variable für das Display-Textfeld
equation = tk.StringVar()
equation.set("0")

# Display-Bereich (Ausgabefeld)
display_frame = tk.Frame(root, bg="#0c0714", highlightbackground="#ff007f", highlightthickness=1)
display_frame.pack(expand=True, fill="both", padx=15, pady=15)

display_label = tk.Label(
    display_frame, 
    textvariable=equation, 
    anchor="e", 
    bg="#140b24",  # Etwas helleres Violett fürs Display
    fg="#39ff14",  # Neon-Grün (Hacker-Terminal-Stil)
    font=("Courier New", 28, "bold"),
    padx=15
)
display_label.pack(expand=True, fill="both")

# Tasten-Layout und Design
button_frame = tk.Frame(root, bg="#0c0714")
button_frame.pack(expand=True, fill="both", padx=15, pady=10)

# Cyberpunk Farb-Palette:
# #00f0ff = Neon Cyan
# #ff007f = Neon Pink / Magenta
# #39ff14 = Neon Grün
# #1a0f30 = Dunkles Tasten-Violett

buttons = [
    ('C', 0, 0, '#ff007f', clear), ('⌫', 0, 1, '#ff007f', backspace), ('%', 0, 2, '#1a0f30', lambda: press('%')), ('÷', 0, 3, '#00f0ff', lambda: press('÷')),
    ('7', 1, 0, '#1a0f30', lambda: press(7)), ('8', 1, 1, '#1a0f30', lambda: press(8)), ('9', 1, 2, '#1a0f30', lambda: press(9)), ('×', 1, 3, '#00f0ff', lambda: press('×')),
    ('4', 2, 0, '#1a0f30', lambda: press(4)), ('5', 2, 1, '#1a0f30', lambda: press(5)), ('6', 2, 2, '#1a0f30', lambda: press(6)), ('-', 2, 3, '#00f0ff', lambda: press('-')),
    ('1', 3, 0, '#1a0f30', lambda: press(1)), ('2', 3, 1, '#1a0f30', lambda: press(2)), ('3', 3, 2, '#1a0f30', lambda: press(3)), ('+', 3, 3, '#00f0ff', lambda: press('+')),
    ('0', 4, 0, '#1a0f30', lambda: press(0)), (',', 4, 2, '#1a0f30', lambda: press('.')), ('=', 4, 3, '#39ff14', equalpress)
]

# Grid für Buttons konfigurieren
for i in range(5):
    button_frame.rowconfigure(i, weight=1)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# Buttons dynamisch erstellen und platzieren
for (text, row, col, bg_color, cmd) in buttons:
    colspan = 2 if text == '0' else 1
    
    # Textfarbe anpassen (Zahlen in Cyan, Funktionstasten schwarz für besseren Kontrast)
    fg_color = "#ffffff"
    if bg_color == '#1a0f30' and text not in ['%', ',']:
        fg_color = "#00f0ff"  # Zahlen leuchten Cyan
    elif bg_color in ['#ff007f', '#39ff14', '#00f0ff']:
        fg_color = "#000000"  # Kontrast für Neon-Buttons
        
    btn = tk.Button(
        button_frame, 
        text=text, 
        bg=bg_color, 
        fg=fg_color, 
        font=("Courier New", 16, "bold"),
        border=1,
        relief="flat",
        highlightbackground="#ff007f",
        cursor="hand2",
        command=cmd,
        activebackground="#ff007f" if bg_color == '#1a0f30' else "#ffffff"
    )
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Programm starten
root.mainloop()
