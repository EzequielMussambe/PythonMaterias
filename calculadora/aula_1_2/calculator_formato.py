import tkinter as tk
bottons='1234567890+-*/=C'
tela=tk.Tk()
tela.geometry("252x190+10+10")
tela.resizable(width=False, height=False)
janela_1=tk.Frame(tela)
janela_2=tk.Frame(tela, bg="orange")
entrada=tk.Entry(janela_1, width=27,font=20,justify="right",bg="yellow", bd=3)
linhas=1
colunas=0
for i in bottons:
    butao=tk.Button(janela_2, text=i, fg="yellow", width=10, bg="grey")
    butao.grid(row=linhas, column=colunas)
    colunas+=1
    if colunas==3:
        colunas=0
        linhas+=1
        
entrada.grid(row=0, column=0)
janela_1.grid()
janela_2.grid()

tela.mainloop()