from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Background image
        bg_img = Image.open(
            r"C:\Users\rejoy\Desktop\face_recognition_system\pictures\developer.jpg")
        bg_img = bg_img.resize((1530, 790))
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        bg_lbl = Label(self.root, image=self.bg_photo)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl = Label(self.root, text="ABOUT DEVELOPER", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, relwidth=1)

        # Developer photo
        dev_img = Image.open(r"C:\Users\rejoy\Downloads\20240201_112534.jpg")
        # Rotate the image 90 degrees clockwise
        dev_img = dev_img.rotate(-90, expand=True)
        dev_img = dev_img.resize((250, 300))
        self.dev_photo = ImageTk.PhotoImage(dev_img)
        dev_lbl = Label(self.root, image=self.dev_photo, bg="white")
        dev_lbl.place(x=50, y=100)
        # Developer info
        dev_info = """Greetings,

My name is Rejoy Varghese, hailing from the picturesque town of Itarsi in the heart of Madhya Pradesh. 
I am currently embarked on a journey of academic enrichment, pursuing a Master's degree in Computer Applications 
from the esteemed Suryadatta Institute of Management & Mass Communication.

Driven by a relentless passion for technology and a fervent desire to contribute meaningfully to the realm of IT infrastructure, 
I aspire to become a DevOps engineer. With a firm commitment to continuous learning and a penchant for innovation, 
I am poised to navigate the dynamic landscape of modern software development practices.

Thank you for visiting this space, and I look forward to the exciting opportunities that lie ahead on this exhilarating journey of professional growth and exploration.

Warm regards,
Rejoy Varghese"""
        dev_info_lbl = Label(self.root, text=dev_info, font=(
            "times new roman", 16), bg="white", fg="black", justify="left", wraplength=1000)
        dev_info_lbl.place(x=350, y=100, width=1000)

        # Back button
        back_btn = Button(self.root, text="Back", command=self.back, font=(
            "times new roman", 18, "bold"), bg="blue", fg="white", cursor="hand2")
        back_btn.place(x=650, y=600)

    def back(self):
        self.root.destroy()
        # Call the main application window or any other appropriate function for navigation


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
