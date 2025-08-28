# CRUD Flask

Um projeto simples de **CRUD (Create, Read, Update, Delete)** utilizando Flask. Permite gerenciar registros de forma prática via API ou interface web.

---

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

- `.gitignore` – arquivos e pastas ignorados pelo Git  
- `app.py` – aplicação principal Flask  
- `create_tables.py` – script para criar tabelas no banco de dados  
- `LICENSE` – licença do projeto  
- `README.md` – este arquivo  
- `requirements.txt` – dependências do projeto  

---

## Tecnologias Utilizadas

- Python – Linguagem principal do projeto  
- Flask – Framework web leve para Python  
- SQLite – Banco de dados simples (pode trocar para outro)  
- pip – Gerenciador de pacotes Python  

---

## Como Instalar

1. Clone o repositório:  

```
git clone <URL_DO_REPOSITORIO>
cd crud_flask-main
```

2. Crie um ambiente virtual (opcional, mas recomendado):  

```
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Linux / Mac

```


3. Instale as dependências:  

```
pip install -r requirements.txt

```

4. Crie as tabelas do banco de dados:  

```
python create_tables.py

```

5. Execute a aplicação:  

```
python app.py

```

6. Acesse no navegador:  

```
http://127.0.0.1:5000

```
---

## Funcionalidades

- Criar novos registros  
- Listar todos os registros  
- Atualizar registros existentes  
- Deletar registros  

---

## Licença

Este projeto está sob a **MIT License** – veja `LICENSE` para detalhes.
