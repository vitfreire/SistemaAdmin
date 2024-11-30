Projeto Django - Desenvolvimento Back-End
Descrição:
Este projeto foi desenvolvido como parte da disciplina de Desenvolvimento Back-End do curso de Análise e Desenvolvimento de Sistemas do Centro Universitário CESMAC. O objetivo do projeto é aplicar os conceitos aprendidos durante a disciplina, utilizando o framework Django para criar uma aplicação funcional com as melhores práticas de desenvolvimento back-end.

Funcionalidades
 Estruturação de um ambiente back-end com Django.
 Cadastro e autenticação de usuários.
 Gerenciamento de dados com banco de dados SQLite.

Tecnologias Utilizadas
Python 3.10
Django 5.1.3
SQLite (banco de dados)

Objetivo do Projeto
Este projeto tem como finalidade:

Demonstrar o domínio dos conceitos fundamentais de desenvolvimento back-end.
Praticar a criação de APIs, autenticação e manipulação de dados em um ambiente controlado.
Servir como base para projetos futuros, permitindo expansão e integração com tecnologias front-end e outras soluções.
Pré-requisitos para Execução
Certifique-se de ter as ferramentas instaladas:

Python 3.10 ou superior
Git
Passo a Passo para Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Acesse o diretório do projeto:

bash
Copiar código
cd nome-do-repositorio
Crie e ative o ambiente virtual:

No Windows:
bash
Copiar código
python -m venv env
.\env\Scripts\activate
No Linux/Mac:
bash
Copiar código
python3 -m venv env
source env/bin/activate
Instale as dependências do projeto:

bash
Copiar código
pip install -r requirements.txt
Configure o banco de dados e aplique as migrações:

bash
Copiar código
python manage.py migrate
Inicie o servidor local:

bash
Copiar código
python manage.py runserver
Acesse o projeto no navegador: Abra o endereço http://127.0.0.1:8000.
