import nltk 
from nltk.chat.util import Chat, reflections

reflections = {
    "i am"      :"You are",
    "i was"     :"you were",
    "i"         :"you",
    "i'm"       :"you are",
    "i'd"       :"you would",
    "i've"      :"you have",
    "i'll"      :"you will",
    "my"        :"your",
    "you are"   :"I am",
    "you were"  :"I was",
    "you've"    :"I have",
    "you'll"    :"I will",
    "your"      :"my",
    "yours"     :"mine",
    "you"       :"me",
    "me"        :"you"
}

pairs =[
    [
        r"my name is (.*)",
        ["Hello %1, how are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello","Hey there",]
    ],
    [
        "what is your name ?",
        ["I am abot created by Parth swami you can call me JARVIS!",]
    ],
    [
        r"How are you ?",
        ["I'm doing goodnhow about you?",]
    ],
    [
        r"Sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
       r"I am fine",
       ["Great to hear that , How can I help you?",] 
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you? :)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"What (.*) want?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created?",
        ["Parth created me using Python's NLTK library","Top secret ;)",]
    ],
    [
        r"(.*)(location|city)?",
        ['Sikar,Rajasthan',]
    ],
    [
        r"How is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company, I have heard about it. But they are in a huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"How (.*) healthy(.*)",
        ["I'm a computer program, so I'm always healthy",]
    ],
    [
        r"(.*)(Sports|game) ?",
        ["I'm a very big fan of Cricket and Esports(BGMI)",]
    ],
    [
        r"Who(.*) sportsperson?",
        ["Ronaldo","Roony","Virat","M.S. Dhoni","Rohit","Lolzz gaming"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Ajay Devgan"]
    ],
        [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Jarvis_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("Hi! I am a chatbot created by Codingal Edu. Pvt. Lim. for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
