# Airbnb Django Project

Bem-vindo ao **Airbnb Django Project**! Este projeto é uma aplicação web desenvolvida em Django que carrega uma lista de dados do Airbnb, limpa e enriquece os dados a partir da latitude e longitude com dados do clima da API Weather, permitindo a vizualização de estadias com informações detalhadas de preço, tipo, clima... A aplicação está containerizada utilizando Docker para facilitar o desenvolvimento, implantação e escalabilidade.

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
- [🧪 Testes Unitários](#testes-unitários)
  - [1. Executar os Testes](#1-executar-os-testes)
  - [2. Escrever Testes](#2-escrever-testes)
- [💡 Melhorias](#melhorias)

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
- [OpwnWeather](https://openweathermap.org/current)

**Nota:** A Weather foi a API usada para enriquecer os dados. Crie uma conta e obtenha sua key.

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
    http://localhost:8009/
    ```

2. Faça login com as credenciais do superusuário que você criou anteriormente.
3. Clique em `Arquivos` no menu

    3.2 Adicione um arquivo cliando em `Adicionar arquivo`.

    3.3 Selecione o arquivo e o tipo e clique em `Salvar`. Você será redirecionado para a tela de listagem de arquivos.

4. Na tela de listagem clique em `Processar` para tratar e enriquecer os dados. Após concluir o processo você será direcionado para a tela com os dados enriquecidos.

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

## 🧪 Testes Unitários

Testes unitários são fundamentais para garantir que sua aplicação funciona conforme o esperado. Este projeto utiliza os testes integrados do Django para verificar funcionalidades essenciais.

### 1. Executar os Testes

Para rodar os testes unitários, utilize o seguinte comando:

```
docker-compose exec app python manage.py test
```
Este comando irá descobrir e executar todos os testes localizados nas pastas de cada aplicativo dentro do seu projeto Django.

### 2. Escrever Testes

Os testes estão localizados na pasta test/<nome_app>/. Para adicionar novos testes, siga as etapas abaixo:

- **Criar Arquivo de Testes:** Dentro da pasta `tests/`, crie uma pasta com o nome do aplicativo desejado caso
não exista e adicione os arquivos de testes dentro dele com prefixo `test_<nome_do_teste>.py`.


## 💡 Melhorias

### 1. **Implementação dos Testes unitários** 
Atualmente os testes não combrem todas as funcionalidades da aplicação.

### 2. **Automatização de Processos com Tarefas Assíncronas**
Utilizar ferramentas como Celery para automatizar tarefas demoradas, como processamento de grandes uploads de arquivos ou envio de e-mails, melhorando a performance e a responsividade da aplicação.

### 3. **Melhorias na Interface do Usuário (UI) e Experiência do Usuário (UX)**
Revisar e aprimorar o design da interface para torná-la mais intuitiva e atraente, melhorando a experiência geral do usuário.

### 4. **Internacionalização e Localização**
Implementar o suporte a múltiplos idiomas e adaptar a aplicação para diferentes regiões, melhorando a acessibilidade para uma audiência global.

### 5. **Implementação de Testes de Integração e End-to-End**
Além dos testes unitários, implementar testes de integração e end-to-end para garantir que diferentes partes do sistema funcionem bem juntas.

### 6. **Deploy Automatizado com CI/CD**
Configurar pipelines de integração e entrega contínuas (CI/CD) para automatizar o processo de deploy, testes e integração, garantindo lançamentos mais rápidos e confiáveis.

### 6. **Automatizar o processamento dos dados**
Atualmente temos que fazer o upload do arquivo para depois processar. Implementar o processamento logo após upload do arquivo deixa o processo automatizado para o usuário final.