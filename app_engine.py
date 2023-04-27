import os
import openai
from similarity import get_similar_context

openai.api_key = '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'

# query = input()
# context = (get_similar_context(query)).strip()
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
# prompt_input_u = f'{context}'


def func(value):
    return ''.join(value.splitlines())




def get_response(prompt_input):
    response = openai.Completion.create(
    model="text-davinci-003",
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

    while True:
        query = input().replace('CSI', 'corporate strategy and implementation in aaruush').replace('ORM', 'Operations and Resource Management in aaruush').replace('PR', 'Public Relations in aaruush')
        context = (get_similar_context(query)).strip()
        prompt_input_u = f'{context}'
        query_f = ((func(prompt_input_u)).strip())
        # print(query)
        print(get_response(((query_f + f'\n\nQ:{query}?\n\nA:'))))

