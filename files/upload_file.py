# Files are used to upload documents that can be used with features such as assistants, fine-tuning,
# and batch API

from dotenv import  dotenv_values
from openai import  OpenAI

config = dotenv_values("../.env")

client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

# Upload a file that can be used across various endpoints for the API. Individual files can be 512mb
# and one organization can upload up to 100gb
# Assistants API accepts files up to 2 million tokens and of specific file types.
file = client.files.create(
    # Specifies the file that should be uploaded, has to be converted to a file object through the
    # open() function. First param is the file we're uploading, second param is the mode. In this
    # case, open is opening the file for reading, and is handling it in binary mode instead of text mode.
    file=open("some_file.txt", "rb"),
    # Defines the purpose of the file being uploaded, in this case we're using it for the assistants
    # tools
    purpose="assistants",
)

# The uploaded file object
print(file)