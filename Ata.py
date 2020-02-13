#IMPORTANDO TODAS AS BIBLIOTECAS NECESSÁRIAS

from tkinter import  *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import sqlite3


try:
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE professor (
            nome TEXT NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            departamento TEXT NOT NULL
    );
    """)
except sqlite3.Error:
    pass


try:
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE aluno (
            nome TEXT NOT NULL,
            cpf VARCHAR(11) NOT NULL
    );
    """)
except sqlite3.Error:
    pass




try:
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE disciplina (
            cod TEXT NOT NULL,
            nome TEXT NOT NULL
    );
    """)
except sqlite3.Error:

    pass

try:
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE turma (
            codt TEXT NOT NULL,
            codd TEXT NOT NULL,
            periodo TEXT NOT NULL,
            cpfp TEXT NOT NULL,
            cpfa TEXT NOT NULL
    );
    """)
except sqlite3.Error:

    pass


def cadastroP(nome,cpf,departamento):


    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor() # definindo um cursor (cursor é oq permite navegar e manipular registos no bd)
    cursor.execute(""" 
    INSERT INTO professor(nome,cpf,departamento)
    VALUES(?,?,?)
    """,(nome,cpf,departamento,))
    conn.commit()
    conn.close()



def cadastroa(nome, cpf):

    # estabelecendo o caminho do bd
    # conectando\criando o bd

    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    # definindo um cursor (cursor é oq permite navegar e manipular registos no bd

    cursor.execute(""" 
    INSERT INTO aluno(nome,cpf)
    VALUES(?,?)
    """, (nome, cpf,))
    conn.commit()
    conn.close()

def cadastrod(nome, cod):

    # estabelecendo o caminho do bd
    # conectando\criando o bd

    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    # definindo um cursor (cursor é oq permite navegar e manipular registros no bd)

    cursor.execute(""" 
    INSERT INTO disciplina(nome,cod)
    VALUES(?,?)
    """, (nome, cod,))
    conn.commit()
    conn.close()

def cadastrot( codt,codd,periodo,cpfp,cpfa):

    # estabelecendo o caminho do bd
    # conectando\criando o bd

    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    # definindo um cursor (cursor é oq permite navegar e manipular registros no bd)

    cursor.execute(""" 
    INSERT INTO turma(codt,codd,periodo,cpfp,cpfa)
    VALUES(?,?,?,?,?)
    """, ( codt,codd,periodo,cpfp,cpfa,))
    conn.commit()
    conn.close()

def consultaesp(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
            SELECT * FROM professor WHERE cpf = ?
            """,(cpf,))
    return r.fetchone()

def consultaespA(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
            SELECT * FROM aluno WHERE cpf = ?
            """,(cpf,))
    return r.fetchone()

def consultaespD(cod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
            SELECT * FROM disciplina WHERE cod = ?
            """,(cod,))
    return r.fetchone()

def consultaespT(cod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
            SELECT * FROM turma WHERE codt = ?
            """,(cod,))

    return r.fetchall()


def consultaespT2(cod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
            SELECT codt FROM turma WHERE codt = ?
            """, (cod,))
    b = r.fetchone()
    if b is None:
        pass
    else:
        return b[0]

def deletaP(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                DELETE  FROM professor WHERE cpf = ?
                """, (cpf,))
    messagebox.showinfo('Deletar','Professor deletado com sucesso')
    conn.commit()
    conn.close()

def deletaA(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                    DELETE  FROM aluno WHERE cpf = ?
                    """, (cpf,))
    messagebox.showinfo('Deletar','Aluno deletado com sucesso')
    conn.commit()
    conn.close()

def deletaD(cod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                    DELETE  FROM disciplina WHERE cod = ?
                    """, (cod,))
    messagebox.showinfo('Deletar','Disciplina deletada com sucesso')
    conn.commit()
    conn.close()

def deletaT(cod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                    DELETE  FROM turma WHERE codt = ?
                    """, (cod,))
    messagebox.showinfo('Deletar','Turma deletada com sucesso')
    conn.commit()
    conn.close()
def deleta_professor_T(cod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                    DELETE  FROM turma WHERE cpfp = ?
                    """, (cod,))
    conn.commit()
    conn.close()
def deleta_aluno_T(cod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                    DELETE  FROM turma WHERE cpfa = ?
                    """, (cod,))
    conn.commit()
    conn.close()
def deleta_disciplina_T(cod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                    DELETE  FROM turma WHERE codd = ?
                    """, (cod,))
    conn.commit()
    conn.close()
def atualizarP(nome,cpf,departamento,novocpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                            UPDATE professor 
                            SET nome = ?, departamento = ?, cpf = ?
                            WHERE cpf = ?
                            """, (nome,departamento,novocpf,cpf,))
    messagebox.showinfo('Atualizar', 'Dados atualizados com sucesso')
    conn.commit()
    conn.close()
def atualizarA(nome,cpf,novocpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                            UPDATE aluno
                            SET nome = ?, cpf = ?
                            WHERE cpf = ?
                            """, (nome,novocpf,cpf,))
    messagebox.showinfo('Atualizar', 'Dados atualizados com sucesso')
    conn.commit()
    conn.close()

def atualizarD(nome,cod,novocod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                            UPDATE disciplina
                            SET nome = ?, cod = ?
                            WHERE cod = ?
                            """, (nome,novocod,cod))
    conn.commit()
    conn.close()

def atualizarT(olcod,ncod,nperiodo):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                            UPDATE turma
                            SET codt = ?,
                            periodo = ?
                            WHERE codt = ?
                            """, (ncod,nperiodo,olcod,))
    conn.commit()
    conn.close()
def atualizarcpfTp (cpf,novocpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                                UPDATE turma
                                SET cpfp = ?
                                WHERE cpfp = ?
                                """, (novocpf,cpf,))
    conn.commit()
    conn.close()

def atualizarcpfTa (cpf,novocpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                                UPDATE turma
                                SET cpfa = ?
                                WHERE cpfa = ?
                                """, (novocpf,cpf,))
    conn.commit()
    conn.close()

def atualizarcodTd (cod,novocod):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
                                UPDATE turma
                                SET codd = ?
                                WHERE codd = ?
                                """, (novocod,cod,))
    conn.commit()
    conn.close()

def atualizar_tabelas(a):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
            SELECT * FROM professor
            """)
    a.delete(1.0,END)
    a.insert(INSERT, 'Nome |  CPF         | Departamento\n\n')
    for i in cursor.fetchall():
        a.insert(INSERT, str(' |  '.join(i)) + '\n')
    conn.commit()
    conn.close()

def atualizar_tabelasa(a):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
            SELECT * FROM aluno
            """)
    a.delete(1.0,END)
    a.insert(INSERT, 'Nome |  CPF         \n\n')
    for i in cursor.fetchall():
        a.insert(INSERT, str(' |  '.join(i)) + '\n')
    conn.commit()
    conn.close()
def atualizar_tabelasd(a):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
            SELECT * FROM disciplina
            """)
    a.delete(1.0,END)
    a.insert(INSERT, 'Código |  Nome         \n\n')
    for i in cursor.fetchall():
        a.insert(INSERT, str(' |  '.join(i)) + '\n')
    conn.commit()
    conn.close()

