# ?????????????????????????????????????????
# nb1.py - neby Test 1
# ?????????????????????????????????????????

# --- Imports Zone ---

import os

from dotenv import load_dotenv
from openai import OpenAI
from rich import print as rpr

from .utz import header1

# --- Global Vars ---
load_dotenv("src/.ass")
NB_T = os.getenv("NBY")

# --- Main Function ---


def nb1_main():
    brint_env()


# --- Sub functions ---

# Printaz Envuiaza
def brint_env():
    header1("Ass Stuff")
    rpr(NB_T)

# API Tezta


def nb_test1():
    header1("NB1 Tezt")

    client = OpenAI(
        base_url="https://api.sambanova.ai/v1",
        api_key=NB_T
    )

    completion = client.chat.completions.create(
        model="Meta-Llama-3.2-1B-Instruct",
        messages=[
            {"role": "user", "content": "Describe booty dancing"}
        ],
        temperature=0.5
    )
