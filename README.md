

# **Projeto Django - Desenvolvimento Back-End**

**Descrição:**  
Este projeto foi desenvolvido como parte da disciplina de **Desenvolvimento Back-End** do curso de **Análise e Desenvolvimento de Sistemas** do **Centro Universitário CESMAC**. O objetivo do projeto é aplicar os conceitos aprendidos durante a disciplina, utilizando o framework Django para criar uma aplicação funcional com as melhores práticas de desenvolvimento back-end.

## **Funcionalidades**
- [x] Estruturação de um ambiente back-end com Django.
- [x] Cadastro e autenticação de usuários.
- [x] Gerenciamento de dados com banco de dados SQLite.

## **Tecnologias Utilizadas**
- Python 3.10
- Django 5.1.3
- SQLite (banco de dados)

## **Objetivo do Projeto**
Este projeto tem como finalidade:
1. Demonstrar o domínio dos conceitos fundamentais de desenvolvimento back-end.
2. Praticar a criação de APIs, autenticação e manipulação de dados em um ambiente controlado.
3. Servir como base para projetos futuros, permitindo expansão e integração com tecnologias front-end e outras soluções.

## **Pré-requisitos para Execução**
Certifique-se de ter as ferramentas instaladas:
- Python 3.10 ou superior
- Git

## **Passo a Passo para Instalação**
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. **Acesse o diretório do projeto:**
   ```bash
   cd nome-do-repositorio
   ```

3. **Crie e ative o ambiente virtual:**
   - No Windows:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

4. **Instale as dependências do projeto:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o banco de dados e aplique as migrações:**
   ```bash
   python manage.py migrate
   ```

6. **Inicie o servidor local:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse o projeto no navegador:**
   Abra o endereço [http://127.0.0.1:8000](http://127.0.0.1:8000).

