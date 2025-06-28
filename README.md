# Agendify API

**Agendify** é uma API RESTful desenvolvida com **Django** e **Django REST Framework** para a gestão de agendamentos. A plataforma permite que prestadores de serviço gerenciem seus horários, agendem clientes e cancelem agendamentos de forma simples e eficiente.

## ✨ Features

- **Autenticação JWT**: Acesso seguro à API utilizando JSON Web Tokens.
- **Gestão de Agendamentos**:
  - Criação de novos agendamentos.
  - Listagem de agendamentos do prestador autenticado.
  - Cancelamento de agendamentos (soft delete).
- **Validação de Dados**:
  - Impede a criação de agendamentos em datas passadas.
  - Garante que um prestador não tenha dois agendamentos no mesmo horário.
- **Estrutura Modular**: O projeto é organizado em apps Django para melhor manutenibilidade: `agendamentos`, `usuarios` e `core`.

## 🛠️ Tecnologias Utilizadas

- **Backend**:
  - Python
  - Django
  - Django REST Framework
  - Simple JWT (para autenticação)
- **Banco de Dados**:
  - SQLite (configuração padrão para desenvolvimento)

## 📂 Estrutura do Projeto

O projeto segue a estrutura padrão do Django, com a lógica de negócio separada em diferentes apps:

agendify/
├── agendify/ # Arquivos de configuração do projeto
├── agendamentos/ # App para gerenciar os agendamentos
├── core/ # App com modelos e lógicas base
├── usuarios/ # App para gerenciar usuários e perfis
├── manage.py # Utilitário de linha de comando do Django
└── .gitignore # Arquivos e pastas a serem ignorados pelo Git

swift
Copiar
Editar

- **`core`**: Contém o `BaseModel`, um modelo abstrato com campos `id` (UUID), `criado_em` e `atualizado_em`, que é herdado pelos outros modelos do projeto.
- **`usuarios`**: Estende o modelo de usuário padrão do Django com um `Perfil`.
- **`agendamentos`**: É o coração da aplicação. Contém o modelo `Agendamento`, as views (`ViewSet`), serializers e URLs para a lógica de agendamentos.

## 🔌 API Endpoints

Todos os endpoints, exceto os de autenticação, requerem um token JWT no header `Authorization`.

| Método         | Endpoint                        | Descrição                                                                 |
|----------------|----------------------------------|---------------------------------------------------------------------------|
| `POST`         | `/api/token/`                   | Autentica um usuário e retorna um par de tokens (access e refresh).       |
| `POST`         | `/api/token/refresh/`           | Gera um novo token de acesso usando o token de refresh.                   |
| `GET`          | `/api/agendamentos/`            | Lista todos os agendamentos não cancelados do prestador autenticado.      |
| `POST`         | `/api/agendamentos/`            | Cria um novo agendamento para o prestador autenticado.                    |
| `GET`          | `/api/agendamentos/{id}/`       | Retorna os detalhes de um agendamento específico.                         |
| `PUT` / `PATCH`| `/api/agendamentos/{id}/`       | Atualiza um agendamento.                                                  |
| `DELETE`       | `/api/agendamentos/{id}/`       | Realiza o cancelamento (soft delete) de um agendamento.                   |

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/agendify.git
```
```bash
cd agendify
```

Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate
# No Windows: venv\Scripts\activate
```

Instale as dependências:

Obs: Se não existir um requirements.txt, instale os pacotes manualmente:
```bash
pip install Django djangorestframework djangorestframework-simplejwt
```
Aplique as migrações do banco de dados:
```bash
python manage.py migrate
```
Crie um superusuário:

```bash
python manage.py createsuperuser
```
Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```
Acesse a API em:
http://127.0.0.1:8000/
