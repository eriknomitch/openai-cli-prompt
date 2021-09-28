# openai-cli-prompt

Simple CLI prompt for easy I/O with OpenAI's API

## Quickstart

Configure the `working_params` in `main.py`.

```Shell
# Install dependencies
$ pipenv install

# Start the prompt
$ pipenv run python main.py

Prompt: Explain what Bitcoin is and how it relates to the blockchain.
> Bitcoin is a digital cryptocurrency that is not backed by any government or central bank. It is used to purchase goods and services, and has a fluctuating value based off of supply and demand. The blockchain is the technology that powers Bitcoin. The blockchain is a decentralized ledger that records all transactions without the need for banks or other intermediaries.
```

Each completion will save JSON in `completions/` with the parameters, prompt, and completion of the completion.

_Example_

```Json
{
    "engine": "davinci-instruct-beta",
    "max_tokens": 200,
    "temperature": 0.5,
    "top_p": 1,
    "presence_penalty": 0,
    "frequency_penalty": 0.4,
    "best_of": 1,
    "prompt": "Explain what Bitcoin is and how it relates to the blockchain.",
    "response": "Bitcoin is a digital cryptocurrency that is not backed by any government or central bank. It is used to purchase goods and services, and has a fluctuating value based off of supply and demand. The blockchain is the technology that powers Bitcoin. The blockchain is a decentralized ledger that records all transactions without the need for banks or other intermediaries."
}
```
