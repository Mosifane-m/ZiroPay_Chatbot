# ZiroPay_Chatbot

ZiroPay Chatbot Documentation

How to install Rasa:
- https://www.youtube.com/watch?v=4ewIABo0OkU&t=1s

Packages to install:
- "pip show tensorflow"
- "pip install openai==0.28.0"
- "pip install flask"

Process
- Trained the Rasa model to recognise:
	- Account Information Questions
	- Statement history questions
	- Financial advice questions
	- Account settings questions 
	- finance question
- run "rasa train"
- To run the intent recognition run: rasa run --enable-api
- Run "https://0.0.0:5005/model/parse"
- body {
"text": {question here}: 
}

Flask Integration
- Plan
	- depending on the type of intent generated, a suitable answer should be given:
- So far
	- Implementing openai through the gpt_services.py modeule (currently receiving a quota issue)

***that's as far as I got***
