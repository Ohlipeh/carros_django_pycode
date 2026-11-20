import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_car_ai_bio(model, brand, year):
    prompt = f"""
    Crie um anúncio de venda para {brand} {model} {year}.
    Use linguagem comercial, natural e atrativa.
    Destaque características relevantes do veículo.
    Não invente especificações.
    Máximo de 200 caracteres.
    """

    response = client.responses.create(
        model="gpt-6-luna", input=prompt, max_output_tokens=150
    )

    descricao = response.output_text.strip()
    return descricao[:200]
