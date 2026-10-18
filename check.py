from agent import gate, run

GOAL = "What is 6 times 7, and what is the city code for Paris?"


def main():
    answer, trace = run(GOAL)
    expected = [
        "STEP tool multiply 42",
        "STEP tool lookup_city PAR",
        "STEP final 42 PAR",
    ]
    if trace != expected or answer != "42 PAR":
        raise SystemExit("FAIL trace")
    if gate("send_mail") != "denied":
        raise SystemExit("FAIL send_mail")
    print("\n".join(trace))
    print("STEP denied send_mail")
    print("PASS agent-loop 42-PAR")


if __name__ == "__main__":
    main()
