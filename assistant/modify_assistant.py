from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values("../.env")
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

updated_assistant = client.beta.assistants.update(
    # ID of the assistant to modify
    "",
#     update any of the assistants properties youd like to update
    name="cunt",
    instructions="eat more cunt"
)

# The newly updated assistant object
print(updated_assistant)