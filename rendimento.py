import tkinter as tk
from tkinter import ttk
from customtkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

disciplinas = {
    "BIOQ": "Bioquímica: estrutura, propriedade e funções de biomoléculas",
    "BECN": "Base Experimental das Ciências Naturais",
    "BECM": "Bases Epistemológicas da Ciência Moderna",
    "BM": "Bases Matemáticas",
    "TQ": "Transformações Químicas",
    "FVV": "Funções de Várias Variáveis",
    "PI": "Processamento da Informação",
    "FUV": "Funções de uma Variável",
    "GA": "Geometria Analítica",
    "FETERM": "Fenômenos Térmicos",
    "FEMEC": "Fenômenos Mecânicos",
    "FEMEL": "Fenômenos Eletromagnéticos",
    "IAM": "Interações Atômicas e Moleculares",
    "IPE": "Introdução à Probabilidade e à Estatística",
    "IEDO": "Introdução às Equações Diferenciais Ordinárias",
    "FQ": "Física Quântica",
    "CR": "Comunicação e Redes",
    "BCC": "Bases Computacionais da Ciência",
    "EM": "Estrutura da Matéria",
    "EDS": "Estrutura e Dinâmica Social",
    "EDVT": "Evolução e Diversificação da Dida na Terra",
    "CTS": "Ciência, Tecnologia e Sociedade",
    "BIOA": "Biodiversidade: interações entre organismos e ambiente",
    "NI": "Natureza da Informação"
}

topicos = {
    "Técnicas de Estudo": {
        "Técnica de Estudo Pomodoro": {
            "DESCRIÇÃO": """A técnica de estudo Pomodoro é um método de gerenciamento de tempo desenvolvido por Francesco Cirillo no final dos anos 1980.
O método é projetado para melhorar a concentração e a produtividade ao dividir o tempo de estudo em intervalos focados (Pomodoros) intercalados 
com breves períodos de descanso.""",

            "PASSOS": [
                "Escolha uma Tarefa: Selecione a tarefa ou matéria que você deseja estudar.",
                "Defina o Timer para 25 Minutos: Inicie um timer e concentre-se completamente na tarefa escolhida até que o tempo de 25 minutos (um Pomodoro) se esgote.",
                "Faça uma Pausa de 5 Minutos: Após completar um Pomodoro de 25 minutos, faça uma pausa de 5 minutos. Use esse tempo para descansar, relaxar e se recuperar mentalmente.",
                "Repita o Processo: Após a pausa de 5 minutos, retome o estudo e repita o ciclo de Pomodoro. Tente completar quatro Pomodoros consecutivos.",
                "Pausa Longa: Após completar quatro Pomodoros, faça uma pausa mais longa de 15 a 30 minutos. Isso ajuda a recuperar a energia e a concentração."
            ]
        },

        "Técnica de Estudo Intermitente": {
            "DESCRIÇÃO": """Similar ao método Pomodoro, mas com intervalos de tempo diferentes.
Pode ser personalizado de acordo com a preferência do indivíduo, por exemplo, 50 minutos de estudo e 10 minutos de descanso.
A Técnica de Estudo Intermitente é uma abordagem de gerenciamento de tempo que combina períodos de estudo focado com intervalos curtos de descanso.""",

            "PASSOS": [
                "Escolha uma Tarefa ou Matéria: Selecione uma matéria ou tarefa específica que você deseja estudar.",
                "Defina o Timer para 50 Minutos: Comece o temporizador e concentre-se completamente na tarefa escolhida durante o período de 50 minutos. \nEvite distrações e mantenha o foco total na tarefa em mãos.",
                "Repita o Processo: Após a pausa de 10 minutos, retorne ao estudo e repita o ciclo de 50 minutos de estudo seguido por 10 minutos de descanso.\n Você pode repetir este ciclo várias vezes conforme sua necessidade e resistência."
            ]
        },

        "Técnica de Estudo Focus 45": {
            "DESCRIÇÃO": """A técnica de estudo Focus 45 é uma variante do método Pomodoro que divide o tempo em blocos de 45 minutos de estudo focado, 
            seguidos por 15 minutos de descanso. Essa técnica é especialmente útil para disciplinas que exigem uma compreensão profunda 
            e reflexiva do conteúdo, como as áreas das ciências biológicas e humanas.""",

            "PASSOS": [
                "Escolha uma Tarefa ou Matéria: Selecione uma tarefa específica ou matéria que você deseja estudar.",
                "Defina o Timer para 45 Minutos: Inicie o temporizador e concentre-se intensamente na tarefa escolhida até que o tempo de 45 minutos termine.",
                "Faça uma Pausa de 15 Minutos: Após completar um bloco de 45 minutos de estudo, faça uma pausa de 15 minutos. Durante esse tempo, é importante descansar e \nrelaxar para recuperar a energia e a concentração.",
                "Repita o Processo: Após a pausa de 15 minutos, retorne ao estudo e repita o bloco de 45 minutos. Tente completar o número de blocos de estudo desejados.",
                "Pausa Longa: Após completar os blocos de estudo desejados, faça uma pausa mais longa de 30 minutos a 1 hora. Isso ajuda a recuperar a energia e a concentração."
            ]
        }
    }
}

