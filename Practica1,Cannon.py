#Importación de librerias --------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

#Definiciones -------------------------------------------------------------------------------------
def salir():
    ven.quit()
    ven.destroy()
    exit()

def caja_mensaje():
    mBox.showwarning('Mauricio Pérez Cárdenas','Ing. Sistemas Computacionales\nCaurto Semestre\nMPCompany')

def Imprimir():
    if enom.get() and ea1.get() and ea2.get() and edir.get() and enum.get() and enum2.get() and enum3.get()  != "":
        if r1.get():
            if caja.get('1.0','end-1c')!="":
                ya2()
            else:  mBox.showerror('I N F O R M A C I Ó N   I N C O M P L E T A','Faltan datos por capturar en la seccion "Extras".')
        else:
            mBox.showerror('I N F O R M A C I Ó N   I N C O M P L E T A','Faltan datos por capturar en la seccion "Extras".')
        
    else:
        mBox.showerror('I N F O R M A C I Ó N   I N C O M P L E T A','Faltan datos por capturar en la seccion "Datos Personales".')
    

def Imprimir_datos():
    if enom.get() and ea1.get() and ea2.get() and edir.get() and enum.get() and enum2.get() and enum3.get()  != "":
        boton.configure(text="Registrado :)")
        ven.configure(background="SpringGreen3")
        ya()
       
    else:
        mBox.showerror('INFORMACIÓN INCOMPLETA','Faltan datos por capturar en esta sección.')


def ya():
    reg = tk.Tk()
    reg.title("R E G I S T R A D O")
    reg.geometry("500x120")
    reg.configure(background='SeaGreen1')
    info1= tk.Label(reg, text = "NOMBRE COMPLETO:", bg='SeaGreen', fg='yellow', font=("",15,"bold italic"))
    info1.place(x=0,y=0)
    info12= tk.Label(reg, text = enom.get() + " " + ea1.get()+" "+ea2.get(),bg='black', fg='white', font=(20))
    info12.place(x=20,y=30)
    info2= tk.Label(reg, text = "DIRECCIÓN:", font=("",15,"bold italic"), bg='SeaGreen', fg='yellow')
    info21= tk.Label(reg, text =edir.get()+", " + enum.get()+", " + enum2.get()+", " + entmun3.get(), bg='black', fg='white', font=(20))
    info2.place(x=0,y=55)
    info21.place(x=20,y=85)

def imp_extra():
    ven.configure(background="dark turquoise")
    if r1.get():
        if caja.get('1.0','end-1c')!="":
            datos=""
            if c1.get() == 1:
                datos = datos + "Leer "
            if c2.get() == 1:
                datos = datos + "- Ver Peliculas "
            if c3.get() == 1:
                datos = datos + "- Redes Sociales "
            
            estado =""
            if r1.get() == 1:
                estado="Soltero"    
            if r1.get() == 2:
                estado="Casado"
            if r1.get() == 3:
                estado="Viudo"

            vacio=""

            ve=tk.Tk()
            ve.title("--> D A T O S <--")
            ve.geometry("500x120")
            ve.configure(background='dark slate gray')
            im1=tk.Label(ve, text = "TE GUSTA: ", bg='dark slate gray', fg='white', font=("",15,"italic"))
            im1.grid(column=0, row=0)
            if datos == "":
                datos = "NADA :("
            m1=tk.Label(ve, text = " " + datos, bg='dark slate gray', fg='spring green')
            m1.grid(column=2, row=0)
            im2=tk.Label(ve, text="TU ESTADO CIVIL ES:",bg='dark slate gray', fg='white', font=("",15,"italic"))
            im2.grid(column=0,row=5)
            m2=tk.Label(ve, text= estado, bg='dark slate gray', fg='spring green')
            m2.grid(column=2,row=5)
            im3=tk.Label(ve, text="OBJETIVO:",bg='dark slate gray', fg='white', font=("",15,"italic"))
            im3.grid(column=0, row=10)
            m3 = tk.Label(ve, text="--> "+ caja.get('1.0', tk.END), bg='dark slate gray', fg='spring green')
            m3.grid(column=2, row=10)

        else:
            mBox.showwarning('INFORMACIÓN INCOMPLETA','Necesitas tener un objetivo de vida.')
    else:
        mBox.showwarning('INFORMACIÓN INCOMPLETA','Necesitas capturar tu estado civil.')

