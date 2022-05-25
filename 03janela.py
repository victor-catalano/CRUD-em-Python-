from tkinter import *
import tkinter as tk
import consulta
from criausuario import criausuario
from update import update
from excluir import excluir



class janela(Frame) :
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        fileMenu = Menu(menu)
        menu.add_cascade(label="Sair", menu=fileMenu)
        fileMenu.add_command(label="Sair", command=self.exitProgram)
        
        
        editMenu = Menu(menu)
        menu.add_cascade(label="Menu", menu=editMenu)
        editMenu.add_command(label="Cadastrar", command = self.btcadastrar)
        editMenu.add_command(label="Atualizar", command = self.btupdate)
        editMenu.add_command(label="Pesquisar",command = self.btpesquisar)
        editMenu.add_command(label="Excluir", command = self.btexcluir)
        
        
    def exitProgram(self):
        exit()
    
    def btcadastrar(self):
        self.master.withdraw() 
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("200x200")
        criausuario(toplevel)
  
    def btupdate(self):
        self.master.withdraw() 
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        update(toplevel)
    
    def btpesquisar(self):
        self.master.withdraw() 
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("300x300")
        consulta.consulta(toplevel)
    
    def btexcluir(self):
        self.master.withdraw() 
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("300x300")
        excluir(toplevel)