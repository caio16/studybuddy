class Planejamento:
    available_subjects = [
        ("Base Experimental das Ciências Naturais", 2),
        ("Bases Computacionais da Ciência", 2),
        ("Bases Epistemológicas da Ciência Moderna", 4),
        ("Bases Matemáticas", 5),
        ("Biodiversidade: Interações entre organismos e ambiente", 4),
        ("Bioquímica: estrutura, propriedade e funções de biomoléculas", 6),
        ("Ciência, Tecnologia e Sociedade", 4),
        ("Comunicação e Redes", 4),
        ("Estrutura da Matéria", 4),
        ("Estrutura e Dinâmica Social", 4),
        ("Evolução e Diversificação da Vida na Terra", 4),
        ("Fenômenos Eletromagnéticos", 6),
        ("Fenômenos Mecânicos", 6),
        ("Fenômenos Térmicos", 4),
        ("Física Quântica", 4),
        ("Funções de Uma Variável", 6),
        ("Funções de Várias Variáveis", 4),
        ("Geometria Analítica", 6),
        ("Interações Atômicas e Moleculares", 4),
        ("Introdução à Probabilidade e à Estatística", 4),
        ("Introdução às Equações Diferenciais Ordinárias", 4),
        ("Natureza da Informação", 4),
        ("Processamento da Informação", 4),
        ("Projeto Dirigido", 10),
        ("Transformações Químicas", 6)
    ]

    # Lista de Matérias Escolhidas
    chosen_subjects = []

    # Quantidade de horas por semana para estudo
    hours_per_week_available = []

    # Uma array de labels para armazenar os valores posteriormente
    subject_and_difficulty_labels_entry = []

    # A lista de matérias e dificuldade
    subjects_and_difficulties = []

    # A soma da dificuldade
    sum_of_difficulty = []

    # Soma final do tempo total
    final_sum_of_time = []

    # Através da array de labels ele pega cada uma e pega o valor da dificuldade e adiciona à lista final com a string e o valor em int
    def generate_list(self):
        self.subjects_and_difficulties.clear()
        for label, diff in self.subject_and_difficulty_labels_entry:
            subject = label.cget("text")
            difficulty = diff.get()
            difficulty = int(difficulty)  # Convert difficulty to an integer
            self.subjects_and_difficulties.append((subject, difficulty))

        self.generate_schedule()

    def generate_schedule(self):
        # Limpa a lista final de tempo
        self.final_sum_of_time.clear()

        # Calcula a dificuldade total somando as dificuldades de todas as matérias
        total_difficulty = sum(difficulty for _, difficulty in self.subjects_and_difficulties)

        # Obtém o total de horas disponíveis por semana
        total_hours_per_week = int(self.hours_per_week_available[0].get())

        # Calcula as horas de estudo por unidade de dificuldade
        hours_per_difficulty_unit = total_hours_per_week / total_difficulty

        # Calcula o tempo de estudo para cada matéria com base na dificuldade
        for subject, difficulty in self.subjects_and_difficulties:
            # Calcula o tempo de estudo para a matéria atual
            study_time = int(difficulty * hours_per_difficulty_unit)

            # Adiciona a matéria e seu tempo de estudo à lista final
            self.final_sum_of_time.append((subject, study_time))

        # Calcula o tempo total de estudo
        total_study_time = sum(time for _, time in self.final_sum_of_time)

        # Se o tempo total de estudo for menor que o tempo desejado
        if total_study_time < total_hours_per_week:
            # Calcula o tempo restante
            remaining_time = total_hours_per_week - total_study_time

            # Encontra a matéria com maior dificuldade
            max_difficulty_subject = max(self.subjects_and_difficulties, key=lambda x: x[1])

            # Adiciona o tempo restante à matéria com maior dificuldade
            for i, (subject, _) in enumerate(self.final_sum_of_time):
                if subject == max_difficulty_subject[0]:
                    self.final_sum_of_time[i] = (subject, self.final_sum_of_time[i][1] + remaining_time)
                    break

