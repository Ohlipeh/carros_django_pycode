# 🚗 Sistema de Gestão de Veículos (Django + IA + Google Cloud)

Aplicação web completa para gerenciamento e vitrine de veículos, desenvolvida em **Python** e **Django**, com geração automática de descrições comerciais via **Inteligência Artificial (OpenAI)** e hospedada em ambiente de produção no **Google Cloud Platform (GCP)**.

🔗 **Acesse o projeto online:** [http://104.196.253.242/cars/](http://104.196.253.242/cars/)

---

## 📸 Demonstração

<!-- Dica: Tire prints das telas principais, suba na pasta do projeto ou arraste direto na edição do README no GitHub e substitua os links abaixo -->
![Tela Inicial - Vitrine de Carros]<img width="847" height="1442" alt="Captura de tela 2026-11-25 184351" src="https://github.com/user-attachments/assets/93998ee6-bb9c-4ee3-b5a5-6160f4f711f7" />

![Detalhes do Veículo]<img width="849" height="1439" alt="Captura de tela 2026-11-25 184405" src="https://github.com/user-attachments/assets/0ab119fa-07f3-48e6-8f67-c34edc84a185" />


---

## ✨ Funcionalidades

* **CRUD Completo de Veículos:** Cadastro, listagem, visualização de detalhes, edição e exclusão de carros utilizando *Class-Based Views* (CBVs) do Django.
* **Descrições Automáticas com IA:** Integração com a API da OpenAI acionada via **Django Signals** para gerar anúncios comerciais atrativos automaticamente ao cadastrar um veículo.
* **Sistema de Autenticação:** Fluxo completo de cadastro de usuários, login, logout e proteção de rotas com senhas criptografadas.
* **Upload de Imagens:** Suporte ao envio e exibição de fotos dos veículos utilizando a biblioteca `Pillow`.
* **Painel Administrativo:** Gestão centralizada de dados e usuários através do Django Admin.

---

## 🛠️ Tecnologias e Infraestrutura

### Backend & Banco de Dados
* **Python 3** & **Django**
* **PostgreSQL** (`psycopg2`)
* **OpenAI API** (geração de textos comerciais)
* **Pillow** (processamento de imagens)
* **python-dotenv** (gerenciamento de variáveis de ambiente)

### Deploy & Produção (Cloud)
* **Google Cloud Platform (Compute Engine):** Máquina virtual Linux (Ubuntu LTS).
* **Gunicorn:** Servidor WSGI rodando como serviço em segundo plano (`systemd`).
* **Nginx:** Proxy reverso responsável por receber as requisições HTTP e servir arquivos estáticos (`static/`) e de mídia (`media/`).

---

## ⚙️ Como executar o projeto localmente

### Pré-requisitos
* Python 3.10+ instalado
* PostgreSQL instalado e rodando

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Ohlipeh/carros_django_pycode.git](https://github.com/Ohlipeh/carros_django_pycode.git)
   cd carros_django_pycode

