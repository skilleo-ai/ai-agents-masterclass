from tools import lookup_city, multiply

TOOLS = {
    "multiply": multiply,
    "lookup_city": lookup_city,
}
ALLOWED = set(TOOLS)


def decide(goal, memory):
    text = goal.lower()
    done = {step["tool"] for step in memory}
    if "multiply" not in done and "times" in text:
        return {"type": "tool", "tool": "multiply", "args": {"a": 6, "b": 7}}
    if "lookup_city" not in done and "paris" in text:
        return {"type": "tool", "tool": "lookup_city", "args": {"name": "Paris"}}
    product = next(step["result"] for step in memory if step["tool"] == "multiply")
    code = next(step["result"] for step in memory if step["tool"] == "lookup_city")
    return {"type": "final", "answer": f"{product} {code}"}


def gate(tool_name):
    if tool_name not in ALLOWED:
        return "denied"
    return "allowed"


def run(goal):
    memory = []
    trace = []
    for _ in range(4):
        action = decide(goal, memory)
        if action["type"] == "final":
            trace.append(f"STEP final {action['answer']}")
            return action["answer"], trace
        tool_name = action["tool"]
        if gate(tool_name) == "denied":
            trace.append(f"STEP denied {tool_name}")
            raise PermissionError(tool_name)
        result = TOOLS[tool_name](**action["args"])
        memory.append({"tool": tool_name, "result": result})
        trace.append(f"STEP tool {tool_name} {result}")
    raise RuntimeError("loop did not finish")
