k = {
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": 'null',
      "text": "abcd"
    }
  ],
  "created": 1677081353,
  "id": "cmpl-6mllB1vFQlopMK58xdkOqGAHaBWRd",
  "model": "curie-instruct-beta",
  "object": "text_completion",
  "usage": {
    "prompt_tokens": 1,
    "total_tokens": 1
  }
}

v = (((k.get('choices'))[0]).get('text'))

print(v)
