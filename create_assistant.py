# Assistants can call models and use tools to perform tasks
# When you create an assistant you configure it with various settings, the only one required is the
# model the assistant will call.
from openai import OpenAI
from dotenv import dotenv_values
config = dotenv_values(".env")
# Instantiate the openai API
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

# create an assistant, returns an assistant object:
assistant = client.beta.assistants.create(
    name="Math tutor",
    model="gpt-4o-mini",
    instructions="You are a personal math tutor. Write and execute code to solve math problems."
)

# assistant object:
print(assistant)
