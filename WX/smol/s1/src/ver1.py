# ================================================
# s1.py -= version 1 of the work - following tutorial
# ================================================

import os

from dotenv import load_dotenv
from rich import print as rprint

from .utz import header1

# === Get Env ===
load_dotenv("src/.env")
hf_token = os.getenv("HF")


# === Main File Entry Funvtion===


def ver1_main():
    env_print()

# === Sun functions ===

# --- test print function of the env ---


def env_print():
    header1("Env Print")
    rprint(hf_token)
