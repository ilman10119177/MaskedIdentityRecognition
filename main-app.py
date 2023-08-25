import sys
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#pengaturan ukuran jendela GUI
window = Tk()
lebar = 400
tinggi = 300
x = 500
y = 100

#label
label = Label(window,text ="Rekognisi Identitas Wajah Bermasker")
label.pack(pady = 10)

#window tidak bisa di resize dan muncul ditengah
window.resizable(0,0)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

newx= int((screenwidth/2 - lebar/2))
newy= int((screenheight/2 - tinggi/2)-50)

window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")

#judul jendela
window.title("YOLOv-5 Masked Face Recognition")

#method button
def buttontest():
    result = messagebox.askyesno("Konfirmasi", "Apakah anda yakin memulai recognition?")
    if result:
        run = os.system('python "C:/Users/Lenovo X390/Desktop/maskedIdentity/detect.py" --weights "C:/Users/Lenovo X390/Desktop/maskedIdentity/best13.pt" --img 416 --conf-thres 0.7 --source 0')
    
def buttonkeluar():
    result = messagebox.askyesno("Konfirmasi", "Apakah anda yakin keluar dari Aplikasi?")
    if result:
        window.destroy()
        

def buttonpetunjuk():
    button2.config(state="normal")
    #setup secondary window
    petunjukWindow = Toplevel(window)
    petunjukWindow.resizable(0,0)
    petunjukWindow.title("Petunjuk Penggunaan Aplikasi")
    petunjukWindow.geometry("500x150+50+300")

    #Heading window
    Label(petunjukWindow,
          text ="Petunjuk Penggunaan").pack()

    #Petunjuk
    Label(petunjukWindow,text ="1. Klik pada tombol Jalankan Recognition untuk memulai proses Recognition").place(x=23, y=50)
    Label(petunjukWindow,text ="2. Tekan huruf Q untuk Menghentikan proses Recognition").place(x=23, y=70)
    Label(petunjukWindow,text ="3. Klik Tutup untuk menutup aplikasi").place(x=23, y=90)

    window.update()
    window.update_idletasks()
    window.on_closing()

#button
button1 = Button(text="Rekognisi dari Webcam", activebackground="#b9babd", command=buttontest)
button2 = Button(window, text="Petunjuk", activebackground="#b9babd", command=buttonpetunjuk)
button3 = Button(text="Keluar", activebackground="#b9babd", command=buttonkeluar)
     
button1.place(x=23, y=50, width="355", height="35")
button2.place(x=23, y=105, width="355", height="35")
button3.place(x=23, y=160, width="355", height="35")

#disable close window icon
window.protocol("WM_DELETE_WINDOW", DISABLED)

window.mainloop()