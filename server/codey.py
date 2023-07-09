"""
$ pip install google-cloud-aiplatform
"""

import vertexai
from vertexai.preview.language_models import CodeGenerationModel

vertexai.init(project="vertexai-hackathon-392118", location="us-central1")

parameters = {"temperature": 0.2, "max_output_tokens": 1024}

model = CodeGenerationModel.from_pretrained("code-bison@001")

response = model.predict(
    prefix="""write a function that takes a list of integers and returns the sum of the list in python
    .""",
    **parameters,
)

print(f"Response from Model: {response.text}")
