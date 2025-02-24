from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(
            r"C:\Users\rejoy\Desktop\face_recognition_system\pictures\help.jpg")
        img_top = img_top.resize((1530, 790))
        self.photoimg_left = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=1530, height=790)

        dev_label = Label(f_lbl, text="Email:rejoyvarghese15@gmail.com",
                          font=("times new roman", 12, "bold"), bg="white")
        # Adjust row and column indices as needed
        dev_label.place(x=670, y=260)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
