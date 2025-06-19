# Language-Learning-Model
For Learning new Language
Tech: Python, LangChain, OpenAI GPT-3.5, SQLite

Modules & Responsibilities 
1.  main.py :  
●  Entry point   
●  Sets up user’s known/target language, level, and practice scenario   
●  Starts the conversation loop   

2.  language_chatbot_setup.py  :  
●  Prompts user for language learning preferences   
●  Offers level-based scenarios for practice  

3.  chatbot_engine.py :  
●  Sends prompts to  OpenAI  models using LangChain   
●  Tracks the conversation   
●  Detects grammar mistakes using a secondary LLM query   
●  Gathers explanations and stores them in the database  

4.  mistake_tracker.py :  
●  Manages  SQLite  database   
●  Functions for logging mistakes, summarizing, and exporting them as CSV or TXT  
