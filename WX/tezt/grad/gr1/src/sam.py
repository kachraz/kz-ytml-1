# ??????????????????????????????????????????????
# sam.py - Samova Chatbot test following the docs
# ??????????????????????????????????????????????

# --- Imports ---
import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from rich import print

from src.utz import header1

# --- Global Vars ---
load_dotenv("src/.ass")
SA_T = os.getenv("SAO")

# --- Main Function ---


def sam_main():
    # ass_print()
    sam_chat1()

# --- Sub Functions ---

# Print Ass


def ass_print():
    header1("Ass Stuff")
    print(SA_T)

# Actual Chat Test from example


def sam_chat1():
    header1("Sam Chat Test 1")

    client = OpenAI(
        base_url="https://api.sambanova.ai/v1",
        api_key=SA_T
    )

    def predict(message, history):
        history.append({"role": "user", "content": message})
        stream = client.chat.completions.create(
            model="Meta-Llama-3.2-1B-Instruct",
            messages=history,
            stream=True
        )
        chunks = []
        for chunk in stream:
            chunks.append(chunk.choices[0].delta.content or "")
            yield "".join(chunks)

    panty = gr.ChatInterface(
        predict,
        title="Samova Chatbot",
        description="Chat with Samova",
        type="messages",
        flagging_mode="manual",
    )

    panty.launch(
        show_error=True
    )
