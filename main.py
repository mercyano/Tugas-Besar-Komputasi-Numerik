from tkinter import *
from tkinter import messagebox

BLUE = "#08d9d6"
FONT_NAME = "Segoe UI"
GRAY = "#eaeaea"

def hitung():
    try:
        t3 = float(t3_input.get())
        t2 = float(t2_input.get())
        t = float(t_input.get())
        d = float(d_input.get())

        t0 = float(t0_input.get())
        h = float(h_input.get())
    except:
        messagebox.showwarning(title="Terdapat kolom yang kosong!", message="Mohon isi kolom yang kosong!")
    
    if h == 0:
        messagebox.showwarning(title="Nilai Selang Waktu (Δt) tidak boleh 0!", message="Mohon isi nilai Selang Waktu (Δt) dengan benar!")

    x = t0 + h
    f1 = float((t3 * x ** 3) + (t2 * x ** 2) + (t * x) + d)
    f0 = float((t3 * t0 ** 3) + (t2 * t0 ** 2) + (t * t0) + d)

    kecepatan_rata = (f1-f0)/h
    hasil_label.config(text=f"{kecepatan_rata} m/s²")

window = Tk()
window.title("KALKULATOR KECEPATAN RATA-RATA")
window.maxsize(450, 450)
window.iconbitmap("img/myIcon.ico")
window.config(padx=30, pady=30, bg=BLUE)

canvas = Canvas(width=200, height=142, bg=BLUE, highlightthickness=0)
calculator_img = PhotoImage(file="img/calculator.png")
canvas.create_image(100, 71, image=calculator_img)
canvas.grid(row=0, column=0, columnspan=2)

judul_label = Label(text="Kalkulator Kecepatan Rata-Rata", font=(FONT_NAME, 13, "bold"), bg=BLUE)
judul_label.grid(row=1, column=0, columnspan=2)

instruksi_label = Label(text="Masukkan Persamaan Pergerakan Benda s(t) (at³ + bt² + ct + d):", font=(FONT_NAME, 9, "bold"), bg=BLUE)
instruksi_label.grid(row=2, column=0, columnspan=2)

t3_label = Label(text="a = ", font=(FONT_NAME, 10), bg=BLUE)
t3_label.grid(row=3, column=0)
t3_input = Entry(width=5, bg=GRAY)
t3_input.grid(row=3, column=1)

t2_label = Label(text="b = ", font=(FONT_NAME, 10), bg=BLUE)
t2_label.grid(row=4, column=0)
t2_input = Entry(width=5, bg=GRAY)
t2_input.grid(row=4, column=1)

t_label = Label(text="c  = ", font=(FONT_NAME, 10), bg=BLUE)
t_label.grid(row=5, column=0)
t_input = Entry(width=5, bg=GRAY)
t_input.grid(row=5, column=1)

d_label = Label(text="d  = ", font=(FONT_NAME, 10), bg=BLUE)
d_label.grid(row=6, column=0)
d_input = Entry(width=5, bg=GRAY)
d_input.grid(row=6, column=1)

t0_label = Label(text="Waktu awal (t₀) = ", font=(FONT_NAME, 10), bg=BLUE)
t0_label.grid(row=7, column=0)
t0_input = Entry(width=5, bg=GRAY)
t0_input.grid(row=7, column=1)

h_label = Label(text="Selang waktu (Δt) = ", font=(FONT_NAME, 10), bg=BLUE)
h_label.grid(row=8, column=0)
h_input = Entry(width=5, bg=GRAY)
h_input.grid(row=8, column=1)

kecepatan_label = Label(text="Kecepatan Rata-Rata = ", font=(FONT_NAME, 13, "bold"), bg=BLUE)
kecepatan_label.grid(row=9, column=0)
kecepatan_label.config(bg=BLUE)
hasil_label = Label(text="m/s²", font=("bold"), bg=BLUE)
hasil_label.grid(row=9, column=1)

# Button
button = Button(text="Hitung!", command=hitung, width=7, font=(FONT_NAME, 10, "bold"), bg=GRAY)
button.grid(row=10, column=1)


window.mainloop()