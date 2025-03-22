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