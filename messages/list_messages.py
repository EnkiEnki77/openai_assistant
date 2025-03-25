# List of messages
from openai import OpenAI
from dotenv import dotenv_values
config = dotenv_values("../.env")
# Instantiate the openai API
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

message_list = client.beta.threads.messages.list(
    # ID of the thread messages belong to
    "thread_id",
    # Content of the message
    after="blah",
    before="blah",
    limit=1,
    order="desc",
    # Filter messages by the run id that generated them
    run_id="blah"
)

# message list object:
print(message_list)