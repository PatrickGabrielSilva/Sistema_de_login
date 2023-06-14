import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk

ctk.set_appearance_mode("light")

class BackEnd():
    def conecta_db(self):
        self.conn = sqlite3.connect("Sistema_cadastros.db")
        self.cursor = self.conn.cursor()
        print("Banco de dados conectado")

    def desconecta_db(self):
        self.conn.close()
        print("Banco de dados desconectado")

    def cria_tabela(self):
        self.conecta_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            Senha TEXT NOT NULL,
            Confirmar_Senha TEXT NOT NULL
            );
        """)
        self.conn.commit()
        print("Tabela criada com sucesso")
        self.desconecta_db()

    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha_cadastro = self.confirma_senha_entry.get()

        self.conecta_db()

        # Verificar se a tela de cadastro está imprimindo os print(self.username_cadastro,self.email_cadastro,self.senha_cadastro,self.confirma_senha_cadastro)

        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Email, Senha, Confirmar_Senha)
            VALUES (?,?,?,?)""", (self.username_cadastro,self.email_cadastro,self.senha_cadastro,self.confirma_senha_cadastro))

        try:
            if (self.username_cadastro== "" or self.email_cadastro =="" or self.senha_cadastro =="" or self.confirma_senha_cadastro ==""):
                messagebox.showerror(title="Sistema De Login", message="Por favor preencha todos os campos!")

            elif (len(self.senha_cadastro) <8 ):
                messagebox.showwarning(title= "Sistema de Login", message="A senha deve ter no minimo 8 caractéres.")

            elif (len(self.senha_cadastro) <8 ):
                messagebox.showwarning(title= "Sistema de Login", message="A senha deve ter no minimo 8 caractéres.")

            elif(self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title="Sistema de login", message="Error! \n a senhas não são iguais.")                

            else:
                self.conn.commit()
                messagebox.showinfo(title="Sistema de login", message=f"Parabéns {self.username_cadastro}, seu cadastro feito com sucesso !")

                self

        except:
            messagebox.showerror(title="Sistema de login", message="Erro no processamento do seu cadastro !\n por favor tente novamente")


class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tela_de_login()
        self.cria_tabela()
    # configurando a janela princial

    def configuracoes_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema De Login")
        self.resizable(False,False)

    def tela_de_login(self):

        # Trabalhando com as imagens
        self.img = PhotoImage(file="vector2.png")
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=30)

        # Titulo da nossa Plataforma
        self.title = ctk.CTkLabel(self, text="Faca o seu login ou Cadastre-se \nna nossa Plataforma para acessar \nos nossos servicos!", font=("Century gothic", 14))
        self.title.grid(row=0, column=0, pady=10)

        # Criar um frame do formulario de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        # Colocando widgets dentro do frame - formulario login

        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faca o Login", font=("Century gothic negrito", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        # Button Usuario
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300,placeholder_text="Digite seu nome de usuario", font=("Century gothic", 16), corner_radius=7)
        self.username_login_entry.grid(row=1, column=0, pady=10, padx=10)

        # Button Senha
        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300,placeholder_text="Digite sua senha", font=("Century gothic", 16), corner_radius=7, show="*")
        self.senha_login_entry.grid(row=2, column=0, pady=10, padx=10)


        # Click para ver a senha
        self.ver_senha = ctk.CTkCheckBox(self.frame_login,text="Clique para ver a senha", font=("Century gothic", 16),corner_radius=3)
        self.ver_senha.grid(row=3, column=0, pady=10, padx=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300,text="Entrar", font=("Century gothic", 16), corner_radius=15)
        self.btn_login.grid(row=4, column=0, pady=10, padx=10)

        self.span = ctk.CTkLabel(self.frame_login,text="caso nao tiver conta, clique no botao abaixo para se cadastrar", font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, pady=10, padx=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color="green",text="Fazer Cadastro", font=("Century gothic", 16), corner_radius=15, command=self.tela_de_cadastro)
        self.btn_cadastro.grid(row=6, column=0, pady=10, padx=10)

    def tela_de_cadastro(self):
        # Remover a tela de login
        self.frame_login.place_forget()

        # Frame de formulario de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)
        
        # Criando nosso titulo
        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="Faca o Login", font=("Century gothic negrito", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=5)


        # Criando os nossos widgets da tela de cadastro
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300,placeholder_text="Digite seu nome de usuario", font=("Century gothic", 16), corner_radius=7)
        self.username_cadastro_entry.grid(row=1, column=0, pady=5, padx=10)

        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300,placeholder_text="Digite seu email", font=("Century gothic", 16), corner_radius=7)
        self.email_cadastro_entry.grid(row=2, column=0, pady=5, padx=10)
        

        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300,placeholder_text="Digite sua senha", font=("Century gothic", 16), corner_radius=7, show="*")
        self.senha_cadastro_entry.grid(row=3, column=0, pady=5, padx=10)


        self.confirma_senha_entry = ctk.CTkEntry(self.frame_cadastro, width=300,placeholder_text="Confirme a senha", font=("Century gothic", 16), corner_radius=7, show="*")
        self.confirma_senha_entry.grid(row=4, column=0, pady=5, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro,text="Clique para ver a senha", font=("Century gothic", 16),corner_radius=3)
        self.ver_senha.grid(row=5, column=0, pady=5, padx=10)

        # Botões
        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="green",text="Fazer Cadastro", font=("Century gothic", 16), corner_radius=15, command=self.cadastrar_usuario)
        self.btn_cadastrar_user.grid(row=6, column=0, pady=5, padx=10)  

        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, width=300,text="Voltar", font=("Century gothic", 16), corner_radius=15, fg_color='#444', hover_color="#333", command=self.tela_de_login)
        self.btn_login_back.grid(row=7, column=0, pady=10, padx=10)

    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.confirma_senha_entry.delete(0, END)
        
    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.senha_login_entry.delete(0, END)


if __name__ == "__main__":
    app = App()
    app.mainloop()
