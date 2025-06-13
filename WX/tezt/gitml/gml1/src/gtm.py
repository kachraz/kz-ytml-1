# ????????????????????????????????????????????????????????????
# gtm.py - Get all github models
# ????????????????????????????????????????????????????????????

# --- Imports Zone ---
import json
import os

import httpx
from dotenv import load_dotenv
from rich.pretty import pprint as ppr

from .utz import header1
from .wm import save_to_markdown

# --- Load the envpussy --
load_dotenv("src/.pussy")
GH_T = os.getenv("GHT")

# --- Models List ---
model_ids = [
    "openai/gpt-4.1",
    "openai/gpt-4.1-mini",
    "openai/gpt-4.1-nano",
    "openai/gpt-4o",
    "openai/gpt-4o-mini",
    "openai/o1",
    "openai/o1-mini",
    "openai/o1-preview",
    "openai/o3",
    "openai/o3-mini",
    "openai/o4-mini",
    "openai/text-embedding-3-large",
    "openai/text-embedding-3-small",
    "ai21-labs/ai21-jamba-1.5-large",
    "ai21-labs/ai21-jamba-1.5-mini",
    "cohere/cohere-command-a",
    "cohere/cohere-command-r",
    "cohere/cohere-command-r-08-2024",
    "cohere/cohere-command-r-plus",
    "cohere/cohere-command-r-plus-08-2024",
    "cohere/cohere-embed-v3-english",
    "cohere/cohere-embed-v3-multilingual",
    "core42/jais-30b-chat",
    "deepseek/deepseek-r1",
    "deepseek/deepseek-r1-0528",
    "deepseek/deepseek-v3-0324",
    "meta/llama-3.2-11b-vision-instruct",
    "meta/llama-3.2-90b-vision-instruct",
    "meta/llama-3.3-70b-instruct",
    "meta/llama-4-maverick-17b-128e-instruct-fp8",
    "meta/llama-4-scout-17b-16e-instruct",
    "meta/meta-llama-3.1-405b-instruct",
    "meta/meta-llama-3.1-70b-instruct",
    "meta/meta-llama-3.1-8b-instruct",
    "meta/meta-llama-3-70b-instruct",
    "meta/meta-llama-3-8b-instruct",
    "mistral-ai/codestral-2501",
    "mistral-ai/ministral-3b",
    "mistral-ai/mistral-large-2411",
    "mistral-ai/mistral-medium-2505",
    "mistral-ai/mistral-nemo",
    "mistral-ai/mistral-small-2503",
    "xai/grok-3",
    "xai/grok-3-mini",
    "microsoft/mai-ds-r1",
    "microsoft/phi-3.5-mini-instruct",
    "microsoft/phi-3.5-moe-instruct",
    "microsoft/phi-3.5-vision-instruct",
    "microsoft/phi-3-medium-128k-instruct",
    "microsoft/phi-3-medium-4k-instruct",
    "microsoft/phi-3-mini-128k-instruct",
    "microsoft/phi-3-mini-4k-instruct",
    "microsoft/phi-3-small-128k-instruct",
    "microsoft/phi-3-small-8k-instruct",
    "microsoft/phi-4",
    "microsoft/phi-4-mini-instruct",
    "microsoft/phi-4-mini-reasoning",
    "microsoft/phi-4-multimodal-instruct",
    "microsoft/phi-4-reasoning"
]

# -- Main Function Call --


def gm1_main():
    get_models_1()

# --- SubFunc---


def get_models_1():

    header1("fetch GitHUb Models")

    url = "https://models.github.ai/catalog/models"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GH_T}"
    }

    with httpx.Client() as client:
        response = client.get(url, headers=headers)

    # Print status code and response JSON
    print(f"Status Code: {response.status_code}")
    try:
        ppr(response.json())
        formatted_output = json.dumps(
            response.json(), indent=2, ensure_ascii=False)

        # Write to markdown file
        save_to_markdown(
            content=f"```json\n{formatted_output}\n```",
            prefix="gitmodelz",
            directory="rez/",
            header_level=2,
            include_time_in_filename=True,
        )

    except Exception:
        print("Failed to decode JSON")
        print(response.text)
