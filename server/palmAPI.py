"""
$ pip install google-generativeai
"""
from dotenv import dotenv_values
import google.generativeai as palm

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

PALM_API_KEY = config["PALM_API_KEY"]
palm.configure(api_key=PALM_API_KEY)

defaults = {
    "model": "models/text-bison-001",
    "temperature": 1,
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


prompt = """Generate 8 points for a person whose business name is:{busName} and its description is:{desc}. If not enough information is available, make assumptions from your side. 
"""
prompt_output = """Your response shoulde be a json object with the following format: {"points": ["point1", "point2", "point3", "point4", "point5", "point6", "point7", "point8"]}
"""

""" sample output:

    type of response: <class 'dict'>

    point:- Samosewala is a food delivery service that delivers samosas to your doorstep.
    point:- It is a very popular service in New Delhi.
    point:- Our customers love our samosas.
    point:- Our samosas are made with the best ingredients.
    point:- We offer a variety of samosas, including vegetarian, meat, and seafood options.
    point:- We also offer a variety of sides, such as chutneys, salads, and naan.
    point:- We are committed to providing our customers with the best possible experience.
    point:- We are always looking for ways to improve our service, so please let us know if you have any feedback.
"""
