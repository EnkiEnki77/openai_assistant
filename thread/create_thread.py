from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values("../.env")
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

assistant = client.beta.assistants.create(
    name="Math tutor",
    model="gpt-4o-mini",
    instructions="You are a personal math tutor. Write and execute code to solve math problems."
)

thread = client.beta.threads.create(
    # List of messages to start the thread with
    messages=[
        {
            # Indicates the role of the entity creating the message. Thread messages will either
            # be user generated or assistant generated. So the role will be user or assistant.
            "role": "user or assistant",
            # The content of the message, can either be a string or an array of content parts with a defined
            # type, text content will have a type of text. Image content a type of image_url or image_file
            # images are only supported for vision compatible models
            "content": "",
            # A list of files attached to the message, and the tools they should be added to
            "attachments": [
                {
                    # ID of the file to attach to the message
                    "file_id": "",
                    # Tools to attach the file to
                    "tools": [
                        {"type": "code_interpreter"},
                        {"type": "file_search"},
                    ]
                }
            ],
            # Stores additional metadata about the message
            "metadata": {}
        }
    ],
    # Additional meta-data for the object
    metadata={},
    # Tool resources for the assistants tools in this thread
    tool_resources={},
)

# thread object
print(thread)