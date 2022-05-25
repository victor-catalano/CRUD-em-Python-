from conexao import conexao
conexao = conexao()

class Usuario:
    def __init__ (self, nome = "", senha = "", mensagem = "", cpf = "", endereco = "", data_nasc = "", idusuario = ""):
        self.nome = nome
        self.senha = senha
        self.mensagem = mensagem
        self.cpf = cpf
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.idusuario = idusuario
    
    
    
    def cadastrar (self): #Funcionando
        cursor = conexao.conexao.cursor()
        sql = "insert into empregado(nome,senha) values('{}','{}');".format(self.nome,self.senha)
        cursor.execute(sql)
        conexao.conexao.commit()
        return "Cadastrado!" 
    
    
    def buscar(self,idusuario): #Funcionando
        cursor = conexao.conexao.cursor()
        sql = "select nome,senha,cpf,data_nasc,endereco from empregado where idusuario='{}';".format(idusuario)
        cursor.execute(sql)
        record = cursor.fetchone()
        self.nome = record[0]
        self.senha = record[1]
        self.cpf = record[2]
        self.data_nasc = record[3]
        self.endereco = record[4]
        conexao.conexao.commit()
        return "Sucesso na pesquisa"
    
    
    
    def atualizar(self): #Funcionando
        cursor = conexao.conexao.cursor()
        update = "update empregado set nome='{}',senha='{}',cpf='{}',data_nasc='{}',endereco='{}' where idusuario='{}';".format(self.nome,self.senha,self.cpf,self.data_nasc,self.endereco,self.idusuario)
        cursor.execute(update)
        conexao.conexao.commit()
        return "Cadastro atualizado com sucesso!"
    
    
    
    def consulta(self, idusuario): #Funcionando
        cursor = conexao.conexao.cursor()
        sql = "select nome,senha from empregado where idusuario='{}';".format(idusuario)
        cursor.execute(sql)
        record = cursor.fetchone()
        self.nome = record[0]
        self.senha = record[1]
        conexao.conexao.commit()
   
   
   
    def autentifica(self,nome, senha): #Funcionando
        cursor = conexao.conexao.cursor()
        sql = "select nome,senha from empregado where nome='{}' and senha='{}' ;".format(nome,senha) 
        cursor.execute(sql)
        record = cursor.fetchone()
        self.nome = record[0]
        self.senha = record[1]
        conexao.conexao.commit()
    
    
    
    def excluir(self,idusuario): #Funcionando
        cursor = conexao.conexao.cursor()
        excluir = "delete from empregado where idusuario='{}';".format(idusuario)
        cursor.execute(excluir)
        record = cursor.fetchone()
        conexao.conexao.commit()
        return "Usuário excluido com sucesso!"