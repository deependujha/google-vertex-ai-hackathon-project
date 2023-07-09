"""
$ pip install google-generativeai
"""
from dotenv import dotenv_values
import pprint
import google.generativeai as palm

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

PALM_API_KEY = config["PALM_API_KEY"]
palm.configure(api_key=PALM_API_KEY)

defaults = {
    "model": "models/text-bison-001",
    "temperature": 0.7,
    "candidate_count": 1,
    "top_k": 40,
    "top_p": 0.95,
    "max_output_tokens": 1024,
    "stop_sequences": [],
    "safety_settings": [
        {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
        {"category": "HARM_CATEGORY_TOXICITY", "threshold": 1},
        {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
        {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
        {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2},
    ],
}


# method to generate text from prompt using palm API
def get_response_from_palmAPI(prompt):
    response = palm.generate_text(**defaults, prompt=prompt)
    return response.result


prompt = "What is the meaning of life?"

print(get_response_from_palmAPI(prompt))
