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
    # res=get_response(query_f)
    # print(res)
    print(query_f)

# with open('file.txt','r+') as f:
#     f.write(query_f)
#     f.close()

# with open('file.txt','r+') as f:
#     k = f.read()
#     print(k)
#     # res = get_response(k)
#     # print(res)
#     print(k)
#     f.close()
