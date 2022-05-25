from tkinter import *
from usuario import Usuario
import janela

 
class excluir:
    def __init__(self, master):
        self.master=master
        janela.janela(master)
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
 
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
 
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
 
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        
        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 10
        self.quintoContainer.pack()
        
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 10
        self.sextoContainer.pack()
        
        self.setmoContainer = Frame(master)
        self.setmoContainer["padx"] = 20
        self.setmoContainer.pack()
        
        self.oitavoContainer = Frame(master)
        self.oitavoContainer["pady"] = 20
        self.oitavoContainer.pack()
 
        self.titulo = Label(self.primeiroContainer, text="Consulta Cadastro Usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
 
        self.idusuarioLabel = Label(self.segundoContainer,text="Id Usuário",
        font=self.fontePadrao)
        self.idusuarioLabel.pack(side=LEFT)
 
        self.idusuario = Entry(self.segundoContainer)
        self.idusuario["width"] = 30
        self.idusuario["font"] = self.fontePadrao
        self.idusuario.pack(side=LEFT)
 
        self.buscar = Button(self.terceiroContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.buscarusuario
        self.buscar.pack()
 
        self.nomeLabel = Label(self.quintoContainer,text="Nome",
        font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
 
        self.nome = Entry(self.quintoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        
        self.senhaLabel = Label(self.sextoContainer,text="Senha",
        font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
 
        self.senha = Entry(self.sextoContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)
        
        self.buscar = Button(self.setmoContainer)
        self.buscar["text"] = "Excluir"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.excluirusuario
        self.buscar.pack()
        
        self.mensagem = Label(self.oitavoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
    def buscarusuario(self):
        usuario = Usuario()
        idusuario = self.idusuario.get()
        usuario.consulta(idusuario)
       
        self.nome.delete(0,END)
        self.nome.insert(INSERT,usuario.nome)
        
        self.senha.delete(0,END)
        self.senha.insert(INSERT,usuario.senha)
        
        
    def excluirusuario(self):
        usuario = Usuario()
        idusuario = self.idusuario.get()
        self.mensagem["text"] = usuario.excluir(idusuario)