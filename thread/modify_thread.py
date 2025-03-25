from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values("../.env")
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

assistant = client.beta.assistants.create(
    name="Math tutor",
    model="gpt-4o-mini",
    instructions="You are a personal math tutor. Write and execute code to solve math problems."
)

thread = client.beta.threads.update(
    # ID of the thread to update
    "thread_id",
    # Set new values for thread properties below:
)

# updated thread object
print(thread)