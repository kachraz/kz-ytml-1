# ????????????????????????????????????????????????????????????
# gtm.py - Get all github models
# ????????????????????????????????????????????????????????????

# --- Imports Zone ---

# -- Globsl Vars

# --- Load the envpussy --
import os

import httpx
from dotenv import load_dotenv

from .utz import header1
from .wm import save_to_markdown

load_dotenv("src/.pussy")
GH_T = os.getenv("GHT")

# -- Main Function Call --


def gm1_main():
    get_models_1()

# --- SubFunc---


def get_models_1():

    header1("fetch GitHUb Models")

    url = "https://api.github.com/catalog/models"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GH_T}"
    }

    with httpx.Client() as client:
        response = client.get(url, headers=headers)

    # Print status code and response JSON
    print(f"Status Code: {response.status_code}")
    try:
        print(response.json())

        # Write to markdown file
        save_to_markdown(
            response.json(),
            prefix="gm1_test",
            directory="rez/",
            header_level=2,
            include_time_in_filename=True,
        )

    except Exception:
        print("Failed to decode JSON")
        print(response.text)