def atualizar_tabelast(a):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    cursor.execute("""
            SELECT * FROM turma
            """)
    a.delete(1.0,END)
    a.insert(INSERT, 'CodT | CodD  |  Periodo   | CPF prof       | CPF aluno          \n')
    for i in cursor.fetchall():
        a.insert(INSERT, str('   |  '.join(i)) + '\n')
    conn.commit()
    conn.close()
def consulta_cpfp_em_turma(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
                SELECT codt, periodo FROM turma WHERE cpfp = ?
                """, (cpf,))
    return r.fetchall()

def consulta_periodop_em_turma(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
                SELECT codt, periodo,codd FROM turma WHERE periodo = ?
                """, (cpf,))
    return r.fetchall()
def consulta_cpfp_em_turma2(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
                SELECT cpfp FROM turma WHERE cpfp = ?
                """, (cpf,))
    b = r.fetchone()
    if b is None:
        pass
    else:
        return b[0]
def consulta_cpfpd_em_turma(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
                SELECT codt, periodo,codd FROM turma WHERE cpfp = ?
                """, (cpf,))
    return r.fetchall()
def consulta_cpfa_em_turma(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
                SELECT codt, periodo FROM turma WHERE cpfa = ?
                """, (cpf,))
    return r.fetchall()

def consulta_periodoa_em_turma(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
                SELECT codt, periodo,codd FROM turma WHERE periodo = ?
                """, (cpf,))
    return r.fetchall()
