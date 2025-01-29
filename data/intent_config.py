available_courses = [
    "Administração",
    "Engenharia de Produção",
    "Sistemas de Informação",
    "Matemática",
]

courses_links = {
    "administracao": [
        {
            "main": "https://www.macae.rj.gov.br/femass/conteudo/titulo/administracao",
            "flowchart": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1691543647.pdf",
            "summary": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1637813629.pdf",
        }
    ]
}

intents = {
    "intents": [
        {
            "intention": "saudacoes",
            "patterns": [
                "Olá",
                "Oi",
                "Oi, tudo bem?",
                "E aí?",
                "Olá, como você está?",
                "Oi, como vai?",
                "Oi, tem alguém aí?",
                "Bom dia",
                "Boa tarde",
                "Boa noite",
                "Tudo bem?",
                "Como você está?",
                "Alguém aí?",
                "Oi, pode me ajudar?",
                "Olá, gostaria de tirar uma dúvida",
                "Poderia me tirar uma dúvida?",
                "Consegue me ajudar?"
            ],
            "responses": [
                "Olá! Como posso ajudar você?",
                "Oi! Em que posso te ajudar hoje?",
                "Oi, tudo bem? Estou aqui para ajudar.",
                "Olá! Diga-me o que você precisa saber.",
                "Oi! Estou pronto para responder suas dúvidas sobre a FeMASS.",
                "Olá, o que você gostaria de saber sobre a FeMASS?",
                "Oi, tudo bem? Estou aqui para ajudar sobre a FeMASS.",
            ],
        },
        {
            "intention": "apresentacao",
            "patterns": [
                "Quem é você?",
                "Qual é o seu nome?",
                "Você pode se apresentar?",
                "Como você se chama?",
                "O que você faz?",
                "Qual é a sua função?",
                "De onde você é?",
                "O que você pode me ajudar?",
                "Qual é o seu trabalho?",
                "Me fale sobre você",
            ],
            "responses": [
                "Eu sou um Chatbot criado para ajudar com informações sobre a FeMASS!",
                "Sou um assistente virtual da FeMASS, estou aqui para responder suas dúvidas.",
                "Eu sou um Chatbot e estou aqui para ajudar você com informações da FeMASS.",
                "Sou um Chatbot treinado para fornecer informações sobre a FeMASS e seus cursos.",
                "Eu sou um Chatbot da FeMASS, pronto para ajudar com qualquer dúvida!",
                "Sou um assistente digital da FeMASS, posso te ajudar com informações sobre cursos e muito mais.",
                "Eu sou um chatbot da FeMASS e estou aqui para responder suas perguntas.",
                "Meu trabalho é fornecer informações sobre os cursos da FeMASS e outros detalhes importantes.",
                "Sou um chatbot criado para tirar dúvidas sobre a FEMASS, cursos e ingressos.",
                "Eu sou um assistente digital da FEMASS, pronto para te ajudar com qualquer questão.",
            ],
        },
        {
            "intention": "cursos_disponiveis",
            "patterns": [
                "Quais são os cursos disponíveis na FeMASS?",
                "Me fale sobre os cursos da FeMASS.",
                "Que cursos a FeMASS oferece?",
                "Quais cursos têm na FeMASS?",
                "Pode me dizer os cursos disponíveis na FeMASS?",
                "O que a FeMASS ensina?",
                "Quais são as opções de cursos da FeMASS?",
                "Você pode listar os cursos da FeMASS?",
                "Quais são os cursos oferecidos pela FeMASS?",
                "Quais graduações estão disponíveis na FeMASS?",
                "A FeMASS oferece quais cursos?",
                "Que opções de cursos tem na FeMASS?",
                "Poderia me informar sobre os cursos da FeMASS?",
                "Me diga os cursos que a FeMASS possui.",
                "Você sabe quais são os cursos da FeMASS?",
                "Que cursos estão disponíveis na FeMASS?",
                "Qual é a lista de cursos da FeMASS?",
                "Você pode me falar sobre os cursos oferecidos pela FeMASS?",
                "Quais são as graduações disponíveis na FeMASS?",
                "Que graduações a FeMASS tem?",
                "Quais cursos posso fazer na FeMASS?",
            ],
            "responses": [
                f"Os cursos disponíveis são {', '.join(available_courses)}",
                f"Fico feliz por estar interessado sobre os cursos oferecidos na FeMASS! Os cursos disponíveis são: {', '.join(available_courses)}.",
                f"Atualmente a FeMASS disponibiliza os cursos de {', '.join(available_courses)}",
                f"A FeMASS possui as seguintes graduações disponíveis: {', '.join(available_courses)}.",
                f"Os cursos oferecidos pela FeMASS são: {', '.join(available_courses)}. Algum desses chamou sua atenção?",
                f"Você pode estudar na FeMASS em um dos seguintes cursos: {', '.join(available_courses)}.",
                f"As opções de cursos disponíveis na FeMASS incluem: {', '.join(available_courses)}.",
                f"Na FeMASS, você encontrará os seguintes cursos: {', '.join(available_courses)}.",
                f"Os cursos atualmente disponíveis na FeMASS são: {', '.join(available_courses)}. Deseja mais informações sobre algum deles?",
                f"Se você está pensando em estudar na FeMASS, as opções de cursos disponíveis são: {', '.join(available_courses)}.",
            ],
        },
        {
            "intention": "administracao",
            "patterns": [
                "Gostaria de saber sobre o curso de Administração",
                "Poderia me falar mais sobre o curso de Administração?",
                "Gostaria de saber mais informações sobre o curso de Administração",
                "Gostaria de informações sobre o curso de Administração",
                "Poderia me informar mais sobre o curso de Administração?",
                "Quais são os detalhes do curso de Administração?",
                "Quero saber sobre Administração",
                "Quero saber sobre o curso de Administração"
            ],
            "responses": [
                "O curso de Administração tem como objetivo formar profissionais com formação generalista, humanista, crítica e reflexiva para proporcionar ao futuro administrador o alcance dos objetivos organizacionais. O curso é oferecido de forma presencial, com duração de oito semestres letivos, cada um com vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min",
                "O curso de Administração visa formar profissionais com uma formação generalista, humanista, crítica e reflexiva, capacitando o futuro administrador a atingir os objetivos organizacionais. O curso é oferecido de forma presencial, com duração de oito semestres letivos, cada um com vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min.",
                "O objetivo do curso de Administração é preparar profissionais com uma base generalista, humanista e crítica, permitindo ao futuro administrador alcançar os objetivos organizacionais. O curso é oferecido na modalidade presencial, com duração de oito semestres letivos, sendo cada semestre composto por vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min.",
            ],
        },
        {
            "intention": "grade_curricular_administracao",
            "patterns": [
                "Qual a grade curricular do curso de Administração?",
                "Quais as matérias da grade curricular do curso de Administração?",
                "Quais matérias o curso de Administração disponibiliza?",
                "Quais matérias estão na grade curricular do curso de Administração",
                "O que vou aprender no curso de Administração?",
                "Quais são as disciplinas do curso de Administração?",
                "Quais são as disciplinas presentes na grade curricular do curso de Administração",
                "Quais matérias fazem parte do curso de Administração?",
                "Quais matérias fazem parte da grade curricular do curso de Administração?",
                "Quais são os conteúdos abordados no curso de Administração?",
                "Quais matérias o curso de Administração oferece?",
                "Quais conteúdos estão na grade curricular do curso de administração?",
                "Matérias"
            ],
            "responses": [
                f"O curso de Administração disponibiliza muitas matérias como Logística, Gestão de Custos e Sociologia. Para saber a ementa do curso entre no link {courses_links['administracao'][0]['summary']} ou caso queira ver o fluxograma da grade entre no link {courses_links['administracao'][0]['flowchart']}.",
                f"No curso de Administração você vai aprender diversas matérias como Logística, Gestão de Custos e Sociologia. Para saber a ementa do curso entre no link {courses_links['administracao'][0]['summary']} ou caso queira ver o fluxograma da grade entre no link {courses_links['administracao'][0]['flowchart']}.",
                f"Para saber mais sobre quais matérias o curso de Administração disponibiliza, entre no seguinte link para acessar a ementa:{courses_links['administracao'][0]['summary']} \nou caso queira ver o fluxograma da grade entre no link {courses_links['administracao'][0]['flowchart']}.",
            ],
        },
        {
            "intention": "grade_curricular_engenharia_producao",
            "patterns": [
                "Qual a grade curricular do curso de Engenharia de Produção?",
                "Quais as matérias da grade curricular do curso de Engenharia de Produção?",
                "Quais matérias o curso de Engenharia de Produção disponibiliza?",
                "Quais matérias estão na grade curricular do curso de Engenharia de Produção",
                "O que vou aprender no curso de Engenharia de Produção?",
                "Quais são as disciplinas do curso de Engenharia de Produção?",
                "Quais são as disciplinas presentes na grade curricular do curso de Engenharia de Produção",
                "Quais matérias fazem parte do curso de Engenharia de Produção?",
                "Quais matérias fazem parte da grade curricular do curso de Engenharia de Produção?",
                "Quais são os conteúdos abordados no curso de Engenharia de Produção?",
                "Quais matérias o curso de Engenharia de Produção oferece?",
                "Quais conteúdos estão na grade curricular do curso de Engenharia de Produção?",
            ],
            "responses": [
                "ENGENHARIA!!!!"
            ],
        },

    ]
}
