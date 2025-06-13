# ????????????????????????????????????????????????????????????
# gm1 - GithubMl Test1
# ????????????????????????????????????????????????????????????

# --- Imports Zone ---
import os

from dotenv import load_dotenv
from openai import OpenAI
from rich.pretty import pprint as ppr

from .utz import header1
from .wm import save_to_markdown

# -- Globsl Vars

# --- Load the envpussy --
load_dotenv("src/.pussy")
GH_T = os.getenv("GHT")

# -- Main Function Call --


def gm1_main():
    # print_env()  # Testing env access
    gm1_1()  # Run the official example test

# --- SubFunc---

# Test ENV Access


def print_env():
    header1("Brint ENV")
    ppr(f"GiGaand = {GH_T}")

# Official Example Test


def gm1_1():

    header1("Official Example Test")

    endpoint = "https://models.github.ai/inference"
    model = "openai/gpt-4.1"

    client = OpenAI(
        base_url=endpoint,
        api_key=GH_T,
    )

    question = "What is smellpanty algoritm ?"

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant, who talks like in rhyming slang",
            },
            {
                "role": "user",
                "content": question,
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    # Print Console Output
    ppr(response.choices[0].message.content)

    # Save to Markdown
    save_to_markdown(
        response.choices[0].message.content,
        prefix="gm1_test",
        directory="rez/",
        header_level=2,
        include_time_in_filename=True,
        metadata={
            "Model": model,
            "Endpoint": endpoint,
            "Question": question
        }
    )
