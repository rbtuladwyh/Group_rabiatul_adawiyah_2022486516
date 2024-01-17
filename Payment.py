import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk

# Payment class
class Payment1(ttk.Frame):
    def __init__(self, root, show_main_menu):
        super().__init__(root)
        self.root = root
        self.show_main_menu = show_main_menu

        self.create_widgets() 

    # Create GUI 
    def create_widgets(self):

        # Frame 
        self.payment_frame = tk.LabelFrame(self, bg='#DCBAA9')
        self.payment_frame.pack(padx=20, pady=10)
        
        # Payment label and type of payment for customer to choose
        self.payment_label = ttk.Label(self.payment_frame, text="Payment Type")
        self.payment_label.pack()
        self.payment_combobox = ttk.Combobox(self.payment_frame, values= ["Online", "Cash"])
        self.payment_combobox.pack(padx= 20, pady= 20)

        # Submit button function to command insert data in MYSQL Database
        self.submit_button = ttk.Button(self.payment_frame, text="Submit", command=self.insert_data)
        self.submit_button.pack(padx= 10, pady= 10)

        # Delete/Cancel button function to command cancel the payment 
        self.delete_button = ttk.Button(self.payment_frame, text="Cancel", command=self.delete_data)
        self.delete_button.pack(padx= 10, pady= 10)

        # Back to main menu button
        self.back_button = ttk.Button(self.payment_frame, text="Back to Main Menu", command=self.back_to_main_menu)
        self.back_button.pack(padx= 10, pady= 10)

        # Frame for Thank You! for Booking with us 
        self.thank_frame = tk.LabelFrame(self, bg='#DCBAA9')
        self.thank_frame.pack(padx= 10, pady= 10)
        thank_label = ttk.Label(self.thank_frame, text= "Thank You! for Booking with us", font=("Hopeful Christmas Solid", 20, "bold"))
        thank_label.pack(padx= 10, pady= 10)

        # Frame for bye image 
        self.yay= tk.Frame(self, bg='#DCBAA9')
        self.yay.pack(padx= 10, pady=10)
        self.yay_frame = tk.LabelFrame(self.yay, text='')
        self.yay_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)                                    
        self.image_yay = Image.open('ASSIGNMENT GROUP/bye_pic.png') 
        self.image_yay= ImageTk.PhotoImage(self.image_yay)
        # Create a label to display the image for bye image
        image_label = tk.Label(self.yay_frame, image=self.image_yay)
        image_label.grid(row=1, column=0, padx=10, pady=5)
        
    # Insert data into MYSQL Database
    def insert_data(self):
        payment = self.payment_combobox.get()


        mydb = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="",  
            database="hotel_booking" 
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO payment (Payment_type) VALUES (%s)"
        val = (payment)
        mycursor.execute(sql, (val,))

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        mycursor.close()
        mydb.close()

    def delete_data(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_booking"
        )

        mycursor = mydb.cursor()

        # Get the total count of rows in the database
        mycursor.execute("SELECT COUNT(*) FROM payment")
        count = mycursor.fetchone()[0]

        if count > 0:
            # Delete the last row in the database
            sql = "DELETE FROM payment ORDER BY Payment_type DESC LIMIT 1"
            mycursor.execute(sql)
            mydb.commit()
            print("Last record deleted.")
        else:
            print("No records to delete.")

        mycursor.close()
        mydb.close()

    def back_to_main_menu(self):
        self.pack_forget()
        self.show_main_menu()

