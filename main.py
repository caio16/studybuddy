import threading  # Biblioteca para rodar Threads
import time  # Biblioteca para colocar o código em modo de 'sleep'
import tkinter # Biblioteca para criar GUI's
import tkinter.messagebox # Biblioteca para criar mensagens de erro
from tkinter import *  # Biblioteca para criar GUI's
from os import *  # Biblioteca para pegar informações do Sistema Opercional
from customtkinter import *  # Biblioteca customizar os elementos do Tkinter
from PIL import Image, ImageTk  # Biblioteca para fazer imagens aparecer no Tkinter
import pdf_generator as pdf # Biblioteca para criar pdfs
import rendimento
import webbrowser # Biblioteca para abrir links gerados
from rendimento import *
import planejamento as pj  # Classe de Planejamento Importada

# Importa a Classe Planejamento de outro arquivo Python
planning = pj.Planejamento()

# -> Configurações de Sistema <-
# Mudando a GUI com a biblioteca CustomTKinter
set_default_color_theme("green")
set_appearance_mode("dark")

# Criando uma variável para manipular a janela
root = CTk()

# Configurando para a janela não mudar de tamanho
root.resizable(False, False)

# Configurando para a janela aparecer no meio da tela ao iniciar
root.eval('tk::PlaceWindow . center')

# Pega o nome do Usuário através da Bilbioteca OS (Operational System)
username = os.getenv("username")


# Retira as bordas do Windows porém buga a visualização
# root.overrideredirect(1)


