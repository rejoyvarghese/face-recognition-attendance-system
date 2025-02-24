from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Variables

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ==============bg image===============

        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\rejoy\Desktop\face_recognition_system\pictures\new_register.jpg")

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left image

        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\rejoy\Downloads\rohit-choudhari-cZx4tDpIwPA-unsplash.jpg")

        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # ===============main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="Register here!", font=(
            "times new roman", 20, "bold"), bg="white", fg="purple")
        register_lbl.place(x=20, y=20)

        # ============labels and entry==============

        # row 1
        fname = Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=(
            "times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)

        self.txt_lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=(
            "times new roman", 15, "bold"))
        self.txt_lname_entry.place(x=370, y=130, width=250)

        # row 2
        contact = Label(frame, text="Contact", font=(
            "times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=(
            "times new roman", 15, "bold"))
        self.txt_contact_entry.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email_entry = ttk.Entry(frame, textvariable=self.var_email, font=(
            "times new roman", 15, "bold"))
        self.txt_email_entry.place(x=370, y=200, width=250)

        # row 3

        securuty_Q = Label(frame, text="Select Security Question", font=(
            "times new roman", 15, "bold"), bg="white")
        securuty_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "Your birth place", "Your first pet", "Your favorite color")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        securuty_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white")
        securuty_A.place(x=370, y=240)

        self.txt_security_entry = ttk.Entry(frame, textvariable=self.var_securityA, font=(
            "times new roman", 15))
        self.txt_security_entry.place(x=370, y=270, width=250)

        # row 4

        pswd = tk.Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd_entry = ttk.Entry(frame, textvariable=self.var_pass, font=(
            "times new roman", 15, "bold"), show="*")  # Show '*' for password
        self.txt_pswd_entry.place(x=50, y=340, width=250)

        confirm_pswd = tk.Label(frame, text="Confirm password", font=(
            "times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd_entry = ttk.Entry(frame, textvariable=self.var_confpass, font=(
            "times new roman", 15, "bold"), show="*")  # Show '*' for password
        self.txt_confirm_pswd_entry.place(x=370, y=340, width=250)

        # ===========check button=============
        self.var_check = IntVar()

        self.checkbtn = Checkbutton(
            frame, text="I Agree with the terms and Conditions", variable=self.var_check, font=(
                "times new roman", 12, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # =============buttons==========

        img = Image.open(
            r"C:\Users\rejoy\Downloads\register-button-png-18460.png")
        img = img.resize((150, 50))
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data, image=self.photoimage,
                    borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=150)

        img1 = Image.open(
            r"C:\Users\rejoy\Downloads\login-button-png-18028.png")
        img1 = img1.resize((150, 50))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,
                    borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=150)

        # ++++++++++++++++function declarations

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Confirm your password again!")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error!", "Agree with Terms and Condition to proceed")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="rejoymysql@15", database="face_recognizer")
            my_cur = conn.cursor()
            query = "SELECT * FROM register WHERE email = %s"
            value = (self.var_email.get(),)
            my_cur.execute(query, value)
            row = my_cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already registered")
            else:
                # Specify column names in the INSERT statement
                insert_query = ("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password)"
                                " VALUES (%s, %s, %s, %s, %s, %s, %s)")
                insert_values = (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                )
                my_cur.execute(insert_query, insert_values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registered successfully")


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
