# language_chatbot_setup.py

SUPPORTED_LANGUAGES = [
    "english", "spanish", "french", "german", "italian", "japanese",
    "korean", "chinese", "hindi", "arabic", "portuguese"
]

SCENARIOS = {
    "Beginner": [
        "Introducing yourself",
        "Ordering food at a restaurant",
        "Asking for directions",
        "Shopping in a store"
    ],
    "Intermediate": [
        "Booking a hotel room",
        "Making a doctor's appointment",
        "Talking about hobbies",
        "Describing your day"
    ],
    "Advanced": [
        "Job interview",
        "Discussing global issues",
        "Making travel plans",
        "Debating a topic"
    ]
}

def get_valid_language(prompt):
    while True:
        lang = input(prompt).strip().lower()
        if lang in SUPPORTED_LANGUAGES:
            return lang.capitalize()
        else:
            print(f" '{lang}' is not supported. Please choose from: {', '.join([l.capitalize() for l in SUPPORTED_LANGUAGES])}")

def get_user_language_info():
    print("Welcome to the Language Learning Chatbot!\n")

    known_language = get_valid_language("🌍 What is your native/known language? (e.g., English): ")
    target_language = get_valid_language("🗣️ What language would you like to learn? (e.g., Spanish): ")

    if known_language == target_language:
        print("You already know this language. Please choose a different one to learn.")
        return get_user_language_info()

    print("\n What is your current level in {}?".format(target_language))
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    level_map = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}

    while True:
        level_choice = input("Enter the number corresponding to your level: ").strip()
        if level_choice in level_map:
            level = level_map[level_choice]
            break
        else:
            print(" Invalid choice. Please enter 1, 2, or 3.")

    return {
        "known_language": known_language,
        "target_language": target_language,
        "level": level
    }

def get_scenario_for_user(level):
    print(f"\nPlease choose a scenario to practice ({level} level):\n")

    scenarios = SCENARIOS.get(level, [])
    for idx, scenario in enumerate(scenarios, 1):
        print(f"{idx}. {scenario}")

    while True:
        choice = input("\nEnter the number of your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(scenarios):
            selected = scenarios[int(choice) - 1]
            print(f"\nGreat! Your scenario is: '{selected}'\n")
            return selected
        else:
            print("Invalid input. Please enter a valid number from the list.")

# Run the complete setup
if __name__ == "__main__":
    user_info = get_user_language_info()
    scenario = get_scenario_for_user(user_info["level"])
    
    print("Setup complete! Here's your session info:")
    print(f"Known Language: {user_info['known_language']}")
    print(f"Learning Language: {user_info['target_language']}")
    print(f"Proficiency Level: {user_info['level']}")
    print(f"Scenario: {scenario}")
