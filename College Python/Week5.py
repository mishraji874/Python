import tkinter as tk


class ContactList:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact List")

        # Create listbox to display contacts
        self.listbox = tk.Listbox(self.master, width=40)
        self.listbox.grid(row=0, column=0, padx=10, pady=10)

        # Create labels and entry widgets for contact details
        tk.Label(self.master, text="Last Name").grid(row=1, column=0, padx=5, pady=5)
        self.last_name_entry = tk.Entry(self.master)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.master, text="First Name").grid(row=2, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(self.master)
        self.first_name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.master, text="Email").grid(row=3, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.master, text="Phone").grid(row=4, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=4, column=1, padx=5, pady=5)

        # Create button to add a new contact
        self.add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, column=1, padx=5, pady=5)

        # Create button to delete selected contact
        self.delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=1, padx=5, pady=5)

        # Populate listbox with sample contacts
        self.contacts = [
            {"last_name": "Doe", "first_name": "John", "email": "johndoe@example.com", "phone": "555-1234"},
            {"last_name": "Smith", "first_name": "Jane", "email": "janesmith@example.com", "phone": "555-5678"}
        ]
        self.display_contacts()

    def display_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact['last_name']}, {contact['first_name']}")

    def add_contact(self):
        contact = {
            "last_name": self.last_name_entry.get(),
            "first_name": self.first_name_entry.get(),
            "email": self.email_entry.get(),
            "phone": self.phone_entry.get()
        }
        self.contacts.append(contact)
        self.display_contacts()

    def delete_contact(self):
        selection = self.listbox.curselection()
        if selection:
            del self.contacts[selection[0]]
            self.display_contacts()


root = tk.Tk()
app = ContactList(root)
root.mainloop()