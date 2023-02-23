import os
import openai
from similarity import get_similar_context

openai.api_key = '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'

query = input()
context = (get_similar_context(query)).strip()
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
prompt_input_u = f'{context}'


def func(value):
    return ''.join(value.splitlines())

query_f = ((func(prompt_input_u)).strip())


def get_response(prompt_input):
    response = openai.Completion.create(
    model="curie-instruct-beta",
    prompt= prompt_input,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
    )

    return (((response.get('choices'))[0]).get('text'))
   
    

if __name__=='__main__':
    print(get_response(((query_f + f'\n\nQ:{query}?\n\nA:'))))

