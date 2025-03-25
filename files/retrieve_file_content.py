# Retrieves content of file object of a certain ID

from dotenv import  dotenv_values
from openai import  OpenAI

config = dotenv_values("../.env")

client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

retrieve_file_content = client.files.content(
    # ID of file to retrieve content from
    "file_id"
)

# content of file
print(retrieve_file_content)