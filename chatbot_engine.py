# chatbot_engine.py

# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
from mistake_tracker import store_mistake, get_mistake_summary, export_mistakes_to_file
import os


load_dotenv()

def start_conversation(user_info, scenario):
    learning_language = user_info["learning_language"]
    known_language = user_info["known_language"]
    level = user_info["proficiency"]

    # LLM setup
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    # System prompt to guide the assistant
    system_message = SystemMessage(
        content=(
            f"You are a helpful and friendly language learning assistant. "
            f"Only speak in {learning_language}. Set the scene: {scenario}. "
            f"The user knows {known_language} and is {level} level in {learning_language}. "
            f"Help them practice by roleplaying this scenario. "
            f"If they make a mistake, gently correct them."
        )
    )

    # Start conversation
    messages = [system_message]

    print(f"\n Assistant (in {learning_language}): Let's begin! {scenario}")

    while True:
        user_input = input(" You: ")

        if user_input.lower() in ["exit", "quit"]:
            print(" Ending session. Here's your mistake summary:\n")

            mistakes = get_mistake_summary()
            if not mistakes:
                print(" No mistakes! Well done!")
            else:
                for idx, (id_, u_inp, corr, explain) in enumerate(mistakes, 1):
                    print(f"\n Mistake {idx}")
                    print(f" You said: {u_inp}")
                    print(f" Correct: {corr}")
                    print(f" Explanation: {explain}")

            # Ask user if they want to export as CSV or TXT
            while True:
                export_format = input("\n📤 Do you want to export the mistakes as a CSV file? (yes/no): ").strip().lower()
                if export_format in ["yes", "y"]:
                    export_mistakes_to_file("mistakes_summary.csv", as_csv=True)
                    break
                elif export_format in ["no", "n"]:
                    export_mistakes_to_file("mistakes_summary.txt", as_csv=False)
                    break
                else:
                    print("❗ Please type 'yes' or 'no'.")

            break

        # Add user message to the conversation
        messages.append(HumanMessage(content=user_input))
        response = llm(messages)
        reply = response.content
        print(f"\n Assistant: {reply}")
        messages.append(response)

        #  Mistake detection
        correction_prompt = [
            SystemMessage(content="You are a grammar teacher. Check the student's sentence for grammar mistakes."),
            HumanMessage(content=user_input)
        ]
        correction_response = llm(correction_prompt)
        corrected_text = correction_response.content

        # Only store mistake if a correction is needed
        if user_input.strip() != corrected_text.strip():
            explanation_prompt = [
                SystemMessage(content="Explain why this sentence is incorrect:"),
                HumanMessage(content=f"Original: {user_input}\nCorrect: {corrected_text}")
            ]
            explanation_response = llm(explanation_prompt)
            explanation = explanation_response.content

            store_mistake(user_input, corrected_text, explanation)
