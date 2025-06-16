# ?????????????????????????????????????????
# nb1.py - neby Test 1
# ?????????????????????????????????????????

# --- Imports Zone ---

import os

from dotenv import load_dotenv
from openai import OpenAI
from rich import print as rpr
from rich.pretty import pprint as ppr

from .utz import header1

# --- Global Vars ---
load_dotenv("src/.ass")
NB_T = os.getenv("NBY")

# --- Main Function ---


def nb1_main():
    # brint_env()
    nb_test1()


# --- Sub functions ---

# Printaz Envuiaza
def brint_env():
    header1("Ass Stuff")
    rpr(NB_T)

# API Tezta


def nb_test1():
    header1("NB1 Tezt")

    client = OpenAI(
        base_url="https://api.studio.nebius.com/v1",
        api_key=NB_T
    )

    modelz = [
        "meta-llama/Meta-Lama-3.1-8B-Instruct",
        "Qwen/Qwen2.5-Coder-7B"
    ]

    completion = client.chat.completions.create(
        model=modelz[1],
        messages=[
            {
                "role": "user",
                "content": "Describe booty dancing"
            }
        ],
        temperature=0.5
    )

    ppr(completion.to_json, expand_all=True)
