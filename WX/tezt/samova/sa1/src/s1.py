# ????????????????????????????????????????????????????????????????????????????????
# Vesion 1 of testing the samnov
# ????????????????????????????????????????????????????????????????????????????????

# --- Imports ---

import os

import httpx
from dotenv import load_dotenv
from openai import OpenAI
from rich import print as rpr
from rich.pretty import pprint

from .utz import header1
from .wm import save_to_markdown

# --- Load the envpussy --
load_dotenv("src/.env")
SA_T = os.getenv("SAO")

# --- Main File Function ---


def s1_file():
    # print_envz()
    get_modelz()

# === Sub Functions ===

# Function to get the env file


def print_envz():
    header1("Get Env")
    rpr(f"[green]SA_T: {SA_T}[/green]")

# Test chat function 1 get all models from the API


def get_modelz():
    header1("Quickstart Code from Docs")

    # Define the API endpoint
    url = "https://api.sambanova.ai/v1/models"

    # Make a synchronous GET request
    with httpx.Client() as client:
        resp = client.get(url)

        # Check if the request succeeded
        if resp.status_code == 200:
            model_names = [model["id"] for model in resp.json()["data"]]
            pprint(model_names)  # Parse JSON resp
            save_to_markdown(
                model_names,
                prefix="model_names",
                directory="rez"
            )
        else:
            rpr(f"Error: {resp.status_code}")
            rpr(resp.text)  # Print raw response if error


# Testing model output , from smbanova the cheapest one is Meta-Llama-3.2-3B-Instruct

def test_model_output():
    header1("Test Model Output - Cheapest one is Meta-Llama-3.2-3B-Instruct")

    client = OpenAI(
        base_url="https://api.sambanova.ai/v1",
        api_key="<YOUR API KEY>"
    )

    modelz = [
        "Meta-Llama-3.2-3B-Instruct"
    ]

    prompt =

    completion = client.chat.completions.create(
        model=[modelz[0]],
        messages=[
            {"role": "system", "content": "Answer the question in a couple sentences."},
            {"role": "user", "content": "Share a happy story with me"}
        ]
    )

    print(completion.choices[0].message.content)