topicos_biblio = {
    "-> Matemática": {
        "Bases Matemáticas": {
            "BIBLIOGRAFIA BÁSICAS": [
                "BOULOS P. Pré calculo, São Paulo, Makron 2006.",
                "LIMA, E.; CARVALHO, P. ; WAGNER, E.; MORGADO, A. A Matemática do Ensino Médio. v. 1. Coleção do Professor de Matemática, Sociedade Brasileira de Matemática, 2003."
            ]
        },
        "Funções de Uma Variável": {
            "BIBLIOGRAFIA BÁSICAS": [
                "STEWART, J. Cálculo. v. I, São Paulo, SP : Cengage Learning, c2017.",
                "GUIDORIZZI, H. L. Um curso de cálculo. v. I, Rio de Janeiro, RJ : LTC, 2018."
            ]
        },
        "Funções de Várias Variáveis": {
            "BIBLIOGRAFIA BÁSICAS": [
                "STEWART, J. Cálculo. v. I, São Paulo, SP : Cengage Learning, c2017.",
                "GUIDORIZZI, H. L. Um curso de cálculo. v. I, Rio de Janeiro, RJ : LTC, 2018."
            ]
        },
        "Geometria Analítica": {
            "BIBLIOGRAFIA BÁSICAS": [
                "MELLO, D.; WATANABE,R. Vetores e uma iniciação à Geometria Analítica. Livraria da Física, 2011.",
                "LIMA, E. Geometria Analítica e Álgebra Linear. Publicação Impa, 2008."
            ]
        },
        "Introdução às Equações Diferenciais Ordinárias": {
            "BIBLIOGRAFIA BÁSICAS": [
                "GUIDORIZZI, H. Um curso de cálculo. v. 4. Rio de Janeiro, RJ: LTC, 2018.",
                "ZILL D.; CULLEN M. Equações Diferencias. v. 1 e 2. São Paulo, SP: Pearson Education do Brasil, 2001."
            ]
        },
        "Introdução à Probabilidade e à Estatística": {
            "BIBLIOGRAFIA BÁSICAS": [
                "ROSS, S. Probabilidade: Um Curso Moderno com Aplicações. Bookman, 2010.",
                "DANTAS, B. Probabilidade: um curso introdutório, São Paulo: EdUSP, 2008. 252 p. ISBN 9788531403996."
            ]
        }
    },
    "-> Física": {
        "Fenômenos Mecânicos": {
            "BIBLIOGRAFIA BÁSICAS": [
                "HALLIDAY, D. RESNICK R. WALKER, J. Fundamentos de Física. v. 1. LTC.",
                "SERWAY, R. A. JEWETT Jr., J. W. Princípios de Física. v. 1. Thomson Learning"
            ]
        },
        "Fenômenos Térmicos": {
            "BIBLIOGRAFIA BÁSICAS": [
                "HALLIDAY, D. RESNICK R. WALKER, J. Fundamentos de Física. v. 1. LTC.",
                "SERWAY, R. A. JEWETT Jr., J. W. Princípios de Física. v. 2. Thomson Learning"
            ]
        },
        "Física Quântica": {
            "BIBLIOGRAFIA BÁSICAS": [
                "TIPLER, P. A., LLEWELLYN, R.A. Física Moderna, SP: LTC GEN (Grupo Editorial Nacional), 2010.",
                "SERWAY, R. A., JEWETT JR, J. W. Jewett, Ótica e Física Moderna, Ed. Thomson."
            ]
        },
        "Fenômenos Eletromagnéticos": {
            "BIBLIOGRAFIA BÁSICAS": [
                "HALLIDAY, D. RESNICK R. WALKER, J., Fundamentos de Física. v. 3. LTC",
                "TIPLER, P.; MOSCA, G. Física. v. 3. LTC."
            ]
        },
        "Estrutura da Matéria": {
            "BIBLIOGRAFIA BÁSICAS": [
                "ATKINS,P.W.; JONES, Loretta. Princípios de Química: questionando a vida moderna e o meio ambiente. 3. ed. Porto Alegre: Bookman, 2006. 965p.",
                "BROWN, Theodore l. et al. Quimica: a ciência central. 9. ed. São Paulo: Pearson Prentice Hall, 2005. 972 p."
            ]
        }
    },
    "-> Química": {
        "Transformações Químicas": {
            "BIBLIOGRAFIA BÁSICAS": [
                "ATKINS, P., JONES, L. Princípios de Química, Questionando a vida e o meio ambiente. 5 ed. Porto Alegre: Bookman, 2011.",
                "BRADY, J. E., RUSSELL, J. W., HOLUM, J. R. Química - a Matéria e Suas Transformações. v. 1 e 2. 5. ed. Rio de Janeiro: LTC , 2012."
            ]
        },
        "Bioquímica: estrutura, propriedade e funções de biomoléculas": {
            "BIBLIOGRAFIA BÁSICAS": [
                "LEHNINGER, A.L.; NELSON, D.L.; COX, M.M. Princípios de bioquímica. 4 ed. São Paulo:Sarvier, 2006. 1202 p",
                "VOET, D.; VOET, J.G. Bioquímica. 3 ed. Porto Alegre:Artmed, 2006, 1596 p."
            ]
        },
        "Interações Atômicas e Moleculares": {
            "BIBLIOGRAFIA BÁSICAS": [
                "TIPLER, P. A., LLEWELLY."]
        }
    },
    "Ciências Biológicas": {
        "Biodiversidade: Interações entre organismos e ambiente": {
            "BIBLIOGRAFIA BÁSICAS": [
                "RELYEA, R.; RICKLEFS, R. A economia da natureza. 6 ed. Rio de Janeiro: Guanabara Koogan, 2010. 656 p.",
                "ODUM, Eugene P.; BARRETT, Gary W. Fundamentos de ecologia. São Paulo: Cengage Learnin.2008. 612 p."
            ]
        },
        "Evolução e Diversificação da Vida na Terra": {
            "BIBLIOGRAFIA BÁSICAS": [
                "SADAVA, David; HELLER, , Craig; PURVES, William; HILLIS, David. Vida: A Ciência da Biologia - volume 1: Célula e hereditariedade. 8. ed. Porto Alegre: Artmed, 2009.",
                "MEYER, D., EL-HANI, C. N. Evolução: o sentido da biologia. São Paulo: UNESP, 2005. 132 p. (Paradidáticos ; Série Evolução)."
            ]
        }
    },
    "-> Área de Programação": {
        "Bases Computacionais da Ciência": {
            "BIBLIOGRAFIA BÁSICAS": [
                "NEVES, Rogério; ZAMPIROLLI, Francisco. Processando a Informação: um livro prático de programação independente de linguagem. 1. ed. Santo André: UFABC, 2017.",
                "MARIETTO, M.G.; MINAMI,M.; WESTERA, P.W. Bases Computacionais da Ciência. Universidade Federal do ABC, 2013."
            ]
        },
        "Processamento da Informação": {
            "BIBLIOGRAFIA BÁSICAS": [
                "NEVES, Rogério; ZAMPIROLLI, Francisco. Processando a Informação: um livro prático de programação independente de linguagem. 1. ed. Santo André: UFABC, 2017. 192 p",
                "SEBESTA, Robert W. Conceitos de linguagens de programação. 9. ed. Porto Alegre: Bookman, 2011. 638 p."
            ]
        },
        "Comunicação e Redes": {
            "BIBLIOGRAFIA BÁSICAS": [
                "BARABÁSI, Albert-László. Network Science. Cambridge University Press, 2016. 475 P. Digital. Disponível gratuitamente através da licença Creative Commons.",
                "KUROSE, James F.; ROSS, Keith W. Redes de computadores e a internet. 5. ed. São Paulo:Addison Wesley, 2010. 614 p"
            ]
        }
    },
    "-> Ciências Humanas e Sociais": {
        "Base Experimental das Ciências Naturais": {
            "BIBLIOGRAFIA BÁSICAS": [
                "LAKATOS, E.M.; MARCONI, M. A. Metodologia Cientifica. 5. ed. São Paulo: Atlas, 2007. 312 p."
            ]
        },
        "Natureza da Informação": {
            "BIBLIOGRAFIA BÁSICAS": [
                "COELHO NETTO, J. T. Semiótica, informação e comunicação. 7. ed. São Paulo, SP: Perspectiva, 2007. 217 p.",
                "FLOYD, T.L. Sistemas digitais: fundamentos e aplicações. 9ed. Porto Alegre, RS: Bookman, 2007. 888 p."
            ]
        },
        "Bases Epistemológicas da Ciência Moderna": {
            "BIBLIOGRAFIA BÁSICAS": [
                "CHALMERS, Alan F. O que é Ciência afinal?. São Paulo: Brasiliense, 1997. 227 p",
                "KUHN, Thomas. A Estrutura das Revoluções Científicas. 9 ed. São Paulo:Perspectiva, 2006. 260 p."
            ]
        },
        "Estrutura e Dinâmica Social": {
            "BIBLIOGRAFIA BÁSICAS": [
                "CASTELLS, Manuel. A sociedade em rede. São Paulo: Paz e Terra, 2008. v. 1. 639 p. (A era da informação economia, sociedade e cultura).",
                "COSTA, Maria Cristina Castilho. Sociologia: introdução a ciência da sociedade. 3 ed. São Paulo: Moderna, 2005. 415 p."
            ]
        },
        "Ciência Tecnologia e Sociedade": {
            "BIBLIOGRAFIA BÁSICAS": [
                "CASTELLS, Manuel. A sociedade em rede. São Paulo: Paz e Terra, 2008. v. 1. 639 p. (A era da informação economia, sociedade e cultura volume 1)."
            ]
        }
    }
}

