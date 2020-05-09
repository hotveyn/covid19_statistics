from tkinter import *
from PIL import Image as Pilimage
from PIL import ImageTk
import requests
from bs4 import BeautifulSoup


class MainWindow:
    def __init__(self, width=350, height=270):
        self.root = Tk()
        self.root.title("COVID-19 statistics")  # Window name
        self.root.geometry(f"{width}x{height}")  # Window scale(x, y coordinates)
        self.root.resizable(False, False)  # Prohibition on scaling the window
        self.root.iconbitmap("F:/covid-19_statistics/resources/icon.ico")  # Window icon
        self.root.configure(bg="#dbdbdb")  # Background color

        # Syringe image loading and processing (healthy persons)
        health_img = Pilimage.open("F:/covid-19_statistics/resources/health.ico")
        health_img = health_img.resize((40, 40), Pilimage.ANTIALIAS)
        self.health_image = ImageTk.PhotoImage(health_img)

        # Skull image upload and processing (death)
        skull_img = Pilimage.open("F:/covid-19_statistics/resources/skull.ico")
        skull_img = skull_img.resize((40, 40), Pilimage.ANTIALIAS)
        self.skull_image = ImageTk.PhotoImage(skull_img)

        # Virus image upload and processing (sick persons)
        sick_img = Pilimage.open("F:/covid-19_statistics/resources/sick.ico")
        sick_img = sick_img.resize((40, 40), Pilimage.ANTIALIAS)
        self.sick_image = ImageTk.PhotoImage(sick_img)

    def run(self):
        # Create the widgets and run main window
        self.create_widgets()
        self.root.mainloop()

    def button_actions(self):
        # When you press the scan button: parses information, changes the text on labels
        url = "https://www.worldometers.info/coronavirus"
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")
        data = s.find_all("div", class_="maincounter-number")

        sick_data = data[0].text.strip()  # Number of sick
        skull_data = data[1].text.strip()  # Number of death
        health_data = data[2].text.strip()  # Number of health persons

        self.health_label.configure(text=f"Healthy: {health_data}")
        self.sick_label.configure(text=f"Sick: {sick_data}")
        self.skull_lable.configure(text=f"Death: {skull_data}")
        self.button_scan.configure(text="Update statistics")

    def create_widgets(self):
        # Label of healthy people
        self.health_label = Label(self.root, width=270, height=28, text="No data", font="SimSan 10", bg="#f794ad",
                                  image=self.health_image, compound=LEFT)
        self.health_label.grid(row=0, column=0, pady=10)

        # Label of sick people
        self.sick_label = Label(self.root, width=270, height=28, text="No data", font="SimSan 10", bg="#a7eb31",
                                image=self.sick_image, compound=LEFT)
        self.sick_label.grid(row=1, column=0, pady=10)

        # Label of deaths from the coronavirus
        self.skull_lable = Label(self.root, width=270, height=28, text="No data", font="SimSan 10", bg="#757575",
                                 image=self.skull_image, compound=LEFT)
        self.skull_lable.grid(row=2, column=0, pady=10)

        # Scan button
        self.button_scan = Button(self.root, width=20, height=2, text="Start scan", font="SimSan 14",
                                  bg="#2ade45", activebackground="#22a836", relief=FLAT, command=self.button_actions)
        self.button_scan.grid(row=3, column=0, padx=62, pady=25)



window = MainWindow()
window.run()