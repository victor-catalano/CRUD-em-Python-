from tkinter import *
from usuario import Usuario
import janela
 
class update:
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
        
        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 10
        self.setimoContainer.pack()
        
        self.oitavoContainer = Frame(master)
        self.oitavoContainer["pady"] = 10
        self.oitavoContainer.pack()
        
        self.nonoContainer = Frame(master)
        self.nonoContainer["pady"] = 10
        self.nonoContainer.pack()
        
        self.decimoContainer = Frame(master)
        self.decimoContainer["padx"] = 20
        self.decimoContainer.pack()
        
        self.decimoumContainer = Frame(master)
        self.decimoumContainer["pady"] = 20
        self.decimoumContainer.pack()
        
 
        self.titulo = Label(self.primeiroContainer, text="Atualizar Usuário")
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
        
        self.atualizar = Button(self.decimoContainer)
        self.atualizar["text"] = "Atualizar"
        self.atualizar["font"] = ("Calibri", "8")
        self.atualizar["width"] = 12
        self.atualizar["command"] = self.atualizarusuario
        self.atualizar.pack()
 
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
        
        self.cpfLabel = Label(self.setimoContainer,text="CPF",
        font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)
 
        self.cpf = Entry(self.setimoContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)
        
        self.data_nascLabel = Label(self.oitavoContainer,text="Data Nascimento",
        font=self.fontePadrao)
        self.data_nascLabel.pack(side=LEFT)
 
        self.data_nasc = Entry(self.oitavoContainer)
        self.data_nasc["width"] = 30
        self.data_nasc["font"] = self.fontePadrao
        self.data_nasc.pack(side=LEFT)
        
        self.enderecoLabel = Label(self.nonoContainer,text="Endereço",
        font=self.fontePadrao)
        self.enderecoLabel.pack(side=LEFT)
 
        self.endereco = Entry(self.nonoContainer)
        self.endereco["width"] = 30
        self.endereco["font"] = self.fontePadrao
        self.endereco.pack(side=LEFT)
        
        self.mensagem = Label(self.decimoumContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
    def buscarusuario(self):
        usuario = Usuario()
        idusuario = self.idusuario.get()
        self.mensagem["text"] = usuario.buscar(idusuario)
        
        if not usuario.nome:
            usuario.nome = ""
        
        if not usuario.senha:
            usuario.senha = ""
        
        if not usuario.cpf: 
            usuario.cpf = ""
        
        if not usuario.data_nasc:
            usuario.data_nasc = ""
        
        if not usuario.endereco:
            usuario.endereco = ""
            
        self.nome.delete(0,END)
        self.nome.insert(INSERT,usuario.nome)
        
        self.senha.delete(0,END)
        self.senha.insert(INSERT,usuario.senha)
        
        self.cpf.delete(0,END)
        self.cpf.insert(INSERT,usuario.cpf)
        
        self.data_nasc.delete(0,END)
        self.data_nasc.insert(INSERT,usuario.data_nasc)
        
        self.endereco.delete(0,END)
        self.endereco.insert(INSERT,usuario.endereco)

  
    def atualizarusuario(self):
        usuario = Usuario()
        usuario.idusuario = self.idusuario.get()
        usuario.nome = self.nome.get()
        usuario.senha = self.senha.get()
        usuario.cpf = self.cpf.get()
        usuario.data_nasc = self.data_nasc.get()
        usuario.endereco = self.endereco.get()
        self.mensagem["text"] = usuario.atualizar()