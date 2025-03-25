# Creating a message
from openai import OpenAI
from dotenv import dotenv_values
config = dotenv_values("../.env")
# Instantiate the openai API
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

message = client.beta.threads.messages.create(
    # ID of the thread to create a message for
    "thread_id",
    # Content of the message
    content= "blah",
    # Role of the entity creating the message, either user or assistant
    role="user",
    # Files attached to the message, and tools they should be added to
    attachments=[],
    metadata={}
)

# message object:
print(message)
