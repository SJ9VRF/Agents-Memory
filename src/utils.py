import getpass
import os

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

def get_user_id(config):
    return config["configurable"].get("user_id", "default_user_id")

_set_env("OPENAI_API_KEY")
_set_env("TAVILY_API_KEY")
