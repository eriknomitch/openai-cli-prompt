import os
import json
import sys
import openai
import hashlib
import argparse

from datetime import datetime
from pprint import pprint
from ipdb import set_trace
from dotenv import load_dotenv

# Local
from config import params

# -----------------------------------------------=
# -----------------------------------------------=
# -----------------------------------------------=
def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def write_prompt_output_to_file(output):
    # filename = f"{hash_string(json.dumps(output))}.json"
    # datetime_string = datetime.now().isoformat('_', 'seconds')
    datetime_string = datetime.now().isoformat('_')

    filename = f"{datetime_string}.json"
    with open(f"completions/{filename}", 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)

def process_prompt(params, prompt, write_to_completions_file=True):
    completion = openai.Completion.create(**{**params, 'prompt': prompt})
    response = completion.choices[0].text.lstrip()

    print(f"{prompt}\n")
    print(f"{response}")

    # print(f"**{prompt}**")
    # print(f"> {response}")

    output = {**params, 'prompt': prompt, 'response': response}

    if write_to_completions_file:
        write_prompt_output_to_file(output)

    return output

# -----------------------------------------------=
# -----------------------------------------------=
# -----------------------------------------------=
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("prompt", help="Prompt", type=str)
args = parser.parse_args()

# pprint(params)

if not args.prompt:
    # print('\n' * 2)
    prompt = input("Prompt: ")
else:
    prompt = args.prompt

# print('\n' * 2)

process_prompt(params, prompt)
