# ///////////////////////////////////////////////////////////////
# App.py- This app is prepared fro uploading
# ///////////////////////////////////////////////////////////////

# --- Imports Zone ---

import time

import gradio as gr

# --- Vars ---

# -- Sub Functions ---

# Chat Interface function


def ch_in():
    def slow_echo(message, history):
        for i in range(len(message)):
            time.sleep(0.05)
            yield "SmellPanty: " + message[:i + 1]
    gr.Markdown("Hello")
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
    with gr.Blocks() as panty:

        with gr.Tab("Panty"):
            ch_in()

    panty.launch(
        show_error=True
    )


if __name__ == "__main__":
    main()
