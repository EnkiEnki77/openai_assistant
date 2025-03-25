# Assistants can call models and use tools to perform tasks
# When you create an assistant you configure it with various settings, the only one required is the
# model the assistant will call.
from openai import OpenAI
from dotenv import dotenv_values
config = dotenv_values("../.env")
# Instantiate the openai API
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

# create an assistant, returns an assistant object:
assistant = client.beta.assistants.create(
    name="Math tutor",
    model="gpt-4o-mini",
    # Description of the assistant
    description="Math tutor",
    # System instructions the assistant uses, to guide it on how it should behave.
    instructions="You are a personal math tutor. Write and execute code to solve math problems.",
    metadata={},
    # Constrains effort on reasoning to low, medium, or high. lower reasoning effort can attribute to
    # faster responses and lower tokens used on reasoning response. Only for o-series models.
    reasoning_effort="high",
    # Defines format response should be in
    response_format="auto",
    # Sets how different each response is from the last, 0 means the model will give the same response
    # each time
    temperature=1,
    # defines what tools the assistant has access to
    tools=[
        {
            "type": "code_interpreter"
        },
        {
            "type": "file_search",
            # Overrides for the file search tool
            "file_search": {
                # Max number of results the file search tool should output
                "max_num_results": 10,
                # Ranking options for the file search
                "ranking_options": {
                    "score_threshold": 10,
                    "ranker": "auto"
                }
            }
        },
        {
            "type": "function",
            "function": {
                # Name of the function to call
                "name": "my_func",
                # Description of what the function does, used by the model to determine when to call it.
                "description": "prints to the terminal",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "Location of the vacation spot",
                        }
                    },
                    "required": ["location"],
                    "additionalProperties": False
                },
                # Defines whether model should strictly follow parameter schema when defining the function
                # call.
                "strict": True
            }
        }
    ],
    # Defines the resources for the tools
    tool_resources= {
        "code_interpreter": {
            # List of file object ID's the code interpreter tool should use
            "file_ids": []
        },
        "file_search": {
            "vector_store_ids": [],
            "vector_stores": []
        }
    },
    # Alternative to temperature, should choose one or the other.
    top_p=1.0
)

# assistant object:
print(assistant)
