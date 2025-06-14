# ///////////////////////////////////////////////////////////////
# App.py- This app is prepared fro uploading
# ///////////////////////////////////////////////////////////////

# --- Imports Zone ---

import time

import gradio as gr

from src.mkd import in_txt2, txt2

# --- Vars ---

# Theme choser
themes = [
    gr.themes.Ocean(),
    gr.themes.Monochrome(),
    gr.themes.Citrus(),
    gr.themes.Glass(),
    gr.themes.Default(),
    gr.themes.Soft()
]
c_th = themes[5]

# -- Sub Functions ---

# Chat Interface function


def ch_in():

    # Chat interface Function Call
    def slow_echo(message, history):
        for i in range(len(message)):
            time.sleep(0.05)
            yield "SmellPanty: " + message[:i + 1]

    # Chat Interface Description
    gr.Markdown(txt2)

    # Building chat interface
    gr.ChatInterface(
        slow_echo,
        type="messages",
        flagging_mode="manual",
        flagging_options=["Good", "Bad", "Shit"],
        save_history=True,
        examples=[
            ["Hi", "Hello"],
            ["How are you?", "Good"],
            ["What's your name?", "My name is SmellPanty"],
        ],
    )


# --- Main Function ---


def panty():
    with gr.Blocks(
        theme=c_th
    ) as panty:

        with gr.Tab("Home"):
            gr.Markdown(in_txt2)

        with gr.Tab("ChatPanty"):
            ch_in()

    panty.launch(
        show_error=True
    )


if __name__ == "__main__":
    panty()
    print("BootySmells")
