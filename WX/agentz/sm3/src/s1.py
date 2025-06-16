# ??????????????????????????????????????????????????????????????????????????????????
# s1.py - Intial tests with smolagents based on the docs
# ??????????????????????????????????????????????????????????????????????????????????

# --- Imports ---

import os

from dotenv import load_dotenv
from rich.pretty import pprint as ppr
from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel

from .utz import header1

# --- Global Vars ---
load_dotenv("src/.ass")
NB_T = os.getenv("NBY")
SA_T = os.getenv("SAO")
os.environ['SAMBANOVA_API_KEY'] = SA_T

env_list = [NB_T, SA_T]


# --- mainFunc ---


def s1_main():
    # hf1()
    # hf2()
    hf3()


# --- SubFunc ---

# BrintaEnv
def brint_env():
    header1("BrintaEnv")
    ppr(env_list, expand_all=True)


# HF Example 1

def hf1():
    header1("HF Main Example1")

    model = InferenceClientModel(

    )
    agent = CodeAgent(
        tools=[],
        model=model,
    )

    result = agent.run("What is BootyDance?")
    ppr(result)

# Execute smolgens with litellm


def hf2():
    header1("HF LiteLLM Example")

    modelz = [
        "sambanova/Meta-Llama-3.2-3B-Instruct"
    ]

    model = LiteLLMModel(
        modelid=modelz[0],
        api_base="https://api.sambanova.ai/v1",
        apikey=SA_T,
        temperature=0.6,
        max_tokens=1000,
    )

    agent = CodeAgent(
        model=model,
        tools=[],
        add_base_tools=True
    )

    agent.run("What is BootyDance? and BootyCandy?")


def hf3():
    header1("HF LiteLLm Direct Example")

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "nWhat is BootyDance? and BootyCandy?"
                }
            ]
        }
    ]

    model = LiteLLMModel(
        modelid="sambanova/Meta-Llama-3.2-3B-Instruct",
        api_base="https://api.sambanova.ai/v1",
        apikey=SA_T,
        temperature=0.6,
        max_tokens=1000
    )

    # agent = CodeAgent(
    #     model=model,
    #     tools=[],
    #     add_base_tools=True
    # )

    # agent.run(messages)
    ppr(model(messages))
