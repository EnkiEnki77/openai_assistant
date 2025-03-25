# Object returned from the assistants.create SDK

assistant_obj = {
  # Assistant ID
  "id": "asst_abc123",
  # Object type which will always be "assistant"
  "object": "assistant",
  #   Unix time in seconds object was created
  "created_at": 1698984975,
  #   name of the assistant
  "name": "Math Tutor",
  #   The description of the assistant
  "description": None,
  #   Model the assistant uses
  "model": "gpt-4o",
  #   The system instructions the model uses.
  "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
  # tools enabled for the assistant
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  #   A list of resources required by the enabled tools
  "tool_resources": {},
  #   Used for storing additional info
  "metadata": {},
  #   An alt to sampling with temperature, called nucleus sampling, where the model considers the results
  #   of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top_p probability
  #   mass are considered
  "top_p": 1.0,
  #   What sampling temperature to use, between 0 and 2. Higher values will make the output more random.
  #   Lower values more focused and deterministic, if you set it to 0 the output from the model will be
  #   the same every time.
  "temperature": 1.0,
  #   Specifies the format the model must output in.
  "response_format": "auto"
}
