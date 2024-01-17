import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

class Registration1(tk.Frame):
    def __init__(self, root="", show_main_menu=None):
        super().__init__()
        self.root = root
        self.show_main_menu = show_main_menu

        self.create_widgets()

        self.current_page = None

    def insert_data(self):
        accepted = self.accept_var.get()

        if accepted=="Accepted":
            #User info
            First_Name = self.first_name_entry.get()
            Last_Name = self.last_name_entry.get()

            if First_Name and Last_Name:
                Title = self.title_combobox.get()
                Email = self.email_entry.get()
                Phone_Number = self.phone_number_entry.get()
                Terms_Accepted = self.accept_var.get()

                #Connect to MySQL
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="hotel_booking"
                )

                mycursor = mydb.cursor()

                sql = "INSERT INTO registration (First_Name, Last_Name, Title, Email, Phone_Number, Terms_Accepted) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (First_Name, Last_Name, Title, Email, Phone_Number, Terms_Accepted)
                mycursor.execute(sql, val)

                mydb.commit()

                print(mycursor.rowcount, "record inserted.")

                mycursor.close()
                mydb.close()
            else:
                tk.messagebox.showwarning(title="Error", message="First Name and Last Name are required.")
        else:
            tk.messagebox.showwarning(title="Error", message="You have not accepted the terms and conditiion!!")

    def update_data(self):
        # Get the ID of the record to be updated (you may replace '1' with the actual ID
        First_Name = self.first_name_entry.get()
        Last_Name = self.last_name_entry.get()
        Title = self.title_combobox.get()
        Email = self.email_entry.get()
        Phone_Number = self.phone_number_entry.get()
        Terms_Accepted = self.accept_var.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_booking"
        )

        mycursor = mydb.cursor()

        # Get the total count of rows in the database
        mycursor.execute("SELECT COUNT(*) FROM registration")
        count = mycursor.fetchone()[0]

        if count > 0:
            # Update the last row in the database
            sql = "UPDATE registration SET First_Name = %s, Last_Name =%s, Title = %s, Email = %s, Phone_Number = %s, Terms_Accepted = %s ORDER BY First_Name DESC LIMIT 1"
            val = (First_Name, Last_Name, Title, Email, Phone_Number, Terms_Accepted)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Last record updated.")
        else:
            print("No records to update.")

        mycursor.close()
        mydb.close()

    def create_widgets(self):

        self.configure(bg='#DCBAA9')

        self.lobby = tk.Label(self, text='Welcome To Chippi Chip Hotel !!', font= ("Times New Roman", 20))
        self.lobby.pack()

        self.pop= tk.Frame(self)
        self.pop.pack(padx=10, pady=10)

        self.pop_frame = tk.LabelFrame(self.pop, text='')
        self.pop_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)
                                             
        self.image_lobby = Image.open('ASSIGNMENT GROUP/lobby2.png')  # Use the correct path
        self.image_lobby= ImageTk.PhotoImage(self.image_lobby)

        # Create a label to display the image for single room
        image_label = tk.Label(self.pop_frame, image=self.image_lobby)
        image_label.grid(row=1, column=0, padx=10, pady=5)

        self.frame = tk.Frame(self)
        self.frame.pack()

        # Frame for registration and update
        self.user_info_frame = tk.LabelFrame(self, text="REGISTRATION", font= ("Arial Narrow", 10), padx=10, pady=10)
        self.user_info_frame.configure(bg='#B99095')

        # Entry and Label widgets
        self.first_name_label = tk.Label(self.user_info_frame, text="First Name:", bg='#B99095')
        self.first_name_entry = tk.Entry(self.user_info_frame)
        self.last_name_label = tk.Label(self.user_info_frame, text="Last Name:", bg='#B99095')
        self.last_name_entry = tk.Entry(self.user_info_frame)
        self.title_label = tk.Label(self.user_info_frame, text="Title:", bg='#B99095')
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=["Mr.", "Ms.", "Dr."])

        self.email_label = tk.Label(self.user_info_frame, text="Email:", bg='#B99095')
        self.email_entry = tk.Entry(self.user_info_frame)
        self.phone_number_label = tk.Label(self.user_info_frame, text="Phone Number:", bg='#B99095')
        self.phone_number_entry = tk.Entry(self.user_info_frame)

        # Grid layout within the registration frame
        self.first_name_label.grid(row=0, column=0, pady=5)
        self.first_name_entry.grid(row=1, column=0, pady=5)
        self.last_name_label.grid(row=0, column=1, pady=5)
        self.last_name_entry.grid(row=1, column=1, pady=5)
        self.title_label.grid(row=2, column=0, pady=5)
        self.title_combobox.grid(row=3, column=0, pady=5)
        self.email_label.grid(row=2, column=1, pady=5)
        self.email_entry.grid(row=3, column=1, pady=5)
        self.phone_number_label.grid(row=4, column=0, pady=5)
        self.phone_number_entry.grid(row=5, column=0, pady=5)

        # Pack the registration frame
        self.user_info_frame.pack(padx=20, pady=5)

        self.terms = tk.Frame(self)
        self.terms.pack()

        self.terms_frame =tk.LabelFrame(self.terms, text="")
        self.terms_frame.configure(bg='#B99095')
        self.terms_frame.grid(row=0, column=0, padx=5, pady=5)


        # Accept terms 
        terms_label = tk.Label(self.terms_frame, text= "Terms & Conditions", bg='#B99095')
        terms_label.grid(row= 1, column= 0,padx= 5, pady= 5)
        
        

        self.accept_var = tk.StringVar(value="Not Accepted")
        terms_check = tk.Checkbutton(self.terms_frame, text= "I accept the terms and conditions.",
                                        variable= self.accept_var, onvalue= "Accepted", offvalue= "Not Accepted", bg='#B99095')
        terms_check.grid(row= 1, column= 1, padx=5, pady=5)

        self.box = tk.Frame(self)
        self.box.pack()

        # Frame for registration and update
        self.button_frame = tk.LabelFrame(self.box, text="", padx=20, pady=10)
        self.button_frame.configure(bg='#B99095')

        # Register button
        self.register_button = tk.Button(self.button_frame, text="Submit", command=self.insert_data)

        # Update button
        self.update_button = tk.Button(self.button_frame, text="Update", command=self.update_data)

        # Back to main menu button
        self.back_button = ttk.Button(self.button_frame, text="Back to Main Menu", command=self.back_to_main_menu)

        # Grid layout within button frame
        self.register_button.grid(row=0, column=0, padx=10, pady=10)
        self.update_button.grid(row=0, column=1, padx=10, pady=10)
        self.back_button.grid(row= 0, column= 2)

        # Pack the button frame
        self.button_frame.pack(padx=5, pady=5)


        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def back_to_main_menu(self):
        self.pack_forget()
        self.show_main_menu()

