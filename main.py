from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import ttk
from tkinter import *

hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, "30 meter persegi"))
hunians.append(Rumah("Gustavo Fring", 5, 2, "80 meter persegi"))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", "30 meter persegi"))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, "95 meter persegi"))
hunians.append(Apartemen("Andria Nartanto", 2, 2, "35 meter persegi"))

root = Tk()
root.title("Praktikum DPBO Python")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    
    if hunians[index].get_jenis() == "Indekos":
        d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary() + "\nPemilik: " + hunians[index].get_nama_pemilik() + "\nPenghuni: " + hunians[index].get_nama_penghuni() + "\nLuas: " + hunians[index].get_luas_bangunan() + "\n\n" + hunians[index].get_dokumen(), anchor="w").grid(row=0, column=0, sticky="w")
    else :
        d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary() + "\nPemilik: " + hunians[index].get_nama_pemilik()+ "\nLuas: " + hunians[index].get_luas_bangunan() + "\n\n" + hunians[index].get_dokumen(), anchor="w").grid(row=0, column=0, sticky="w")

    b_exitfd = Button(d_frame, text="Exit", command=top.quit)
    b_exitfd.grid(row=6, column=2)

def about():
    top = Toplevel()
    top.title("About")

    d_frame = LabelFrame(top, text="About", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Hunians\n\n" + "Aplikasi Pendataan Hunian Sewaan\n", anchor="w").grid(row=0, column=0, sticky="w")

def add_data():
    top = Toplevel()
    top.title("Add Data")

    d_frame = LabelFrame(top, text="Add Data", padx=12, pady=12)
    d_frame.pack(padx=12, pady=12)
    
    e_jenis_hunian = StringVar()
    ttk.Label(d_frame, text="Jenis Hunian : ").grid(row=0, column=0, sticky="w")
    pilihan = ttk.Combobox(d_frame, width=20, textvariable=e_jenis_hunian)

    pilihan['values'] = ('Apartemen', 'Rumah', 'Indekos')
    pilihan.grid(row=1, column=0, sticky="w")
    pilihan.current()

    e_pemilik = Label(d_frame, text="Nama Pemilik : ").grid(row=2, column=0, sticky="w")
    e_pemilik = Entry(d_frame).grid(row=3, column=0, sticky="w")

    e_penghuni = Label(d_frame, text="Nama Penghuni : ").grid(row=4, column=0, sticky="w")
    e_penghuni = Entry(d_frame).grid(row=5, column=0, sticky="w")

    e_jml_kamar = Label(d_frame, text="Jumlah Kamar : ").grid(row=6, column=0, sticky="w")
    e_jml_kamar = Entry(d_frame).grid(row=7, column=0, sticky="w")

    e_jml_penghuni = IntVar()
    jml_penghuni = Label(d_frame, text="Jumlah Penghuni : ").grid(row=8, column=0, sticky="w")
    R1 = Radiobutton(d_frame,text="1", variable = e_jml_penghuni, value=1).grid(row=9, column=0, sticky="w")
    R2 = Radiobutton(d_frame,text="2", variable = e_jml_penghuni, value=2).grid(row=10, column=0, sticky="w")
    R3 = Radiobutton(d_frame,text="3", variable = e_jml_penghuni, value=3).grid(row=11, column=0, sticky="w")
    R4 = Radiobutton(d_frame,text="4", variable = e_jml_penghuni, value=4).grid(row=12, column=0, sticky="w")
    R5 = Radiobutton(d_frame,text="5", variable = e_jml_penghuni, value=5).grid(row=13, column=0, sticky="w")

    e_luas = Label(d_frame, text="Luas Bangunan : ").grid(row=14, column=0, sticky="w")
    e_luas = Entry(d_frame).grid(row=15, column=0, sticky="w")

    b_input = Button(d_frame, text="Add", command=lambda:tambah_data())
    b_input.grid(row=16, column=1)

    def tambah_data():
        if e_jenis_hunian == "Indekos":
            hunians.append(e_jenis_hunian(e_pemilik, e_penghuni, e_luas))
        else :
            hunians.append(e_jenis_hunian(e_pemilik, e_jml_penghuni, e_jml_kamar, e_luas))


frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", command=lambda : add_data())
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

b_exitd = Button(opts, text="About", command=lambda : about())
b_exitd.grid(row=0, column=3)

for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
