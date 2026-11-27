# Import os
import os

# Import .env
from dotenv import load_dotenv

# Import Open Ai
from openai import OpenAI

# Call dotenv
load_dotenv()

# Key OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Create function for prompt.
def get_car_ai_bio(model, brand, year):
    prompt = f"""
    Crie um anúncio de venda para {brand} {model} {year}.
    Use linguagem comercial, natural e atrativa.
    Destaque características relevantes do veículo.
    Não invente especificações.
    Máximo de 200 caracteres.
    """
    # try case the error.
    try:
        response = client.responses.create(
            model="gpt-6-luna", input=prompt, max_output_tokens=150
        )

        descricao = response.output_text.strip()
        return descricao[:200]
    except Exception:
        return f"{brand} {model} {year} in excelent estate. Comi in cotact for more details."
