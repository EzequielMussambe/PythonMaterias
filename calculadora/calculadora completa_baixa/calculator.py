import tkinter as tk

def apagar_tudo():
    entrada.delete(0,tk.END)
def colocar(x):
    entrada.insert(tk.END, x)
def igualdade():
    pegar_na_entrada=entrada.get()
    try:
        vindo_da_entrada=eval(pegar_na_entrada)
        apagar_tudo()
        entrada.insert(0, vindo_da_entrada)
    except:
        apagar_tudo()
        entrada.insert(0, "Erro")
tela=tk.Tk()
tela.geometry("252x208+10+10")
tela.resizable(width=False, height=False)
bottons='1234567890+-*/=C'
janela_1=tk.Frame(tela)

janela_2=tk.Frame(tela, bg="orange")
entrada=tk.Entry(janela_1, width=27, font=20, justify="right",bg="yellow", bd=3)
linhas=1
colunas=0
for i in bottons:
    if i=="C":
            botao=tk.Button(janela_2, text=i, width=5, bg="grey", command=lambda:apagar_tudo())
            botao.grid(row=linhas, column=colunas, padx=2,pady=2, sticky="EW")
    elif i=="=":
            botao=tk.Button(janela_2, text=i, width=10, bg="grey", command=lambda:igualdade())
            botao.grid(row=linhas, column=colunas,padx=2, pady=2, sticky="EW")
    else:    
        botao=tk.Button(janela_2, text=i, width=10, bg="grey", command=lambda n=i:colocar(n))
        botao.grid(row=linhas, column=colunas,padx=2, pady=2, sticky="EW")
    colunas+=1
    if colunas==3:
            linhas+=1
            colunas=0
    
entrada.grid(row=0, column=0)
janela_1.grid()
janela_2.grid()

tela.mainloop()