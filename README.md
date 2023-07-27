# 🦜️🔗 chatgpt_web_validation.py
	Python script demonstrating how to ask ChatGPT to validate its knowledge against web search results.
	1) Prompts user for a question.
	2) Uses the Google API to execute a web search
	3) Takes the first three websites, tokenizes the contents to see if the contents at least match the question
	4) If they appear to match the question, then use the ChatGPT API to check if the contents match its own knowlegdge and tally the results

## ✅ Dependencies
	pip install openai, google, beautifulsoup4, nltk

## 📚 Technical description
	Sample message:
	messages = [{'role': 'system', 'content': 'Answer in the format Response: supports, refutes, inconclusive followed by Reason:'}, 
	{'role': 'user', 'content': 'With regards to the question: what is the population of Taiwan? Does the following text support or refute your knowledge: .................."}]
	
	Have fun and keep programming!
