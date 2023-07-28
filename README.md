# 🦜️🔗 chatgpt_web_validation.py
Python script demonstrating how to ask ChatGPT to validate its knowledge against web search results.
	1) Prompts user for a question, which it then answers
	2) Uses the Google API to execute a web search
	3) Takes the first three websites, tokenizes the contents to see if the contents at least match the question
	4) If they appear to match the question, then use the ChatGPT API to check if the contents match its own knowlegdge and tally the results

## ✅ Dependencies
pip install openai, google, beautifulsoup4, nltk

## 📚 Technical description
Sample message:
messages = [{'role': 'system', 'content': 'Answer in the format Response: supports, refutes, inconclusive followed by Reason:'}, 
			{'role': 'user', 'content': 'With regards to the question: what is the population of Tokyo? Does the following text support or refute your knowledge: .................."}]
	

Sample sessions:
Question: what is the population of tokyo
ChatGPT Answer:  As of 2021, the estimated population of Tokyo, Japan is approximately 14 million people.

URL: https://en.wikipedia.org/wiki/Tokyo
 Responsive answer from https://en.wikipedia.org/wiki/Tokyo
 ChatGPT's answer: Response: supports
Reason: The text mentions that there is information about the population of Tokyo in the "Demographics" section.

URL: https://en.wikipedia.org/wiki/Greater_Tokyo_Area
 Responsive answer from https://en.wikipedia.org/wiki/Greater_Tokyo_Area
 ChatGPT's answer: Response: supports
Reason: The text states that the population of the Greater Tokyo Area is 38,050,000 in the urban area and 40,700,000 in the metropolitan area.

URL: https://en.wikipedia.org/wiki/List_of_cities_in_Tokyo_Metropolis_by_population
 Responsive answer from https://en.wikipedia.org/wiki/List_of_cities_in_Tokyo_Metropolis_by_population
 ChatGPT's answer: Response: supports
Reason: The text provides information about the population of Tokyo and lists the population of various cities, towns, and villages within Tokyo Metropolis.

Sites Queried:  3
Supports:  3
Refutes:  0
Inconclusive:  0


Question: When was the last major U.S. recession
ChatGPT Answer:  The last major U.S. recession was the Great Recession, which began in December 2007 and lasted until June 2009.

URL: https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/U.S._Recovery_from_Great_Recession_-_Govt_Contribution_to_Pct_Chg_in_Real_GDP_-_v1.png/450px-U.S._Recovery_from_Great_Recession_-_Govt_Contribution_to_Pct_Chg_in_Real_GDP_-_v1.png?sa=X&ved=2ahUKEwi0jr3706-AAxW9HzQIHf2nAdIQ_B16BAgEEAI
 No joy from https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/U.S._Recovery_from_Great_Recession_-_Govt_Contribution_to_Pct_Chg_in_Real_GDP_-_v1.png/450px-U.S._Recovery_from_Great_Recession_-_Govt_Contribution_to_Pct_Chg_in_Real_GDP_-_v1.png?sa=X&ved=2ahUKEwi0jr3706-AAxW9HzQIHf2nAdIQ_B16BAgEEAI

URL: https://en.wikipedia.org/wiki/Great_Recession_in_the_United_States
 Responsive answer from https://en.wikipedia.org/wiki/Great_Recession_in_the_United_States
 ChatGPT's answer: Response: supports
Reason: The text mentions the "Great Recession" in the United States, which indicates that there was a major recession in the country.

URL: https://en.wikipedia.org/wiki/List_of_recessions_in_the_United_States
 Responsive answer from https://en.wikipedia.org/wiki/List_of_recessions_in_the_United_States
 ChatGPT's answer: Response: supports
Reason: The text provides a comprehensive list of recessions in the United States, indicating that there have been multiple recessions in the country's history.

Sites Queried:  2
Supports:  2
Refutes:  0
Inconclusive:  0

Have fun and keep programming!