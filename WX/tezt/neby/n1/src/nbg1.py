# ?????????????????????????????????????????
# nbg1.py - Running Neby wih gradio
# ?????????????????????????????????????????

# --- Imports Zone ---

import os

import gradio as gr
from dotenv import load_dotenv
from rich import print as rpr

from .utz import header1

# --- Global Vars ---
load_dotenv("src/.ass")
NB_T = os.getenv("NBY")

modelz = [
    "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "Qwen/Qwen2.5-Coder-7B"
]

themes = [
    gr.themes.Ocean(),
    gr.themes.Monochrome(),
    gr.themes.Citrus(),
    gr.themes.Glass(),
    gr.themes.Default(),
    gr.themes.Soft()
]
c_th = themes[5]

# Styling Css
czz = """ 
.gradio-container {background: url(https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTJ4b21tZ3hxdmQwYzVuejU1cnZ3dXZkc3hwYnJwdDhmcjlxbWY1MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7b8jdNUoFBdcoILjjv/giphy.gif); background-attachment: fixed; background-repeat: no-repeat; background-size: cover; background-position: center;} 
"""

# --- Main Function ---


def nbg1_main():
    # brint_env()
    # nb_test1()
    nb_hf_1()


# --- Sub functions ---

# Printaz Envuiaza
def brint_env():
    header1("Ass Stuff")
    rpr(NB_T)

# Gradio Test 1 - Taken from
