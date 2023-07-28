#pip install openai, google, beautifulsoup4, nltk
import openai, googlesearch, requests, nltk, constants
from googlesearch import search
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
#nltk.download('punkt') #These only need to be run once to download, unless you want updates
#nltk.download('stopwords')
#nltk.download('wordnet')

def remove_noise_words(text):
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    result = [word for word in words if word.lower() not in stop_words]
    result = ' '.join(result)  
    return result

def text_cleanup(text:str):
	text = text.encode('ascii', 'ignore').decode('ascii')
	text =  remove_noise_words(text)
	for i in range(0,10): 
		text = text.replace("\n\n", "\n")
		text = text.replace("  ", " ")
	return text

def add_synonyms(words):
    expanded_set = set()
    for word in words:
        synonyms = set()
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                synonyms.add(lemma.name().replace("_", " "))
        expanded_set.add(word)
        expanded_set.update(synonyms)
    return expanded_set

def get_plain_text_from_url(url):
	success = True
	try:
		response = requests.get(url)
	except:
		print(" Request for url " + url + " failed.")
		success = False
		result = ""
	if success:	
		soup = BeautifulSoup(response.text, 'html.parser')
		result = soup.get_text()
		result = text_cleanup(result)
	return result

def tokenize_text(text: str):
	return nltk.word_tokenize(remove_noise_words(text.lower()))

def rough_evaluate_answer(question: str, response: str):
	question_tokens = tokenize_text(question)
	response_tokens = tokenize_text(response)
	hit_count = 0
	for x in question_tokens:
		if x in response_tokens: hit_count +=1
	return hit_count > (len(question_tokens)/2)
	
def ask_chatgpt(question:str, system_command:str = "", model:str = 'gpt-3.5-turbo', temperature:float=.2, max_tokens:int=256):
	openai.api_key = constants.openai_api_key
	messages = []
	if system_command !="": messages.append({"role": "system", "content": system_command})
	messages.append({"role": "user", "content": question})
	try: 
		result = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens )
		success = True
	except Exception as e:
		print("ChatGPT query failed:", e)
		success = False
		result = "API Call Failed"
	if success: result = result.choices[0].message.content
	return result

def google_search(query):
	results = search(query)
	return list(results)

# Main script
if __name__ == "__main__":
	question = input("What is your question?")
	print("Question:", question)
	#print("Tokens: ", tokenize_text(question))
	
	#Get ChatGPT's answer to the question
	chatgpt_result = ask_chatgpt(question)
	print("ChatGPT Answer: ", chatgpt_result, "\n")

	#Test if that corresponds to web results
	gpt_system = "Answer in the format Response: supports, refutes, inconclusive followed by Reason:"
	gpt_question = "With regards to the question: " + question + " Does the following text support or refute your knowledge: "
	tally_supports = 0
	tally_refutes = 0
	tally_inconclusive = 0
	web_search_results = google_search(question)
	if web_search_results:
		urls =[web_search_results[0], web_search_results[1], web_search_results[2]]
		for url in urls:
			print("URL:", url)
			result = get_plain_text_from_url(url)
			if rough_evaluate_answer(question, result):
				print(" Responsive answer from " + url)
				chatgpt_result = ask_chatgpt(gpt_question + result[:2500], gpt_system)
				if 'supports' in chatgpt_result[:50].lower():
					tally_supports +=1
				elif 'refutes' in chatgpt_result[:50].lower():
					tally_refutes +=1
				else:
					tally_inconclusive +=1
				print(" ChatGPT's answer:", chatgpt_result)
			else:
				print(" No joy from " + url, "\n")
		print("Sites Queried: ", (tally_supports + tally_refutes + tally_inconclusive))
		print("Supports: ", tally_supports)
		print("Refutes: ", tally_refutes)
		print("Inconclusive: ", tally_inconclusive)
	else:
		print("Web search didn't return any results.")

