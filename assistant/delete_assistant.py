from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values("../.env")
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

delete_assistant = client.beta.assistants.delete(
    # ID of the assistant to be deleted
    "assistant_id"
)

# deletion status object
print(delete_assistant)