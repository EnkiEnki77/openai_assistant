# The anatomy of a run object
run = {
    # The runs id which can be referenced in API endpoints
    "id": str,
    # The object type, which is always thread.run
    "object": str,
    # A UNIX timestamp in seconds for when the run was created.
    "create_at": int,
    # The id of the assistant used for executing this run
    "assistant_id": str,
    # The id of the thread this run is being executed on
    "thread_id": str,
    # The status of the run which can be either: queued, in_progress, requires_action, cancelling, cancelled,
    # failed, completed, incomplete, or expired.
    "status": str,
    # The UNIX time in seconds the run was started at
    "started_at": int,
    # The UNIX time in seconds the run will expire at if applicable
    "expires_at": int | None,
    # The UNIX time in seconds the run was cancelled at if applicable
    "canceled_at": int | None,
    # The UNIX time in seconds the run was failed at if applicable
    "failed_at": int | None,
    # The UNIX time in seconds the run was completed at if applicable
    "completed_at": int | None,
    # An error object if applicable. Contains an error code of either server_error, rate_limit_exceeded, or
    # invalid_prompt, and a human readable error message.
    "last_error": {"code": str, "message": str} | None,
    # The GPT model used by the assistant in this run
    "model": str,
    # The instructions for the assistant in this run, will be in addition to the instructions given to the
    # assistant at its creation.
    "instructions": str,
    # The list of tools the assistant used for this run. Each tool is an object that has a type property
    "tools": [{"type": str}, {"type": str}],
    # Set of 16 key-value pairs stored in a map that can be attached to an object. Used for storing additional
    # info about an object in a structured format, and querying for objects via API or the Dashboard
    "metadata": map,
    # Details on why the run is incomplete if applicable
    "incomplete_details": {"reason": str} | None,
    # Usage statistics related to the run, only applicable if the run is in terminal state (queued, in_progress,
    # etc.)
    "usage": {
        "completion_tokens": int,
        "prompt_tokens": int,
        "total_tokens": int,
    } | None,
    # The sampling temp for this run, if not set defaults to 1.0
    "temperature": float,
    # The nucleus smapling value set for this run, if not used defaults to 1.0
    "top_p": float,
    "max_prompt_tokens": int | None,
    "max_completion_tokens": int | None,
    "truncation_strategy": {
        # Defaults to auto, if set to last_messages the thread will be truncated to the n most recent
        # messages in the thread. When set to auto messages in the middle will be dropped to fit the
        # context length of the model, max_prompt_tokens.
        "type": str,
        # The number of most recent messages from the thread when constructing the context for the run
        "last_messages": int | None
    } | None,
    # Specifies the format the model must output
    "response_format":
        "auto" |
        # ensures model will match the specified json schema
        {
            "type": "json_schema",
            "json_schema": {...}
        } |
        # enables json mode which ensures the models output is valid json. You must also instruct the model
        # to produce json in json mode through a system or user message
        { "type": "json_object" },
    # Specifies which if any tools will be called by the model. None means the model will just output a
    # message, auto means the model gets to choose if it uses tools or not, and required means the model
    # must use a specific tool.
    "tool_choice": str | {
        "type": str,
        "function": {}
    },
    # Whether to enable parallel function calling during tool use
    "parallel_tool_calls": bool
}