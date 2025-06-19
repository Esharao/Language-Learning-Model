from language_chatbot_setup import get_user_language_info, get_scenario_for_user
from chatbot_engine import start_conversation
from mistake_tracker import init_db

def main():
    # Step 1: Get user preferences
    user_info = get_user_language_info()
    scenario = get_scenario_for_user(user_info["level"])

    # Step 2: Create the chatbot engine
    bot = start_conversation(
        known_language=user_info["known_language"],
        target_language=user_info["target_language"],
        user_level=user_info["level"],
        scenario=scenario
    )

    # Step 3: Start the conversation
    print("\n Chat session started! Type 'exit' to end.\n")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() == "exit":
            break
        response = bot.get_bot_response(user_input)
        print(f"Bot: {response}\n")

    # Step 4: Show mistakes summary
    bot.summarize_mistakes()

    # Step 5: Offer export
    export = input("Would you like to export your mistakes as a .txt or .csv file? (yes/no): ").strip().lower()
    if export == "yes":
        filetype = input("Choose file format (txt/csv): ").strip().lower()
        if filetype in ["txt", "csv"]:
            bot.export_mistakes(filetype)
        else:
            print("Unsupported format. Export canceled.")
    else:
        print("No export selected.")

if __name__ == "__main__":
    init_db()  # Initialize the mistake tracking database

    user_info = get_user_language_info()
    scenario = get_scenario_for_user(user_info["proficiency"])

    user_info["scenario"] = scenario

    start_conversation(user_info, scenario)
