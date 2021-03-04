################################################################################
################################# BIBLIOTECAS ##################################
################################################################################
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as tkMessageBox

################################################################################
################################### TELA LOGIN #################################
################################################################################

tela_login = tk.Tk()
tela_login.title("Login")
tela_login.tk.call('wm', 'iconphoto', tela_login._w, tk.PhotoImage(file='icone.png'))
tela_login.geometry("250x140+600+340")
tela_login.resizable(False, False)
tela_login["background"]="white"

################################################################################
################################## ÍCONES ######################################
################################################################################

ico_estudante = PhotoImage(file="estudante.png")
ico_funcionario = PhotoImage(file="funcionario.png")
ico_registro = PhotoImage(file="registro.png")
ico_rotina = PhotoImage(file="rotinas.png")
ico_em_breve = PhotoImage(file="breve.png")

################################################################################
################################## FUNÇÕES #####################################
################################################################################
def entrar():
    print("Entrou com sucesso!")

def sair():
    result=tkMessageBox.askquestion("ATENÇÃO",
                                    "Tem certeza que deseja sair?",
                                    icon="warning")
    if result== "yes":
        tela_login.destroy()
        exit

def aviso_salvo():
    result=tkMessageBox.showinfo("Salvo",
                                 "Os dados foram salvos",
                                 icon="warning")

def aviso_em_breve():
    result=tkMessageBox.showinfo("Em breve",
                                 "Aguarde atualizações futuras!",
                                 icon="warning")

def salvar():
    result=tkMessageBox.askquestion("ATENÇÃO",
                                    "Tem certeza que deseja salvar?",
                                    icon="warning")
    if result== "yes":
        result=tkMessageBox.showinfo("Salvo",
                                     "Os dados foram salvos",
                                     icon="warning")

def registrar():
    result=tkMessageBox.askquestion("ATENÇÃO",
                                    "Tem certeza que deseja registrar este estudante?",
                                    icon="warning")
    if result== "yes":
        result=tkMessageBox.showinfo("Registrado",
                                     "O ID foi registrado!",
                                     icon="warning")

def rotina():
    result=tkMessageBox.askquestion("ATENÇÃO",
                                    "Tem certeza que deseja contabilizar este estudante?",
                                    icon="warning")
    if result== "yes":
        result=tkMessageBox.showinfo("Salvo",
                                     "O ID foi computado!",
                                     icon="warning")
        
