import tkinter as tk 
from tkinter import ttk 
from tkcalendar import DateEntry 
import mysql.connector 
from PIL import Image, ImageTk


# Function connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hotel_booking")

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Class for room selection
class Room_Selection(tk.Frame):
    def __init__(self, root, show_main_menu):
        super().__init__(root)
        self.root = root
        self.show_main_menu = show_main_menu

        self.create_widgets()

    def create_widgets(self):

        # User Date for check in hotel
        self.date_label = tk.Label(self, text= "Date", foreground= "white")
        self.date_label.pack(pady= 10)
        self.date_entry = DateEntry(self, date_pattern="yyyy-mm-dd")
        self.date_label['background'] = "#A49393"
        self.date_entry.pack(padx=20, pady=10)

        # Frame for how long you want to stay
        self.d = tk.Frame(self)
        self.d.pack()
        self.d_info_frame =tk.LabelFrame(self.d, text="")
        self.d_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=20)
        self.d_info_frame.configure(background="#A49393")

        # Label and entry for customer to put how long you want to stay
        self.days_label = tk.Label(self.d, text= "how long you want to stay?")
        self.days_label.grid(row=0, column=0, padx=10, pady=10)
        self.days_entry = tk.Entry(self.d)
        self.days_entry.grid(row=0, column=1, padx=10, pady=10)

        # Prices List 
        self.select = tk.Frame(self)
        self.select.pack()
        self.select_info_frame =tk.LabelFrame(self.select, text="")
        self.select_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=20)
        self.select_info_frame.configure(background="#DCBAA9")

        # Label and entry for customer to choose your room
        self.label = tk.Label(self.select_info_frame, text='Choose Your Room', font= ("Hopeful Christmas Solid", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # Single room image
        self.image_s = Image.open('ASSIGNMENT GROUP/single.png')  # Use the correct path
        self.image_s = ImageTk.PhotoImage(self.image_s)

        # Create a label to display the image for single room
        image_label = tk.Label(self.select_info_frame, image=self.image_s)
        image_label.grid(row=1, column=0, padx=10, pady=5)

        self.select_label = tk.Label(self.select_info_frame, text="Single Room include breakfast for per pax : RM 300")
        self.select_label.grid(row=2, column=0, padx=10, pady=5)

        # Queen room image
        self.image2 = Image.open('ASSIGNMENT GROUP/queen.png')
        self.image2 = ImageTk.PhotoImage(self.image2)

        # Create a label to display the image for queen* room
        image_label = tk.Label(self.select_info_frame, image=self.image2)
        image_label.grid(row=1, column=1, padx=10, pady=5)

        self.select_label = tk.Label(self.select_info_frame, text="Queen Room include breakfast for 2 pax : RM 500")
        self.select_label.grid(row=2, column=1, padx=10, pady=5)

        # King room image
        self.image3 = Image.open('ASSIGNMENT GROUP/king.png')
        self.image3 = ImageTk.PhotoImage(self.image3)

        # Create a label to display the image for the_king room
        image_label = tk.Label(self.select_info_frame, image=self.image3)
        image_label.grid(row=3, column=0, padx=10, pady=5)

        self.select_label = tk.Label(self.select_info_frame, text="King Room include breakfast for 3 pax : RM 700")
        self.select_label.grid(row=4, column=0, padx=10, pady=5)

        # Deluxe room image
        self.image4 = Image.open('ASSIGNMENT GROUP/deluxe.png')
        self.image4 = ImageTk.PhotoImage(self.image4)

        # Create a label to display the image for Deluxe 
        image_label = tk.Label(self.select_info_frame, image=self.image4)
        image_label.grid(row=3, column=1, padx=10, pady=5)

        self.select_label = tk.Label(self.select_info_frame, text="Suite Room for maximum 5 pax : RM 1200")
        self.select_label.grid(row=4, column=1, padx=10, pady=5)

        # List of size to choose and user's total item and user can insert the number thru spinbox
        self.box = tk.Frame(self)
        self.box.pack()

        self.room_info_frame =tk.LabelFrame(self.box, text="")
        self.room_info_frame.grid(row=5, column=0, sticky="news", padx=10, pady=10)
        self.room_info_frame.configure(background="#A49393")

        self.room_label = tk.Label(self.room_info_frame, text="Select Your Room")
        self.room_combobox = ttk.Combobox(self.room_info_frame, values=["Single Room", "Queen Room", "King Room", "Suite Room"])
        self.room_label.grid(row=0, column=0, padx=20, pady=10)
        self.room_combobox.grid(row=0, column=1, padx=20, pady=10)

        self.box_two = tk.Frame(self)
        self.box_two.pack()

        self.price_info_frame =tk.LabelFrame(self.box_two, text="")
        self.price_info_frame.grid(row=0, column=0, padx=10, pady=10)

        self.label = tk.Label(self.price_info_frame, text='Total Price and Stays: ', font=("stencil", 11))
        self.label.grid(row= 1, column=0, padx=5, pady=5)
        self.output_label = tk.Label(self.price_info_frame, text="")
        self.output_label.grid(row= 1, column=1, padx=5, pady=5)


        # Frame for button
        self.button_frame = tk.LabelFrame(self)
        self.button_frame.pack(padx= 5, pady= 5)
        self.button_frame.configure(background="#67595E")

        # Submit button to command the calculation
        self.button = tk.Button(self.button_frame, text="Submit", command= self.collect_data)
        self.button.grid(row= 0, column= 0)

        # Back to main menu button
        self.back_button = ttk.Button(self.button_frame, text="Back to Main Menu", command=self.back_to_main_menu)
        self.back_button.grid(row= 0, column= 1)

        for widget in self.button_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    # Calculation function
    def collect_data(self):
        date_booking = self.date_entry.get()
        days = int(self.days_entry.get())
        room_type = self.room_combobox.get()
            
        # the price below is to defined the value from the selections
        prices = {
        "Single Room": 300,
        "Queen Room": 500,
        "King Room": 700,
        "Suite Room": 1200,
        }

        # Calculate the total price
        total_price = (prices[room_type] * days)

        # Function to insert data into table in database
        sql = "INSERT INTO room_selection (date_booking, days, room_type, total_price) VALUES (%s, %s, %s, %s)"
        val = (date_booking, days, room_type, total_price) # val = value 
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "room selection record updated.")

        self.output_label.config(text=f"Date: {date_booking}, Days: {days},  Room Selection: {days}, Total Price: RM{total_price}")
            
    # Back to main menu function
    def back_to_main_menu(self):
        self.show_main_menu()
