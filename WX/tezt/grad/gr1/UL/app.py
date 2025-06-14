# ///////////////////////////////////////////////////////////////
# App.py- This app is prepared fro uploading
# ///////////////////////////////////////////////////////////////

# --- Imports Zone ---

import time

import gradio as gr

from src.mkd import in_txt2

# --- Vars ---

# -- Sub Functions ---


def ch_in():
    # Intro tab
    def intro_section():
        gr.Markdown(in_txt2)

    # Chat Interface function
    def ch_in():

        def slow_echo(message, history):
            for i in range(len(message)):
                time.sleep(0.05)
                yield "SmellPanty: " + message[:i + 1]

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


def main():
    pass


if __name__ == "__main__":
    main()