def tela_inicial():
    tela_inicial = Toplevel()
    tela_inicial.title("System-SA")
    tela_inicial.tk.call('wm', 'iconphoto', tela_inicial._w, tk.PhotoImage(file='icone.png'))
    tela_inicial.geometry("520x160+470+320")
    tela_inicial.resizable(False, False)
    
    #FUNÇÕES MENU CADASTRO ESTUDANTES
    def tela_cadastro_estudantes():
        tela_cadastro_estudantes = Tk()
        tela_cadastro_estudantes.title("Cadastro dos Estudantes")
        tela_cadastro_estudantes.geometry("700x335+380+210")
        tela_cadastro_estudantes.resizable(False, False)
        def voltar_inicial_tela_cadastro_estudantes():
            tela_cadastro_estudantes.destroy()
            return

    #    def limpar_tela_estudantes(text):
    #        ent_nome_estudante.reset(0,END)
    #        ent_nome_estudante.insert(0, text)
    #            ent_rg_estudante.delete(0, END)
    #            ent_email_estudante.delete(0, END)
    #            ent_cpf_estudante.delete(0, END)
    #            ent_escola_origem_estudante.delete(0, END)
    #            data_nascimento_combobox_dia.delete(0, END)
    #            data_nascimento_combobox_mes.delete(0, END)
    #            data_nascimento_combobox_ano.delete(0, END)
    #            self.ent_telefone_estudante.delete(0, END)
    #            telefone_combobox_telefone_ddi.delete(0, END)
    #            telefone_combobox_telefone_ddd.delete(0, END)
    #            ent_telefone_estudante.delete(0, END)
    #            ent_endereco_estudante_pais.delete(0, END)
    #            ent_endereco_estudante_estado.delete(0, END)
    #            ent_endereco_estudante_cidade.delete(0, END)
    #            ent_endereco_estudante_bairro.delete(0, END)
    #            ent_endereco_estudante_rua.delete(0, END)
    #            ent_endereco_estudante_numero.delete(0, END)
    #            ent_nome_responsavel.delete(0, END)
    #            ent_rg_responsavel.delete(0, END)
    #            ent_email_responsavel.delete(0, END)
    #            ent_cpf_responsavel.delete(0, END)
    #            ent_telefone_responsavel.delete(0, END)
    #            telefone_combobox_telefone_ddi.delete(0, END)
    #            telefone_combobox_telefone_ddd.delete(0, END)
    #            termo_responsavel_combobox.delete(0, END)
    #            ent_combobox_responsavel_pais.delete(0, END)
    #            ent_endereco_responsavel_estado.delete(0, END)
    #            ent_endereco_responsavel_cidade.delete(0, END)
    #            ent_endereco_responsavel_bairro.delete(0, END)
    #            ent_endereco_responsavel_rua.delete(0, END)
    #            ent_endereco_responsavel_numero.delete(0, END)
    #            tipo_sanguineo_combobox.delete(0, END)
    #            ent_alergia_estudante.delete(0, END)
            
        #CHAMAR BIBLIOTECA TTK
        note = ttk.Notebook(tela_cadastro_estudantes)
        note.place(x=0,
                   y=0,
                   width=800,
                   height=500)

        #FAZENDO OS NOTEBOOKS
        #CRIANDO NOTEBOOK 1
        tab_1 = Frame(note)
        note.add(tab_1,
                 text="Dados do Estudante")
        #NOME DO ESTUDANTE
        lbl_nome_estudante = Label(tab_1,
                                   text="Nome: ",
                                   font="Times 12 bold").place(relx=0.018,
                                                               rely=0.007)
        ent_nome_estudante = tk.Entry(tab_1,
                                   bg="lightgrey").place(relx=0.1,
                                                         rely=0.01,
                                                         relwidth=0.40)
        #RG DO ESTUDANTE
        lbl_rg_estudante = Label(tab_1,
                                 text="RG: ",
                                 font="Times 12 bold").place(relx=0.53,
                                                             rely=0.007,
                                                             relwidth=0.05)
        ent_rg_estudante = Entry(tab_1,
                                 bg="lightgrey").place(relx=0.59,
                                                       rely=0.01,
                                                       relwidth=0.24)
        #E-MAIL DO ESTUDANTE
        lbl_email_estudante = Label(tab_1,
                                    text="E-mail: ",
                                    font="Times 12 bold").place(relx=0.018,
                                                                rely=0.058)
        ent_email_estudante = Entry(tab_1,
                                   bg="lightgrey").place(relx=0.1,
                                                         rely=0.065,
                                                         relwidth=0.40)
        #CPF DO ESTUDANTE
        lbl_cpf_estudante = Label(tab_1,
                                    text="CPF: ",
                                    font="Times 12 bold").place(relx=0.53,
                                                                rely=0.06,
                                                                relwidth=0.05)
        ent_cpf_estudante = Entry(tab_1,
                                  bg="lightgrey").place(relx=0.59,
                                                        rely=0.065,
                                                        relwidth=0.24)
        #ESCOLA DE ORIGEM
        lbl_escola_origem_estudante = Label(tab_1,
                                            text="Escola de Origem: ",
                                            font="Times 12 bold").place(relx=0.018,
                                                                        rely=0.115,
                                                                        relwidth=0.165)
        ent_escola_origem_estudante = Entry(tab_1,
                                            bg="lightgrey").place(relx=0.19,
                                                         rely=0.125,
                                                         relwidth=0.31)
        #DATA DE NASCIMENTO
        lbl_data_nascimento_estudante = Label(tab_1,
                                              text="Data de Nasc.: ",
                                              font="Times 12 bold").place(relx=0.53,
                                                                          rely=0.115)
    
        #Dias da Semana
        data_nascimento_combobox_dia = ttk.Combobox(tab_1,
                                                    values=[" 01 ",
                                                            " 02 ",
                                                            " 03 ",
                                                            " 04 ",
                                                            " 05 ",
                                                            " 06 ",
                                                            " 07 ",
                                                            " 08 ",
                                                            " 09 ",
                                                            " 10 ",
                                                            " 11 ",
                                                            " 12 ",
                                                            " 13 ",
                                                            " 14 ",
                                                            " 15 ",
                                                            " 16 ",
                                                            " 17 ",
                                                            " 18 ",
                                                            " 19 ",
                                                            " 20 ",
                                                            " 21 ",
                                                            " 22 ",
                                                            " 23 ",
                                                            " 24 ",
                                                            " 25 ",
                                                            " 26 ",
                                                            " 27 ",
                                                            " 28 ",
                                                            " 29 ",
                                                            " 30 ",
                                                            " 31 "])
        data_nascimento_combobox_dia.set("Dia")
        data_nascimento_combobox_dia.place(relx=0.67,
                                           rely=0.12,
                                           relwidth=0.052)

        #Meses do ano
        data_nascimento_combobox_mes = ttk.Combobox(tab_1,
                                                    values=[" 01 ",
                                                            " 02 ",
                                                            " 03 ",
                                                            " 04 ",
                                                            " 05 ",
                                                            " 06 ",
                                                            " 07 ",
                                                            " 08 ",
                                                            " 09 ",
                                                            " 10 ",
                                                            " 11 ",
                                                            " 12 "])
        data_nascimento_combobox_mes.set("Mês")
        data_nascimento_combobox_mes.place(relx=0.717,
                                           rely=0.12,
                                           relwidth=0.057)

        #Anos
        data_nascimento_combobox_ano = ttk.Combobox(tab_1,
                                                    values=["1960",
                                                            "1961",
                                                            "1962",
                                                            "1963",
                                                            "1964",
                                                            "1965",
                                                            "1966",
                                                            "1967",
                                                            "1968",
                                                            "1969",
                                                            "1970",
                                                            "1971",
                                                            "1972",
                                                            "1972",
                                                            "1973",
                                                            "1974",
                                                            "1975",
                                                            "1976",
                                                            "1977",
                                                            "1978",
                                                            "1979",
                                                            "1980",
                                                            "1981",
                                                            "1982",
                                                            "1983",
                                                            "1984",
                                                            "1985",
                                                            "1986",
                                                            "1987",
                                                            "1988",
                                                            "1989",
                                                            "1990",
                                                            "1991",
                                                            "1992",
                                                            "1993",
                                                            "1994",
                                                            "1995",
                                                            "1996",
                                                            "1997",
                                                            "1998",
                                                            "1999",
                                                            "2000",
                                                            "2001",
                                                            "2002",
                                                            "2003",
                                                            "2004",
                                                            "2005",
                                                            "2006",
                                                            "2007",
                                                            "2008",
                                                            "2009",
                                                            "2010",
                                                            "2011",
                                                            "2012",
                                                            "2013",
                                                            "2014",
                                                            "2015",
                                                            "2016",
                                                            "2017",
                                                            "2018",
                                                            "2019",
                                                            "2020"])
        data_nascimento_combobox_ano.set("Ano")
        data_nascimento_combobox_ano.place(relx=0.77,
                                           rely=0.12,
                                           relwidth=0.061)

        #TELEFONE DO ESTUDANTE
        lbl_telefone_estudante = Label(tab_1,
                                       text="Telefone para Contato: ",
                                       font="Times 12 bold").place(relx=0.0168,
                                                                   rely=0.17,
                                                                   relwidth=0.21)
        ent_telefone_estudante = Entry(tab_1,
                                       bg="lightgrey").place(relx=0.34,
                                                             rely=0.18,
                                                             relwidth=0.16)

        #DDI do Número de Telefone
        telefone_combobox_telefone_ddi = ttk.Combobox(tab_1,
                                                      values=["+1",
                                                              "+7",
                                                              "+20",
                                                              "+27",
                                                              "+30",
                                                              "+31",
                                                              "+32",
                                                              "+33",
                                                              "+34",
                                                              "+36",
                                                              "+39",
                                                              "+40",
                                                              "+41",
                                                              "+43",
                                                              "+44",
                                                              "+45",
                                                              "+46",
                                                              "+47",
                                                              "+48",
                                                              "+49",
                                                              "+51",
                                                              "+52",
                                                              "+53",
                                                              "+54",
                                                              "+55",
                                                              "+56",
                                                              "+57",
                                                              "+58",
                                                              "+60",
                                                              "+61",
                                                              "+62",
                                                              "+63",
                                                              "+64",
                                                              "+65",
                                                              "+66",
                                                              "+81",
                                                              "+82",
                                                              "+84",
                                                              "+86",
                                                              "+90",
                                                              "+91",
                                                              "+92",
                                                              "+93",
                                                              "+94",
                                                              "+95",
                                                              "+98",
                                                              "+212",
                                                              "+213",
                                                              "+216",
                                                              "+218",
                                                              "+220",
                                                              "+221"])
        telefone_combobox_telefone_ddi.set("DDI")
        telefone_combobox_telefone_ddi.place(relx=0.22,
                                             rely=0.18,
                                             relwidth=0.06,
                                             relheight=0.037)

        #DDD do Número de Telefone
        telefone_combobox_telefone_ddd = ttk.Combobox(tab_1,
                                                      values=["11",
                                                              "12",
                                                              "13",
                                                              "14",
                                                              "15",
                                                              "16",
                                                              "17",
                                                              "18",
                                                              "19",
                                                              "21",
                                                              "22",
                                                              "24",
                                                              "27",
                                                              "27",
                                                              "28",
                                                              "31",
                                                              "32",
                                                              "33",
                                                              "34",
                                                              "35",
                                                              "37",
                                                              "38",
                                                              "41",
                                                              "42",
                                                              "43",
                                                              "44",
                                                              "45",
                                                              "46",
                                                              "47",
                                                              "48",
                                                              "49",
                                                              "51",
                                                              "53",
                                                              "54",
                                                              "55",
                                                              "61",
                                                              "62",
                                                              "63",
                                                              "64",
                                                              "65",
                                                              "67",
                                                              "68",
                                                              "69",
                                                              "71",
                                                              "73",
                                                              "74",
                                                              "75",
                                                              "77",
                                                              "79",
                                                              "81",
                                                              "82",
                                                              "83",
                                                              "84",
                                                              "85",
                                                              "86",
                                                              "87",
                                                              "88",
                                                              "89",
                                                              "91",
                                                              "92",
                                                              "93",
                                                              "94",
                                                              "95",
                                                              "96",
                                                              "97",
                                                              "98",
                                                              "99"])
        telefone_combobox_telefone_ddd.set("DDD")
        telefone_combobox_telefone_ddd.place(relx=0.28,
                                             rely=0.18,
                                             relwidth=0.06,
                                             relheight=0.037)

        #CURSOS
        lbl_cursos_estudante = Label(tab_1,
                                     text="Cursos: ",
                                     font="Times 12 bold").place(relx=0.53,
                                                                 rely=0.17,
                                                                 relwidth=0.075)
        cursos_combobox_estudante = ttk.Combobox(tab_1,
                                                 values=["Técnico em Administração",
                                                         "Técnico em Marketing",
                                                         "Técnico em Sistemas",
                                                         "Técnico em Turismo"])
        cursos_combobox_estudante.set("Cursos")
        cursos_combobox_estudante.place(relx=0.61,
                                        rely=0.18,
                                        relwidth=0.22)

        #ENDEREÇO DO ESTUDANTE
        lbl_endereco_estudante = Label(tab_1,
                                       text="Endereço",
                                       font="Times 12 bold").place(relx=0.0168,
                                                                   rely=0.235,
                                                                   relwidth=0.09)
    
        #Endereço do Estudante País
        lbl_endereco_estudante_pais = Label(tab_1,
                                            text="País: ",
                                            font="Times 12 bold").place(relx=0.0168,
                                                                        rely=0.285,
                                                                        relwidth=0.06)
        ent_endereco_estudante_pais = Entry(tab_1,
                                            bg="lightgrey").place(relx=0.1,
                                                                  rely=0.29,
                                                                  relwidth=0.16)
    
        #Endereço do Estudante Estado
        lbl_endereco_estudante_estado = Label(tab_1,
                                              text="Estado: ",
                                              font="Times 12 bold").place(relx=0.275,
                                                                          rely=0.285,
                                                                          relwidth=0.07)
        ent_endereco_estudante_estado = Entry(tab_1,
                                              bg="lightgrey").place(relx=0.345,
                                                                    rely=0.29,
                                                                    relwidth=0.175)

        #Endereço do Estudante Cidade
        lbl_endereco_estudante_cidade = Label(tab_1,
                                              text="Cidade: ",
                                              font="Times 12 bold").place(relx=0.535,
                                                                          rely=0.285,
                                                                          relwidth=0.08)
        ent_endereco_estudante_cidade = Entry(tab_1,
                                              bg="lightgrey").place(relx=0.62,
                                                                    rely=0.29,
                                                                    relwidth=0.212)
        #Endereço do Estudante Bairro
        lbl_endereco_estudante_bairro = Label(tab_1,
                                              text="Bairro: ",
                                              font="Times 12 bold").place(relx=0.0168,
                                                                          rely=0.337,
                                                                          relwidth=0.075)
        ent_endereco_estudante_bairro = Entry(tab_1,
                                              bg="lightgrey").place(relx=0.1,
                                                                    rely=0.342,
                                                                    relwidth=0.16)
        #Endereço do Estudante Rua
        lbl_endereco_estudante_rua = Label(tab_1,
                                           text="Rua: ",
                                           font="Times 12 bold").place(relx=0.27,
                                                                       rely=0.337,
                                                                       relwidth=0.062)
        ent_endereco_estudante_rua = Entry(tab_1,
                                           bg="lightgrey").place(relx=0.345,
                                                                 rely=0.342,
                                                                 relwidth=0.375)
        #Endereço do Estudante Número
        lbl_endereco_estudante_numero = Label(tab_1,
                                              text="N°: ",
                                              font="Times 12 bold").place(relx=0.735,
                                                                          rely=0.337,
                                                                          relwidth=0.04)
        ent_endereco_estudante_numero = Entry(tab_1,
                                              bg="lightgrey").place(relx=0.77,
                                                                    rely=0.342,
                                                                    relwidth=0.06)
        #Foto do Estudante
        btn_foto_estudante = Button(tab_1,
                                    text="Fazer upload da foto",
                                    font="Times 12 bold",
                                    bg="lightgrey").place(relx=0.33,
                                                          rely=0.4,
                                                          relheight=0.05)
    
        #CRIANDO NOTEBOOK 2
        tab_2 = Frame(note)
        note.add(tab_2,
                 text="Dados do Responsável")
        #NOME DO RESPONSÁVEL
        lbl_nome_responsavel = Label(tab_2,
                                     text="Nome: ",
                                     font="Times 12 bold").place(relx=0.018,
                                                                 rely=0.007)
        ent_nome_responsavel = Entry(tab_2,
                                     bg="lightgrey").place(relx=0.1,
                                                           rely=0.01,
                                                           relwidth=0.40)
        #RG DO RESPONSÁVEL
        lbl_rg_responsavel = Label(tab_2,
                                   text="RG: ",
                                   font="Times 12 bold").place(relx=0.53,
                                                               rely=0.007,
                                                               relwidth=0.05)
        ent_rg_responsavel = Entry(tab_2,
                                   bg="lightgrey").place(relx=0.59,
                                                         rely=0.01,
                                                         relwidth=0.24)
        #E-MAIL DO RESPONSÁVEL
        lbl_email_responsavel = Label(tab_2,
                                      text="E-mail: ",
                                      font="Times 12 bold").place(relx=0.018,
                                                                  rely=0.058)
        ent_email_responsavel = Entry(tab_2,
                                      bg="lightgrey").place(relx=0.1,
                                                            rely=0.065,
                                                            relwidth=0.40)
        #CPF DO RESPONSÁVEL
        lbl_cpf_responsavel = Label(tab_2,
                                    text="CPF: ",
                                    font="Times 12 bold").place(relx=0.53,
                                                                rely=0.06,
                                                                relwidth=0.05)
        ent_cpf_responsavel = Entry(tab_2,
                                    bg="lightgrey").place(relx=0.59,
                                                          rely=0.065,
                                                          relwidth=0.24)
        #TELEFONE DO RESPONSÁVEL
        lbl_telefone_responsavel = Label(tab_2,
                                         text="Telefone para Contato: ",
                                         font="Times 12 bold").place(relx=0.0168,
                                                                     rely=0.11,
                                                                     relwidth=0.21)
        ent_telefone_responsavel = Entry(tab_2,
                                         bg="lightgrey").place(relx=0.34,
                                                               rely=0.12,
                                                               relwidth=0.16)

        #DDI do Número de Telefone
        telefone_combobox_telefone_ddi = ttk.Combobox(tab_2,
                                                      values=["+1",
                                                              "+7",
                                                              "+20",
                                                              "+27",
                                                              "+30",
                                                              "+31",
                                                              "+32",
                                                              "+33",
                                                              "+34",
                                                              "+36",
                                                              "+39",
                                                              "+40",
                                                              "+41",
                                                              "+43",
                                                              "+44",
                                                              "+45",
                                                              "+46",
                                                              "+47",
                                                              "+48",
                                                              "+49",
                                                              "+51",
                                                              "+52",
                                                              "+53",
                                                              "+54",
                                                              "+55",
                                                              "+56",
                                                              "+57",
                                                              "+58",
                                                              "+60",
                                                              "+61",
                                                              "+62",
                                                              "+63",
                                                              "+64",
                                                              "+65",
                                                              "+66",
                                                              "+81",
                                                              "+82",
                                                              "+84",
                                                              "+86",
                                                              "+90",
                                                              "+91",
                                                              "+92",
                                                              "+93",
                                                              "+94",
                                                              "+95",
                                                              "+98",
                                                              "+212",
                                                              "+213",
                                                              "+216",
                                                              "+218",
                                                              "+220",
                                                              "+221"])
        telefone_combobox_telefone_ddi.set("DDI")
        telefone_combobox_telefone_ddi.place(relx=0.22,
                                             rely=0.12,
                                             relwidth=0.06,
                                             relheight=0.037)

        #DDD do Número de Telefone
        telefone_responsavel_combobox_telefone_ddd = ttk.Combobox(tab_2,
                                                                  values=["11",
                                                                          "12",
                                                                          "13",
                                                                          "14",
                                                                          "15",
                                                                          "16",
                                                                          "17",
                                                                          "18",
                                                                          "19",
                                                                          "21",
                                                                          "22",
                                                                          "24",
                                                                          "27",
                                                                          "27",
                                                                          "28",
                                                                          "31",
                                                                          "32",
                                                                          "33",
                                                                          "34",
                                                                          "35",
                                                                          "37",
                                                                          "38",
                                                                          "41",
                                                                          "42",
                                                                          "43",
                                                                          "44",
                                                                          "45",
                                                                          "46",
                                                                          "47",
                                                                          "48",
                                                                          "49",
                                                                          "51",
                                                                          "53",
                                                                          "54",
                                                                          "55",
                                                                          "61",
                                                                          "62",
                                                                          "63",
                                                                          "64",
                                                                          "65",
                                                                          "67",
                                                                          "68",
                                                                          "69",
                                                                          "71",
                                                                          "73",
                                                                          "74",
                                                                          "75",
                                                                          "77",
                                                                          "79",
                                                                          "81",
                                                                          "82",
                                                                          "83",
                                                                          "84",
                                                                          "85",
                                                                          "86",
                                                                          "87",
                                                                          "88",
                                                                          "89",
                                                                          "91",
                                                                          "92",
                                                                          "93",
                                                                          "94",
                                                                          "95",
                                                                          "96",
                                                                          "97",
                                                                          "98",
                                                                          "99"])
        telefone_responsavel_combobox_telefone_ddd.set("DDD")
        telefone_responsavel_combobox_telefone_ddd.place(relx=0.28,
                                                         rely=0.12,
                                                         relwidth=0.06,
                                                         relheight=0.037)

        #DATA DE NASCIMENTO
        lbl_data_nascimento_responsavel = Label(tab_2,
                                                text="Data de Nasc.: ",
                                                font="Times 12 bold").place(relx=0.53,
                                                                            rely=0.12)
        
        #Dias da Semana
        data_nascimento_responsavel_combobox_dia = ttk.Combobox(tab_2,
                                                                values=[" 01 ",
                                                                        " 02 ",
                                                                        " 03 ",
                                                                        " 04 ",
                                                                        " 05 ",
                                                                        " 06 ",
                                                                        " 07 ",
                                                                        " 08 ",
                                                                        " 09 ",
                                                                        " 10 ",
                                                                        " 11 ",
                                                                        " 12 ",
                                                                        " 13 ",
                                                                        " 14 ",
                                                                        " 15 ",
                                                                        " 16 ",
                                                                        " 17 ",
                                                                        " 18 ",
                                                                        " 19 ",
                                                                        " 20 ",
                                                                        " 21 ",
                                                                        " 22 ",
                                                                        " 23 ",
                                                                        " 24 ",
                                                                        " 25 ",
                                                                        " 26 ",
                                                                        " 27 ",
                                                                        " 28 ",
                                                                        " 29 ",
                                                                        " 30 ",
                                                                        " 31 "])
        data_nascimento_responsavel_combobox_dia.set("Dia")
        data_nascimento_responsavel_combobox_dia.place(relx=0.67,
                                                       rely=0.12,
                                                       relwidth=0.052)

        #Meses do ano
        data_nascimento_responsavel_combobox_mes = ttk.Combobox(tab_2,
                                                                values=[" 01 ",
                                                                        " 02 ",
                                                                        " 03 ",
                                                                        " 04 ",
                                                                        " 05 ",
                                                                        " 06 ",
                                                                        " 07 ",
                                                                        " 08 ",
                                                                        " 09 ",
                                                                        " 10 ",
                                                                        " 11 ",
                                                                        " 12 "])
        data_nascimento_responsavel_combobox_mes.set("Mês")
        data_nascimento_responsavel_combobox_mes.place(relx=0.717,
                                                       rely=0.12,
                                                       relwidth=0.057)

        #Anos
        data_nascimento_responsavel_combobox_ano = ttk.Combobox(tab_2,
                                                                values=["1960",
                                                                        "1961",
                                                                        "1962",
                                                                        "1963",
                                                                        "1964",
                                                                        "1965",
                                                                        "1966",
                                                                        "1967",
                                                                        "1968",
                                                                        "1969",
                                                                        "1970",
                                                                        "1971",
                                                                        "1972",
                                                                        "1972",
                                                                        "1973",
                                                                        "1974",
                                                                        "1975",
                                                                        "1976",
                                                                        "1977",
                                                                        "1978",
                                                                        "1979",
                                                                        "1980",
                                                                        "1981",
                                                                        "1982",
                                                                        "1983",
                                                                        "1984",
                                                                        "1985",
                                                                        "1986",
                                                                        "1987",
                                                                        "1988",
                                                                        "1989",
                                                                        "1990",
                                                                        "1991",
                                                                        "1992",
                                                                        "1993",
                                                                        "1994",
                                                                        "1995",
                                                                        "1996",
                                                                        "1997",
                                                                        "1998",
                                                                        "1999",
                                                                        "2000",
                                                                        "2001",
                                                                        "2002",
                                                                        "2003",
                                                                        "2004",
                                                                        "2005",
                                                                        "2006",
                                                                        "2007",
                                                                        "2008",
                                                                        "2009",
                                                                        "2010",
                                                                        "2011",
                                                                        "2012",
                                                                        "2013",
                                                                        "2014",
                                                                        "2015",
                                                                        "2016",
                                                                        "2017",
                                                                        "2018",
                                                                        "2019",
                                                                        "2020"])
        data_nascimento_responsavel_combobox_ano.set("Ano")
        data_nascimento_responsavel_combobox_ano.place(relx=0.77,
                                                       rely=0.12,
                                                       relwidth=0.061)

        #VOCÊ É?
        lbl_termo_responsavel = Label(tab_2,
                                      text="Você é: ",
                                      font="Times 12 bold").place(relx=0.0162,
                                                                  rely=0.165,
                                                                  relwidth=0.07)
        termo_responsavel_combobox = ttk.Combobox(tab_2,
                                                  values=["Familiar",
                                                          "Mãe",
                                                          "Pai",
                                                          "Responsável Legal"])
        termo_responsavel_combobox.set("Responsável")
        termo_responsavel_combobox.place(relx=0.1,
                                         rely=0.17,
                                         relwidth=0.16)
            
        #ENDEREÇO DO RESPONSÁVEL
        lbl_endereco_responsavel = Label(tab_2,
                                         text="Endereço",
                                         font="Times 12 bold").place(relx=0.0168,
                                                                     rely=0.235,
                                                                     relwidth=0.09)
        
        #Endereço do Responsável País
        lbl_endereco_responsavel_pais = Label(tab_2,
                                              text="País: ",
                                              font="Times 12 bold").place(relx=0.0168,
                                                                          rely=0.285,
                                                                          relwidth=0.06)
        ent_combobox_responsavel_pais = Entry(tab_2,
                                              bg="lightgrey").place(relx=0.1,
                                                                    rely=0.29,
                                                                    relwidth=0.16)
        
        #Endereço do Responsável Estado
        lbl_endereco_responsavel_estado = Label(tab_2,
                                                text="Estado: ",
                                                font="Times 12 bold").place(relx=0.275,
                                                                            rely=0.285,
                                                                            relwidth=0.07)
        ent_endereco_responsavel_estado = Entry(tab_2,
                                                bg="lightgrey").place(relx=0.345,
                                                                      rely=0.29,
                                                                      relwidth=0.175)

        #Endereço do Responsável Cidade
        lbl_endereco_responsavel_cidade = Label(tab_2,
                                                text="Cidade: ",
                                                font="Times 12 bold").place(relx=0.535,
                                                                            rely=0.285,
                                                                            relwidth=0.08)
        ent_endereco_responsavel_cidade = Entry(tab_2,
                                                bg="lightgrey").place(relx=0.62,
                                                                      rely=0.29,
                                                                      relwidth=0.212)
        #Endereço do Responsável Bairro
        lbl_endereco_responsavel_bairro = Label(tab_2,
                                                text="Bairro: ",
                                                font="Times 12 bold").place(relx=0.0168,
                                                                            rely=0.337,
                                                                            relwidth=0.075)
        ent_endereco_responsavel_bairro = Entry(tab_2,
                                                bg="lightgrey").place(relx=0.1,
                                                                      rely=0.342,
                                                                      relwidth=0.16)
        #Endereço do Responsável Rua
        lbl_endereco_responsavel_rua = Label(tab_2,
                                             text="Rua: ",
                                             font="Times 12 bold").place(relx=0.27,
                                                                         rely=0.337,
                                                                         relwidth=0.062)
        ent_endereco_responsavel_rua = Entry(tab_2,
                                             bg="lightgrey").place(relx=0.345,
                                                                   rely=0.342,
                                                                   relwidth=0.375)
        #Endereço do Responsável Número
        lbl_endereco_responsavel_numero = Label(tab_2,
                                                text="N°: ",
                                                font="Times 12 bold").place(relx=0.735,
                                                                            rely=0.337,
                                                                            relwidth=0.04)
        ent_endereco_responsavel_numero = Entry(tab_2,
                                                bg="lightgrey").place(relx=0.77,
                                                                      rely=0.342,
                                                                      relwidth=0.06)
        
        #CRIANDO NOTEBOOK 3
        tab_3 = Frame(note)
        note.add(tab_3,
                 text="Observações")
        #TIPO SANGUÍNEO
        lbl_tipo_sanguineo_estudante = Label(tab_3,
                                             text="Tipo Sanguíneo: ",
                                             font="Times 12 bold").place(relx=0.0168,
                                                                         rely=0.007,
                                                                         relwidth=0.15)
        tipo_sanguineo_combobox = ttk.Combobox(tab_3,
                                               values=["     A+   ",
                                                       "     A-   ",
                                                       "     B+   ",
                                                       "     B-   ",
                                                       "     AB+   ",
                                                       "     AB-   ",
                                                       "     O+   ",
                                                       "     O-   ",
                                                       "     Rh nulo   "])
        tipo_sanguineo_combobox.set("  Tipo Sanguíneo  ")
        tipo_sanguineo_combobox.place(relx=0.165,
                                      rely=0.012,
                                      relwidth=0.16)
        #ALERGIAS
        lbl_alergia_estudante = Label(tab_3,
                                      text="Alergia: ",
                                      font="Times 12 bold").place(relx=0.0168,
                                                                  rely=0.06,
                                                                  relwidth=0.085)
        ent_alergia_estudante = Entry(tab_3,
                                      bg="lightgrey").place(relx=0.095,
                                                            rely=0.065,
                                                            relwidth=0.23)
        #STATUS DO ESTUDANTE
        lbl_status_estudante = Label(tab_3,
                                     text="Status: ",
                                     font="Times 12 bold").place(relx=0.0168,
                                                                 rely=0.11,
                                                                 relwidth=0.078)
        valor = IntVar()
        valor.set(0)
        rdbtn_estudante_ativo = Radiobutton(tab_3,
                                            text="Ativo",
                                            font="Times 12 bold",
                                            variable=valor,
                                            value=4).place(relx=0.115,
                                                           rely=0.108,
                                                           relwidth=0.068)
        rdbtn_estudante_inativo = Radiobutton(tab_3,
                                              text="Inativo",
                                              font="Times 12 bold",
                                              variable=valor,
                                              value=5).place(relx=0.21,
                                                             rely=0.108,
                                                             relwidth=0.082)
        
        #BUTTONS
        btn_tela_inicial_cadastro_estudantes_limpar = tk.Button(tela_cadastro_estudantes,
                                                             text="Limpar",
                                                             font="Times 12 bold",
                                                             bg="lightgrey").place(x=444,
                                                                                   y=285)
        
        btn_tela_inicial_cadastro_estudantes_salvar = Button(tela_cadastro_estudantes,
                                                             text="Salvar",
                                                             font="Times 12 bold",
                                                             bg="lightgrey",
                                                             command=salvar).place(x=517,
                                                                                   y=285)
        
        btn_tela_inicial_cadastro_estudantes_cancelar = Button(tela_cadastro_estudantes,
                                                          text="Cancelar",
                                                          font="Times 12 bold",
                                                          bg="lightgrey",
                                                          command=voltar_inicial_tela_cadastro_estudantes).place(x=585,
                                                                                                                 y=285)

    #FUNÇÕES MENU CONSULTAR ESTUDANTES
    def tela_consulta_estudantes():
        tela_consulta_estudantes = Tk()
        tela_consulta_estudantes.title("Consultar Estudantes")
        tela_consulta_estudantes.geometry("700x335+380+210")
        tela_consulta_estudantes.resizable(False, False)
        tela_consulta_estudantes["background"]="white"
        def voltar_inicial_tela_consulta_estudantes():
            tela_consulta_estudantes.destroy()
            return

        frame_superior = Frame(tela_consulta_estudantes,
                               bg="lightgrey").place(relx=0.0525,
                                                     rely=0.19,
                                                     relwidth=0.9,
                                                     relheight=0.6)
        lista_consulta_estudantes = ttk.Treeview(tela_consulta_estudantes,
                                                 column=("col1",
                                                         "col2",
                                                         "col3",
                                                         "col4"))

        lista_consulta_estudantes.heading("#0",
                                          text="Id")
        lista_consulta_estudantes.heading("#1",
                                          text="Nome")
        lista_consulta_estudantes.heading("#2",
                                          text="Data de Nasc.")
        lista_consulta_estudantes.heading("#3",
                                          text="Foto")

        lista_consulta_estudantes.column("#0",
                                         width=60)
        lista_consulta_estudantes.column("#1",
                                         width=380)
        lista_consulta_estudantes.column("#2",
                                         width=120)
        lista_consulta_estudantes.column("#3",
                                         width=80)
        
        lista_consulta_estudantes.place(relx=0.0525,
                                        rely=0.19,
                                        relwidth=0.9,
                                        relheight=0.06)
            

        #BARRA DE PESQUISA
        lbl_consulta_estudantes = Label(tela_consulta_estudantes,
                                        text="Digite o Nome: ",
                                        font="Times 13 bold",
                                        bg="white").place(relx=0.1,
                                                          rely=0.043)
        ent_consulta_estudantes = Entry(tela_consulta_estudantes,
                                        bg="lightgrey").place(relx=0.277,
                                                              rely=0.049,
                                                              relwidth=0.47,
                                                              relheight=0.065)
        #BOTÃO DE CONSULTA
        btn_consulta_tela_estudantes = Button(tela_consulta_estudantes,
                                              text="Consultar",
                                              font="Times 12 bold",
                                              bg="lightgrey").place(relx=0.75,
                                                                    rely=0.045,
                                                                    relheight=0.065)
        #BOTÃO DE CANCELAR 
        btn_tela_inicial_consulta_estudantes = Button(tela_consulta_estudantes,
                                                      text="Cancelar",
                                                      font="Times 12 bold",
                                                      bg="lightgrey",
                                                      command=voltar_inicial_tela_consulta_estudantes).place(x=585,
                                                                                                             y=285)

    #FUNÇÕES MENU CONSULTAR CURSOS
    def tela_cursos_estudantes():
        tela_cursos_estudantes = Tk()
        tela_cursos_estudantes.title("Consultar Cursos")
        tela_cursos_estudantes.geometry("700x335+380+210")
        tela_cursos_estudantes.resizable(False, False)
        tela_cursos_estudantes["background"]="white"
        def voltar_inicial_tela_cursos_estudantes():
            tela_cursos_estudantes.destroy()
            return

        frame_superior = Frame(tela_cursos_estudantes,
                               bg="lightgrey").place(relx=0.0525,
                                                     rely=0.19,
                                                     relwidth=0.9,
                                                     relheight=0.6)
        lista_cursos_estudantes = ttk.Treeview(tela_cursos_estudantes,
                                                 column=("col1",
                                                         "col2",
                                                         "col3",
                                                         "col4"))

        lista_cursos_estudantes.heading("#0",
                                          text="Id")
        lista_cursos_estudantes.heading("#1",
                                          text="Nome")
        lista_cursos_estudantes.heading("#2",
                                          text="Data de Nasc.")
        lista_cursos_estudantes.heading("#3",
                                          text="Foto")

        lista_cursos_estudantes.column("#0",
                                         width=60)
        lista_cursos_estudantes.column("#1",
                                         width=380)
        lista_cursos_estudantes.column("#2",
                                         width=120)
        lista_cursos_estudantes.column("#3",
                                         width=80)
        
        lista_cursos_estudantes.place(relx=0.0525,
                                        rely=0.19,
                                        relwidth=0.9,
                                        relheight=0.06)
            

        #BARRA DE PESQUISA
        lbl_consulta_estudantes_cursos = Label(tela_cursos_estudantes,
                                               text="Digite o Curso: ",
                                               font="Times 13 bold",
                                               bg="white").place(relx=0.1,
                                                                 rely=0.043)
        consulta_cursos_combobox = ttk.Combobox(tela_cursos_estudantes,
                                                values=["  Técnico em Administração  ",
                                                        "  Técnico em Marketing  ",
                                                        "  Técnico em Desenvolvimento de Sistemas  ",
                                                        "  Técnico em Turismo  "])
        consulta_cursos_combobox.set("Escolha o Curso")
        consulta_cursos_combobox.place(relx=0.277,
                                       rely=0.049,
                                       relwidth=0.47,
                                       relheight=0.065)
        
        #BOTÃO DE CONSULTA
        btn_consulta_tela_cursos = Button(tela_cursos_estudantes,
                                          text="Consultar",
                                          font="Times 12 bold",
                                          bg="lightgrey").place(relx=0.75,
                                                                rely=0.045,
                                                                relheight=0.065)
        #BOTÃO CANCELAR    
        btn_tela_inicial_cursos_estudantes = Button(tela_cursos_estudantes,
                                                    text="Cancelar",
                                                    font="Times 12 bold",
                                                    bg="lightgrey",
                                                    command=voltar_inicial_tela_cursos_estudantes).place(x=585,
                                                                                                         y=285)

    #FUNÇÕES MENU CADASTRO FUNCIONÁRIOS
    def tela_cadastro_funcionarios():
        tela_cadastro_funcionarios = Tk()
        tela_cadastro_funcionarios.title("Cadastro dos Funcionários")
        tela_cadastro_funcionarios.geometry("700x335+380+210")
        tela_cadastro_funcionarios.resizable(False, False)
        def voltar_inicial_tela_cadastro_funcionarios():
            tela_cadastro_funcionarios.destroy()
            return

        #CHAMAR BIBLIOTECA TTK
        note = ttk.Notebook(tela_cadastro_funcionarios)
        note.place(x=0, y=0, width=800, height=500)

        #FAZENDO OS NOTEBOOKS
        #CRIANDO NOTEBOOK 1
        tab_1 = Frame(note)
        note.add(tab_1,
                     text="Dados do Funcionário")
        #NOME DO FUNCIONÁRIO
        lbl_nome_funcionario = Label(tab_1,
                                     text="Nome: ",
                                     font="Times 12 bold").place(relx=0.018,
                                                                 rely=0.007)
        ent_nome_funcionario = Entry(tab_1,
                                     bg="lightgrey").place(relx=0.1,
                                                           rely=0.01,
                                                           relwidth=0.40)
        #RG DO FUNCIONÁRIO
        lbl_rg_funcionario = Label(tab_1,
                                   text="RG: ",
                                   font="Times 12 bold").place(relx=0.53,
                                                               rely=0.007,
                                                               relwidth=0.05)
        ent_rg_funcionario = Entry(tab_1,
                                   bg="lightgrey").place(relx=0.59,
                                                         rely=0.01,
                                                         relwidth=0.24)
        #E-MAIL DO FUNCIONÁRIO
        lbl_email_funcionario = Label(tab_1,
                                      text="E-mail: ",
                                      font="Times 12 bold").place(relx=0.018,
                                                                  rely=0.058)
        ent_email_funcionario = Entry(tab_1,
                                      bg="lightgrey").place(relx=0.1,
                                                            rely=0.065,
                                                            relwidth=0.40)
        #CPF DO FUNCIONÁRIO
        lbl_cpf_funcionario = Label(tab_1,
                                    text="CPF: ",
                                    font="Times 12 bold").place(relx=0.53,
                                                                rely=0.06,
                                                                relwidth=0.05)
        ent_cpf_funcionario = Entry(tab_1,
                                    bg="lightgrey").place(relx=0.59,
                                                          rely=0.065,
                                                          relwidth=0.24)
        #ESCOLA DE ORIGEM
        lbl_escola_origem_funcionario = Label(tab_1,
                                              text="Escola de Origem: ",
                                              font="Times 12 bold").place(relx=0.018,
                                                                          rely=0.115,
                                                                          relwidth=0.165)
        ent_escola_origem_funcionario = Entry(tab_1,
                                              bg="lightgrey").place(relx=0.19,
                                                                    rely=0.125,
                                                                    relwidth=0.31)
        #DATA DE NASCIMENTO
        lbl_data_nascimento_funcionario = Label(tab_1,
                                                text="Data de Nasc.: ",
                                                font="Times 12 bold").place(relx=0.53,
                                                                            rely=0.115)
            
        #Dias da Semana
        data_nascimento_combobox_funcionario_dia = ttk.Combobox(tab_1,
                                                                values=[" 01 ",
                                                                        " 02 ",
                                                                        " 03 ",
                                                                        " 04 ",
                                                                        " 05 ",
                                                                        " 06 ",
                                                                        " 07 ",
                                                                        " 08 ",
                                                                        " 09 ",
                                                                        " 10 ",
                                                                        " 11 ",
                                                                        " 12 ",
                                                                        " 13 ",
                                                                        " 14 ",
                                                                        " 15 ",
                                                                        " 16 ",
                                                                        " 17 ",
                                                                        " 18 ",
                                                                        " 19 ",
                                                                        " 20 ",
                                                                        " 21 ",
                                                                        " 22 ",
                                                                        " 23 ",
                                                                        " 24 ",
                                                                        " 25 ",
                                                                        " 26 ",
                                                                        " 27 ",
                                                                        " 28 ",
                                                                        " 29 ",
                                                                        " 30 ",
                                                                        " 31 "])
        data_nascimento_combobox_funcionario_dia.set("Dia")
        data_nascimento_combobox_funcionario_dia.place(relx=0.67,
                                                       rely=0.12,
                                                       relwidth=0.052)

        #Meses do ano
        data_nascimento_combobox_funcionario_mes = ttk.Combobox(tab_1,
                                                                values=[" 01 ",
                                                                        " 02 ",
                                                                        " 03 ",
                                                                        " 04 ",
                                                                        " 05 ",
                                                                        " 06 ",
                                                                        " 07 ",
                                                                        " 08 ",
                                                                        " 09 ",
                                                                        " 10 ",
                                                                        " 11 ",
                                                                        " 12 "])
        data_nascimento_combobox_funcionario_mes.set("Mês")
        data_nascimento_combobox_funcionario_mes.place(relx=0.717,
                                                       rely=0.12,
                                                       relwidth=0.057)

        #Anos
        data_nascimento_combobox_funcionario_ano = ttk.Combobox(tab_1,
                                                                values=["1960",
                                                                        "1961",
                                                                        "1962",
                                                                        "1963",
                                                                        "1964",
                                                                        "1965",
                                                                        "1966",
                                                                        "1967",
                                                                        "1968",
                                                                        "1969",
                                                                        "1970",
                                                                        "1971",
                                                                        "1972",
                                                                        "1972",
                                                                        "1973",
                                                                        "1974",
                                                                        "1975",
                                                                        "1976",
                                                                        "1977",
                                                                        "1978",
                                                                        "1979",
                                                                        "1980",
                                                                        "1981",
                                                                        "1982",
                                                                        "1983",
                                                                        "1984",
                                                                        "1985",
                                                                        "1986",
                                                                        "1987",
                                                                        "1988",
                                                                        "1989",
                                                                        "1990",
                                                                        "1991",
                                                                        "1992",
                                                                        "1993",
                                                                        "1994",
                                                                        "1995",
                                                                        "1996",
                                                                        "1997",
                                                                        "1998",
                                                                        "1999",
                                                                        "2000",
                                                                        "2001",
                                                                        "2002",
                                                                        "2003",
                                                                        "2004",
                                                                        "2005",
                                                                        "2006",
                                                                        "2007",
                                                                        "2008",
                                                                        "2009",
                                                                        "2010",
                                                                        "2011",
                                                                        "2012",
                                                                        "2013",
                                                                        "2014",
                                                                        "2015",
                                                                        "2016",
                                                                        "2017",
                                                                        "2018",
                                                                        "2019",
                                                                        "2020"])
        data_nascimento_combobox_funcionario_ano.set("Ano")
        data_nascimento_combobox_funcionario_ano.place(relx=0.77,
                                                       rely=0.12,
                                                       relwidth=0.061)

        #TELEFONE DO ESTUDANTE
        lbl_telefone_funcionario = Label(tab_1,
                                         text="Telefone para Contato: ",
                                         font="Times 12 bold").place(relx=0.0168,
                                                                     rely=0.17,
                                                                     relwidth=0.21)
        ent_telefone_funcionario = Entry(tab_1,
                                         bg="lightgrey").place(relx=0.34,
                                                               rely=0.18,
                                                               relwidth=0.16)

        #DDI do Número de Telefone
        telefone_combobox_telefone_funcionario_ddi = ttk.Combobox(tab_1,
                                                                  values=["+1",
                                                                          "+7",
                                                                          "+20",
                                                                          "+27",
                                                                          "+30",
                                                                          "+31",
                                                                          "+32",
                                                                          "+33",
                                                                          "+34",
                                                                          "+36",
                                                                          "+39",
                                                                          "+40",
                                                                          "+41",
                                                                          "+43",
                                                                          "+44",
                                                                          "+45",
                                                                          "+46",
                                                                          "+47",
                                                                          "+48",
                                                                          "+49",
                                                                          "+51",
                                                                          "+52",
                                                                          "+53",
                                                                          "+54",
                                                                          "+55",
                                                                          "+56",
                                                                          "+57",
                                                                          "+58",
                                                                          "+60",
                                                                          "+61",
                                                                          "+62",
                                                                          "+63",
                                                                          "+64",
                                                                          "+65",
                                                                          "+66",
                                                                          "+81",
                                                                          "+82",
                                                                          "+84",
                                                                          "+86",
                                                                          "+90",
                                                                          "+91",
                                                                          "+92",
                                                                          "+93",
                                                                          "+94",
                                                                          "+95",
                                                                          "+98",
                                                                          "+212",
                                                                          "+213",
                                                                          "+216",
                                                                          "+218",
                                                                          "+220",
                                                                          "+221"])
        telefone_combobox_telefone_funcionario_ddi.set("DDI")
        telefone_combobox_telefone_funcionario_ddi.place(relx=0.22,
                                                         rely=0.18,
                                                         relwidth=0.06,
                                                         relheight=0.037)

        #DDD do Número de Telefone
        telefone_combobox_telefone_funcionario_ddd = ttk.Combobox(tab_1,
                                                                  values=["11",
                                                                          "12",
                                                                          "13",
                                                                          "14",
                                                                          "15",
                                                                          "16",
                                                                          "17",
                                                                          "18",
                                                                          "19",
                                                                          "21",
                                                                          "22",
                                                                          "24",
                                                                          "27",
                                                                          "27",
                                                                          "28",
                                                                          "31",
                                                                          "32",
                                                                          "33",
                                                                          "34",
                                                                          "35",
                                                                          "37",
                                                                          "38",
                                                                          "41",
                                                                          "42",
                                                                          "43",
                                                                          "44",
                                                                          "45",
                                                                          "46",
                                                                          "47",
                                                                          "48",
                                                                          "49",
                                                                          "51",
                                                                          "53",
                                                                          "54",
                                                                          "55",
                                                                          "61",
                                                                          "62",
                                                                          "63",
                                                                          "64",
                                                                          "65",
                                                                          "67",
                                                                          "68",
                                                                          "69",
                                                                          "71",
                                                                          "73",
                                                                          "74",
                                                                          "75",
                                                                          "77",
                                                                          "79",
                                                                          "81",
                                                                          "82",
                                                                          "83",
                                                                          "84",
                                                                          "85",
                                                                          "86",
                                                                          "87",
                                                                          "88",
                                                                          "89",
                                                                          "91",
                                                                          "92",
                                                                          "93",
                                                                          "94",
                                                                          "95",
                                                                          "96",
                                                                          "97",
                                                                          "98",
                                                                          "99"])
        telefone_combobox_telefone_funcionario_ddd.set("DDD")
        telefone_combobox_telefone_funcionario_ddd.place(relx=0.28,
                                                         rely=0.18,
                                                         relwidth=0.06,
                                                         relheight=0.037)

        #FUNÇÃO
        lbl_cursos_funcionario = Label(tab_1,
                                       text="Cursos: ",
                                       font="Times 12 bold").place(relx=0.53,
                                                                   rely=0.17,
                                                                   relwidth=0.075)
        cursos_combobox_funcionario = ttk.Combobox(tab_1,
                                                   values=["Chef",
                                                           "Coordenador",
                                                           "Faxineiro",
                                                           "Gestor",
                                                           "Porteiro",
                                                           "Professor",
                                                           "Secretária",
                                                           "Vigilante"])
        cursos_combobox_funcionario.set("Função")
        cursos_combobox_funcionario.place(relx=0.61,
                                          rely=0.18,
                                          relwidth=0.22)

        #ENDEREÇO DO FUNCIONÁRIO
        lbl_endereco_funcionario = Label(tab_1,
                                         text="Endereço",
                                         font="Times 12 bold").place(relx=0.0168,
                                                                     rely=0.235,
                                                                     relwidth=0.09)
        
        #Endereço do Funcionário País
        lbl_endereco_funcionario_pais = Label(tab_1,
                                              text="País: ",
                                              font="Times 12 bold").place(relx=0.0168,
                                                                          rely=0.285,
                                                                          relwidth=0.06)
        ent_endereco_funcionario_pais = Entry(tab_1,
                                              bg="lightgrey").place(relx=0.1,
                                                                    rely=0.29,
                                                                    relwidth=0.16)
            
        #Endereço do Funcionário Estado
        lbl_endereco_funcionario_estado = Label(tab_1,
                                                text="Estado: ",
                                                font="Times 12 bold").place(relx=0.275,
                                                                            rely=0.285,
                                                                            relwidth=0.07)
        ent_endereco_funcionario_estado = Entry(tab_1,
                                                bg="lightgrey").place(relx=0.345,
                                                                      rely=0.29,
                                                                      relwidth=0.175)

        #Endereço do Estudante Cidade
        lbl_endereco_funcionario_cidade = Label(tab_1,
                                                text="Cidade: ",
                                                font="Times 12 bold").place(relx=0.535,
                                                                            rely=0.285,
                                                                            relwidth=0.08)
        ent_endereco_funcionario_cidade = Entry(tab_1,
                                                bg="lightgrey").place(relx=0.62,
                                                                      rely=0.29,
                                                                      relwidth=0.212)
        #Endereço do Funcionário Bairro
        lbl_endereco_funcionario_bairro = Label(tab_1,
                                                text="Bairro: ",
                                                font="Times 12 bold").place(relx=0.0168,
                                                                            rely=0.337,
                                                                            relwidth=0.075)
        ent_endereco_funcionario_bairro = Entry(tab_1,
                                                bg="lightgrey").place(relx=0.1,
                                                                      rely=0.342,
                                                                      relwidth=0.16)
        #Endereço do Funcionário Rua
        lbl_endereco_funcionario_rua = Label(tab_1,
                                             text="Rua: ",
                                             font="Times 12 bold").place(relx=0.27,
                                                                         rely=0.337,
                                                                         relwidth=0.062)
        ent_endereco_funcionario_rua = Entry(tab_1,
                                             bg="lightgrey").place(relx=0.345,
                                                                   rely=0.342,
                                                                   relwidth=0.375)
        #Endereço do Funcionário Número
        lbl_endereco_funcionario_numero = Label(tab_1,
                                                text="N°: ",
                                                font="Times 12 bold").place(relx=0.735,
                                                                            rely=0.337,
                                                                            relwidth=0.04)
        ent_endereco_funcionario_numero = Entry(tab_1,
                                                bg="lightgrey").place(relx=0.77,
                                                                      rely=0.342,
                                                                      relwidth=0.06)
        #Foto do Funcionário
        btn_foto_funcionario = Button(tab_1,
                                      text="Fazer upload da foto",
                                      font="Times 12 bold",
                                      bg="lightgrey").place(relx=0.33,
                                                            rely=0.4,
                                                            relheight=0.05)
            
        #CRIANDO NOTEBOOK 2
        tab_2 = Frame(note)
        note.add(tab_2,
                 text="Dados Complementares")
        #TIPO SANGUÍNEO
        lbl_tipo_sanguineo_funcionario = Label(tab_2,
                                               text="Tipo Sanguíneo: ",
                                               font="Times 12 bold").place(relx=0.0168,
                                                                           rely=0.007,
                                                                           relwidth=0.15)
        tipo_sanguineo_combobox_funcionario = ttk.Combobox(tab_2,
                                                           values=["     A+   ",
                                                                   "     A-   ",
                                                                   "     B+   ",
                                                                   "     B-   ",
                                                                   "     AB+   ",
                                                                   "     AB-   ",
                                                                   "     O+   ",
                                                                   "     O-   ",
                                                                   "     Rh nulo   "])
        tipo_sanguineo_combobox_funcionario.set("  Tipo Sanguíneo  ")
        tipo_sanguineo_combobox_funcionario.place(relx=0.165,
                                                  rely=0.012,
                                                  relwidth=0.16)
        #ALERGIAS
        lbl_alergia_funcionario = Label(tab_2,
                                        text="Alergia: ",
                                        font="Times 12 bold").place(relx=0.0168,
                                                                    rely=0.06,
                                                                    relwidth=0.085)
        ent_alergia_funcionario = Entry(tab_2,
                                        bg="lightgrey").place(relx=0.095,
                                                              rely=0.065,
                                                              relwidth=0.23)
        #STATUS DO ESTUDANTE
        lbl_status_funcionario = Label(tab_2,
                                       text="Status: ",
                                       font="Times 12 bold").place(relx=0.0168,
                                                                   rely=0.11,
                                                                   relwidth=0.078)
        valor = IntVar()
        valor.set(0)
        rdbtn_funcionario_ativo = Radiobutton(tab_2,
                                              text="Ativo",
                                              font="Times 12 bold",
                                              variable=valor,
                                              value=4).place(relx=0.115,
                                                             rely=0.108,
                                                             relwidth=0.068)
        rdbtn_funcionario_inativo = Radiobutton(tab_2,
                                                text="Inativo",
                                                font="Times 12 bold",
                                                variable=valor,
                                                value=5).place(relx=0.21,
                                                               rely=0.108,
                                                               relwidth=0.082)
            
        btn_tela_inicial_cadastro_funcionario_limpar = Button(tela_cadastro_funcionarios,
                                                              text="Limpar",
                                                              font="Times 12 bold",
                                                              bg="lightgrey").place(x=444,
                                                                                    y=285)
            
        btn_tela_inicial_cadastro_funcionario_salvar = Button(tela_cadastro_funcionarios,
                                                              text="Salvar",
                                                              font="Times 12 bold",
                                                              bg="lightgrey",
                                                              command=salvar).place(x=517,
                                                                                    y=285)
            
        btn_tela_inicial_cadastro_funcionario = Button(tela_cadastro_funcionarios,
                                                       text="Cancelar",
                                                       font="Times 12 bold",
                                                       bg="lightgrey",
                                                       command=voltar_inicial_tela_cadastro_funcionarios).place(x=585,
                                                                                                                y=285)

    #FUNÇÕES MENU CONSULTAR FUNCIONÁRIOS
    def tela_consulta_funcionarios():
        tela_consulta_funcionarios = Tk()
        tela_consulta_funcionarios.title("Consultar Funcionários")
        tela_consulta_funcionarios.geometry("700x335+380+210")
        tela_consulta_funcionarios.resizable(False, False)
        tela_consulta_funcionarios["background"]="white"
        def voltar_inicial_tela_consulta_funcionarios():
            tela_consulta_funcionarios.destroy()
            return
        
        frame_superior = Frame(tela_consulta_funcionarios,
                               bg="lightgrey").place(relx=0.0525,
                                                     rely=0.19,
                                                     relwidth=0.9,
                                                     relheight=0.6)
        lista_consulta_funcionario = ttk.Treeview(tela_consulta_funcionarios,
                                                  column=("col1",
                                                          "col2",
                                                          "col3",
                                                          "col4"))

        lista_consulta_funcionario.heading("#0",
                                           text="Id")
        lista_consulta_funcionario.heading("#1",
                                           text="Nome")
        lista_consulta_funcionario.heading("#2",
                                           text="Data de Nasc.")
        lista_consulta_funcionario.heading("#3",
                                           text="Foto")

        lista_consulta_funcionario.column("#0",
                                          width=60)
        lista_consulta_funcionario.column("#1",
                                          width=380)
        lista_consulta_funcionario.column("#2",
                                          width=120)
        lista_consulta_funcionario.column("#3",
                                          width=80)
        
        lista_consulta_funcionario.place(relx=0.0525,
                                         rely=0.19,
                                         relwidth=0.9,
                                         relheight=0.06)
            

        #BARRA DE PESQUISA
        lbl_consulta_funcionario = Label(tela_consulta_funcionarios,
                                         text="Digite o Nome: ",
                                         font="Times 13 bold",
                                         bg="white").place(relx=0.1,
                                                           rely=0.043)
        ent_consulta_funcionario = Entry(tela_consulta_funcionarios,
                                         bg="lightgrey").place(relx=0.277,
                                                               rely=0.049,
                                                               relwidth=0.47,
                                                               relheight=0.065)
        #BOTÃO DE CONSULTA
        btn_consulta_tela_funcionarios = Button(tela_consulta_funcionarios,
                                                text="Consultar",
                                                font="Times 12 bold",
                                                bg="lightgrey").place(relx=0.75,
                                                                      rely=0.045,
                                                                      relheight=0.065)
        #BOTÃO DE CANCELAR    
        btn_tela_inicial_consulta_funcionarios = Button(tela_consulta_funcionarios,
                                                        text="Cancelar",
                                                        font="Times 12 bold",
                                                        bg="lightgrey",
                                                        command=voltar_inicial_tela_consulta_funcionarios).place(x=585,
                                                                                                                 y=285)
        
    #FUNÇÕES MENU CONSULTAR FUNÇÕES
    def tela_funcao_funcionarios():
        tela_funcao_funcionarios = Tk()
        tela_funcao_funcionarios.title("Funções dos Funcionários")
        tela_funcao_funcionarios.geometry("700x335+380+210")
        tela_funcao_funcionarios.resizable(False, False)
        tela_funcao_funcionarios["background"]="white"
        def voltar_inicial_tela_funcao_funcionarios():
            tela_funcao_funcionarios.destroy()
            return
            
        frame_superior = Frame(tela_funcao_funcionarios,
                               bg="lightgrey").place(relx=0.0525,
                                                     rely=0.19,
                                                     relwidth=0.9,
                                                     relheight=0.6)
        lista_funcao_funcionarios = ttk.Treeview(tela_funcao_funcionarios,
                                                 column=("col1",
                                                         "col2",
                                                         "col3",
                                                         "col4"))

        lista_funcao_funcionarios.heading("#0",
                                          text="Id")
        lista_funcao_funcionarios.heading("#1",
                                          text="Nome")
        lista_funcao_funcionarios.heading("#2",
                                          text="Data de Nasc.")
        lista_funcao_funcionarios.heading("#3",
                                          text="Foto")

        lista_funcao_funcionarios.column("#0",
                                         width=60)
        lista_funcao_funcionarios.column("#1",
                                         width=380)
        lista_funcao_funcionarios.column("#2",
                                         width=120)
        lista_funcao_funcionarios.column("#3",
                                         width=80)
        
        lista_funcao_funcionarios.place(relx=0.0525,
                                        rely=0.19,
                                        relwidth=0.9,
                                        relheight=0.06)
            

        #BARRA DE PESQUISA
        lbl_consulta_funcao_funcionarios = Label(tela_funcao_funcionarios,
                                                 text="Digite o Curso: ",
                                                 font="Times 13 bold",
                                                 bg="white").place(relx=0.1,
                                                                 rely=0.043)
        consulta_funcao_combobox = ttk.Combobox(tela_funcao_funcionarios,
                                                values=["  Chef  ",
                                                        "  Coordenador  ",
                                                        "  Faxineiro  ",
                                                        "  Gestor  ",
                                                        "  Porteiro  ",
                                                        "  Professor  ",
                                                        "  Secretária  ",
                                                        "  Vigilante  "])
        consulta_funcao_combobox.set("Escolha a Função")
        consulta_funcao_combobox.place(relx=0.277,
                                       rely=0.049,
                                       relwidth=0.47,
                                       relheight=0.065)
        
        #BOTÃO DE CONSULTA
        btn_consulta_tela_funcao = Button(tela_funcao_funcionarios,
                                          text="Consultar",
                                          font="Times 12 bold",
                                          bg="lightgrey").place(relx=0.75,
                                                                rely=0.045,
                                                                relheight=0.065)
            
        #BOTÃO DE CANCELAR            
        btn_tela_inicial_funcao_funcionarios = Button(tela_funcao_funcionarios,
                                                      text="Cancelar",
                                                      font="Times 12 bold",
                                                      bg="lightgrey",
                                                      command=voltar_inicial_tela_funcao_funcionarios).place(x=585,
                                                                                                             y=285)
    
    #FUNÇÕES MENU ROTINAS
    def tela_rotinas():
        tela_rotinas = Tk()
        tela_rotinas.title("Rotinas")
        tela_rotinas.geometry("700x335+380+210")
        tela_rotinas.resizable(False, False)
        tela_rotinas["background"]="white"
        def voltar_inicial_tela_rotinas():
            tela_rotinas.destroy()
            return

        frame_superior = Frame(tela_rotinas,
                               bg="lightgrey").place(relx=0.0525,
                                                     rely=0.19,
                                                     relwidth=0.9,
                                                     relheight=0.6)
        lista_rotinas = ttk.Treeview(tela_rotinas,
                                                 column=("col1",
                                                         "col2",
                                                         "col3",
                                                         "col4"))

        lista_rotinas.heading("#0",
                              text="Id")
        lista_rotinas.heading("#1",
                              text="Nome")

        lista_rotinas.column("#0",
                             width=315)
        lista_rotinas.column("#1",
                             width=315)
        
        lista_rotinas.place(relx=0.0525,
                            rely=0.19,
                            relwidth=0.9,
                            relheight=0.06)

        #BARRA PARA ADICIONAR
        lbl_rotinas = Label(tela_rotinas,
                            text="Insira o ID: ",
                            font="Times 13 bold",
                            bg="white").place(relx=0.2,
                                              rely=0.043)
        ent_rotinas = Entry(tela_rotinas,
                            bg="lightgrey").place(relx=0.337,
                                                  rely=0.049,
                                                  relwidth=0.36,
                                                  relheight=0.065)
        #BOTÃO DE INSERIR
        btn_rotinas = Button(tela_rotinas,
                             text="Inserir",
                             font="Times 12 bold",
                             bg="lightgrey",
                             command=rotina).place(relx=0.7,
                                                   rely=0.045,
                                                   relheight=0.065)

        #BOTÃO DE CANCELAR
        btn_tela_inicial_rotinas = Button(tela_rotinas,
                                          text="Cancelar",
                                          font="Times 12 bold",
                                          bg="lightgrey",
                                          command=voltar_inicial_tela_rotinas).place(x=585,
                                                                                     y=285)

    #FUNÇÕES MENU REGISTROS
    def tela_registros():
        tela_registros = Tk()
        tela_registros.title("Registros")
        tela_registros.geometry("700x335+380+210")
        tela_registros.resizable(False, False)
        tela_registros["background"]="white"
        def voltar_inicial_tela_registros():
            tela_registros.destroy()
            return

        frame_superior = Frame(tela_registros,
                               bg="lightgrey").place(relx=0.0525,
                                                     rely=0.19,
                                                     relwidth=0.9,
                                                     relheight=0.6)
        lista_registros = ttk.Treeview(tela_registros,
                                       column=("col1",
                                               "col2",
                                               "col3",
                                               "col4"))

        lista_registros.heading("#0",
                                text="Id")
        lista_registros.heading("#1",
                                text="Nome")

        lista_registros.column("#0",
                               width=315)
        lista_registros.column("#1",
                               width=315)
        
        lista_registros.place(relx=0.0525,
                              rely=0.19,
                              relwidth=0.9,
                              relheight=0.06)

        #BARRA PARA ADICIONAR
        lbl_registros = Label(tela_registros,
                              text="Insira o ID: ",
                              font="Times 13 bold",
                              bg="white").place(relx=0.2,
                                                rely=0.043)
        ent_registros = Entry(tela_registros,
                              bg="lightgrey").place(relx=0.337,
                                                    rely=0.049,
                                                    relwidth=0.36,
                                                    relheight=0.065)
        #BOTÃO DE INSERIR
        btn_registros = Button(tela_registros,
                               text="Inserir",
                               font="Times 12 bold",
                               bg="lightgrey",
                               command=registrar).place(relx=0.7,
                                                     rely=0.045,
                                                     relheight=0.065)
        #BOTÃO DE CANCELAR
        btn_tela_inicial_registros = Button(tela_registros,
                                            text="Cancelar",
                                            font="Times 12 bold",
                                            bg="lightgrey",
                                            command=voltar_inicial_tela_registros).place(x=585,
                                                                                         y=285)
    #CHAMANDO OS BOTÕES COM ÍCONES
    #BOTÃO DO ÍCONE ESTUDANTES
    btn_ico_estudante = Button(tela_inicial,
                               image=ico_estudante,
                               relief="flat",
                               width=80,
                               height=80,
                               command=tela_cadastro_estudantes).place(relx=0.01,
                                                                       rely=0.01)
    #BOTÃO DO ÍCONE FUNCIONÁRIOS
    btn_ico_funcionario = Button(tela_inicial,
                                 image=ico_funcionario,
                                 relief="flat",
                                 width=80,
                                 height=80,
                                 command=tela_cadastro_funcionarios).place(relx=0.185,
                                                                           rely=0.01)
    #BOTÃO DO ÍCONE REGISTROS
    btn_ico_registro = Button(tela_inicial,
                              image=ico_registro,
                              relief="flat",
                              width=80,
                              height=80,
                              command=tela_registros).place(relx=0.365,
                                                            rely=0.01)
    #BOTÃO DO ÍCONE ROTINAS
    btn_ico_rotina = Button(tela_inicial,
                            image=ico_rotina,
                            relief="flat",
                            width=80,
                            height=80,
                            command=tela_rotinas).place(relx=0.535,
                                                        rely=0.01)
    #BOTÃO DO ÍCONE EM BREVE
    btn_ico_em_breve = Button(tela_inicial,
                              image=ico_em_breve,
                              relief="flat",
                              width=80,
                              height=80,
                              command=aviso_em_breve).place(relx=0.69,
                                                            rely=0.01)

    #NOMES ABAIXO DOS ÍCONES
    #LABEL ESTUDANTES
    lbl_ico_estudante = Label(tela_inicial,
                              text="Estudante",
                              font="Times 12 bold").place(relx=0.025,
                                                          rely=0.6)
    #LABEL FUNCIONÁRIOS
    lbl_ico_funcionarios = Label(tela_inicial,
                                 text="Funcionário",
                                 font="Times 12 bold").place(relx=0.185,
                                                             rely=0.6)
    #LABEL REGISTROS
    lbl_ico_registros = Label(tela_inicial,
                              text="Registro",
                              font="Times 12 bold").place(relx=0.385,
                                                          rely=0.6)
    #LABEL ROTINAS
    lbl_ico_rotinas = Label(tela_inicial,
                            text="Rotina",
                            font="Times 12 bold").place(relx=0.57,
                                                        rely=0.6)
    #LABEL EM BREVE
    lbl_ico_em_breve = Label(tela_inicial,
                             text="Em breve",
                             font="Times 12 bold").place(relx=0.71,
                                                         rely=0.6)