def ext():
    ven.geometry("100x100")

def ya2():
    reg = tk.Tk()
    reg.title("I M P R E S I Ó N   G E N E R A L")

    reg.geometry("600x400")
    reg.configure(background='slate gray')

    ti= tk.Label(reg,text="--> DATOS PERSONALES", bg='slate gray', fg='black', font=("", 15, "bold"))
    ti.place(x=0, y=0)

    info1= tk.Label(reg, text = "NOMBRE COMPLETO:", bg='slate gray', fg='white', font=("",12,"italic"))
    info1.place(x=0,y=25)
    info12= tk.Label(reg, text = enom.get() + " " + ea1.get()+" "+ea2.get(),bg='black', fg='gold', font=(10))
    info12.place(x=80,y=50)

    info2= tk.Label(reg, text = "DIRECCIÓN:", font=("",12,"italic"), bg='slate gray', fg='white')
    info21= tk.Label(reg, text =edir.get()+", " + enum.get()+", " + enum2.get()+", " + entmun3.get(), bg='black', fg='gold', font=(10))
    info2.place(x=0,y=90)
    info21.place(x=80,y=115)

    datos=""
    if c1.get() == 1:
        datos = datos + "Leer "
    if c2.get() == 1:
        datos = datos + "- Ver Peliculas "
    if c3.get() == 1:
        datos = datos + "- Redes Sociales "
    
    estado =""
    if r1.get() == 1:
        estado="Soltero"    
    if r1.get() == 2:
        estado="Casado"
    if r1.get() == 3:
        estado="Viudo"
    
    vacio =""


    ti2= tk.Label(reg,text="--> EXTRAS", bg='slate gray', fg='black', font=("", 15, "bold"))
    ti2.place(x=0, y=150)
    im1=tk.Label(reg, text = "TE GUSTA: ",  font=("",12,"italic"), bg='slate gray', fg='white')
    im1.place(x=0, y=175)
    if datos == "":
        datos = "NADA :("
    m1=tk.Label(reg, text = " " + datos, bg='black', fg='gold', font=(10))
    m1.place(x=80, y=200)
    im2=tk.Label(reg, text="TU ESTADO CIVIL ES:", font=("",12,"italic"), bg='slate gray', fg='white')
    im2.place(x=0, y=240)
    m2=tk.Label(reg, text= estado,bg='black', fg='gold', font=(10))
    m2.place(x=80, y=265)
    im3=tk.Label(reg, text="TU OBJETIVO:", font=("",12,"italic"), bg='slate gray', fg='white')
    im3.place(x=0, y=305)
    m3=tk.Label(reg, text= caja.get('1.0', tk.END),bg='black', fg='gold', font=(10))
    m3.place(x=80, y=325)
    if caja.get('1.0', tk.END)+vacio == "":
        print("Esta vacio")
    else:
        print("no")

#Ventana PRINCIPAL-------------------------------------------------------------------------------------
ven=tk.Tk()
ven.title("---> S I S T E M A   E S C O L A R <---")
ven.geometry('400x400')

#Creacion de MENU------------------------------------
barra_menu= Menu(ven)
ven.configure(menu=barra_menu)
opcioones_menu= Menu(barra_menu)
opcioones_menu2=Menu(barra_menu)
opcioones_menu.add_command(label="Imprimir", command=Imprimir)
opcioones_menu.add_command(label="Salir", command=salir)
opcioones_menu2.add_command(label="Acerca de", command=caja_mensaje)
barra_menu.add_cascade(label="Sistema", menu=opcioones_menu)
barra_menu.add_cascade(label="Ayuda", menu=opcioones_menu2)

#Creación de Pestañas--------------------------------------------------------------------------------------
tabcontrol = ttk.Notebook(ven)
tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text='Datos Personales')
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab2, text="Extras")
tabcontrol.pack(expand=1, fill="both")

