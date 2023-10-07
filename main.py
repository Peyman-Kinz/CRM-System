import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class CRMSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CRM System")

        # Farben definieren
        self.primary_color = "#005A9E"  # Dunkelblau
        self.secondary_color = "#FFFFFF"  # Weiß
        self.button_color = "#0088D1"  # Hellblau

        # Schriftarten definieren
        self.title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=12)
        self.button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

        # Kundeninformationen
        self.name_label = tk.Label(root, text="Name:", font=self.label_font, bg=self.secondary_color)
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(root, font=self.label_font)
        self.name_entry.pack()

        self.email_label = tk.Label(root, text="E-Mail:", font=self.label_font, bg=self.secondary_color)
        self.email_label.pack(pady=10)

        self.email_entry = tk.Entry(root, font=self.label_font)
        self.email_entry.pack()

        self.phone_label = tk.Label(root, text="Telefon:", font=self.label_font, bg=self.secondary_color)
        self.phone_label.pack(pady=10)

        self.phone_entry = tk.Entry(root, font=self.label_font)
        self.phone_entry.pack()

        # Aktionen
        self.action_frame = tk.Frame(root, bg=self.secondary_color)
        self.action_frame.pack(pady=10)

        self.add_button = tk.Button(self.action_frame, text="Kunde hinzufügen", command=self.add_customer, font=self.button_font, bg=self.button_color, fg=self.secondary_color)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(self.action_frame, text="Kunde suchen", command=self.search_customer, font=self.button_font, bg=self.button_color, fg=self.secondary_color)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(self.action_frame, text="Kunde entfernen", command=self.remove_customer, font=self.button_font, bg=self.button_color, fg=self.secondary_color)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.display_button = tk.Button(self.action_frame, text="Alle Kunden anzeigen", command=self.display_all_customers, font=self.button_font, bg=self.button_color, fg=self.secondary_color)
        self.display_button.pack(side=tk.LEFT, padx=5)

        # Kundenliste
        self.customers = []

    def add_customer(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if name and email and phone:
            customer = Customer(name, email, phone)
            self.customers.append(customer)
            messagebox.showinfo("Erfolg", f"Kunde {name} wurde erfolgreich hinzugefügt.")
            self.clear_entries()
        else:
            messagebox.showwarning("Fehler", "Bitte füllen Sie alle Felder aus.")

    def search_customer(self):
        name = self.name_entry.get()

        if name:
            for customer in self.customers:
                if customer.name == name:
                    messagebox.showinfo("Kunde gefunden",
                                        f"Name: {customer.name}\nE-Mail: {customer.email}\nTelefon: {customer.phone}")
                    self.clear_entries()
                    return
            messagebox.showinfo("Kunde nicht gefunden", f"Es wurde kein Kunde mit dem Namen {name} gefunden.")
        else:
            messagebox.showwarning("Fehler", "Bitte geben Sie den Namen des Kunden ein.")

    def remove_customer(self):
        name = self.name_entry.get()

        if name:
            for customer in self.customers:
                if customer.name == name:
                    self.customers.remove(customer)
                    messagebox.showinfo("Erfolg", f"Kunde {name} wurde erfolgreich entfernt.")
                    self.clear_entries()
                    return
            messagebox.showinfo("Kunde nicht gefunden", f"Es wurde kein Kunde mit dem Namen {name} gefunden.")
        else:
            messagebox.showwarning("Fehler", "Bitte geben Sie den Namen des Kunden ein.")

    def display_all_customers(self):
        if self.customers:
            message = ""
            for customer in self.customers:
                message += f"Name: {customer.name}\nE-Mail: {customer.email}\nTelefon: {customer.phone}\n\n"
            messagebox.showinfo("Alle Kunden", message)
        else:
            messagebox.showinfo("Keine Kunden", "Es sind keine Kunden vorhanden.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

# Hauptprogramm
root = tk.Tk()
crm_gui = CRMSystemGUI(root)
root.mainloop()
