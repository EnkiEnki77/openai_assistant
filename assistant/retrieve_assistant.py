from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values("../.env")
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

retrieved_assistant = client.beta.assistants.retrieve(
    # ID of the assistant to retrieve
    assistant_id=""
)

# Assistant object of the specified assistant
print(retrieved_assistant)