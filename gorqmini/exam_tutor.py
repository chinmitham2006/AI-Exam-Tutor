
from groq import Groq

client = Groq()

messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly engineering exam tutor. "
            "Explain concepts in simple English. "
            "For 2 marks, give a concise definition. "
            "For 5 marks, give a definition and key points. "
            "For 10 marks, give a detailed explanation with examples. "
            "Use clear headings and bullet points where useful."
        )
    }
]

print("=" * 35)
print("       AI EXAM TUTOR")
print("=" * 35)
print("Type 'exit' to stop.\n")

while True:
    question = input("Enter your question: ").strip()

    if question.lower() == "exit":
        print("Good luck with your studies!")
        break

    if not question:
        print("Please enter a question.\n")
        continue

    marks = input("Choose marks (2, 5, or 10): ").strip()

    if marks not in ["2", "5", "10"]:
        print("Please choose 2, 5, or 10.\n")
        continue

    temp_input = input(
        "Choose temperature (0.2 = focused, 0.7 = balanced, 1.0 = varied): "
    ).strip()

    try:
        temperature = float(temp_input)

        if not 0 <= temperature <= 2:
            print("Temperature must be between 0 and 2.\n")
            continue

    except ValueError:
        print("Please enter a valid number, such as 0.7.\n")
        continue

    messages.append({
        "role": "user",
        "content": (
            f"Question: {question}\n"
            f"Marks: {marks}\n"
            "Prepare an exam-ready answer."
        )
    })

    try:
        stream = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=temperature,
            max_completion_tokens=2048,
            stream=True
        )

        print("\n=== AI Tutor's Answer ===\n")
        answer = ""

        for chunk in stream:
            text = chunk.choices[0].delta.content or ""
            print(text, end="", flush=True)
            answer += text

        print("\n")

        messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as error:
        messages.pop()
        print(f"\nRequest failed: {error}")
        print("Check the error message and try again.\n")
