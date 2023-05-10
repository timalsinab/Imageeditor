# Create a Tkinter window
from tkinter import *
from tkinter import  ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

from PIL import Image,ImageTk, ImageFilter, ImageEnhance, ImageOps

import os

class PhotoEditor:
    def __init__(self,canvas2):
        self.canvas2 = canvas2
        self.v1 = None
        self.v2 = None
        self.v3 = None
        self.rotate_combo = None
        self.flip_combo = None
        self.img_path = None
        self.border_combo = None
        self.imgg = None
        self.img = None
        self.img1 = None
        self.img2 = None
        self.img3 = None
        self.img4 = None
        self.img5 = None
        self.img6 = None
        self.img7 = None
        self.img8 = None
        self.img9 = None
        self.img10 = None
        self.img11 = None
        self.img12 = None

    def select(self):

        self.img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        self.img = Image.open(self.img_path)
        self.img.thumbnail((350, 350))
        self.img1 = ImageTk.PhotoImage(self.img)
        self.canvas2.create_image(300, 210, image=self.img1)
        self.canvas2.image = self.img1

    def blur(self,event):
        for m in range(0, self.v1.get()+1):
            self.img = Image.open(self.img_path)
            self.img.thumbnail((350, 350))
            self.imgg = self.img.filter(ImageFilter.BoxBlur(m))
            self.img1 = ImageTk.PhotoImage(self.imgg)
            self.canvas2.create_image(300, 210, image=self.img1)
            self.canvas2.image = self.img1

    def brightness(self, event):

        for m in range(0, self.v2.get()+1):
            self.img = Image.open(self.img_path)
            self.img.thumbnail((350, 350))
            self.imgg = ImageEnhance.Brightness(self.img)
            self.img2 = self.imgg.enhance(m)
            self.img3 = ImageTk.PhotoImage(self.img2)
            self.canvas2.create_image(300, 210, image=self.img3)
            self.canvas2.image = self.img3

    def contrast(self, event):
        for m in range(0, self.v3.get() + 1):
            self.img = Image.open(self.img_path)
            self.img.thumbnail((350, 350))
            self.imgg = ImageEnhance.Contrast(self.img)
            self.img4 = self.imgg.enhance(m)
            self.img5 = ImageTk.PhotoImage(self.img4)
            self.canvas2.create_image(300, 210, image=self.img5)
            self.canvas2.image = self.img5


    def rotatephoto(self,event):
        self.img = Image.open(self.img_path)
        self.img.thumbnail((350, 350))
        self.img6 = self.img.rotate(int(self.rotate_combo.get()))
        self.img7 = ImageTk.PhotoImage(self.img6)
        self.canvas2.create_image(300, 210, image=self.img7)
        self.canvas2.image = self.img7

    def flipphoto(self,event):
        self.img = Image.open(self.img_path)
        self.img.thumbnail((350, 350))
        if self.flip_combo.get() == "FLIP_LEFT_RIGHT":
            self.img8 = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        elif self.flip_combo.get() == "FLIP TOP TO BOTTOM":
            self.img8 = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        self.img9 = ImageTk.PhotoImage(self.img8)
        self.canvas2.create_image(300, 210, image=self.img9)
        self.canvas2.image = self.img9

    def addborder(self,event):
        self.img = Image.open(self.img_path)
        self.img.thumbnail((350, 350))
        self.img10 = ImageOps.expand(self.img, border=int(self.border_combo.get()), fill=95)
        self.img11 = ImageTk.PhotoImage(self.img10)
        self.canvas2.create_image(300, 210, image=self.img11)
        self.canvas2.image = self.img11

    def save(self):
        pass
        ext = self.img_path.split(".")[-1]
        file = asksaveasfilename(defaultextension=f".{ext}", filetypes=[(
            "All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
        if file:
            if self.canvas2.image == self.img1:
                self.imgg.save(file)
            elif self.canvas2.image == self.img3:
                self.img2.save(file)
            elif self.canvas2.image == self.img5:
                self.img4.save(file)
            elif self.canvas2.image == self.img7:
                self.img6.save(file)
            elif self.canvas2.image == self.img9:
                self.img8.save(file)
            elif self.canvas2.image == self.img11:
                self.img10.save(file)






def main():
    # Create a Tkinter window
    root = Tk()  # Create a window
    root.title("Photo Editor")  # Set the title of the window
    root.geometry("640x640")  # Set the size of the window
    print("This s the main function")
    # Create the window here
    # create canvas to display image
    canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)

    canvas2.place(x=15, y=150)
    myPhotoEditor = PhotoEditor(canvas2 = canvas2)

    blurr = Label(root, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
    blurr.place(x=15,
                y=8)  # Following the placement of objects on the screen, the blurr command is being placed at these respective coordinates
    v1 = IntVar()
    myPhotoEditor.v1 = v1
    scale1 = ttk.Scale(root, from_=0, to=10, variable=myPhotoEditor.v1,
                       orient=HORIZONTAL, command=myPhotoEditor.blur)
    scale1.place(x=150, y=10)
    bright = Label(root, text="Brightness:", font=("ariel 17 bold"))
    bright.place(x=8, y=50)
    v2 = IntVar()
    myPhotoEditor.v2 = v2
    scale2 = ttk.Scale(root, from_=0, to=10, variable=myPhotoEditor.v2,
                       orient=HORIZONTAL, command=myPhotoEditor.brightness)
    scale2.place(x=150, y=55)
    contrast = Label(root, text="Contrast:",
                     font=("ariel 17 bold"))  # Line of code makes the contrast lebel to appear on the menu
    contrast.place(x=35, y=92)
    v3 = IntVar()
    myPhotoEditor.v3 = v3
    scale3 = ttk.Scale(root, from_=0, to=10, variable=myPhotoEditor.v3,
                       orient=HORIZONTAL,
                       command=myPhotoEditor.contrast)  # Orient creates a horizontal space on the menu bar for the user to interact with
    scale3.place(x=150, y=100)
    rotate = Label(root, text="Rotate:", font=("ariel 17 bold"))
    rotate.place(x=370, y=8)
    values = [0, 90, 180, 270, 360]
    rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
    myPhotoEditor.rotate_combo = rotate_combo
    rotate_combo.place(x=460, y=15)
    rotate_combo.bind("<<ComboboxSelected>>",
                      myPhotoEditor.rotatephoto)  # Bind makes the user instructions to be implemented immediately as they are given

    flip = Label(root, text="Flip:", font=("ariel 17 bold"))
    flip.place(x=400, y=50)
    values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
    flip_combo = ttk.Combobox(root, values=values1, font=('ariel 10 bold'))
    myPhotoEditor.flip_combo = flip_combo
    flip_combo.place(x=460, y=57)
    flip_combo.bind("<<ComboboxSelected>>", myPhotoEditor.flipphoto)
    border = Label(root, text="Add border:", font=("ariel 17 bold"))
    border.place(x=320, y=92)
    values2 = [i for i in range(10, 45, 5)]
    border_combo = ttk.Combobox(root, values=values2, font=("ariel 10 bold"))
    myPhotoEditor.border_combo = border_combo
    border_combo.place(x=460, y=99)
    border_combo.bind("<<ComboboxSelected>>", myPhotoEditor.addborder)




    btn1 = Button(root, text="Select Image", bg='black', fg='gold',
                  font=('ariel 15 bold'), relief=GROOVE, command=myPhotoEditor.select)
    btn1.place(x=100, y=595)
    btn2 = Button(root, text="Save", width=12, bg='black', fg='gold',
                  font=('ariel 15 bold'), relief=GROOVE)
    btn2.place(x=280, y=595)
    btn3 = Button(root, text="Exit", width=12, bg='black', fg='gold',
                  font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
    btn3.place(x=460, y=595)

    # modifying the pictures in the class
    root.mainloop()

main()