class GUI:
    def main(self):
        # Configuração de Tela (tamanho, título, local de visualização)
        root.geometry("700x500")
        root.title("StudyBuddy ✏️")
        frame = CTkFrame(root, width=700, height=500)
        frame.place(x=0, y=0)

        # Adiciona a Label com nome do usuário obtido através do OS
        user_text = "Olá " + username
        labeluser = CTkLabel(frame, text=user_text, font=("Arial", 23, "bold"), bg_color='#2b2b2b')
        labeluser.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Adiciona uma imagem e uma label para visualização da mesma.
        button_image = CTkImage(Image.open("robot.png"), size=(220, 200))
        label = CTkLabel(frame, image=button_image, bg_color='#2b2b2b', text="")
        label.place(relx=0.5, rely=0.48, anchor=CENTER)

        # Adiciona a label com o texto de boas vindas, utilizando a função descrita abaixo para dar um efeito de digitação.
        initial_text = ["Você pode me chamar de Study Buddy\nSeu assistente virtual de estudos. ✍️(◔◡◔)"]
        label = TypingLabel(frame, bg_color='#2b2b2b', font=("Arial", 15, "bold"))
        label.place(relx=0.5, rely=0.2, anchor=CENTER)
        label.type_text(initial_text)

        # Adiciona o botão para a tela principal do programa, contém configurações como comando, tamanho, fonte e cores.
        button_presentation = CTkButton(master=frame,
                                        text="Começar",
                                        command=self.initProgressBarLoading,
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=8,
                                        font=("Arial", 15, "bold"),
                                        bg_color='#2b2b2b')
        button_presentation.pack(padx=20, pady=10)
        button_presentation.place(relx=0.5, rely=0.8, anchor=CENTER)

        # Adiciona o botão para encerrar o programa.
        button_leave = CTkButton(master=frame,
                                 text="Sair",
                                 command=lambda: frame.quit(),
                                 font=("Arial", 15, "bold"))
        button_leave.configure(fg_color='red', bg_color='#2b2b2b')
        button_leave.pack(padx=20, pady=10)
        button_leave.place(relx=0.5, rely=0.90, anchor=CENTER)

    def initProgressBarLoading(self):
        # Inicia a Thread da barra de progreso, utilizando um Looping para preencher ela
        t = threading.Thread(target=self.progressBar)
        t.start()

    def progressBar(self):
        # Cria um barra de progresso e coloca o início dela em 0
        progress = CTkProgressBar(root, width=400, height=15, determinate_speed=0.8, mode='determinate')
        progress.place(relx=0.5, rely=0.7, anchor=CENTER)
        progress.set(0)
        # Abaixo contém um looping que serve para preencher os espaços da barra de progresso, também o tempo que cada espaço levará para ser preenchido
        steps = 100
        for i in range(steps + 1):
            value = (i * steps) / 10000
            progress.set(value)
            time.sleep(0.02)
            #  Se o progresso da barra chegar em 1.0, que é o limite, ela irá levar o usuário para a tela de apresentação do Aplicativo
            if progress.get() == 1.0:
                self.introduction()

    def introduction(self):
        # Configuração de Tela (tamanho, local de visualização)
        root.geometry('700x500')
        root.title("StudyBuddy ✏️")
        frame = CTkFrame(root, width=700, height=500)
        frame.place(x=0, y=0)

        backbtn = Button(frame, text='← Voltar',
                         command=self.main,
                         width=10, height=1,
                         bg='#2b2b2b',
                         fg='white',
                         font=("Arial", 9, "bold"),
                         borderwidth=0)
        backbtn.place(relx=0.06, rely=0.04, anchor=CENTER)

        welcome_text = "Bem-vindo ao Study Buddy!"
        labelWelcome = CTkLabel(frame,
                                text=welcome_text,
                                bg_color='#2b2b2b',
                                font=("Arial", 25, "bold"),
                                justify="center")
        labelWelcome.place(relx=0.5, rely=0.2, anchor="center")

        presentation_text = (
            "O Study Buddy, um aplicativo desenvolvido pelos estudantes do bacharelado em Ciência e Tecnologia da Universidade Federal do ABC, oferece duas ferramentas principais: planejamento e rendimento de estudos.\n\n"
            "→ Planejamento\nPermite que os estudantes organizem sua semana escolhendo matérias e aproveitando a flexibilidade para estudar. \n"
            "\n→ Rendimento\nGera relatórios detalhados do desempenho acadêmico, fornecendo insights valiosos para ajustar a rotina de estudos. Com uma interface intuitiva, o aplicativo simplifica o processo de planejamento e acompanhamento de estudos.")
        labelText = CTkLabel(frame, text=presentation_text,
                             bg_color='#2b2b2b',
                             font=("Arial", 16, "normal"),
                             justify="center",
                             wraplength=500)
        labelText.place(relx=0.5, rely=0.5, anchor=CENTER)

        button_planejamento = CTkButton(frame,
                                        bg_color='#2b2b2b',
                                        width=180,
                                        height=35,
                                        text="Planejamento",
                                        text_color='white',
                                        font=("Arial", 16, "bold"),
                                        command=self.chooseSubjects)
        button_planejamento.place(relx=0.35, rely=0.82, anchor=CENTER)

        button_rendimento = CTkButton(frame,
                                      bg_color='#2b2b2b',
                                      width=180,
                                      height=35,
                                      text="Rendimento",
                                      command=self.rendimento,
                                      text_color='white',
                                      font=("Arial", 16, "bold"))
        button_rendimento.place(relx=0.65, rely=0.82, anchor=CENTER)

        ufabc_logo = CTkImage(Image.open("ufabc.png"), size=(70, 70))
        label = CTkLabel(frame, image=ufabc_logo, bg_color='#2b2b2b', text="")
        label.place(relx=0.94, rely=0.08, anchor=CENTER)


    def chooseSubjects(self):
        root.title("StudyBuddy ✏️")
        # Configuração de Tela (tamanho, local de visualização)
        root.geometry('700x500')
        frame = CTkFrame(root, width=700, height=500)
        frame.place(x=0, y=0)

        presentationBackButton = Button(frame, text='← Voltar',
                                        width=10, height=1,
                                        bg='#2b2b2b',
                                        fg='white',
                                        font=("Arial", 9, "bold"),
                                        borderwidth=0,
                                        command=self.introduction)
        presentationBackButton.place(relx=0.06, rely=0.04, anchor=CENTER)

        presentationLabel = CTkLabel(frame,
                                     text="Escolha as matérias que você deseja \ninserir no cronograma de estudo:",
                                     bg_color='#2b2b2b', font=("Arial", 16, "bold"))
        presentationLabel.place(relx=0.5, rely=0.17, anchor=CENTER)

        # Adicionar Scrollbar
        scrollbar = CTkScrollbar(frame)
        scrollbar.place(relx=0.78, rely=0.55, relheight=0.6, anchor=CENTER)

        # Adicionar Canvas
        canvas = Canvas(frame, yscrollcommand=scrollbar.set, bg='#2b2b2b', highlightbackground='white',
                        highlightthickness=0)
        canvas.place(relx=0.5, rely=0.56, relwidth=0.5, relheight=0.6, anchor=CENTER)

        scrollbar.configure(command=canvas.yview)

        # Adicionar Frame interno
        inner_frame = Frame(canvas, bg='#2b2b2b')
        canvas.create_window((0, 0), window=inner_frame, anchor=NW)

        # Adicionar Checkboxes
        checkboxes = []  # Lista para armazenar as checkboxes criadas
        available_subjects = planning.available_subjects  # Obtém as matérias disponíveis do planejamento

        # Itera sobre as matérias disponíveis para criar as checkboxes
        for i in range(len(available_subjects)):
            var = IntVar()  # Cria uma variável de controle do tipo IntVar para cada checkbox
            checkbox = CTkCheckBox(inner_frame,  # Cria uma checkbox dentro do frame interno
                                   text=f'{available_subjects[i].__getitem__(0)}',
                                   text_color='white',
                                   bg_color='#2b2b2b',
                                   variable=var)  # Define a variável de controle associada à checkbox
            checkbox.var = var  # Define manualmente o atributo var na instância da CTkCheckBox (definida pois ocorreu um erro)
            checkbox.pack(anchor=W)
            checkboxes.append(checkbox)  # Adiciona a checkbox à lista de checkboxes

        # Atualizar scrollregion para permitir a rolagem
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Adiciona o botão para selecionas as matérias
        uf_recommended = CTkButton(frame, text='Recomendação da UFABC',
                                   width=20,
                                   height=10,
                                   font=("Arial", 15, "bold"),
                                   command=lambda: self.createSubjectList(checkboxes))
        uf_recommended.place(relx=0.5, rely=0.92, anchor=CENTER)

    def createSubjectList(self, checkboxes):
        planning.chosen_subjects.clear()  # Limpa a lista de matérias escolhidas no planejamento
        checked = 0  # Variável para contar o número de checkboxes marcadas
        for checkbox in checkboxes:
            if checkbox.var.get() == 1:  # Verifica se a checkbox está marcada (valor 1)
                checked += 1
                planning.chosen_subjects.append(
                    checkbox.cget("text"))
        if checked != 0:  # Se houver pelo menos uma checkbox marcada
            self.formularyScreen()  # Chama o método para exibir a tela de formulário
        if checked == 0:  # Se nenhuma checkbox estiver marcada
            labelNotChecked = CTkLabel(root, text='Nenhuma matéria selecionada',
                                       # Cria um rótulo para indicar que nenhuma matéria foi selecionada
                                       bg_color='#2b2b2b',
                                       font=("Arial", 16, "bold"),
                                       justify="center",
                                       text_color='red',
                                       wraplength=500)
            labelNotChecked.place(relx=0.5, rely=0.1, anchor=CENTER)

    def formularyScreen(self):
        root.title("StudyBuddy ✏️")
        root.geometry('700x500')
        frame = CTkFrame(root, width=700, height=500)
        frame.place(x=0, y=0)
        backButton = Button(frame, text='← Voltar',
                            width=10, height=1,
                            bg='#2b2b2b',
                            fg='white',
                            font=("Arial", 9, "bold"),
                            borderwidth=0,
                            command=self.chooseSubjects)
        backButton.place(relx=0.06, rely=0.04, anchor=CENTER)

        labelFormulary = CTkLabel(root,
                                  text='Agora responda o formulário abaixo com um número de 1 à 5 (sendo 1 Execelente e 5 Péssimo):',
                                  bg_color='#2b2b2b',
                                  font=("Arial", 16, "bold"),
                                  justify="center",
                                  text_color='white',
                                  wraplength=500)
        labelFormulary.place(relx=0.5, rely=0.15, anchor=CENTER)

        labelHours = CTkLabel(root, text='Quantas horas por semana você deseja estudar?',
                              bg_color='#2b2b2b',
                              font=("Arial", 16, "bold"),
                              justify="center",
                              text_color='white',
                              wraplength=500)
        labelHours.place(relx=0.5, rely=0.6, anchor=CENTER)

        hours_per_week = CTkEntry(frame, validate='key', placeholder_text='Digite em horas', width=110)
        hours_per_week.place(relx=0.5, rely=0.66, anchor=CENTER)
        planning.hours_per_week_available.clear()
        planning.hours_per_week_available.append(hours_per_week)

        saveFormulary = CTkButton(frame, text='Gerar Cronograma',
                                  width=20,
                                  height=10,
                                  font=("Arial", 15, "bold"), command=self.validateDifficulty)
        saveFormulary.place(relx=0.5, rely=0.92, anchor=CENTER)

        # Adicionar Scrollbar
        scrollbar = CTkScrollbar(frame)
        scrollbar.place(relx=0.78, rely=0.35, relheight=0.3, anchor=CENTER)

        # Adicionar Canvas
        canvas = Canvas(frame, yscrollcommand=scrollbar.set, bg='#2b2b2b', highlightbackground='white',
                        highlightthickness=0)
        canvas.place(relx=0.5, rely=0.35, relwidth=0.5, relheight=0.3, anchor=CENTER)

        scrollbar.configure(command=canvas.yview)

        # Adicionar Frame interno
        inner_frame = Frame(canvas, bg='#2b2b2b')  # Cria um novo frame dentro do canvas para organizar os elementos
        canvas.create_window((0, 0), window=inner_frame,
                             anchor=NW)  # Define a posição e âncora do frame dentro do canvas

        # Limpar a lista de rótulos e entradas para garantir que esteja vazia
        planning.subject_and_difficulty_labels_entry.clear()

        # Iterar sobre as matérias selecionadas pelo usuário
        for subject in planning.chosen_subjects:
            label = CTkLabel(inner_frame, text=subject)
            label.pack(anchor=W)

            # Adicionar uma entrada para permitir que o usuário insira a dificuldade da matéria
            entry_dificuldade = CTkEntry(inner_frame, validate='key',
                                         placeholder_text=f'Digite sua dificuldade em {subject}',
                                         width=350)
            entry_dificuldade.pack(anchor=W)

            # Armazenar o par de rótulo e entrada na lista para o acesso posterior
            planning.subject_and_difficulty_labels_entry.append((label, entry_dificuldade))

        # Atualizar scrollregion para permitir a rolagem
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def validateDifficulty(self):
        all_subjects_ok = True  # Define uma flag para indicar se todas as matérias estão com dificuldade válida

        # Itera sobre os rótulos e entradas das matérias e suas dificuldades
        for label, diff in planning.subject_and_difficulty_labels_entry:
            difficulty_str = diff.get()

            # Verifica se a dificuldade é um número inteiro entre 1 e 5
            if not (difficulty_str.isdigit() and 1 <= int(difficulty_str) <= 5):
                all_subjects_ok = False  # Define a variável como False se a dificuldade não for válida
                break  # Interrompe o loop, já que uma dificuldade inválida foi encontrada

        hours_str = planning.hours_per_week_available[0].get()

        # Verifica se o número de horas por semana é um número inteiro
        if not (hours_str.isdigit()):
            all_subjects_ok = False  # Define a varável como False se o número de horas por semana não for um número válido

        # Verifica se todas as disciplinas têm dificuldade e se o número de horas por semana é válido
        if all_subjects_ok:
            self.scheduleGenerated()  # Gera o cronograma se todas as disciplinas e horas por semana forem válidos
        else:
            # Mostra uma mensagem de erro se alguma disciplina tiver uma dificuldade inválida ou se as horas por semana não forem válidas
            tkinter.messagebox.showerror("Erro",
                                         "A dificuldade de todas as disciplinas deve ser um número entre 1 e 5.\nA hora por semana também não deve ser letras.\nVerifique os campos antes de continuar")

    def scheduleGenerated(self):
        root.title("StudyBuddy ✏️")
        root.geometry('700x500')
        frame = CTkFrame(root, width=700, height=500)
        frame.place(x=0, y=0)
        presentationBackButton = Button(frame, text='← Voltar',
                                        width=10, height=1,
                                        bg='#2b2b2b',
                                        fg='white',
                                        font=("Arial", 9, "bold"),
                                        borderwidth=0,
                                        command=self.formularyScreen)
        presentationBackButton.place(relx=0.06, rely=0.04, anchor=CENTER)

        planning.generate_list()

        labelResult = CTkLabel(root, text='CRONOGRAMA DE ESTUDOS SEMANAIS',
                               bg_color='#2b2b2b',
                               font=("Arial", 16, "bold"),
                               justify="center",
                               text_color='white',
                               wraplength=500)
        labelResult.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Adicionar Scrollbar
        scrollbar = CTkScrollbar(frame)
        scrollbar.place(relx=0.97, rely=0.5, relheight=0.7, anchor=CENTER)

        # Adicionar Canvas
        canvas = Canvas(frame, yscrollcommand=scrollbar.set, bg='#2b2b2b', highlightbackground='white',
                        highlightthickness=0)
        canvas.place(relx=0.52, rely=0.56, relwidth=0.87, relheight=0.8, anchor=CENTER)

        scrollbar.configure(command=canvas.yview)

        # Adicionar Frame interno
        inner_frame = Frame(canvas, bg='#2b2b2b')
        canvas.create_window((0, 0), window=inner_frame, anchor=NW)

        planning.subject_and_difficulty_labels_entry.clear()
        for i, (subject, time) in enumerate(planning.final_sum_of_time):
            # Adicionar labels uma abaixo da outra com o grid
            label_subject = CTkLabel(inner_frame, text=f'{subject}:', bg_color='#2b2b2b', text_color='white',
                                     font=("Arial", 12, "normal"))
            label_subject.grid(row=i, column=0, padx=(5, 20), pady=5, sticky=W)
            if time != 0:
                label_recommendation = CTkLabel(inner_frame, text=f'Recomendação: {time} horas semanais',
                                                bg_color='#2b2b2b', text_color='white', font=("Arial", 12, "bold"))
                label_recommendation.grid(row=i, column=1, padx=(20, 5), pady=5, sticky=W)
            if time == 0:
                label_recommendation = CTkLabel(inner_frame, text='Você já possui conhecimento suficiente',
                                                bg_color='#2b2b2b', text_color='red', font=("Arial", 10, "bold"))
                label_recommendation.grid(row=i, column=1, padx=(20, 5), pady=5, sticky=W)

        # Atualizar scrollregion para permitir a rolagem
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        directory = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        pdf.generate_pdf(planning.final_sum_of_time, directory)

    def rendimento(self):
        root.geometry('700x500')
        frame = CTkFrame(root, width=700, height=500)
        frame.place(x=0, y=0)

        presentationBackButton = Button(frame, text='← Voltar',
                                        width=10, height=1,
                                        bg='#2b2b2b',
                                        fg='white',
                                        font=("Arial", 9, "bold"),
                                        borderwidth=0,
                                        command=self.introduction)
        presentationBackButton.place(relx=0.06, rely=0.04, anchor=CENTER)

        # Use a mesma instância de VisualizacaoDados
        rendimento_screen = CTkButton(frame, text='Gráfico de Rendimento',
                                      width=35,
                                      height=30,
                                      font=("Arial", 15, "bold"),
                                      command=self.criar_interface_grafica)
        rendimento_screen.place(relx=0.5, rely=0.3, anchor=CENTER)

        tipos_de_estudo = CTkButton(frame, text='Tipos de Estudo',
                                    width=35,
                                    height=30,
                                    font=("Arial", 15, "bold"),
                                    command=self.tecnicas_de_estudo)
        tipos_de_estudo.place(relx=0.5, rely=0.40, anchor=CENTER)

        parte_bibliografica = CTkButton(frame, text='Bibliografia',
                                        width=35,
                                        height=30,
                                        font=("Arial", 15, "bold"),
                                        command=self.bibliografia)
        parte_bibliografica.place(relx=0.5, rely=0.51, anchor=CENTER)

        parte_de_canais = CTkButton(frame, text='Canais de Estudo',
                                    width=35,
                                    height=30,
                                    font=("Arial", 15, "bold"),
                                    command=self.canais
                                    )
        parte_de_canais.place(relx=0.5, rely=0.61, anchor=CENTER)

    def canais(self):
        root.geometry('1500x800+100+100')
        frame = CTkFrame(root, width=1500, height=800,
                         bg_color='#2b2b2b')  # Defina a cor de fundo do frame principal
        frame.place(x=0, y=0)

        backButton = Button(frame, text='← Voltar',
                            width=10, height=1,
                            bg='#2b2b2b',
                            fg='white',
                            font=("Arial", 9, "bold"),
                            borderwidth=0,
                            command=self.introduction)
        backButton.place(relx=0.06, rely=0.04, anchor=CENTER)

        # Adicionar Canvas
        canvas = Canvas(frame, bg='#2b2b2b', highlightbackground='white',
                        highlightthickness=0)
        canvas.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor=tk.CENTER)

        inner_frame = Frame(canvas, bg='#2b2b2b')
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        row = 1
        for categoria, canais in recomendacoes_canais.items():
            # Adicionar rótulo com o nome da categoria
            label_categoria = Label(inner_frame, text=categoria, bg='#2b2b2b', fg='red',
                                    font=("Arial", 16, "bold"))
            label_categoria.grid(row=row, column=0, padx=14, pady=10, sticky=tk.W)

            # Incrementar a próxima linha
            row += 1

            # Adicionar canais e seus links
            for canal, info in canais.items():
                # Adicionar rótulo com o nome do canal
                label_canal = Label(inner_frame, text=canal, bg='#2b2b2b', fg='white',
                                    font=("Arial", 14, "bold"))
                label_canal.grid(row=row, column=0, padx=14, pady=5, sticky=tk.W)

                # Adicionar link clicável do canal
                link = info["Link"]
                link_label = Label(inner_frame, text=link, fg="white", cursor="hand2", bg='#2b2b2b',
                                   font=("Arial", 12, "underline"))
                link_label.grid(row=row, column=1, padx=14, pady=5, sticky=tk.W)
                link_label.bind("<Button-1>", lambda event, l=link: self.open_link(l))

                # Incrementar a próxima linha
                row += 1

        # Adicionar scrollbar
        scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.place(relx=0.97, rely=0.5, relheight=0.9, anchor=tk.E)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Atualizar scrollregion para permitir a rolagem
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        def on_canvas_configure(event):
            canvas.itemconfig(inner_frame, width=event.width)

        canvas.bind('<Configure>', on_canvas_configure)

    @staticmethod
    def open_link(link):
        webbrowser.open_new_tab(link)

    def bibliografia(self):
        root.geometry('1200x800+100+100')
        frame = CTkFrame(root, width=1200, height=800, bg_color='#2b2b2b')  # Defina a cor de fundo do frame principal
        frame.place(x=0, y=0)

        backButton = Button(frame, text='← Voltar',
                            width=10, height=1,
                            bg='#2b2b2b',
                            fg='white',
                            font=("Arial", 9, "bold"),
                            borderwidth=0,
                            command=self.introduction)
        backButton.place(relx=0.06, rely=0.04, anchor=CENTER)

        # Adicionar Canvas
        canvas = Canvas(frame, bg='#2b2b2b', highlightbackground='white',
                        highlightthickness=0)
        canvas.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.9, anchor=CENTER)

        # Adicionar Frame interno
        inner_frame = Frame(canvas, bg='#2b2b2b')
        canvas.create_window((0, 0), window=inner_frame, anchor=NW)

        row = 1
        for area, subareas in topicos_biblio.items():
            # Adicionar rótulo com o nome da área
            label_area = CTkLabel(inner_frame, text=area, bg_color='#2b2b2b', text_color='red',
                                  font=("Arial", 16, "bold"))
            label_area.grid(row=row, column=0, padx=14, pady=10, sticky=W)

            # Incrementar a próxima linha
            row += 1

            # Adicionar subáreas e suas bibliografias
            for subarea, bibliografias in subareas.items():
                # Adicionar rótulo com o nome da subárea
                label_subarea = CTkLabel(inner_frame, text=subarea, bg_color='#2b2b2b', text_color='red',
                                         font=("Arial", 14, "bold"))
                label_subarea.grid(row=row, column=0, padx=14, pady=5, sticky=W)

                # Incrementar a próxima linha
                row += 1

                # Adicionar bibliografias
                for tipo, livros in bibliografias.items():
                    # Adicionar rótulo com o tipo de bibliografia
                    label_tipo = CTkLabel(inner_frame, text=tipo, bg_color='#2b2b2b', text_color='white',
                                          font=("Arial", 12, "bold"))
                    label_tipo.grid(row=row, column=0, padx=14, pady=5, sticky=W)

                    # Incrementar a próxima linha
                    row += 1

                    # Adicionar lista de livros
                    for livro in livros:
                        label_livro = CTkLabel(inner_frame, text="- " + livro, bg_color='#2b2b2b', text_color='white',
                                               font=("Arial", 12))
                        label_livro.grid(row=row, column=0, padx=30, pady=2, sticky=W)
                        row += 1

        # Adicionar scrollbar
        scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.place(relx=0.97, rely=0.5, relheight=0.9, anchor=E)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Atualizar scrollregion para permitir a rolagem
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def tecnicas_de_estudo(self):
        root.geometry('1500x800+100+100')
        frame = CTkFrame(root, width=1500, height=800, bg_color='#2b2b2b')  # Defina a cor de fundo do frame principal
        frame.place(x=0, y=0)

        backButton = Button(frame, text='← Voltar',
                            width=10, height=1,
                            bg='#2b2b2b',
                            fg='white',
                            font=("Arial", 9, "bold"),
                            borderwidth=0,
                            command=self.introduction)
        backButton.place(relx=0.06, rely=0.04, anchor=CENTER)

        # Adicionar Frame interno
        inner_frame = Frame(frame, bg='#2b2b2b')
        inner_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        row = 1
        for tecnica, detalhes in topicos['Técnicas de Estudo'].items():
            # Adicionar rótulo com o nome da técnica
            label_tecnica = CTkLabel(inner_frame, text=tecnica, bg_color='#2b2b2b', text_color='red',
                                     font=("Arial", 16, "bold"))
            label_tecnica.grid(row=row, column=0, padx=14, pady=10, sticky=W)

            # Adicionar descrição da técnica
            descricao = detalhes['DESCRIÇÃO']
            label_descricao = CTkLabel(inner_frame, text=descricao, bg_color='#2b2b2b', text_color='white',
                                       font=("Arial", 15, "bold"))
            label_descricao.grid(row=row, column=1, padx=10, pady=10, sticky=W)

            # Adicionar passos da técnica
            passos = detalhes['PASSOS']
            for j, passo in enumerate(passos, start=1):
                label_passo = CTkLabel(inner_frame, text=f"{j}. {passo}", bg_color='#2b2b2b', text_color='white',
                                       font=("Arial", 14))
                label_passo.grid(row=row + j, column=1, padx=20, pady=5, sticky=W)

            # Incrementar a próxima linha
            row += len(passos) + 1

        # Atualizar a geometria do root para garantir que a tela seja exibida corretamente
        root.update()

    @staticmethod
    def criar_interface_grafica():
        root.geometry('700x1200+700-10')
        root.config(bg='#2B2B2B')
        frame = CTkFrame(root, width=700, height=1200, bg_color='#2B2B2B')
        frame.place(x=100, y=50)

        labelTip = CTkLabel(root, text='Insira conceitos abaixo para as matérias que deseja calcular\n(A, B, C, D, F)',
                            bg_color='#2b2b2b',
                            font=("Arial", 16, "bold"),
                            justify="center",
                            text_color='white',
                            wraplength=500)
        labelTip.place(relx=0.5, rely=0.0195, anchor=CENTER)

        # Dicionário para mapear conceitos para valores numéricos
        conceitos_dict = {'F': 0, 'D': 1, 'C': 2, 'B': 3, 'A': 4}
        entry_values = {}

        # Label e Entry para cada disciplina
        for i, (sigla, descricao) in enumerate(rendimento.disciplinas.items()):  # Usando enumerate para obter o índice da linha
            CTkLabel(frame, text=descricao).grid(row=i, column=0, sticky="w")  # Coluna 0 para o rótulo
            entry_values[sigla] = StringVar()
            CTkEntry(frame, textvariable=entry_values[sigla]).grid(row=i, column=1, padx=5,
                                                                   pady=5)  # Coluna 1 para a entrada

        def plot_grafico_nova_janela():
            # Dados para o gráfico
            dados_x = []
            dados_y = []

            for sigla, descricao in disciplinas.items():
                if sigla in entry_values:
                    conceito = entry_values[sigla].get()
                    if conceito in conceitos_dict:
                        dados_x.append(sigla)
                        dados_y.append(conceitos_dict[conceito])

            # Criando a figura do gráfico
            fig = Figure(figsize=(10, 6))
            plot = fig.add_subplot(111)
            plot.scatter(dados_x, dados_y, color='purple')  # Definindo a cor das bolinhas como roxas
            plot.plot(dados_x, dados_y, color='purple', linestyle='-')  # Adicionando a linha ligando os pontos
            plot.set_title("Conceitos por Disciplina")
            plot.set_xlabel("Disciplina (Sigla)")
            plot.set_ylabel("Conceito Numérico")
            plot.set_xticks(dados_x)
            plot.set_yticks(range(5))  # Define os ticks do eixo y para valores de 0 a 4
            plot.grid(True)

            # Criando uma nova janela para o gráfico
            nova_janela = CTkToplevel(root)
            nova_janela.title("Gráfico de Conceitos por Disciplina")

            # Criando o widget FigureCanvasTkAgg
            canvas = FigureCanvasTkAgg(fig, master=nova_janela)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Botão para plotar o gráfico em uma nova janela
        btn_plotar_nova_janela = CTkButton(frame, text="Plotar Gráfico em Nova Janela",
                                           font=("Arial", 16, "bold"),
                                           command=plot_grafico_nova_janela)
        btn_plotar_nova_janela.grid(row=len(entry_values) + 1, columnspan=2, pady=10)


class TypingLabel(
    CTkLabel):  # Através de um método que é executado a cada 40 milisegundos, para cada letra na frase atualiza mostrando uma por uma através de um looping.
    def type_text(self, text):
        for k in text:  # Para cada texto dentro do vetor...
            for i in range(
                    len(k)):  # Ele percorre letra por letra e atualiza o texto da Label como um efeito de digitação.
                self.configure(text=k[:i + 1])
                self.update()
                root.after(40)
        root.after(1000)


gui = GUI()
gui.main()
root.mainloop()
