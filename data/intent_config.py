available_courses = [
    "Administração",
    "Engenharia de Produção",
    "Sistemas de Informação",
    "Matemática",
]

utils_links = {
    "administracao": {
            "main": "https://www.macae.rj.gov.br/femass/conteudo/titulo/administracao",
            "flowchart": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1691543647.pdf",
            "summary": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1637813629.pdf"
        },
    "engenharia-producao": {
            "main": "https://www.macae.rj.gov.br/femass/conteudo/titulo/engenharia-de-producao",
            "flowchart": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1637783091.pdf",
            "summary": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1637859038.pdf"
        },
    "sistemas-informacao": {
            "main": "https://www.macae.rj.gov.br/femass/conteudo/titulo/sistemas-de-informacao",
            "flowchart": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1600942973.pdf",
            "summary": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1631371724.pdf"
        },
    "matematica": {
            "main": "https://www.macae.rj.gov.br/femass/conteudo/titulo/matematica",
            "flowchart": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1595451069.pdf",
            "summary": "https://www.macae.rj.gov.br/midia/conteudo/arquivos/1631373494.pdf"
        },
    "metodos_ingresso": {
            "vestibular": "https://www.macae.rj.gov.br/femass/conteudo/titulo/vestibular",
            "transferencia_externa": "https://www.macae.rj.gov.br/femass/conteudo/titulo/transferencia-externa",
            "reingresso": "https://www.macae.rj.gov.br/femass/conteudo/titulo/reingresso"
        },
    "outros": {
            "corpo_docente": "https://www.macae.rj.gov.br/femass/conteudo/titulo/corpo-docente"
    }
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
                "Quais cursos estão disponíveis?",
                "Me fale sobre os cursos da FeMASS",
                "Me fale sobre os cursos",
                "Que cursos a FeMASS oferece?",
                "Quais cursos têm na FeMASS?",
                "Quais cursos têm?",
                "Pode me dizer os cursos disponíveis na FeMASS?",
                "Pode me dizer os cursos disponíveis?",
                "O que a FeMASS ensina?",
                "Quais são as opções de cursos da FeMASS?",
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
                "Cursos",
                "Curso"
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
                "Quero saber sobre o curso de Administração",
                "Gostaria de saber sobre Administração",
                "Administração"
                "Poderia falar mais sobre o curso de Administração?"
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
                "Gostaria de saber das matérias de Administração",
                "Quais matérias irei cursar em Administração?",
            ],
            "responses": [
                f"O curso de Administração disponibiliza muitas matérias como Logística, Gestão de Custos e Sociologia. Para saber a ementa do curso entre no link {utils_links['administracao']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['administracao']['flowchart']}.",
                f"No curso de Administração você vai aprender diversas matérias como Logística, Gestão de Custos e Sociologia. Para saber a ementa do curso entre no link {utils_links['administracao']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['administracao']['flowchart']}.",
                f"Para saber mais sobre quais matérias o curso de Administração disponibiliza, entre no seguinte link para acessar a ementa:{utils_links['administracao']['summary']} \nou caso queira ver o fluxograma da grade entre no link {utils_links['administracao']['flowchart']}.",
            ],
        },
        {
            "intention": "engenharia-producao",
            "patterns": [
                "Gostaria de saber sobre o curso de Engenharia de Produção",
                "Poderia me falar mais sobre o curso de Engenharia de Produção?",
                "Gostaria de saber mais informações sobre o curso de Engenharia de Produção",
                "Gostaria de informações sobre o curso de Engenharia de Produção",
                "Poderia me informar mais sobre o curso de Engenharia de Produção?",
                "Quais são os detalhes do curso de Engenharia de Produção?",
                "Quero saber sobre Engenharia de Produção",
                "Quero saber sobre o curso de Engenharia de Produção",
                "Gostaria de saber sobre Engenharia de Produção",
                "Gostaria de saber sobre o curso de Engenharia",
                "Poderia me falar mais sobre o curso de Engenharia",
                "Gostaria de saber mais informações sobre o curso de Engenharia",
                "Gostaria de informações sobre o curso de Engenharia",
                "Poderia me informar mais sobre o curso de Engenharia",
                "Quais são os detalhes do curso de Engenharia",
                "Quero saber sobre Engenharia",
                "Quero saber sobre o curso de Engenharia",
                "Gostaria de saber sobre Engenharia",
                "Engenharia de Produção",
                "Engenharia",
                "Poderia falar mais sobre o curso de Engenharia de Produção?",
                "Poderia falar mais sobre o curso de Engenharia?"
            ],
            "responses": [
                "O curso de Engenharia de Produção tem como objetivo formar profissionais que desempenham um papel importante na corporação, pois atua nas atividades de projetar e viabilizar, de forma estratégica, processos produtivos, planejando, produzindo e distribuindo produtos que agregam valor à sociedade. O curso é oferecido de forma presencial, com duração de dez semestres letivos, cada um com vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min",
                "O curso de Engenharia de Produção visa formar profissionais com capacidade de projetar e viabilizart de forma estratégica , processos produtivos que agregam valor à sociedade. O curso é oferecido de forma presencial, com duração de dez semestres letivos, cada um com vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min.",
                "O objetivo do curso de Engenharia de Produção é preparar profissionais estratégicos e que agreguem valor à sociedade. O curso é oferecido na modalidade presencial, com duração de dez semestres letivos, sendo cada semestre composto por vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min.",
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
                "Qual a grade curricular de Engenharia?",
                "Quais as matérias da grade curricular de Engenharia?",
                "Quais matérias o curso de Engenharia disponibiliza?",
                "Quais matérias estão na grade curricular de Engenharia?",
                "O que vou aprender no curso de Engenharia?",
                "Quais são as disciplinas do curso de Engenharia?",
                "Quais são as disciplinas presentes na grade curricular de Engenharia?",
                "Quais matérias fazem parte do curso de Engenharia?",
                "Quais matérias fazem parte da grade curricular de Engenharia?",
                "Quais são os conteúdos abordados no curso de Engenharia?",
                "Quais matérias o curso de Engenharia oferece?",
                "Quais conteúdos estão na grade curricular de Engenharia?",
                "Gostaria de saber das matérias de Engenharia de Produção",
                "Gostaria de saber das matérias de Engenharia",
                "Quais matérias irei cursar em Engenharia de Produção?",
                "Quais matérias irei cursar em Engenharia?",

            ],
            "responses": [
                f"O curso de Engenharia de Produção disponibiliza muitas matérias como Resistência dos Materiais, Física e Logística. Para saber a ementa do curso entre no link {utils_links['engenharia-producao']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['engenharia-producao']['flowchart']}.",
                f"No curso de Engenharia de Produção você vai aprender diversas matérias como Resistência dos Materiais, Física e Logística. Para saber a ementa do curso entre no link {utils_links['engenharia-producao']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['engenharia-producao']['flowchart']}.",
                f"Para saber mais sobre quais matérias o curso de Engenharia de Produção disponibiliza, entre no seguinte link para acessar a ementa:{utils_links['engenharia-producao']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['engenharia-producao']['flowchart']}.",
            ],
        },
        {
            "intention": "sistemas-informacao",
            "patterns": [
                "Gostaria de saber sobre o curso de Sistemas de Informação",
                "Poderia me falar mais sobre o curso de Sistemas de Informação?",
                "Gostaria de saber mais informações sobre o curso de Sistemas de Informação",
                "Gostaria de informações sobre o curso de Sistemas de Informação",
                "Poderia me informar mais sobre o curso de Sistemas de Informação?",
                "Quais são os detalhes do curso de Sistemas de Informação?",
                "Quero saber sobre Sistemas de Informação",
                "Quero saber sobre o curso de Sistemas de Informação",
                "Gostaria de saber sobre Sistemas de Informação",
                "Gostaria de saber sobre o curso de Sistemas",
                "Poderia me falar mais sobre o curso de Sistemas ?",
                "Gostaria de saber mais informações sobre o curso de Sistemas",
                "Gostaria de informações sobre o curso de Sistemas",
                "Poderia me informar mais sobre o curso de Sistemas",
                "Quais são os detalhes do curso de Sistemas",
                "Quero saber sobre Sistemas",
                "Quero saber sobre o curso de Sistemas",
                "Gostaria de saber sobre Sistemas",
                "Sistemas de Informação",
                "Sistemas",
                "Poderia falar mais sobre o curso de Sistemas de Informação?",
                "Poderia falar mais sobre o curso de Sistemas?"
            ],
            "responses": [
                "O curso de Sistemas de Informação tem como objetivo formar profissionais aptos a analisar, desenvolver e implantar sistemas, infraestruturas de hardware, infraestrutura de dados e também realizar análise técnica de novas tecnologias. O curso é oferecido de forma presencial, com duração de oito semestres letivos, cada um com vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min.",
                "O curso de Sistemas de Informação visa formar profissionais com uma visão analítica para desenvolver e implantar sistemas além de fazer análises técnicas de novas tecnologias. O curso é oferecido de forma presencial, com duração de oito semestres letivos, cada um com vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min.",
                "O objetivo do curso de Sistemas de Informação é preparar profissionais capacitados para desenvolver e implantar sistemas. O curso é oferecido na modalidade presencial, com duração de oito semestres letivos, sendo cada semestre composto por vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min."
            ],
        },
        {
            "intention": "grade_curricular_sistemas_informacao",
            "patterns": [
                "Qual a grade curricular do curso de Sistemas de Informação?",
                "Quais as matérias da grade curricular do curso de Sistemas de Informação?",
                "Quais matérias o curso de Sistemas de Informação disponibiliza?",
                "Quais matérias estão na grade curricular do curso de Sistemas de Informação",
                "O que vou aprender no curso de Sistemas de Informação?",
                "Quais são as disciplinas do curso de Sistemas de Informação?",
                "Quais são as disciplinas presentes na grade curricular do curso de Sistemas de Informação",
                "Quais matérias fazem parte do curso de Sistemas de Informação?",
                "Quais matérias fazem parte da grade curricular do curso de Sistemas de Informação?",
                "Quais são os conteúdos abordados no curso de Sistemas de Informação?",
                "Quais matérias o curso de Sistemas de Informação oferece?",
                "Quais conteúdos estão na grade curricular do curso de Sistemas de Informação?",
                "Qual a grade curricular de Sistemas?",
                "Quais as matérias da grade curricular de Sistemas?",
                "Quais matérias o curso de Sistemas disponibiliza?",
                "Quais matérias estão na grade curricular de Sistemas?",
                "O que vou aprender no curso de Sistemas?",
                "Quais são as disciplinas do curso de Sistemas?",
                "Quais são as disciplinas presentes na grade curricular de Sistemas?",
                "Quais matérias fazem parte do curso de Sistemas?",
                "Quais matérias fazem parte da grade curricular de Sistemas?",
                "Quais são os conteúdos abordados no curso de Sistemas?",
                "Quais matérias o curso de Sistemas oferece?",
                "Quais conteúdos estão na grade curricular de Sistemas?",
                "Gostaria de saber das matérias de Sistemas de Informação"
                "Gostaria de saber das matérias de Sistemas",
                "Quais matérias irei cursar em Sistemas de Informação?",
                "Quais matérias irei cursar em Sistemas?",
            ],
            "responses": [
                f"O curso de Sistemas de Informação disponibiliza muitas matérias como Programação, Banco de Dados e Redes de Computadores. Para saber a ementa do curso entre no link {utils_links['sistemas-informacao']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['sistemas-informacao']['flowchart']}.",
                f"No curso de Sistemas de Informação você vai aprender diversas matérias como Programação, Banco de Dados e Redes de Computadores. Para saber a ementa do curso entre no link {utils_links['sistemas-informacao']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['sistemas-informacao']['flowchart']}.",
                f"Para saber mais sobre quais matérias o curso de Sistemas de Informação disponibiliza, entre no seguinte link para acessar a ementa: {utils_links['sistemas-informacao']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['sistemas-informacao']['flowchart']}."
            ]
        },
        {
            "intention": "matematica",
            "patterns": [
                "Gostaria de saber sobre o curso de Matemática",
                "Poderia me falar mais sobre o curso de Matemática?",
                "Gostaria de saber mais informações sobre o curso de Matemática",
                "Gostaria de informações sobre o curso de Matemática",
                "Poderia me informar mais sobre o curso de Matemática?",
                "Quais são os detalhes do curso de Matemática?",
                "Quero saber sobre Matemática",
                "Quero saber sobre o curso de Matemática",
                "Gostaria de saber sobre Matemática",
                "Matemática",
                "Poderia falar mais sobre o curso de Matemática?"
            ],
            "responses": [
                "O curso de Matemática tem como objetivo formar um profissional comprometido com a educação de qualidade, capaz de transmitir conhecimento de forma estratégica e alinhada à realidade social, política e cultural. O curso é oferecido de forma presencial, com duração de oito semestres letivos, cada um com vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min",
                "O curso de Matemática visa formar um profissional dedicado à educação de qualidade, que utilize estratégias didáticas conectadas ao contexto social, político e cultural. O curso é oferecido de forma presencial, com duração de oito semestres letivos, cada um com vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min.",
                "O objetivo do curso de Matemática é preparar profissionais capacitados e comprometidos com a edução de qualidade. O curso é oferecido na modalidade presencial, com duração de oito semestres letivos, sendo cada semestre composto por vinte semanas, em horário noturno de segunda a sexta, das 18h às 22h30min.",
            ],
        },
        {
            "intention": "grade_curricular_matematica",
            "patterns": [
                "Qual a grade curricular do curso de Matemática?",
                "Quais as matérias da grade curricular do curso de Matemática?",
                "Quais matérias o curso de Matemática disponibiliza?",
                "Quais matérias estão na grade curricular do curso de Matemática",
                "O que vou aprender no curso de Matemática?",
                "Quais são as disciplinas do curso de Matemática?",
                "Quais são as disciplinas presentes na grade curricular do curso de Matemática",
                "Quais matérias fazem parte do curso de Matemática?",
                "Quais matérias fazem parte da grade curricular do curso de Matemática?",
                "Quais são os conteúdos abordados no curso de Matemática?",
                "Quais matérias o curso de Matemática oferece?",
                "Quais conteúdos estão na grade curricular do curso de Matemática?",
                "Gostaria de saber das matérias de Matemática",
                "Quais matérias irei cursar em Matemática?",
            ],
            "responses": [
                f"O curso de Matemática disponibiliza muitas matérias como Cálculo, Álgebra e Geometria. Para saber a ementa do curso entre no link {utils_links['matematica']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['matematica']['flowchart']}.",
                f"No curso de Matemática você vai aprender diversas matérias como Cálculo, Álgebra e Geometria. Para saber a ementa do curso entre no link {utils_links['matematica']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['matematica']['flowchart']}.",
                f"Para saber mais sobre quais matérias o curso de Matemática disponibiliza, entre no seguinte link para acessar a ementa: {utils_links['matematica']['summary']} ou caso queira ver o fluxograma da grade entre no link {utils_links['matematica']['flowchart']}.",
            ]
        },
        {
            "intention": "metodos_ingresso",
            "patterns": [
                "Quais são os métodos de ingresso na FEMASS?",
                "Como posso ingressar na FEMASS?",
                "Quais são as formas de entrar na FEMASS?",
                "Como funciona o ingresso na FEMASS?",
                "Quais são as opções para ingressar na FEMASS?",
                "Quais são as maneiras de entrar na FEMASS?",
                "Como faço para ingressar na FEMASS?",
                "Quais são os processos de ingresso na FEMASS?",
                "Quais são as modalidades de ingresso na FEMASS?",
                "Como é o ingresso na FEMASS?",
                "Quais são as vias de ingresso na FEMASS?",
                "Quais são as alternativas para ingressar na FEMASS?",
                "Como posso me matricular na FEMASS?",
                "Quais são os caminhos para ingressar na FEMASS?",
                "Quais são as possibilidades de ingresso na FEMASS?",
                "Como é o processo de ingresso na FEMASS?",
                "Quais são as formas de ingresso disponíveis na FEMASS?",
                "Quais são as formas de acesso à FEMASS?",
                "Como posso conseguir uma vaga na FEMASS?",
                "Quais são as formas de admissão na FEMASS?",
                "Como é o sistema de ingresso na FEMASS?",
                "Quais são as formas de ingresso oferecidas pela FEMASS?",
                "Quais são as opções de ingresso na FEMASS?",
                "Como posso entrar na FEMASS?",
                "Quais são as formas de ingresso na faculdade FEMASS?",
                "Quais são as maneiras de se matricular na FEMASS?",
                "Como funciona o acesso à FEMASS?",
                "Quais são as formas de ingresso na instituição FEMASS?",
                "Quais são as formas de ingresso na faculdade FEMASS?",
                "Como posso me inscrever para ingressar na FEMASS?"
            ],
            "responses": [
                "Você pode ingressar na FeMASS através do vestibular, transferência externa ou reingresso. Caso tenha dúvida em algum método específico é só me perguntar!",
                "Existem três formas de ingressar na FeMASS: vestibular, transferência externa e reingresso.",
                "Ótima pergunta! Para ingressar na FeMASS você pode fazer o vestibular, transferência externa e reingresso. Para mais informações sobre cada um deles recomendo entrar nos seguintes sites:\nVestibular: {utils_links['metodos_ingresso']['vestibular']}\nTransferência Externa: {utils_links['metodos_ingresso']['transferencia_externa']}\nReingresso: {utils_links['metodos_ingresso']['reingresso']}",
                "Na FeMASS, você tem três opções para ingressar: vestibular, transferência externa e reingresso. Se precisar de detalhes sobre algum desses métodos, é só me perguntar!",
                "Para se matricular na FeMASS, você pode optar por uma das três formas de ingresso: vestibular, transferência externa ou reingresso. Qualquer dúvida sobre esses métodos, estou aqui para ajudar!",
                "Interessado em ingressar na FeMASS? Você pode escolher entre três métodos: vestibular, transferência externa ou reingresso. Se quiser mais detalhes sobre algum deles, é só avisar!"

            ]
        },
        {
            "intention": "vestibular",
            "patterns": [
                "Como faço o vestibular da FeMASS?",
                "Gostaria de saber mais informações sobre o vestibular",
                "Aonde faço minha matrícula para o vestibular da FeMASS?",
                "Onde faço o vestibular da FeMASS?",
                "Quais os requisitos para fazer o vestibular?",
                "Como me inscrevo para o vestibular da FeMASS?",
                "Quais são as etapas do vestibular da FeMASS?",
                "O vestibular da FeMASS é online ou presencial?",
                "Quando abrem as inscrições para o vestibular da FeMASS?",
                "Qual é a documentação necessária para fazer o vestibular?",
                "Como funciona o vestibular?",
                "Vestibular",
            ],
            "responses": [
                f"O Processo Seletivo para ingresso nos Cursos de Graduação da FeMASS segue critérios estabelecidos pelo Conselho Superior e detalhados em Edital Próprio. Podem participar candidatos que tenham concluído o ensino médio ou equivalente. Para mais informações, acesse {utils_links['metodos_ingresso']['vestibular']}.",
                f"Para ingressar nos Cursos de Graduação da FeMASS, é necessário participar do Processo Seletivo, que avalia a aptidão intelectual dos candidatos conforme as normas definidas pelo Conselho Superior e publicadas em Edital Próprio. Saiba mais em {utils_links['metodos_ingresso']['vestibular']}.",
                f"O vestibular da FeMASS é aberto a candidatos com escolaridade completa em nível médio ou equivalente. O processo de seleção segue critérios estabelecidos pelo Conselho Superior e visa classificar os candidatos conforme seu desempenho. Consulte os detalhes acessando {utils_links['metodos_ingresso']['vestibular']}.",
                f"A seleção para os Cursos de Graduação da FeMASS ocorre por meio de Processo Seletivo, que busca avaliar as potencialidades dos candidatos de maneira equânime. As normas e critérios de ingresso são definidos em Edital Próprio. Para mais detalhes, visite {utils_links['metodos_ingresso']['vestibular']}."
            ]
        },
        {
            "intention": "vestibular_taxa",
            "patterns": [
                "Existe alguma taxa para fazer o vestibular?",
                "Quanto é a taxa para fazer o vestibular?",
                "Quando custa fazer o vestibular?",
                "Qual valor do vestibular da FeMASS?",
                "Quais os métodos de pagamento do vestibular da FeMASS?"
                "O vestibular da FeMASS é gratuito?",
                "Onde posso pagar a taxa do vestibular?",
                "O valor do vestibular muda a cada ano?",
                "A taxa do vestibular muda a cada ano?",
                "A taxa do vestibular pode mudar a cada ano?"
            ],
            "responses": [
                f"O valor da taxa de inscrição para o vestibular é no valor de R$70,00 e o pagamento pode ser efetuado através de um Boleto Bancário. Recomendo acessar o site {utils_links['metodos_ingresso']['vestibular']} e escolher o ano do vestibular que irá fazer para obter informações mais precisar!",
                f"O valor da taxa de inscrição para o vestibular é de R$70,00 e o pagamento pode ser efetuado através de um Boleto Bancário. Para mais informações, acesse o site {utils_links['metodos_ingresso']['vestibular']} e escolha o ano do vestibular que deseja realizar!",
                f"A inscrição para o vestibular tem uma taxa de R$70,00, e o pagamento deve ser feito via Boleto Bancário. Recomendo acessar {utils_links['metodos_ingresso']['vestibular']} para obter detalhes específicos sobre o vestibular do ano desejado!",
                f"O vestibular possui uma taxa de inscrição no valor de R$70,00, que pode ser paga através de Boleto Bancário. Para informações mais detalhadas, visite {utils_links['metodos_ingresso']['vestibular']} e selecione o ano correspondente ao vestibular de interesse!",

            ]
        },
        {
            "intention": "transferencia_externa",
            "patterns": [
                "Como faço a transferência externa?",
                "É possível fazer transferência externa?",
                "Quais os métodos para realizar a transferência externa?",
                "Quais são os requisitos para a transferência externa?",
                "Como funciona o processo de transferência externa?",
                "Quais documentos são necessários para solicitar a transferência externa?",
                "Existe alguma taxa para a transferência externa?",
                "Qual o prazo para solicitar a transferência externa?",
                "A transferência externa é válida para todos os cursos?",
                "Onde encontro o edital sobre a transferência externa?"
            ],
            "responses": [
                f"O processo de Transferência Externa é realizado em três etapas: inscrição, prova de conhecimentos e entrega de documentação para análise de dispensa de disciplinas. Os documentos exigidos incluem declaração de matrícula, comprovantes do curso, cópia da identidade e uma foto 3x4. Para mais detalhes, acesse {utils_links['metodos_ingresso']['transferencia_externa']}.",
                f"Para ingressar via Transferência Externa, o candidato deve seguir três etapas: inscrição, realização da prova de conhecimentos e envio da documentação exigida. Dentre os documentos necessários estão declaração de matrícula, identidade e comprovantes do curso. Todas as informações detalhadas estão disponíveis em {utils_links['metodos_ingresso']['transferencia_externa']}.",
                f"A Transferência Externa exige que o candidato passe por três etapas: inscrição, prova de conhecimentos e entrega de documentos para análise. É necessário apresentar declaração de matrícula, identidade, comprovante do curso e outros documentos. Consulte todos os requisitos e prazos acessando {utils_links['metodos_ingresso']['transferencia_externa']}.",
                f"Se você deseja solicitar a Transferência Externa, fique atento às três etapas do processo: inscrição, prova de conhecimentos e envio da documentação necessária. Os documentos incluem declaração de matrícula, identidade e comprovantes acadêmicos. Para informações detalhadas, acesse {utils_links['metodos_ingresso']['transferencia_externa']}."
            ]
        },
        {
            "intention": "reingresso",
            "patterns": [
                "Como posso solicitar o Reingresso?",
                "Quais são os critérios para quem deseja fazer o Reingresso?",
                "Quem está apto a participar do Reingresso?",
                "É necessário atender a algum requisito para o Reingresso?",
                "O que eu preciso para ser elegível ao Reingresso?",
                "Quais são as condições exigidas para o Reingresso?",
                "Quem pode se inscrever para o Reingresso?",
                "Posso fazer o Reingresso mesmo tendo sido aluno de outra instituição?",
                "Quais são as exigências para quem quer fazer o Reingresso na instituição?",
                "Como saber se sou qualificado para o Reingresso?"
            ],
            "responses": [
                f"O processo de Reingresso segue duas etapas: inscrição e prova de conhecimentos. A avaliação inclui uma prova discursiva de Matemática e uma Redação, sendo necessário obter nota mínima de 7,0 em cada uma. Para mais informações, acesse {utils_links['metodos_ingresso']['reingresso']}."  
                f"Para solicitar o Reingresso, o candidato deve se inscrever e realizar uma prova de conhecimentos. Apenas graduados em cursos superiores reconhecidos podem participar, e a aprovação exige nota mínima de 7,0 em cada avaliação. Confira os detalhes no edital disponível em {utils_links['metodos_ingresso']['reingresso']}."  
                f"O Reingresso é um processo seletivo com duas etapas: inscrição e prova de conhecimentos. Apenas candidatos graduados podem participar, e a prova exige um desempenho mínimo de 7,0 em cada avaliação para classificação. Saiba mais acessando {utils_links['metodos_ingresso']['reingresso']}."  
                f"Se você deseja participar do processo de Reingresso, é necessário se inscrever e fazer uma prova de conhecimentos, que inclui questões discursivas de Matemática e uma Redação. A classificação depende de uma nota mínima de 7,0 em cada avaliação. Veja mais detalhes no site: {utils_links['metodos_ingresso']['reingresso']}."

            ]
        },
        {
            "intention": "corpo_docente",
            "patterns": [
                "Quem faz parte do corpo docente da instituição?",
                "Como posso consultar a lista de professores da faculdade?",
                "Quais são os professores responsáveis pelo curso?",
                "Como encontrar informações sobre os professores do corpo docente?",
                "Qual é o nome dos professores do curso de graduação?",
                "Os professores da instituição têm algum departamento específico?",
                "Como posso saber quem são os professores do meu curso?",
                "O corpo docente da faculdade é formado por quais professores?",
                "Quais são os professores da FeMASS?",
                "Posso obter informações sobre os professores?"
            ],
            "responses": [
                f"O corpo docente da instituição é composto por professores altamente capacitados em suas respectivas áreas. Para consultar a lista completa de professores, acesse {utils_links['outros']['corpo_docente']}.",
                f"Você pode encontrar informações detalhadas sobre o corpo docente através do seguinte link: {utils_links['outros']['corpo_docente']}.",
                f"Para saber mais sobre os professores e suas áreas de atuação, consulte o corpo docente no link: {utils_links['outros']['corpo_docente']}.",
                f"Para acessar informações sobre o corpo docente e os professores da instituição, acesse o site {utils_links['outros']['corpo_docente']}."
            ]
        }

    ]
}