################################################################################
################################## MENU SUSPENSO ###############################
################################################################################

    menu_principal = Menu(tela_inicial)

    cadastro_estudantes_menu = Menu(menu_principal,
                                    tearoff=0)
    cadastro_funcionarios_menu = Menu(menu_principal,
                                      tearoff=0)
    registro_menu = Menu(menu_principal,
                         tearoff=0)
    rotinas_menu = Menu(menu_principal,
                        tearoff=0)

    #MENU CADASTRO ESTUDANTES
    cadastro_estudantes_menu.add_command(label="Cadastro",
                                         command=tela_cadastro_estudantes)
    cadastro_estudantes_menu.add_command(label="Consulta",
                                         command=tela_consulta_estudantes)
    cadastro_estudantes_menu.add_command(label="Cursos",
                                         command=tela_cursos_estudantes)
    cadastro_estudantes_menu.add_separator()
    cadastro_estudantes_menu.add_command(label="Sair")
    menu_principal.add_cascade(label="    Estudantes   ",
                               menu=cadastro_estudantes_menu)

    #MENU CADASTRO FUNCIONÁRIOS
    cadastro_funcionarios_menu.add_command(label="Cadastro",
                                           command=tela_cadastro_funcionarios)
    cadastro_funcionarios_menu.add_command(label="Consulta",
                                           command=tela_consulta_funcionarios)
    cadastro_funcionarios_menu.add_command(label="Função",
                                           command=tela_funcao_funcionarios)
    cadastro_funcionarios_menu.add_separator()
    cadastro_funcionarios_menu.add_command(label="Sair")
    menu_principal.add_cascade(label="  Funcionários   ",
                               menu=cadastro_funcionarios_menu)

    #MENU REGISTRO
    registro_menu.add_command(label="Registros",
                              command=tela_registros)
    registro_menu.add_separator()
    registro_menu.add_command(label="Sair")
    menu_principal.add_cascade(label="    Registros   ",
                               menu=registro_menu)

    #MENU ROTINAS
    rotinas_menu.add_command(label="Rotinas",
                             command=tela_rotinas)
    rotinas_menu.add_separator()
    rotinas_menu.add_command(label="Sair")
    menu_principal.add_cascade(label="     Rotinas     ",
                               menu=rotinas_menu)

    tela_inicial.config(menu=menu_principal)
    
