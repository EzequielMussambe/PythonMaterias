import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
import csv
import os
#from PIL import Image, ImageTk, ImageFilter
storege=dict()
check=set()
df=[]
data_2=[]
nam=""
ag=""
datas=[]
def receber():
    name=entrada_1.get()
    global nam, ag
    nam=name
    age=entrada_2.get()
    ag=age

    t=name.lower()

    if entrada_3.get():
        data=entrada_3.get()+".csv"

    else:
        data="default.csv"
    try:
        if os.stat(data).st_size == 0:
            pass
        else:
            dat=pd.read_csv(data)
    except:
        pass
    try:
      for s in dat.Name:
          data_2.append(s)
    except:
        pass
    if name and age.isdigit():
        if t not in check and  name.title() not in data_2:
            janela_3.delete(0, tk.END)
            janela_3.insert(0,"As informação de '{}' foram adicionadas.Obrigado".format(name.title()))
            check.add(t)
            df.append({"Name":name.title(), "Age":age})
            entrada_1.delete(0,tk.END)
            entrada_2.delete(0,tk.END)
            
        else:
           janela_3.delete(0, tk.END)
           janela_3.insert(0,"O nome {} já existe na base de dados.".format(name.title()))
           janela_3.insert(1,"Ofereça mais um nome.")
           entrada_1.delete(0,tk.END)
           entrada_2.delete(0,tk.END)
    else:
         messagebox.showerror("Vazio","Preencher bem os campos")
         janela_3.delete(0, tk.END)
         janela_3.insert(0,("CUIDADO!,Não existe informação para adicionar."))
         entrada_1.delete(0,tk.END)
         entrada_2.delete(0,tk.END)
   
def eraise():

    entrada_1.delete(0, tk.END)# DOES NOT MATTER IF IT IS A WORD OR NUMBER. THIS IS THE WAY.
    entrada_2.delete(0, tk.END)
    janela_3.delete(0,tk.END)
def only_te():
    janela_3.delete(0,tk.END)
def telas():
    janela_3.delete(tk.ACTIVE)
    
def writedata():
    #name=entrada_1.get()
    #age=entrada_2.get()
    entry_3=janela_3.get(tk.ACTIVE)
    if entrada_3.get():
        data=entrada_3.get()+".csv"
    else:
        data="default.csv"
    dfs=pd.DataFrame(df, columns=['Name','Age'])
    global nam, ag
    if nam and ag and entry_3:
        nam=""
        ag=""
        #global nam=[]
        #global ag=[]
        #nam=[]
        #ag=[]
        try:
            if os.stat(data).st_size == 0:#THIS IS THE PROBLEMA BECAUSE IF THE FILE IS NOT IN THE PATH IT GIVES ERRORS.
                dfs.to_csv(data, index=False)
            else:
                name=entrada_1.get()
    
                dat=pd.read_csv(data)
    
                for s in dat.Name:
                    datas.append(s)
                if name.title() not in datas:
                    
                    ns=pd.DataFrame(dat,columns=['Name', 'Age'])
                
                    novo=pd.DataFrame(df, columns=['Name', 'Age'])
                    dfs.update(novo, join='left', overwrite=True)
                   
                    dfs.append(ns,ignore_index=True)
    
                    dfs.to_csv(data, mode='a', header=False, index=False)#check this one i eraised a data=dat
                    eraise()
                    messagebox.showinfo("Dados adicionado com successo")
                else:
                    janela_3.insert(0,"O nome {} foi ignorado".format(name.title()))
                    eraise()
                    pass
        except:
            dfs.to_csv(data, index=False)
            eraise()
    else:
        messagebox.showerror("Vazio","Complenta os campos")
        #only_te():
        janela_3.delete(0, tk.END)
        janela_3.insert(0,("Porfavor: "))
        janela_3.insert(1,("Não te esqueça de preencher os seguintes\n campos obrigatórios:"))
        janela_3.insert(2,("Nome Completo, Idade; antes de qualquer Acão."))
        janela_3.insert(3,("Se os campos já estão preenchidos. Volta e guardar."))
        
        
        
        
def sair():
    tela.destroy()
    
    
tela=tk.Tk()
tela.iconbitmap("nice_ev2_icon.ico")
fotos=tk.PhotoImage(file="nice.png")
tela.geometry("670x400")
tela.title("BASE DE DADOS SIMPLES")
tela.config(bg="yellow")
tela.resizable(0,0)
janela_1=tk.Frame(tela, bg="black")
janela_2=tk.Frame(tela, bg="red", width=670)
janela_3=tk.Listbox(tela, width=108, font=("Arial", 15, "bold"),bg="yellow",bd=7)
nome="Nome Completo"
ano="Idade"
label_1=tk.Label(janela_1, text=nome.upper(), bg="black", fg="white", font=("Arial", 15,"bold" ))
label_2=tk.Label(janela_1, text=ano.upper(),  bg="black", fg="white", font=("Arial", 15,"bold" ))
label_4=tk.Label(janela_1, text="Nome do File".upper(), bg="black", fg="white", font=("Arial", 15,"bold" ))
entrada_3=tk.Entry(janela_1, width=30, bd=3, font=("Arial", 20,"bold" ))

entrada_1=tk.Entry(janela_1, width=30, bd=3, font=("Arial", 20,"bold" ))
entrada_2=tk.Entry(janela_1,width=30, bd=3, font=("Arial", 20,"bold" ))
button_1=tk.Button(janela_2,  text="Criar csv".upper(),width=11, relief="raised", bd=3, font=("Arial", 15,"bold" ), command=lambda:writedata())
button_2=tk.Button(janela_2, text="Apagar da Tela".upper(),width=20,  relief="raised", bd=3, font=("Arial", 15,"bold" ), command=lambda:telas())
button_3=tk.Button(janela_2, text="adicionar".upper(), width=20, relief="raised", bd=3, font=("Arial", 15,"bold" ), command=lambda:receber())
button_4=tk.Button(janela_2,text="apagar info".upper(), width=20, relief="raised", bd=3, font=("Arial", 15,"bold" ), command=lambda:eraise())
button_5=tk.Button(janela_2,text="Sair".upper(), width=11, relief="raised", bd=3, font=("Arial", 15,"bold" ), command=lambda:sair())

label_1.grid(row=0, column=0, padx=2,sticky="W")
label_4.grid(row=2,column=0, padx=2,sticky="W")
entrada_3.grid(row=2,column=1,padx=5, pady=5, sticky="S")
entrada_1.grid(row=0,column=1, padx=5, pady=5, sticky="S")
label_2.grid(row=1, column=0, padx=2, sticky="W")

entrada_2.grid(row=1,column=1, padx=5, pady=5)
button_2.grid(row=0, column=0, padx=4, pady=4, sticky="W")
button_1.grid(row=0, column=1,padx=4, pady=4, sticky="W")
button_3.grid(row=0, column=2,padx=4, pady=4, sticky="W")
button_4.grid(row=1, column=0,padx=4, pady=4, sticky="W")
button_5.grid(row=1, column=1,padx=4, pady=4, sticky="W")
# colocar datas de colletions and also checque if the file already exist
janela_2.pack(side="bottom")
janela_1.pack(side="top")
janela_3.pack()


tela.mainloop()
