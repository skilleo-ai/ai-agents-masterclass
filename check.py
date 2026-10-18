from client import load_settings, run

GOAL = "How many words are in: agents keep state"

def main():
    settings = load_settings()
    if settings["provider"] != "local" or settings["model"] != "local-tool":
        raise SystemExit("FAIL provider")
    if settings["api_key"] != "YOUR_API_KEY":
        raise SystemExit("FAIL key")
    answer, trace = run(GOAL)
    expected = [
        "STEP provider local",
        "STEP model local-tool",
        "STEP tool word_count 3",
        "STEP final 3 words",
    ]
    if trace != expected or answer != "3 words":
        raise SystemExit("FAIL trace")
    print("\n".join(trace))
    print("PASS agent-env local 3")

if __name__ == "__main__":
    main()
