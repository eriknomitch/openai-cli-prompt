import os
import json
import sys
import openai
from pprint import pprint

from ipdb import set_trace
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# - davinci
# - davinci-codex
# - davinci-instruct-beta
engines = openai.Engine.list()

working_params = dict(
    engine="davinci-instruct-beta",
    max_tokens=100,
    temperature=0.5,
    top_p=1,
    # stop=[],
    presence_penalty=0,
    frequency_penalty=0.4,
    best_of=1
    # logit_bias=None
)

def process_prompt(params, prompt):
    completion = openai.Completion.create(**{**params, 'prompt': prompt})
    response = completion.choices[0].text.lstrip()

    print(f"**{prompt}**")
    print(f"> {response}")

    return {**params, 'prompt': 'prompt', 'response': response}



# PROMPT = """Explain the moon landing to a 6 year old in a few sentences."""
# PROMPT = """Explain what Bitcoin is and how it relates to the blockchain."""
# PROMPT = """Why is the sky blue?"""
# PROMPT = """How much wood could a woodchuck chuck if a woodchuck could chuck wood?"""
# PROMPT = """How many three-point field goals did Michael Jordan make in 1992 and 1993 combined?"""
# PROMPT = "What's the answer to this riddle: A clerk at a butcher shop stands five feet ten inches tall and wears size 13 sneakers. What does he weigh?"
# PROMPT = "What's the answer to this riddle: What language does a billboard speak?"
# PROMPT = "Can God create a boulder so heavy that even he cannot lift it?"
# PROMPT = "Have you ever had a dream that you, um, you had, your, you- you could, you’ll do, you- you wants, you, you could do so, you- you’ll do, you could- you, you want, you want them to do you so much you could do anything?"
# PROMPT = "Does a photon experience time? If not, why?"
PROMPT = "Does a photon experience time? If not, why?"


output = process_prompt(working_params, PROMPT)

pprint(output)

