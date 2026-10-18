import os

from dotenv import load_dotenv

from tools import word_count

TOOLS = {"word_count": word_count}


def load_settings():
    load_dotenv()
    return {
        "provider": os.getenv("MODEL_PROVIDER", "local"),
        "model": os.getenv("MODEL_NAME", "local-tool"),
        "api_key": os.getenv("OPENAI_API_KEY", ""),
    }


def request_tool(goal, settings):
    if settings["provider"] != "local":
        raise RuntimeError(settings["provider"])
    if "words" not in goal.lower():
        raise RuntimeError("goal")
    return {"tool": "word_count", "args": {"text": "agents keep state"}}


def run(goal):
    settings = load_settings()
    call = request_tool(goal, settings)
    result = TOOLS[call["tool"]](**call["args"])
    answer = f"{result} words"
    trace = [
        f"STEP provider {settings['provider']}",
        f"STEP model {settings['model']}",
        f"STEP tool {call['tool']} {result}",
        f"STEP final {answer}",
    ]
    return answer, trace
