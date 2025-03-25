# The file object represents a document that has been uploaded to OpenAI

file_object = {
  #   ID of the uploaded file, which can be referenced in the API endpoints
  "id": "file-abc123",
  #   Object type which will always be "file".
  "object": "file",
  #   Size of the file uploaded in bytes
  "bytes": 120000,
  #   UNIX time in seconds the file was uploaded at
  "created_at": 1677610602,
  #   UNIX time in seconds the file will expire at
  "expires_at": 1680202602,
  #   Name of the file that was uploaded
  "filename": "salesOverview.pdf",
  #   Purpose the file was uploaded for, supported purposes are: assistants, assistants_output, batch,
  #   batch_output, fine-tune, fine-tune-results, and vision.
  "purpose": "assistants",
}
