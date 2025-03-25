# Delete file object of a certain ID

from dotenv import  dotenv_values
from openai import  OpenAI

config = dotenv_values("../.env")

client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

delete_file = client.files.delete(
    # ID of file to delete
    "file_id"
)

# deletion status object
print(delete_file)