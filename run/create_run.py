# from dotenv import dotenv_values
# config = dotenv_values("../.env")
# from openai import OpenAI
# client = OpenAI(api_key=config["api_key"])
#
# # Executes a run on a particular thread, allowing a conversation to take place between a user and assistant
# run = client.beta.threads.runs.create(
#     # ID of thread to run
#     thread_id="",
#     # ID of assistant to use for run
#     assistant_id="",
#     # For including file search result
#     include=[],
#     # Appends additional instructions at the end of the instructions for the run. Useful for modifying
#     # behaviour on a per run basis without overriding other instructions
#     additional_instructions=,
#     # adds additional messages to the thread before creating the run
#     additional_messages=,
#     # Overrides the instructions of the assistant, useful for modifying behaviour on a per run basis
#     instructions=,
#     max_completion_tokens=,
#     max_prompt_tokens=,
#     metadata={},
#     model=,
#     response_format=,
#     reasoning_effort=,
#     parallel_tool_calls=,
#     stream=,
#     temperature=,
#     tool_choice=,
#     tools=,
#     truncation_strategy=,
# )