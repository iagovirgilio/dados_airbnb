# Airbnb Django Project

Bem-vindo ao **Airbnb Django Project**! Este projeto é uma aplicação web desenvolvida em Django que replica funcionalidades similares ao Airbnb, permitindo o gerenciamento de propriedades (Stays), uploads de arquivos, processamento de dados e muito mais. A aplicação está containerizada utilizando Docker para facilitar o desenvolvimento, implantação e escalabilidade.

## 📋 Índice

- [Características](#características)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
  - [1. Clonar o Repositório](#1-clonar-o-repositório)
  - [2. Configurar Variáveis de Ambiente](#2-configurar-variáveis-de-ambiente)
  - [3. Construir as Imagens Docker](#3-construir-as-imagens-docker)
  - [4. Iniciar os Containers](#4-iniciar-os-containers)
  - [5. Aplicar Migrações e Coletar Arquivos Estáticos](#5-aplicar-migrações-e-coletar-arquivos-estáticos)
  - [6. Criar Superusuário](#6-criar-superusuário)
- [🚀 Uso](#uso)
  - [Executando o Projeto](#executando-o-projeto)
  - [Acessando o Django Admin](#acessando-o-django-admin)
- [📜 Scripts Úteis](#scripts-úteis)
- [🐛 Resolução de Problemas](#resolução-de-problemas)
  - [1. Erro: `Method Not Allowed (GET): /admin/logout/`](#1-erro-method-not-allowed-get-adminlogout)
  - [2. Erro: `AttributeError: 'dict' object has no attribute 'SUCCESS'`](#2-erro-attributeerror-dict-object-has-no-attribute-success)
  - [3. Avisos do Pandas: `SettingWithCopyWarning`](#3-avisos-do-pandas-settingwithcopywarning)
  - [4. Erro: `CommandError: Can't find msguniq`](#4-erro-commanderror-cant-find-msguniq)
- [📝 Contribuição](#contribuição)
- [📄 Licença](#licença)

## 🛠 Características

- **Autenticação de Usuários**: Login e logout seguros com proteção contra ataques CSRF.
- **Django Admin Customizado**: Interface administrativa personalizada com funcionalidades adicionais, como upload e processamento de arquivos.
- **Processamento de Dados**: Manipulação e enriquecimento de dados utilizando Pandas.
- **Containerização com Docker**: Ambiente de desenvolvimento e produção isolado para maior consistência e facilidade de implantação.

## 🖥 Tecnologias Utilizadas

- **Back-end**: Django 5.1.2
- **Front-end**: HTML, CSS (Bootstrap opcional)
- **Banco de Dados**: PostgreSQL (ou outro conforme configuração)
- **Containerização**: Docker, Docker Compose
- **Processamento de Dados**: Pandas

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas na sua máquina:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)

## 📦 Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/airbnb-django-project.git
cd airbnb-django-project
```

### 2. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis (ajuste conforme necessário)

```env
# .env
DEBUG=1
SECRET_KEY=django-insecure-(9dx3037w-^zj&hdxs%7$)1!6fr5jc#e_6g%b6!_i-a3)jnh6l
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=app_dev
SQL_USER=app
SQL_PASSWORD=app
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
OPEN_WEATHER_KEY=your-secret-key
```
**Nota**: Certifique-se de substituir your-secret-key e outras variáveis sensíveis por valores seguros.

### 3. Construir as Imagens Docker
Construa as imagens Docker necessárias para a aplicação e o banco de dados.

```bash
docker-compose build
```

### 4. Iniciar os Containers
Inicie os containers em segundo plano.

```bash
docker-compose up -d
```
**Nota:** O projeto já está configurado para rodar migrate e collectstatic. Mas caso precise siga os comando abaixo

### 5. Aplicar Migrações e Coletar Arquivos Estáticos

Execute as migrações do Django e colete os arquivos estáticos.

```bash
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py collectstatic --noinput
```

### 6. Criar Superusuário
Crie um superusuário para acessar o Django Admin.

```bash
docker-compose exec app python manage.py createsuperuser
```

Siga as instruções no terminal para definir o nome de usuário, email e senha.

## 🚀 Uso

### Executando o Projeto

Após seguir os passos de instalação, o projeto estará disponível em:

```bash
http://localhost:8009/
```

### Acessando o Django Admin
Para acessar a interface administrativa do Django:

1. Abra o navegador e vá para:
    ``` bash
    http://localhost:8009/admin/
    ```

2. Faça login com as credenciais do superusuário que você criou anteriormente.

## 📜 Scripts Úteis
Aqui estão alguns comandos úteis para gerenciar o projeto:

- Construir as imagens Docker:

    ```bash
    docker-compose build
    ```

- Iniciar os containers:
    ```bash
    docker-compose up -d
    ```

- Parar os containers:
    ```bash
    docker-compose down
    ```

- Aplicar migrações:
    ```bash
    docker-compose exec app python manage.py migrate
    ```

- Criar superusuário:
    ```bash
    docker-compose exec app python manage.py createsuperuser
    ```

- Coletar arquivos estáticos:
    ```bash
    docker-compose exec app python manage.py collectstatic --noinput
    ```

- Executar comandos Django:

    Para executar qualquer comando Django, use:
    ```bash
    docker-compose exec app python manage.py <comando>
    ```

    Exemplo:
    ```bash
    docker-compose exec app python manage.py shell
    ```

## 🐛 Executando testes unitário

### 