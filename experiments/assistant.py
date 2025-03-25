# 1. Create assistant by defining it's custom instructions and picking a model. Optionally can
# add files and enable tools like code interpreter, file search, and call functions
from openai import OpenAI
from dotenv import dotenv_values
config = dotenv_values("../.env")
client = OpenAI(api_key=config.get("OPENAI_API_KEY"), base_url=config.get("BASE_URL"))

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o-mini"
)

# 2. Create a thread when a user starts a conversation with assistant
thread = client.beta.threads.create()

# 3. Add message object to the thread as the user asks questions. Can contain text, files, images, etc.
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# 4. Run the assistant on the thread to generate a response by calling the model and tools. Response
#    will be added to the thread as an assistant message.

#    Runs are asynchronous, and there are two ways you can go about handling them. Either through streams
#    or by monitoring the status of the run object through polling until a terminal status is reached.

# For the latter, we have the create_and_poll sdk. It creates a run and then polls for its completion.