def consulta_cpfa_em_turma2(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
                SELECT cpfa FROM turma WHERE cpfa = ?
                """, (cpf,))
    b = r.fetchone()
    if b is None:
        pass
    else:
        return b[0]
def consulta_cpfad_em_turma(cpf):
    conn = sqlite3.connect('projeto.db')
    cursor = conn.cursor()
    r = cursor.execute("""
                SELECT codt, periodo,codd FROM turma WHERE cpfa = ?
                """, (cpf,))
    return r.fetchall()

#PASSANDO AS MEDIDAS DA TELA
root = Tk()

root.geometry("900x500")

#definindo o tamanho maximo da minha janela
root.maxsize(width=900, height=500)

#DEFININDO A COR DO BACKRGROUND DA TELA
root.configure(background = '#707070')

#CRIANDO O LABEL DO INICIO

lblInicio = Label(root, font = 'arial 35 ',text = 'Bem vindo',bg = '#707070')
lblInicio.pack()

#CRIANDO O FRAME DA ESQUERDA

fleft = Frame(root, width = 680, height = 440)
fleft.configure(background = 'white')
fleft.pack(side = RIGHT)
fleft.propagate(0)

#criando as abas

aba_control = ttk.Notebook(fleft)
abaC = ttk.Frame(aba_control)
abaA = ttk.Frame(aba_control)
abaD = ttk.Frame(aba_control)
abaCON = ttk.Frame(aba_control)
abarel = ttk.Frame(aba_control)
abaata = ttk.Frame(aba_control)

FrameC = Frame(abaC, width =680 , height = 440)
FrameC.propagate(0)
FrameA = Frame(abaA, width =680 , height = 440)
FrameD = Frame(abaD, width =680 , height = 440)
FrameCON = Frame(abaCON, width =680 , height = 440)

FrameCa = Frame(abaC, width =680 , height = 440)
FrameAa = Frame(abaA, width =680 , height = 440)
FrameDa = Frame(abaD, width =680 , height = 440)
FrameCONa = Frame(abaCON, width =680 , height = 440)

FrameCt = Frame(abaC, width =680 , height = 440)
FrameAt = Frame(abaA, width =680 , height = 440)
FrameDt = Frame(abaD, width =680 , height = 440)
FrameCONt = Frame(abaCON, width =680 , height = 440)
Framerelt = Frame(abarel, width =680 , height = 440)
Frameatat= Frame(abaata, width =680 , height = 440)

FrameCd = Frame(abaC, width =680 , height = 440)
FrameAd = Frame(abaA, width =680 , height = 440)
FrameDd = Frame(abaD, width =680 , height = 440)
FrameCONd = Frame(abaCON, width =680 , height = 440)


#CRIANDO AS FUNÇÕES QUE OS BOTÕES IRÃO EXECUTAR
def btfprofessor ():
    aba_control.forget

    FrameCa.place(x=1000, y=10000)
    FrameAa.place(x=1000, y=10000)
    FrameDa.place(x=1000, y=10000)
    FrameCONa.place(x=1000, y=10000)
    FrameCd.place(x=1000, y=10000)
    FrameAd.place(x=1000, y=10000)
    FrameDd.place(x=1000, y=10000)
    FrameCONd.place(x=1000, y=10000)
    FrameCt.place(x=1000, y=10000)
    FrameAt.place(x=1000, y=10000)
    FrameDt.place(x=1000, y=10000)
    FrameCONt.place(x=1000, y=10000)
    Framerelt.destroy()
    Frameatat.destroy()
    # criando a aba de cadastro

    aba_control.add(abaC, text='Cadastrar')
    aba_control.pack(expand=1, fill='both')
    # declarando todos os labels de cadastro
    FrameC.place(x = 20, y = 20)

    lblNomeC = Label(FrameC, text='Nome:')
    lblNomeC.place(x=90, y=100)
    lblCPFC = Label(FrameC, text='CPF:')
    lblCPFC.place(x=90, y=120)
    lblDepartamentoC = Label(FrameC, text='Departamento:')
    lblDepartamentoC.place(x=90, y=140)

    # declarando todos os text fields de cadastro
    tfNomec = Entry(FrameC, font='arial')
    tfNomec.place(x=190, y=100)
    tfCPFc = Entry(FrameC, font='arial')
    tfCPFc.place(x=190, y=120)
    tfDepac = Entry(FrameC, font='arial')
    tfDepac.place(x=190, y=140)
    #pegando os dados dos textfields
    def pegandoDC():
        dadosN = tfNomec.get()
        dadosCpf = tfCPFc.get()
        dadosD = tfDepac.get()

        if dadosCpf == '' or dadosN == '' or dadosD == '':
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfCPFc.delete(0, END), tfNomec.delete(0, END)
        elif dadosCpf.isalpha() or dadosN.isnumeric() or len(dadosCpf) != 11:
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfCPFc.delete(0, END), tfNomec.delete(0, END), tfDepac.delete(0,END)
        elif consultaespA(dadosCpf) != None:
            messagebox.showinfo('Cadastro', 'Este cpf já foi cadastrado!')
            tfNomec.delete(0, END), tfCPFc.delete(0, END),tfDepac.delete(0,END)
        elif consultaesp(dadosCpf) != None:
            messagebox.showinfo('Cadastro', 'Este professor já foi cadastrado!')
            tfNomec.delete(0, END), tfCPFc.delete(0, END), tfDepac.delete(0,END)
        else:
            messagebox.showinfo('Cadastro', 'Cadastro feito com sucesso!')
            cadastroP(dadosN, dadosCpf,dadosD)
            tfNomec.delete(0, END), tfCPFc.delete(0, END),tfDepac.delete(0,END)

    btcadastrarc = Button(FrameC, text='Cadastrar',command = pegandoDC)
    btcadastrarc.pack()
    btcadastrarc.place(x = 200,y = 200)

    #criando a aba de atualizar

    aba_control.add(abaA, text='Atualizar')
    aba_control.pack(expand=1, fill='both')

    # declarando todos os labels de Atualizar
    FrameA.place(x=20, y=20)
    lblCPF = Label(FrameA, text='CPF:')
    lblCPF.place(x=90, y=20)
    lblNome = Label(FrameA, text='Nome:')
    lblNome.place(x=90, y=200)
    lblDepartamento = Label(FrameA, text='Departamento:')
    lblDepartamento.place(x=90, y=222)
    lblnovoCPF = Label(FrameA, text = 'Novo CPF:')
    lblnovoCPF.place(x = 90, y = 244)

    # declarando todos os text fields de Atualizar

    tfCPFa = Entry(FrameA, font='arial')
    tfCPFa.place(x=190, y=20)
    tfCPFa.configure(width=24)
    tfNomea = Entry(FrameA, font='arial')
    tfNomea.place(x=190, y=200)
    tfNomea.configure(width = 24)
    tfDepaa = Entry(FrameA, font='arial')
    tfDepaa.place(x=190, y=222)
    tfDepaa.configure(width = 24)
    tfnovocpf = Entry(FrameA, font = 'arial')
    tfnovocpf.place(x = 190, y = 244)
    def pegandoDA():
        dadosN = tfNomea.get()
        dadosCPF = tfCPFa.get()
        dadosDE = tfDepaa.get()
        novocpf = tfnovocpf.get()
        if dadosCPF == '' or dadosN == '' or dadosDE == '' or novocpf == '':
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfNomea.delete(0, END)
            tfCPFa.delete(0, END)
            tfDepaa.delete(0, END)
        elif dadosCPF.isalpha() or dadosN.isnumeric() or len(dadosCPF)!=11 or novocpf.isalpha() or len(novocpf)!=11:
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfNomea.delete(0, END)
            tfCPFa.delete(0, END)
            tfDepaa.delete(0, END)
        elif consultaesp(dadosCPF)==None:
            messagebox.showinfo('Cadastro', 'Este professor não existe!')
            tfNomea.delete(0, END)
            tfCPFa.delete(0, END)
            tfDepaa.delete(0, END)
        else:
            atualizarP(dadosN, dadosCPF, dadosDE,novocpf),tfNomea.delete(0, END),tfCPFa.delete(0, END),tfDepaa.delete(0, END),tfnovocpf.delete(0, END)
            atualizarcpfTp(dadosCPF,novocpf)
    def consulta():
        cpf = tfCPFa.get()
        if cpf == '':
            atualizar_tabelas(stcon)
            tfCPFa.delete(0, END)
        elif cpf.isalpha() or len(cpf)!=11:
            messagebox.showinfo('Atualizar', 'Dados inválidos')
            tfCPFa.delete(0,END)
        elif consultaesp(cpf) == None:
            messagebox.showinfo('Atualizar', 'Este professor não existe')
        else:
            stcon.delete(1.0,END)
            stcon.insert(INSERT, 'Nome |  CPF         | Departamento\n\n')
            stcon.insert(INSERT, str(' |  '.join(consultaesp(cpf))) + '\n')
    stcon = scrolledtext.ScrolledText(FrameA, width=40, height=5)
    stcon.place(x = 90, y = 70)
    atualizar_tabelas(stcon)
    btatualizar = Button(FrameA, text='Atualizar',command = pegandoDA)
    btatualizar.place(x=150, y=300)
    btconsultaratu = Button(FrameA, text='Consultar', command=consulta)
    btconsultaratu.place(x=220, y=300)

    # declarando todos os labels de Deletar
    FrameD.place(x=20, y=20)

    lblCPF = Label(FrameD, text='CPF:').place(x=90, y=20)
    # declarando todos os text fields de Deletar

    tfCPF = Entry(FrameD, font='arial')
    tfCPF.place(x=190, y=20)
    stconsultad = scrolledtext.ScrolledText(FrameD, width=35, height=10)
    stconsultad.place(x=90, y=60)
    def pegandDdelete():
        cpf = tfCPF.get()
        if cpf == '':
            messagebox.showinfo('Deletar', 'Dados inválidos')
            tfCPF.delete(0, END)
        elif cpf.isalpha() or len(cpf)!=11:
            messagebox.showinfo('Deletar', 'Dados inválidos')
            tfCPF.delete(0, END)
        elif consultaesp(cpf) == None:
            messagebox.showinfo('Deletar', 'Este professor não existe!')
            tfCPF.delete(0, END)
        else:
            deletaP(cpf)
            deleta_professor_T(cpf)
            tfCPF.delete(0,END)
    def consultad():
        cpf = tfCPF.get()
        if cpf == '':
            atualizar_tabelas(stconsultad)
        elif consultaesp(cpf) == None:
            messagebox.showinfo('Deletar', 'Este professor não existe')
        elif cpf.isalpha() or len(cpf)!=11:
            messagebox.showinfo('Deletar', 'Dados Inválidos')
        else:
            stconsultad.delete(1.0, END)
            stconsultad.insert(INSERT, 'Nome |  CPF         | Departamento\n\n')
            stconsultad.insert(INSERT, str(' |  '.join(consultaesp(cpf))) + '\n')
    btdeletar = Button(FrameD, text='Deletar', command = pegandDdelete)
    btdeletar['command'] = atualizar_tabelas(stconsultad)
    btdeletar.place(x=150, y=300)
    btconsultad = Button(FrameD, text='Consultar', command=consultad)
    btconsultad.place(x = 220, y = 300)

    # declarando todos os labels de Consultar
    FrameCON.place(x=20, y=20)

    lblCPF = Label(FrameCON, text='CPF:').place(x=90, y=20)

    # declarando todos os text fields de Consultar

    tfCPFcon = Entry(FrameCON, font='arial')
    tfCPFcon.place(x=190, y=20)

    # declarando uma scrolled text box de consultar

    stconsulta = scrolledtext.ScrolledText(FrameCON,width = 35, height = 10)
    stconsulta.place(x =90 , y =60 )

    #declarando os botões de consultar
    def pegandoDCON():
        cpf = tfCPFcon.get()
        if cpf == '':
            atualizar_tabelas(stconsulta)
            tfCPFcon.delete(0, END)
        elif cpf.isalpha() or len(cpf)!=11:
            messagebox.showinfo('Consulta', 'Dados inválidos')
            tfCPFcon.delete(0, END)
        elif consultaesp(cpf)==None:
            messagebox.showinfo('Consulta','Esse professor não existe')
            tfCPFcon.delete(0, END)
        else:
            stconsulta.delete(1.0, END)
            stconsulta.insert(INSERT, 'Nome |  CPF         | Departamento\n\n')
            stconsulta.insert(INSERT, str(' |  '.join(consultaesp(cpf))) + '\n')
            tfCPFcon.delete(0,END)
    btconsulta = Button(FrameCON, text='Consultar',command =pegandoDCON)
    btconsulta['command'] = atualizar_tabelas(stconsulta)
    btconsulta.pack()
    btconsulta.place(x=200, y=300)

    aba_control.add(abaD, text='Deletar')
    aba_control.pack(expand=1, fill='both')
    aba_control.add(abaCON, text='Consultar')
    aba_control.pack(expand=1, fill='both')
    lblInicio['text'] = 'Professor'

def btaluno():
    aba_control.forget
    FrameC.place(x = 1000, y = 10000)
    FrameA.place(x = 1000, y = 10000)
    FrameD.place(x=1000, y=10000)
    FrameCON.place(x=1000, y=10000)
    FrameCd.place(x=1000, y=10000)
    FrameAd.place(x=1000, y=10000)
    FrameDd.place(x=1000, y=10000)
    FrameCONd.place(x=1000, y=10000)
    FrameCt.place(x=1000, y=10000)
    FrameAt.place(x=1000, y=10000)
    FrameDt.place(x=1000, y=10000)
    FrameCONt.place(x=1000, y=10000)
    Framerelt.destroy()
    Frameatat.destroy()
    #criando a aba de cadastrar
    aba_control.add(abaC, text='Cadastrar')
    aba_control.pack(expand=1, fill='both')

    FrameCa.place(x = 20, y = 20)

    #Declarando todos os labels de cadastro

    lblNome = Label(FrameCa, text='Nome:')
    lblNome.place(x=90, y=100)
    lblCPF = Label(FrameCa, text='CPF:')
    lblCPF.place(x=90, y=120)

    #Declarando todos os text fields de cadastro

    tfNomeCa = Entry(FrameCa, font='arial')
    tfNomeCa.place(x=190, y=100)
    tfCPFCa = Entry(FrameCa, font='arial')
    tfCPFCa.place(x=190, y=120)

    #declarando todos o botoões de cadastro
    def pegandoDCa():
        dadosN = tfNomeCa.get()
        dadosCPF = tfCPFCa.get()
        if dadosCPF == '' or dadosN =='':
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfCPFCa.delete(0, END), tfNomeCa.delete(0, END)
        elif dadosCPF.isalpha() or dadosN.isnumeric() or len(dadosCPF) != 11:
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfCPFCa.delete(0, END), tfNomeCa.delete(0, END)
        elif consultaesp(dadosCPF)!=None:
            messagebox.showinfo('Cadastro', 'Este aluno já foi cadastrado!')
            tfNomeCa.delete(0, END), tfCPFCa.delete(0, END)
        elif consultaespA(dadosCPF)!=None:
            messagebox.showinfo('Cadastro', 'Este aluno já foi cadastrado!')
            tfNomeCa.delete(0, END), tfCPFCa.delete(0, END)
        else:
            messagebox.showinfo('Cadastro', 'Cadastro feito com sucesso!')
            cadastroa(dadosN,dadosCPF)
            tfNomeCa.delete(0, END), tfCPFCa.delete(0, END)


    btcadastro = Button(FrameCa, text = 'Cadastrar',command = pegandoDCa)
    btcadastro.place(x=200, y=200)

    FrameAa.place(x=20, y=20)

    # Declarando todos os labels de atualizar

    lblCPF = Label(FrameAa, text='CPF:')
    lblCPF.place(x=90, y=20)
    lblNome = Label(FrameAa, text='Nome:')
    lblNome.place(x=90, y=200)
    lblnovocpf = Label(FrameAa, text = 'Novo CPF:')
    lblnovocpf.place(x = 90, y = 220)

    # Declarando todos os text fields de atualizar
    tfCPFAa = Entry(FrameAa, font='arial')
    tfCPFAa.place(x=190, y=20)
    tfCPFAa.configure(width = 24)
    tfNomeAa = Entry(FrameAa, font='arial')
    tfNomeAa.place(x=190, y=200)
    tfNomeAa.configure(width = 24)
    tfnovocpf = Entry(FrameAa, font = 'arial')
    tfnovocpf.place(x =  190, y = 220)

    # declarando todos o botoões de atualizar
    def pegandoDAa():
        nome = tfNomeAa.get()
        cpf = tfCPFAa.get()
        novocpf = tfnovocpf.get()
        if cpf == '' or nome == '' or novocpf == '' :
            messagebox.showinfo('Atualizar', 'Dados inválidos!')
            tfNomeAa.delete(0, END), tfCPFAa.delete(0, END)
        elif cpf.isalpha() or nome.isnumeric() or len(cpf) != 11 or novocpf.isalpha() or len(novocpf)!=11:
            messagebox.showinfo('Atualizar', 'Dados inválidos!')
            tfNomeAa.delete(0, END), tfCPFAa.delete(0, END)
        elif consultaespA(cpf) == None:
            messagebox.showinfo('Atualizar', 'Este aluno não existe!')
            tfNomeAa.delete(0, END), tfCPFAa.delete(0, END)
        else:
            tfNomeAa.delete(0, END), tfCPFAa.delete(0, END),tfnovocpf.delete(0, END)
            atualizarA(nome,cpf,novocpf)
            atualizarcpfTa(cpf,novocpf)
    def consulta():
        cpf = tfCPFAa.get()
        if cpf == '':
            atualizar_tabelasa(stcon)
        elif cpf.isalpha() or len(cpf)!=11:
            messagebox.showinfo('Atualizar', 'Dados inválidos')
            tfCPFAa.delete(0,END)
        elif consultaespA(cpf) == None:
            messagebox.showinfo('Atualizar', 'Este aluno não existe')
        else:
            stcon.delete(1.0, END)
            stcon.insert(INSERT, 'Nome |  CPF         \n\n')
            stcon.insert(INSERT, str(' |  '.join(consultaespA(cpf))) + '\n')
    stcon = scrolledtext.ScrolledText(FrameAa, width=40, height=5)
    stcon.place(x = 90, y = 70)
    atualizar_tabelasa(stcon)


    btatualizar = Button(FrameAa, text='Atualizar',command = pegandoDAa)
    btatualizar.place(x=150, y=300)
    btcon = Button(FrameAa, text='Consultar', command=consulta)
    btcon.place(x=220, y=300)

    FrameDa.place(x=20, y=20)

    # Declarando todos os labels de deletar

    lblCPF = Label(FrameDa, text='CPF:')
    lblCPF.place(x=90, y=20)

    # Declarando todos os text fields de deletar

    tfCPFAd = Entry(FrameDa, font='arial')
    tfCPFAd.place(x=190, y=20)
    stconsultAd = scrolledtext.ScrolledText(FrameDa, width=35, height=10)
    stconsultAd.place(x=90, y=60)

    def pegandDDa():
        cpf = tfCPFAd.get()
        if cpf == '':
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfCPFAd.delete(0, END)
        elif cpf.isalpha() or len(cpf)!=11 :
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfCPFAd.delete(0, END)
        elif consultaespA(cpf)==None:
            messagebox.showinfo('Cadastro', 'Este aluno não existe!')
            tfCPFAd.delete(0, END)
        else:
            tfCPFAd.delete(0,END)
            deletaA(cpf)
            deleta_aluno_T(cpf)
    # declarando todos o botoões de deletar
    def consultad():
        cpf = tfCPFAd.get()
        if cpf == '':
            atualizar_tabelasa(stconsultAd)
        elif consultaespA(cpf) == None:
            messagebox.showinfo('Deletar', 'Este aluno não existe')
        elif cpf.isalpha() or len(cpf)!=11:
            messagebox.showinfo('Deletar', 'Dados Inválidos')
        else:
            stconsultAd.delete(1.0, END)
            stconsultAd.insert(INSERT, 'Nome |  CPF         | Departamento\n\n')
            stconsultAd.insert(INSERT, str(' |  '.join(consultaespA(cpf))) + '\n')
    btdeletar = Button(FrameDa, text='Deletar', command = pegandDDa)
    btdeletar.place(x=150, y=300)
    btdeletar['command'] = atualizar_tabelasa(stconsultAd)
    btdeletarc = Button(FrameDa, text='Consultar', command=consultad)
    btdeletarc.place(x=220, y=300)

    FrameCONa.place(x=0, y=0)

    # Declarando todos os labels de consultar

    lblCPF = Label(FrameCONa, text='CPF:')
    lblCPF.place(x=110, y=40)

    # Declarando todos os text fields de consultar

    tfCPFAcon = Entry(FrameCONa, font='arial')
    tfCPFAcon.place(x=210, y=40)

    #criando uma scrolled text box

    stconsultaAcon = scrolledtext.ScrolledText(FrameCONa, width = 35, height = 10)
    stconsultaAcon.place(x = 110,y = 80)

    # declarando todos o botões de consultar
    def pegandoDCona():
        cpf = tfCPFAcon.get()
        if cpf ==  '':
            atualizar_tabelasa(stconsultaAcon)
            tfCPFAcon.delete(0, END)
        elif cpf.isalpha() and len(cpf) == 11:
            messagebox.showinfo('Consulta', 'Dados inválidos!')
            tfCPFAcon.delete(0, END)
        elif consultaespA(cpf)==None:
            messagebox.showinfo('Consulta', 'Este aluno não existe!')
            tfCPFAcon.delete(0, END)
        else:
            tfCPFAcon.delete(0, END)
            stconsultaAcon.delete(1.0, END)
            stconsultaAcon.insert(INSERT, 'Nome |  CPF         \n\n')
            stconsultaAcon.insert(INSERT, str(' |  '.join(consultaespA(cpf))) + '\n')
    btconsultar = Button(FrameCONa, text='Consultar', command = pegandoDCona)
    btconsultar['command']= atualizar_tabelasa(stconsultaAcon)
    btconsultar.pack()
    btconsultar.place(x=220, y=320)

    aba_control.add(abaA, text='Atualizar')
    aba_control.pack(expand=1, fill='both')
    aba_control.add(abaD, text='Deletar')
    aba_control.pack(expand=1, fill='both')
    aba_control.add(abaCON, text='Consultar')
    aba_control.pack(expand=1, fill='both')
    lblInicio['text'] = 'Aluno'

def btturma():
    aba_control.forget
    FrameC.place(x=1000, y=10000)
    FrameA.place(x=1000, y=10000)
    FrameD.place(x=1000, y=10000)
    FrameCON.place(x=1000, y=10000)
    FrameCa.place(x=1000, y=10000)
    FrameAa.place(x=1000, y=10000)
    FrameDa.place(x=1000, y=10000)
    FrameCONa.place(x=1000, y=10000)
    FrameCd.place(x=1000, y=10000)
    FrameAd.place(x=1000, y=10000)
    FrameDd.place(x=1000, y=10000)
    FrameCONd.place(x=1000, y=10000)
    Framerelt = Frame(abarel, width=680, height=440)
    Frameatat = Frame(abaata, width=680, height=440)
    #CRIANDO A ABA DE CADASTRAR DE TURMA

    aba_control.add(abaC, text='Cadastrar')
    aba_control.pack(expand=1, fill='both')

    #CHAMANDO O FRAME DE CADSTRO DE TURMA
    FrameCt.place(x = 0, y = 0)

    #DECLARANDO OS LABELS DO CADASTRO DE TURMA
    lblcodT = Label(FrameCt, font='arial', text='Código da Turma:')
    lblcodT.place(x=60, y=60)

    lblperiodoT = Label(FrameCt, font='arial', text='Periodo da Turma:')
    lblperiodoT.place(x=60, y=90)

    lblcodD = Label(FrameCt, font='arial', text='Cod da Disciplina:')
    lblcodD.place(x=60, y=120)

    lblcpfprofT = Label(FrameCt, font='arial', text='Cpf do professor:')
    lblcpfprofT.place(x=60, y=150)

    lblcpfaluT = Label(FrameCt, font='arial', text='Cpf do aluno:')
    lblcpfaluT.place(x=60, y=180)

    #DECLARANDO TODOS OS TEXTFIELDS DO CADASTRO DE TURMA

    tfcodT = Entry(FrameCt, font = 'arial')
    tfcodT.place(x = 220, y = 60)

    tfperiodoT = Entry(FrameCt, font='arial')
    tfperiodoT.place(x=220, y=90)

    tfcodD = Entry(FrameCt, font='arial')
    tfcodD.place(x=220, y=120)

    tfcpfprofT = Entry(FrameCt, font='arial')
    tfcpfprofT.place(x=220, y=150)

    tfcpfaluT = Entry(FrameCt, font='arial')
    tfcpfaluT.place(x=220, y=180)

    def pegandoDT():
        cod = tfcodT.get()
        codD = tfcodD.get()
        periodo = tfperiodoT.get()
        cpfprof = tfcpfprofT.get()
        cpfalu = tfcpfaluT.get()

        if cod == ''  or periodo == '' or cpfprof == '' or cpfalu == '' or codD == '':
            messagebox.showinfo('Cadastro', 'Dados inválidos')
        elif cpfalu.isalpha() or cpfprof.isalpha() or len(cpfalu) != 11 or len(cpfprof)!= 11 or codD.isalpha():
            messagebox.showinfo('Cadastro', 'Dados inválidos')
        elif consultaesp(cpfprof) == None:
            messagebox.showinfo('Cadastro', 'Professor não existe')
        elif consultaespA(cpfalu)==None:
            messagebox.showinfo('Cadastro', 'Aluno não existe')
        elif consultaespT2(cod)== cod and consulta_cpfp_em_turma2(cpfprof)  == cpfprof:
            print(consultaespT2(cod))
            print(consulta_cpfp_em_turma2(cpfprof))
            messagebox.showinfo('Cadastro', 'Professor já foi cadastrado')
        elif consultaespT2(cod)== cod and consulta_cpfa_em_turma2(cpfprof)  == cpfalu:
            messagebox.showinfo('Cadastro', 'Aluno já foi cadastrado')
        else:
            cadastrot(cod,codD,periodo,cpfprof,cpfalu)
            messagebox.showinfo('Cadastro', 'Cadastro feito com sucesso!')
            tfcodD.delete(0,END)
            tfcpfprofT.delete(0,END)
            tfcpfaluT.delete(0,END)

    btcadastroT = Button(FrameCt, font = 'arial', text = 'Cadastrar', command = pegandoDT)
    btcadastroT.place(x = 200, y = 280)
    #CRIANDO A ABA DE ATUALIZAR DE TURMA

    aba_control.add(abaA, text='Atualizar')
    aba_control.pack(expand=1, fill='both')

    #CHAMANDO O FRAME DE ATUALIZAR DE TURMA

    FrameAt.place(x = 0, y = 0)

    #CRIANDO TODOS OS LABELS DE ATUALIZAR
    lblcodatu = Label(FrameAt, font='arial', text='Cod Turma:')
    lblcodatu.place(x = 60 ,y = 20)

    lblnovocodatu = Label(FrameAt, font = 'arial', text= 'Novo cod Turma:')
    lblnovocodatu.place(x = 60, y = 180)

    lblnovoperiodo = Label(FrameAt, font = 'arial', text = 'Novo periodo:')
    lblnovoperiodo.place(x = 60, y = 210)

    #CRIANDO TODOS OS TEXT FIELDS DE ATUALIZAR DA TURMA

    tfolcod = Entry(FrameAt, font = 'arial')
    tfolcod.place(x = 220, y = 20)

    tfnovocod =  Entry(FrameAt, font = 'arial')
    tfnovocod.place(x = 220, y = 180)

    tfnovoperiodo = Entry(FrameAt, font='arial')
    tfnovoperiodo.place(x=220, y=210)


    #CRIANDO A SCROLLED TEXT DE ATUALIZAR EM TURMA

    stcona = scrolledtext.ScrolledText(FrameAt,width = 70, height = 5)
    stcona.place(x = 30, y = 70)
    atualizar_tabelast(stcona)

    #CRIANDO TODOS OS BOTÕES DE ATUALIZAR EM TURMA

    def pegandDatu():
        olcod = tfolcod.get()
        ncod = tfnovocod.get()
        nperiodo = tfnovoperiodo.get()

        if olcod.isalpha() or ncod.isalpha()  or olcod == '' or ncod == '' or nperiodo == '' :
            messagebox.showinfo('Atualizar', 'Dados inválidos')
        elif consultaespT(olcod)==None:
            messagebox.showinfo('Atualizar', 'Essa turma não existe')
        else:
            atualizarT(olcod,ncod,nperiodo)
            tfolcod.delete(0,END)
            tfnovocod.delete(0,END)
            tfnovoperiodo.delete(0,END)
            messagebox.showinfo('Atualizar', 'Dados atualizados com sucesso')

    def consultaatu():
        olcod = tfolcod.get()
        if olcod == '':
            atualizar_tabelast(stcona)
        elif olcod.isalpha():
            messagebox.showinfo('Atualizar', 'Dados inválidos')
        else:
            stcona.delete(1.0, END)
            stcona.insert(INSERT, 'CodT | CodD   | Periodo   | CPF prof       | CPF aluno          \n')
            for i in consultaespT(olcod):
                stcona.insert(INSERT, str('   |  '.join(i) + '\n'))



    btatu = Button(FrameAt, text= 'Atualizar',command = pegandDatu)
    btatu.place(x = 200, y = 350)

    btconatu = Button(FrameAt, text='Consultar', command = consultaatu)
    btconatu.place(x=270, y=350)


    #CRIANDO A ABA DE DELETAR DE TURMA

    aba_control.add(abaD, text='Deletar')
    aba_control.pack(expand=1, fill='both')

    #CHAMANDO O FRAME DE DELETAR DE TURMA

    FrameDt.place(x = 0, y = 0)

    #CRIANDO TODOS OS LABELS DE DELETAR DE TURMA

    lbldel = Label(FrameDt, font = 'arial', text = 'Cod Turma')
    lbldel.place(x=100, y=30)

    #CRIANDO TODOS OS TEXT FIELS DE DELETAR DE TURMA

    tfdel = Entry(FrameDt, font = 'arial')
    tfdel.place(x=220, y=30)

    #CRIANDO A SCROLLED TEXT DE DELETAR DE TURMA

    stcond = scrolledtext.ScrolledText(FrameDt, width=70, height=17)
    stcond.place(x=40, y=60)

    atualizar_tabelast(stcond)

    def pegandoDdel():
        cod = tfdel.get()
        if cod == '':
            messagebox.showinfo('Consulta', 'Dados inválidos')
        elif cod.isalpha():
            messagebox.showinfo('Consulta', 'Dados inválidos')
        else:
            deletaT(cod)
            tfdel.delete(0,END)
    def consultad():
        cod = tfdel.get()
        if cod == '':
            atualizar_tabelast(stcond)
        elif cod.isalpha():
            messagebox.showinfo('Consulta', 'Dados inválidos')
        else:
            stcond.delete(1.0, END)
            stcond.insert(INSERT, 'CodT | CodD   | Periodo   | CPF prof       | CPF aluno          \n')
            for i in consultaespT(cod):
                stcond.insert(INSERT, str('   |  '.join(i) + '\n'))
    #CRIANDO TODOS OS BOTÕES DE DELETAR DA TURMA

    btdel = Button(FrameDt, text = 'Deletar',command = pegandoDdel)
    btdel.place(x = 240, y = 350)

    btcond = Button(FrameDt, text='Consultar', command = consultad)
    btcond.place(x=320, y=350)

    #CRIANDO A ABA DE CONSULTAR DE TURMA

    aba_control.add(abaCON, text='Consultar')
    aba_control.pack(expand=1, fill='both')

    #CHAMANDO O FRAME DE CONSULTAR DE TURMA

    FrameCONt.place(x = 0, y = 0)

    #DECLARANDO TODOS OS LABELS DA CONSULTA DE TURMA

    lblcon = Label(FrameCONt, font = 'arial', text = 'Cod da turma:')
    lblcon.place(x = 100, y = 30)

    #DECLARANDO TODOS OS TEXT FIELDS DA CONSULTA DE TURMA

    tfcon = Entry(FrameCONt, font = 'arial')
    tfcon.place(x = 220,y = 30)

    #DECLARANDO TODAS AS SCROLLED TEXT DA CONSULTA DE TURMA

    stcon = scrolledtext.ScrolledText(FrameCONt, width = 70, height = 17)
    stcon.place(x = 40, y = 60)

    atualizar_tabelast(stcon)

    def pegandoDCON():
        cod = tfcon.get()
        if cod == '':
            atualizar_tabelast(stcon)
        elif cod.isalpha():
            messagebox.showinfo('Consulta', 'Dados inválidos')
        else:

            stcon.delete(1.0, END)
            stcon.insert(INSERT, 'CodT | CodD   | Periodo   | CPF prof       | CPF aluno          \n')
            for i in consultaespT(cod):
                stcon.insert(INSERT, str('   |  '.join(i) + '\n'))

    #DECLARANDO TODOS OS BOTÕES DA CONSULTA DE TURMA

    btcon = Button(FrameCONt, text = 'Consultar',command = pegandoDCON)
    btcon.place(x = 260, y = 350)

    #CRIANDO A ABA DE RELATORIO

    aba_control.add(abarel, text='Relatório')
    aba_control.pack(expand=1, fill='both')

    #CHAMANDO O FRAME DE RELATÓRIO

    Framerelt.place(x = 0, y = 0)

    #DECLARANDO TODOS OS LABELS DE RELATORIO EM TURMA

    lblcpfrel = Label(Framerelt, font = 'arial', text = 'CPF:')
    lblcpfrel.place(x = 100, y = 40)

    lblperel = Label(Framerelt, font='arial', text='Periodo:')
    lblperel.place(x=100, y=60)

    #DECLARANDO TODOS OS TEXT FIELDS DE RELATORIO EM TURMA

    tfcpfrel = Entry(Framerelt, font = 'arial')
    tfcpfrel.place(x = 190, y = 40)
    tfperiodorel = Entry(Framerelt, font='arial')
    tfperiodorel.place(x=190, y=60)

    #DECLARANDO A SCROLLED TEXT DE RELATORIO

    stconrel = scrolledtext.ScrolledText(Framerelt, width = 70, height = 15)
    stconrel.place(x = 40, y= 100)

    #DECLARANDO O BOTÃO DE RELATORIO

    def pegandDrel():
        cpf = tfcpfrel.get()
        periodo = tfperiodorel.get()
        if cpf == '' or len(cpf)!=11 or cpf.isalpha() or periodo.isalpha():
            messagebox.showinfo('Relatório','Dados inválidos')
        elif periodo != '':
            if consulta_cpfa_em_turma(cpf) == []:
                stconrel.delete(1.0, END)
                stconrel.insert(INSERT, 'Turma     |   Periodo    | Disciplina\n')
                for i in consulta_periodop_em_turma(periodo):
                    stconrel.insert(INSERT, '        |   '.join(i)+"\n")
            else:
                stconrel.delete(1.0, END)
                stconrel.insert(INSERT, 'Turma     |   Periodo    | Disciplina\n')
                for i in consulta_periodoa_em_turma(periodo):
                    stconrel.insert(INSERT, '        |   '.join(i)+'\n')
        else:
            if consulta_cpfa_em_turma(cpf) == []:
                stconrel.delete(1.0,END)
                stconrel.insert(INSERT,'Turma     |   Periodo \n')
                for i in consulta_cpfp_em_turma(cpf):
                    stconrel.insert(INSERT, '        |      '.join(i)+'\n')
            else:
                stconrel.delete(1.0, END)
                stconrel.insert(INSERT, 'Turma     |   Periodo \n')
                for i in consulta_cpfa_em_turma(cpf):
                    stconrel.insert(INSERT, '        |      '.join(i)+'\n')

    btrel = Button(Framerelt, font = 'arial',text = 'Gerar',command = pegandDrel)
    btrel.place(x = 250, y = 350)

    #CRIANDO A ABA DA ATA

    aba_control.add(abaata, text='ATA')
    aba_control.pack(expand=1, fill='both')

    #CHAMANDO O FRAME DA ATA

    Frameatat.place(x = 0, y = 0)

    #CRIANDO OS LABELS DA ATA

    lblata = Label(Frameatat, text = 'Código da turma:')
    lblata.place(x = 60, y = 40)

    #CRIANDO OS CAMPOS TE TEXTO DA ATA

    tfata = Entry(Frameatat, font = 'arial')
    tfata.place(x = 190, y = 40)

    #CRIANDO A SCROLED TEXT DA ATA

    stconata= scrolledtext.ScrolledText(Frameatat, width=70, height=15)
    stconata.place(x=40, y=100)
    stconata.insert(INSERT, '----------------------------------------------------------------------   ')
    stconata.insert(INSERT, '                         ATA da Turma        \n')
    stconata.insert(INSERT,'----------------------------------------------------------------------\n   ')
    stconata.insert(INSERT, '             Turma    |     Periodo    |     Cod disc    \n')
    stconata.insert(INSERT, '----------------------------------------------------------------------\n   ')
    #CRIANDO O BOTAO DA ATA

    def pegandoData():

        cod = tfata.get()
        if cod == '':
            messagebox.showinfo('ATA', 'Dados invalidos')

        elif consultaespT2(cod) is None:
            messagebox.showinfo('ATA', 'Essa turma não existe')
            tfata.delete(0, END)
        else:
            tfata.delete(0,END)
            stconata.delete(1.0, END)
            conn = sqlite3.connect('projeto.db')
            cursor = conn.cursor()
            cursor2 = conn.cursor()
            cursor3 = conn.cursor()
            cursor4 = conn.cursor()
            cursor5 = conn.cursor()
            r = cursor.execute("""
                        SELECT codt,periodo,codd FROM turma WHERE codt = ?
                        """, (cod,))
            cpfp = cursor2.execute("""
                        SELECT cpfp FROM turma WHERE codt = ?
                        """, (cod,))
            cpfa = cursor3.execute("""
                               SELECT cpfa FROM turma WHERE codt = ?
                               """, (cod,))
            a = []
            b = []
            for i in cpfp.fetchall():

                cpfp2 = cursor4.execute("""
                            SELECT nome FROM professor WHERE cpf = ?
                            """, (str(i[0]),))
                a.append(cpfp2.fetchone())
            for i in cpfa.fetchall():
                cpfa2 =cursor5.execute("""
                            SELECT nome FROM aluno WHERE cpf = ?
                            """, (str(i[0]),))
                b.append(cpfa2.fetchone())
            stconata.insert(INSERT, '----------------------------------------------------------------------')
            stconata.insert(INSERT, '                            ATA da Turma        \n')
            stconata.insert(INSERT, '----------------------------------------------------------------------\n')
            stconata.insert(INSERT, '                Turma    |     Periodo    |     Cod disc    \n')
            stconata.insert(INSERT, '----------------------------------------------------------------------\n')
            stconata.insert(INSERT, "                " + "       |     ".join(r.fetchone()) +'\n')
            stconata.insert(INSERT, '----------------------------------------------------------------------\n')
            stconata.insert(INSERT, 'Professores:\n')
            for i in a:
                stconata.insert(INSERT, "            " + str(i[0]) + '\n')
            stconata.insert(INSERT, '----------------------------------------------------------------------\n')
            stconata.insert(INSERT, 'Alunos:\n')
            for i in b:
                stconata.insert(INSERT, "            " + str(i[0]) + '\n')

    btata = Button(Frameatat, font='arial', text='Gerar', command=pegandoData)
    btata.place(x=250, y=350)

    lblInicio['text'] = 'Turma'
def btdisciplina():
    aba_control.forget
    FrameC.place(x=1000, y=10000)
    FrameA.place(x=1000, y=10000)
    FrameD.place(x=1000, y=10000)
    FrameCON.place(x=1000, y=10000)
    FrameCa.place(x=1000, y=10000)
    FrameAa.place(x=1000, y=10000)
    FrameDa.place(x=1000, y=10000)
    FrameCONa.place(x=1000, y=10000)
    Framerelt.destroy()
    Frameatat.destroy()
    #criando a aba de cadastrar

    aba_control.add(abaC, text='Cadastrar')
    aba_control.pack(expand=1, fill='both')

    #chamando o frame do cadastro de disciplinas
    FrameCd.place(x=20, y=20)

    # Declarando todos os labels de cadastro

    lblNome = Label(FrameCd, text='Nome:')
    lblNome.place(x=90, y=100)
    lblCod = Label(FrameCd, text='Código:')
    lblCod.place(x=90, y=120)

    # Declarando todos os text fields de cadastro

    tfNome = Entry(FrameCd, font='arial')
    tfNome.place(x=190, y=100)
    tfCod = Entry(FrameCd, font='arial')
    tfCod.place(x=190, y=120)

    #criando uma função parar pegar os dados e que chama a função qeu de fato vai efetuar os cadastros

    def pegandoDCD():
        dadosN = tfNome.get()
        dadosCod = tfCod.get()
        if dadosCod == '' or dadosN == '':
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfCod.delete(0, END), tfNome.delete(0, END)
        elif dadosCod.isalpha() or dadosN.isnumeric():
            messagebox.showinfo('Cadastro', 'Dados inválidos!')
            tfCod.delete(0, END), tfNome.delete(0, END)
        elif consultaespD(dadosCod) != None:
            messagebox.showinfo('Cadastro', 'Esta disciplina já foi cadastrado!')
            tfNome.delete(0, END), tfCod.delete(0, END)
        else:
            messagebox.showinfo('Cadastro', 'Cadastro feito com sucesso!')
            cadastrod(dadosN, dadosCod)
            tfNome.delete(0, END), tfCod.delete(0, END)

    #criando o botão de cadastro

    btcadastro = Button(FrameCd, text = 'Cadastrar',command = pegandoDCD)
    btcadastro.place(x=200, y=200)

    #criando a aba de atualizar

    aba_control.add(abaA, text='Atualizar')
    aba_control.pack(expand=1, fill='both')

    #chamando o frame de atualizar de disciplina
    FrameAd.place(x = 20, y =20)

    # Declarando todos os labels de atualizar

    lblNome = Label(FrameAd, text='Nome:')
    lblNome.place(x=90, y=200)
    lblCod = Label(FrameAd, text='Código:')
    lblCod.place(x=90, y=20)
    lblnovocod = Label(FrameAd, text = 'Novo cod')
    lblnovocod.place(x = 90, y = 220)

    # Declarando todos os text fields de atualizar

    tfCoda = Entry(FrameAd, font='arial')
    tfCoda.place(x=190, y=20)
    tfCoda.configure(width = 24)
    tfNomea = Entry(FrameAd, font='arial')
    tfNomea.place(x=190, y=200)
    tfNomea.configure(width = 24)
    tfnovocod = Entry(FrameAd, font = 'arial')
    tfnovocod.place(x = 190, y = 220)

    # declarando todos o botoões de atualizar
    def pegandoDDa():
        nome = tfNomea.get()
        cod = tfCoda.get()
        novocod = tfnovocod.get()
        if nome == '' or cod == ''or novocod == '':
            messagebox.showinfo('Atualizar', 'Dados inválidos')
            tfNomea.delete(0, END), tfCoda.delete(0, END)
        elif nome.isnumeric() or cod.isalpha() or novocod.isalpha():
            messagebox.showinfo('Atualizar', 'Dados inválidos')
            tfNomea.delete(0, END), tfCoda.delete(0, END)
        elif consultaespD(cod) == None:
            messagebox.showinfo('Atualizar', 'Está disciplina não existe!')
            tfNomea.delete(0, END), tfCoda.delete(0, END)
        else:
            tfNomea.delete(0, END), tfCoda.delete(0, END),tfnovocod.delete(0, END)
            atualizarD(nome, cod,novocod)
            atualizarcodTd(cod,novocod)
            messagebox.showinfo('Atualizar', 'Dados atualizados com sucesso')
    def consulta():
        cod = tfCoda.get()
        if cod =='':
            atualizar_tabelasd(stcon)
        elif cod.isalpha():
            messagebox.showinfo('Atualizar', 'Dados inválidos')
            tfCoda.delete(0,END)
        elif consultaespD(cod) == None:
            messagebox.showinfo('Atualizar', 'Este aluno não existe')
        else:
            stcon.insert(INSERT, str(' |  '.join(consultaespD(cod))) + '\n')
    stcon = scrolledtext.ScrolledText(FrameAd, width=40, height=5)
    stcon.place(x = 90, y = 70)
    atualizar_tabelasd(stcon)
    btatualizar = Button(FrameAd, text='Atualizar', command=pegandoDDa)
    btatualizar.place(x=150, y=300)
    btcon = Button(FrameAd, text='Consultar', command=consulta)
    btcon.place(x=220, y=300)

    #crianda a aba deletar

    aba_control.add(abaD, text='Deletar')
    aba_control.pack(expand=1, fill='both')

    #chamando o frame de deletar de diciplina

    FrameDd.place(x = 20, y = 20)

    # Declarando todos os labels de deletar

    lblCodD = Label(FrameDd, text='Código:')
    lblCodD.place(x=90, y=20)

    # Declarando todos os text fields de deletar

    tfCodd = Entry(FrameDd, font='arial')
    tfCodd.place(x=190, y=20)
    stconsultaDd = scrolledtext.ScrolledText(FrameDd, width=35, height=10)
    stconsultaDd.place(x=90, y=60)

    def pegandDDd():
        cod = tfCodd.get()
        if cod == '':
            atualizar_tabelasd(stconsultaDd)
        elif cod.isalpha():
            messagebox.showinfo('Deletar', 'Dados inválidos')
            tfCodd.delete(0, END)
        elif consultaespD(cod) == None:
            messagebox.showinfo('Deletar', 'Esta disciplina não existe!')
            tfCodd.delete(0, END)
        else:
            tfCodd.delete(0, END)
            deletaD(cod)
            deleta_disciplina_T(cod)
    def consultad():
        cod = tfCodd.get()
        if cod == '':
            atualizar_tabelasd(stconsultaDd)
        elif consultaespA(cod) == None:
            messagebox.showinfo('Deletar', 'Esta disciplina não existe')
        elif cod.isalpha():
            messagebox.showinfo('Deletar', 'Dados Inválidos')
        else:
            stconsultaDd.delete(1.0, END)
            stconsultaDd.insert(INSERT, 'Código | Nome\n\n')
            stconsultaDd.insert(INSERT, str(' |  '.join(consultaespD(cod))) + '\n')
    # declarando todos o botoões de deletar

    btdeletar = Button(FrameDd, text='Deletar', command=pegandDDd)
    btdeletar.place(x=200, y=300)
    btcond = Button(FrameDd, text='Consultarr', command=consultad)
    btcond.place(x=260, y=300)
    atualizar_tabelasd(stconsultaDd)

    aba_control.add(abaCON, text='Consultar')
    aba_control.pack(expand=1, fill='both')

    FrameCONd.place(x = 20, y = 20)

    lblCod = Label(FrameCONd, text='Código:').place(x=90, y=20)

    # declarando todos os text fields de Consultar

    tfCodcon = Entry(FrameCONd, font='arial')
    tfCodcon.place(x=190, y=20)

    stconsultaDcon = scrolledtext.ScrolledText(FrameCONd, width=35, height=10)
    stconsultaDcon.place(x=90, y=60)

    def pegandoDCond():
        cod = tfCodcon.get()
        if cod == '':
            atualizar_tabelasd(stconsultaDcon)
            tfCodcon.delete(0, END)
        elif cod.isalpha():
            messagebox.showinfo('Consulta', 'Esta disciplina não existe')
            tfCodcon.delete(0, END)
        elif consultaespD(cod) == None:
            messagebox.showinfo('Consulta', 'Esta disciplina não existe!')
            tfCodcon.delete(0, END)
        else:
            stconsultaDcon.delete(1.0, END)
            stconsultaDcon.insert(INSERT, 'Código |  Nome          \n\n')
            stconsultaDcon.insert(INSERT, str(' |  '.join(consultaespD(cod))) + '\n')
            tfCodcon.delete(0,END)

    btconsultar = Button(FrameCONd, text='Consultar', command = pegandoDCond)
    btconsultar['command']= atualizar_tabelasd(stconsultaDcon)
    btconsultar.pack()
    btconsultar.place(x=200, y=300)



    lblInicio['text'] = 'Disciplina'

#CRIANDO TODOS OS BOTÕES DA TELA INICIAL
btprofessor = Button(root, text = 'Professor',width  =30, height = 8, command = btfprofessor)
btprofessor.place(x = 0, y = 60)
btaluno = Button(root, text = 'Aluno',width  = 30, height = 7, command = btaluno)
btaluno.place(x = 0, y = 180)
btdisciplina = Button(root, text = 'Disciplina',width  = 30, height = 7,command = btdisciplina)
btdisciplina.place(x = 0, y = 286)
btturma = Button(root, text = 'Turma',width  = 30, height = 7,command = btturma)
btturma.place(x = 0, y = 397)


root.mainloop()