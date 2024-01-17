import tkinter as tk
from Registration import Registration1
from Room_Selection import Room_Selection
from Payment import Payment1
from PIL import Image, ImageTk


class MainMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry("800x800")
        self.root.configure(background="#DCBAA9")

        self.pages = {
            "Registration": Registration1(self.root, self.show_main_menu),
            "Room Selection": Room_Selection(self.root, self.show_main_menu),
            "Payment": Payment1(self.root, self.show_main_menu),
        }

        self.current_page = None

        self.create_main_menu()

    def create_main_menu(self):
        main_menu = tk.Menu(self.root)
        self.root.config(menu=main_menu)

        page_menu = tk.Menu(main_menu, tearoff=False)
        main_menu.add_cascade(label="Chippi Chip Hotel", menu=page_menu)

        for page_name, page in self.pages.items():
            page_menu.add_command(label=page_name, command=lambda p=page: self.show_page(p))

    def show_page(self, page):
        if self.current_page:
            self.current_page.pack_forget()

        self.current_page = page
        self.current_page.pack(fill='both', expand=True)

    def show_main_menu(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.create_main_menu()



if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuApp(root)
    root.mainloop()


