# Book_Catalog

Web application project for reviews books, developed using Flask framework. This application allows that users register, log in, add, edit and remove reviews books. Were used Python, HTML, CSS, JavaScript and MySQL in the project.

Este é um aplicativo web de catálogo de livros onde os usuários podem registrar, editar e visualizar livros associados às suas contas. O projeto utiliza Flask como framework web e MySQL como banco de dados.

## Sumário

- [Tecnologias](#tecnologias)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Banco de Dados](#banco-de-dados)
- [Rotas](#rotas)
- [Contribuição](#contribuição)

## Tecnologias

- Python
- Flask
- SQLAlchemy
- MySQL
- Bootstrap
- HTML
- CSS

## Requisitos

- Python 3.x
- MySQL
- pip (Python package installer)
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/PablinMartins/Book_Catalog/book_catalog.git
    cd book_catalog
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:
    - Crie um banco de dados no MySQL:
      ```sql
      CREATE DATABASE books;
      ```
    - Atualize as configurações do banco de dados em `config.py`:
      ```python
      SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:senha@localhost:3306/books'
      ```

5. Inicialize o banco de dados:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Uso

1. Execute o servidor Flask:
    ```sh
    flask run
    ```

2. Acesse o aplicativo em seu navegador:
    ```
    http://127.0.0.1:5000
    ```

## Estrutura do Projeto

```plaintext
book_catalog/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── templates/
│       ├── index.html
│       ├── add_book.html
│       ├── edit_book.html
│       ├── book_detail.html
│       └── login.html
│
├── static/
│   ├── css/
│   └── js/
│
│
├── venv/
│
├── config.py
│
└── run.py
```

##  Banco de dados

```sql
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    comment TEXT
);

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

ALTER TABLE book ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user(id);
```

## Rotas

```plaintext

/: Página inicial com formulário de login
/register: Página de registro de novos usuários
/login: Página de login
/logout: Endpoint para logout
/catalog: Página com o catálogo de livros do usuário logado
/add_book: Página para adicionar um novo livro
/edit/<int:book_id>: Página para editar um livro existente
/book/<int:book_id>: Página de detalhes de um livro específico

```

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request para discutir melhorias ou novas funcionalidades.








