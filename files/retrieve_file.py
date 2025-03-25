# Retrieves file object of a certain ID

from dotenv import  dotenv_values
from openai import  OpenAI

config = dotenv_values("../.env")

client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

retrieve_file = client.files.retrieve(
    # ID of file to retrieve
    "file_id"
)

# File object retrieved
print(retrieve_file)