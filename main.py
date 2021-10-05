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
# UTILITY ---------------------------------------=
# -----------------------------------------------=
def omit_empty_last_line(lst):
    """
    Remove n members of a list if they are at the end of the list and also empty
    """
    if lst[-1] == '':
        return omit_empty_last_line(lst[:-1])
    else:
        return lst

def limit_to_single_answer(completion):
  lines = completion.splitlines()

  limited_lines = []

  for line in lines:
    if not line.endswith("?"):
      limited_lines.append(line)
    else:
      break

  limited_lines = omit_empty_last_line(limited_lines)
  
  return "\n".join(limited_lines)

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
    full_response = completion.choices[0].text.lstrip()

    response = limit_to_single_answer(full_response)

    print(f"{prompt}\n")
    print(f"{response}")

    # print(f"**{prompt}**")
    # print(f"> {response}")

    output = {**params, 'prompt': prompt, 'response': response, full_response: 'full_response'}

    if write_to_completions_file:
        write_prompt_output_to_file(output)

    return output

# ================================================
# MAIN ===========================================
# ================================================
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
