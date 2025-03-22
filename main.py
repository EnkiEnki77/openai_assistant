# The assistants API allows you to AI assistants in your applications.

# An assistant has instructions and can leverage models, tools, and files to respond to user queries.

# It currently supports three kinds of tools: Code interpreter, file search, and function calling.


# Assistants can do things such as:
# 1. call openai's models with specific instructions to tune their personality and capabilities
# 2. can access multiple tools in parallel. openai's builtin tools such as code interpreter and file search
#    or tools you build via function calling
# 3. can access persistent threads. threads simplify ai app development, by storing message history and
#    truncating it when the conversation gets too long for the models content length. You create a thread
#    once and append messages to it as your users reply.
# 4. can access files in several formats. either as part of their creation, or part of threads between
#    assistants and users. When using tools, assistants can also create files, and site files they reference
#    in the messages they create.

# Assistants are purpose built AI that use openai's models and calls tools

# Threads are a conversation session between an assistant and a user. Threads store messages and automatically
# handle truncation to fit content into a model's context.

# Messages are created by an assistant or user. They can include text, images, or other files, and are
# stored as a list on the thread.

# A run is an invocation of the assistant on a thread in response to a users message. The assistant uses
# its configuration and the messages on the thread to perform tasks by calling models and tools. As part
# of the run the assistant appends a message to the thread in response to a user message

# Run Step is a detailed list of steps an assistant took as part of it's run.



from openai import OpenAI, AssistantEventHandler
from typing_extensions import  override
# Instantiate client
client = OpenAI()

# Initialize assistant. Needs a name, it's instructions, tools it can use, and model to use.
assistant = client.beta.assistants.create(
    name="Math tutor",
    instructions="You are a math tutor. Write and run code to solve math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o-mini"
)

# Initialize a thread for the user and assistant to store their conversation
thread = client.beta.threads.create()

# Add a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What's 2 * 8 + 4?"
)



# Once all the user messages have been added to the thread you can Run the thread with any assistant.
# Creating a run uses the model and tools associated with the assistant to generate a response. Those
# responses are then added to the thread as assistant responses.

# You can create a run either with or without streaming. Runs are asynchronous and streams are a way
# to handle asynchronous functions without having to use callbacks or low level protocols

# With streaming you can use the create and stream helpers in the Python SDK to create a run and stream
# the response.


# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.

class EventHandler(AssistantEventHandler):
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)

    @override
    def on_text_delta(self, delta, snapshot):
        print(delta.value, end="", flush=True)

    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end="", flush=True)
            if delta.code_interpreter.outputs:
                print(f"\n\noutput >", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        print(f"\n{output.logs}", flush=True)


# Then we use the stream SDK helper with the EventHandler class to create the run and stream the response
with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Refer to the user as John Doe.",
    event_handler=EventHandler(),
) as stream:
    stream.until_done()

