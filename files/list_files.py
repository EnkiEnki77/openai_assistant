# Returns a list of files

from dotenv import  dotenv_values
from openai import  OpenAI

config = dotenv_values("../.env")

client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

file_list = client.files.list(
    # Cursor for use in pagination, is an object ID that defines your place in the list, showing only
    # a page after a given ID
    after="",
    # Order the list is presented based on created_at property of the files. Can be asc or desc
    order="asc",
    # Limit of items for the list, defaults to 10,000
    limit=100,
    # Show only files of a certain purpose
    purpose="fine-tune",
)

# File list object
print(file_list)