#Captura de DATOS-----------------------------------------------------------------------------------------
capnom=ttk.Label(tab1, text="-> N O M B R E : ", background='black', foreground='gold')
capnom.place(x=0,y=30)
enom= tk.StringVar()
entnom= tk.Entry(tab1,width=20,textvariable=enom)
entnom.place(x=150,y=30)

capa1=ttk.Label(tab1, text="-> Apellido Paterno: ", background='black', foreground='gold')
capa1.place(x=0,y=70)
ea1= tk.StringVar()
enta1= tk.Entry(tab1,width=20,textvariable=ea1)
enta1.place(x=150,y=70)

capa2=ttk.Label(tab1, text="-> Apellido Materno: ", background='black', foreground='gold')
capa2.place(x=0,y=110)
ea2= tk.StringVar()
enta2= tk.Entry(tab1,width=20,textvariable=ea2)
enta2.place(x=150,y=110)


capdir=ttk.Label(tab1, text="-> Dirección: ", background='black', foreground='gold')
capdir.place(x=0,y=150)
edir= tk.StringVar()
entdir= ttk.Combobox(tab1,width=20,textvariable=edir)
entdir ['values'] = ("Av. Madero", "Av. Solidaridad", "Mil cumbres", "Salida Charo", "Salida Salamanca")
entdir.place(x=150,y=150)
entdir.current(0)

capmun=ttk.Label(tab1, text="-> Colonia: ", background='black', foreground='gold')
capmun.place(x=0,y=190)
enum= tk.StringVar()
entmun= ttk.Combobox(tab1, width=19, textvariable=enum)
entmun ['values'] = ("Adolfo Lopez Mateos","Niños Heroes","Lucio Cabañas")
entmun.place(x=150,y=190)
entmun.current(0)
capmun2=ttk.Label(tab1, text="-> Ciudad: ", background='black', foreground='gold')
capmun2.place(x=0,y=230)
enum2= tk.StringVar()
entmun2= ttk.Combobox(tab1, width=19, textvariable=enum2)
entmun2 ['values'] = ("Morelia","Queretaro","Colima")
entmun2.place(x=150,y=230)
entmun2.current(0)

capmun3=ttk.Label(tab1, text="-> Municipio: ", background='black', foreground='gold')
capmun3.place(x=0,y=270)
enum3= tk.StringVar()
entmun3= ttk.Combobox(tab1, width=19, textvariable=enum3)
entmun3 ['values'] = ("Zamora","Lazaro Cárdenas","Acuitzio")
entmun3.place(x=150,y=270)
entmun3.current(0)

boton = ttk.Button(tab1, text="Imprimir Datos Personales", command=Imprimir_datos)
boton.place(x=150,y= 320)


#Captutra de datos--------------------------------------------------------------------------------------
pasa = ttk.Label(tab2, text="Pasatiempos...")
pasa.grid(column=0, row=0)

c1 = tk.IntVar()
cas1=tk.Checkbutton(tab2, text="Leer", variable=c1)
cas1.grid(column=0, row=1)

c2 = tk.IntVar()
cas2=tk.Checkbutton(tab2, text="Películas", variable=c2)
cas2.grid(column=1, row=1)

c3 = tk.IntVar()
cas3=tk.Checkbutton(tab2, text="Redes Sociales", variable=c3)
cas3.grid(column=3, row=1)


esta = ttk.Label(tab2, text="Estado Civil...")
esta.grid(column=0, row=5)

r1=tk.IntVar()

rad1=tk.Radiobutton(tab2, text="Soltero", variable=r1, value=1)
rad1.grid(column=0, row=6)
rad2=tk.Radiobutton(tab2, text="Casado", variable=r1, value=2)
rad2.grid(column=1, row=6)
rad3=tk.Radiobutton(tab2, text="Viudo", variable=r1, value=3)
rad3.grid(column=2, row=6)


come = tk.Label(tab2,text="Objetivo de vida: ")
come.grid(column=0, row=7)
caja = scrolledtext.ScrolledText(tab2,width=30, height=3, wrap=tk.WORD)
caja.place(x=0,y=100)

bot_ex = ttk.Button(tab2, text="Imprimir Datos", command=imp_extra)
bot_ex.place(x=260, y=120)
ven.mainloop()