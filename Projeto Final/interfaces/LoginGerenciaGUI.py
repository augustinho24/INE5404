from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def Login():
    if UsuarioEntry.get() == '' or SenhaEntry.get() == '':
        messagebox.showerror('Erro!', 'Campos não podem ficar vazios.')
    elif UsuarioEntry.get() == 'mangastore' and SenhaEntry.get() == 'adm123':
        messagebox.showinfo('Bem Vindo!', 'Login feito com sucesso.')
        Janela.destroy()
        import GerenciaProdutosGUI  
    else:
        messagebox.showerror('Erro!', 'Insira os dados corretamente.')
        
        
        

# Cria janela
Janela = Tk()

# Tamanho janela
Janela.geometry('1280x720+0+0')
Janela.resizable(False, False)

# Plano de fundo
PlanoDeFundo = ImageTk.PhotoImage(file = 'Bg.jpg')
BgLabel = Label(Janela, image = PlanoDeFundo)
BgLabel.place(x=0, y=0)

# Log in
FrameLogin = Frame(Janela)
FrameLogin.place(x=500, y=200)

    # Imagem do Perfil
ImgPerfil = PhotoImage(file = 'Box.png')
ImgPerfilLabel = Label(FrameLogin, image = ImgPerfil)
ImgPerfilLabel.grid(row=0,column=0,columnspan=2,padx=10,pady=5)

    # Usuário
IconUsuario =  PhotoImage(file = 'User.png')
UsuarioLabel = Label(FrameLogin, text =' Usuário', image = IconUsuario, compound = LEFT)
UsuarioLabel.grid(row=1,column=0,pady=5)

UsuarioEntry = Entry(FrameLogin, bd=3)
UsuarioEntry.grid(row=1,column=1,padx=10,pady=5)

    # Senha
IconSenha =  PhotoImage(file = 'Password.png')
SenhaLabel = Label(FrameLogin, text =' Senha', image = IconSenha, compound = LEFT)
SenhaLabel.grid(row=2,column=0,pady=5)

SenhaEntry = Entry(FrameLogin, bd=3)
SenhaEntry.grid(row=2,column=1,padx=10,pady=5)

    #Botão
BotaoLogin =Button(FrameLogin, text='Login', width=10, activebackground='white', cursor='hand2', command=Login)
BotaoLogin.grid(row=3,column=1,pady=5)

# Cria loop da janela
Janela.mainloop()