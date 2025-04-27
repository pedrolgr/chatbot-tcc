# 🤖 Chatbot FeMASS

Este projeto é um chatbot desenvolvido em Python para auxiliar alunos e usuários da FeMASS, utilizando técnicas de Processamento de Linguagem Natural (PLN) e uma API web simples com Flask.

## 🚀 Como instalar

Siga os passos abaixo para rodar o projeto na sua máquina:

### 1. Clone o repositório

```bash
git clone https://github.com/pedrolgr/chatbot-tcc.git
cd chatbot-tcc
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou, se preferir, instale manualmente:

```bash
pip install Flask==3.1.0
pip install nltk==3.9.1
pip install spacy==3.8.5
pip install Unidecode==1.3.8
```

### 4. Configurações adicionais

#### Baixar recursos do NLTK

No terminal Python, execute:

```python
import nltk
nltk.download('punkt')
```

#### Baixar modelo de linguagem do spaCy

Execute no terminal:

```bash
python -m spacy download pt_core_news_sm
```

### 5. Como rodar o projeto

Dentro da raiz do projeto, execute o arquivo app.py ou execute os seguinte comandos:

```bash
flask run
```
ou:
```bash
python app.py
```




A aplicação estará disponível em:

## 🛠 Tecnologias utilizadas

- [Flask](https://flask.palletsprojects.com/) — Framework web para Python
- [NLTK](https://www.nltk.org/) — Processamento de Linguagem Natural
- [spaCy](https://spacy.io/) — Biblioteca avançada de NLP
- [Unidecode](https://pypi.org/project/Unidecode/) — Conversão de caracteres Unicode para ASCII



## 🔗 Link do projeto

[https://github.com/pedrolgr/chatbot-tcc](https://github.com/pedrolgr/chatbot-tcc)