recomendacoes_canais = {
    "Pré-cálculo e Cálculos": {
        "Equaciona Com Paulo Pereira": {
            "Link": "https://www.youtube.com/c/EquacionaComPauloPereira"
        },
        "Prof. MURAKAMI - MATEMÁTICA RAPIDOLA": {
            "Link": "https://www.youtube.com/c/MATMATICARAPIDOLA"
        },
        "Matemateca - Ester Velasquez": {
            "Link": "https://www.youtube.com/c/MatematecaEsterVelasquez"
        },
        "Projeto Newton": {
            "Link": "https://www.youtube.com/c/ProjetoNewton"
        }
    },
    "Fenômenos Mecânicos/Térmicos/Eletromagnéticos": {
        "DOUG.FISICA": {
            "Link": "https://www.youtube.com/c/DOUGFISICA"
        }
    },
    "Geometria Analítica e Álgebra Linear": {
        "Matemateca - Ester Velasquez": {
            "Link": "https://www.youtube.com/c/MatematecaEsterVelasquez"
        },
        "Professor Aquino - Matemática": {
            "Link": "https://www.youtube.com/c/ProfessorAquinoMatematica"
        },
        "Prof. MURAKAMI - MATEMÁTICA RAPIDOLA": {
            "Link": "https://www.youtube.com/c/MATMATICARAPIDOLA"
        }
    },
    "Área de Programação": {
        "Refatorando": {
            "Link": "https://www.youtube.com/c/Refatorando"
        },
        "Curso em Vídeo": {
            "Link": "https://www.youtube.com/c/CursoemVideo"
        }
    },
    "Transformações Químicas e Estrutura da Matéria": {
        "QUÍMICA DO MONSTRO": {
            "Link": "https://www.youtube.com/c/QUIMICADOMONSTRO"
        },
        "Prof. Rui Alves": {
            "Link": "https://www.youtube.com/c/ProfRuiAlves"
        },
        "Professor Gabriel Cabral": {
            "Link": "https://www.youtube.com/c/ProfessorGabrielCabral"
        },
        "Café com química - Prof Michel": {
            "Link": "https://www.youtube.com/c/CafecomquimicaProfMichel"
        }
    }
}
