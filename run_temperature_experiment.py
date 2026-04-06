from template import call_openai

PROMPT = "Hay ke cho toi mot su that thu vi ve Viet Nam."
TEMPERATURES = [0.0, 0.5, 1.0, 1.5]


def main() -> None:
    print("Prompt:", PROMPT)
    for temp in TEMPERATURES:
        try:
            response_text, latency = call_openai(prompt=PROMPT, temperature=temp)
            print("\n" + "=" * 72)
            print(f"Temperature: {temp}")
            print(f"Latency: {latency:.2f}s")
            print("Response:")
            print(response_text)
        except Exception as exc:
            print("\n" + "=" * 72)
            print(f"Temperature: {temp}")
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
