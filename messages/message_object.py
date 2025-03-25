# Object returned when a message is created

message_obj = {
  #   ID of the message
  "id": "msg_abc123",
  #   object type of the message which will always be thread.message
  "object": "thread.message",
  #   UNIX time in seconds message was created
  "created_at": 1698983503,
  #   ID of the thread the message belongs to
  "thread_id": "thread_abc123",
  #   Entity that created the message
  "role": "assistant",
  #   list of content parts message contains
  "content": [
    {
      "type": "text",
      "text": {
        "value": "Hi! How can I help you today?",
        "annotations": []
      }
    }
  ],
  # If applicable, the ID of the assistant that authored the message
  "assistant_id": "asst_abc123",
  #   ID of the run associated with this message, null if message was created manually through create_message
  #   or create_thread.
  "run_id": "run_abc123",
# A list of files attached to the message, and the tools they were added to.
  "attachments": [
      {
          # ID of file attached to the message
          "file_id":"",
          # Tools to add the file to
          "tools": []
      }
  ],
  "metadata": {},
    # status of the message which can be pending, incomplete, or complete
  "status": "pending",
}
