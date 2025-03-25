# The object returned from the list method of the assistants sdk

list_assistant_obj = {
  #   object type which will always be list
  "object": "list",
  #   the list of assistants that have been created
  "data": [
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1698982736,
      "name": "Coding Tutor",
      "description": None,
      "model": "gpt-4o",
      "instructions": "You are a helpful assistant designed to make me better at coding!",
      "tools": [],
      "tool_resources": {},
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    },
    {
      "id": "asst_abc456",
      "object": "assistant",
      "created_at": 1698982718,
      "name": "My Assistant",
      "description": None,
      "model": "gpt-4o",
      "instructions": "You are a helpful assistant designed to make me better at coding!",
      "tools": [],
      "tool_resources": {},
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    },
    {
      "id": "asst_abc789",
      "object": "assistant",
      "created_at": 1698982643,
      "name": None,
      "description": None,
      "model": "gpt-4o",
      "instructions": None,
      "tools": [],
      "tool_resources": {},
      "metadata": {},
      "top_p": 1.0,
      "temperature": 1.0,
      "response_format": "auto"
    }
  ],
  #   ID of the first assistant in the list
  "first_id": "asst_abc123",
  #   ID of the last assistant in the list
  "last_id": "asst_abc789",
  #   Defines whether there are more assistants than what was queried and stored in data
  "has_more": False
}

# An assistant_list object
print(list_assistant_obj)