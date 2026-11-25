# Sistema de Gestão de Veículos

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

Aplicação web full-stack para gerenciamento e vitrine de veículos, construída com **Python** e **Django**. O sistema conta com geração automatizada de descrições comerciais via **OpenAI API** (acionada por *Django Signals*) e está implantado em ambiente de produção no **Google Cloud Platform (GCP)**.

> **Ambiente de Produção (Online):** [http://104.196.253.242/cars/](http://104.196.253.242/cars/)

---

## Interface

![Tela Inicial - Vitrine de Carros]<img width="847" height="1442" alt="Captura de tela 2026-11-25 184351" src="https://github.com/user-attachments/assets/93998ee6-bb9c-4ee3-b5a5-6160f4f711f7" />

![Detalhes do Veículo]<img width="849" height="1439" alt="Captura de tela 2026-11-25 184405" src="https://github.com/user-attachments/assets/0ab119fa-07f3-48e6-8f67-c34edc84a185" />


---

## Funcionalidades

* **Gestão de Veículos (CRUD):** Cadastro, listagem, detalhamento, atualização e exclusão de registros estruturados com *Class-Based Views* (CBVs).
* **Automação com IA:** Integração com a API da OpenAI disparada via *Django Signals* para gerar descrições comerciais padronizadas no momento do cadastro.
* **Autenticação e Controle de Acesso:** Registro de usuários, login, logout e gerenciamento de sessões com criptografia nativa do Django.
* **Gestão de Mídia:** Upload, armazenamento e exibição de imagens dos veículos utilizando `Pillow`.
* **Painel Administrativo:** Administração centralizada de inventário e usuários via Django Admin.

---

## Arquitetura e Tecnologias

| Camada | Tecnologia | Função no Projeto |
| :--- | :--- | :--- |
| **Backend** | Python / Django | Regras de negócio, ORM, rotas, CBVs e Signals |
| **Banco de Dados** | PostgreSQL (`psycopg2`) | Persistência relacional dos dados em produção |
| **Inteligência Artificial** | OpenAI API | Geração automatizada de textos comerciais |
| **Servidor de Aplicação** | Gunicorn (`systemd`) | Servidor WSGI rodando como serviço em segundo plano |
| **Servidor Web** | Nginx | Proxy reverso e entrega de arquivos estáticos e de mídia |
| **Infraestrutura** | Google Cloud (Compute Engine) | Máquina virtual Linux (Ubuntu LTS) |

---

## ⚙️ Como executar o projeto localmente

### Pré-requisitos
* Python 3.10+
* PostgreSQL instalado e em execução

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Ohlipeh/carros_django_pycode.git
   cd carros_django_pycode
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   SENHA_BD=sua_senha_do_postgres
   OPENAI_API_KEY=sua_chave_da_openai
   ```

5. **Execute as migrações:**
   *(Certifique-se de que o banco de dados `carros` já foi criado no PostgreSQL)*
   ```bash
   python manage.py migrate
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```
   A aplicação estará disponível em `[http://127.0.0.1:8000/cars/](http://127.0.0.1:8000/cars/)`.

---

## Autor

**André Felipe**  
[![GitHub](https://img.shields.io/badge/GitHub-Ohlipeh-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ohlipeh)

