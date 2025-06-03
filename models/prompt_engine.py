# models/prompt_engine.py

"""
Simple parser for extracting structured room data from user input prompts.
This module can be upgraded to use NLP in future versions.
"""

def parse_prompt(prompt: str):
    """
    Convert a comma-separated room prompt into a list of room names.

    Args:
        prompt (str): User input like "bedroom, kitchen, bathroom"

    Returns:
        List[str]: Cleaned list of room names
    """
    return [room.strip().lower() for room in prompt.split(',') if room.strip()]