#TELA DE LOGIN
#CAMPO PARA ADICIONAR O LOGIN
  
lbl_login = Label(tela_login,
                  text="Usuário: ",
                  font="Times 13 bold",
                  bg="white").place(relx=0.03,
                                    rely=0.15)

ent_login = Entry(tela_login,
                  bg="lightgrey").place(relx=0.325,
                                        rely=0.175,
                                        relwidth=0.56,
                                        relheight=0.145)
#CAMPO PARA ADICIONAR A SENHA
lbl_senha = Label(tela_login,
                  text="Senha: ",
                  font="Times 13 bold",
                  bg="white").place(relx=0.06,
                                   rely=0.32)

ent_senha = Entry(tela_login,
                  bg="lightgrey",
                  show="*").place(relx=0.325,
                                  rely=0.356,
                                  relwidth=0.56,
                                  relheight=0.14)
#BOTÃO PARA LOGAR NO SISTEMA
btn_entrar = Button(tela_login,
                    text="Entrar",
                    font="Times 13 bold",
                    command=tela_inicial,
                    bg="lightgrey").place(relx=0.33,
                                          rely=0.57,
                                          relwidth=0.25)
#BOTÃO PARA SAIR DO SISTEMA
btn_sair = Button(tela_login,
                  text="Sair",
                  font="Times 13 bold",
                  bg="lightgrey",
                  command=sair).place(relx=0.62,
                                      rely=0.57,
                                      relwidth=0.25)

################################################################################
################################### FECHAMENTO #################################
################################################################################

tela_login.mainloop()
