from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values("../.env")
client = OpenAI(api_key=config["OPENAI_API_KEY"], base_url=config["BASE_URL"])

assistant_list = client.beta.assistants.list(
    # Order based on the created_at time
    order="asc",
    # Limit from 1 to 100, defaults to 20
    limit=25,
    # A cursor for pagination, gives page before a given object_id
    before="asst_abc123",
    # A cursor for pagination, gives page after a given object_id
    after="asst_abc789",
)