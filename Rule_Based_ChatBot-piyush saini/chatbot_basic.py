from datetime import datetime

responses = {       # the knowledge base of the bot #
    "hello": "Hi there! How can I help you?",
    "hi": "Hello!",
    "how are you": "I'm doing great!",
    "what is your name": "I am an AI chatbot, but you can call me whatever you like.",
    "help": "what can i help you with today ! ",
    "okay great": "thanks for the compliment ",
  }
greetings=["hi","hello","how are you","hey","what's up"] # greetings response list #
while True:
  user_input= input("You: ").lower().strip() # user inputs the bot #
  if user_input in greetings:
    reply = "hi there ! how can i help you"
  elif user_input.lower() in ["bye","exit","okay we are done","thanks for today"]: # while true condition till the loop breakes #
    print(" bot: okay good bye!")
    break
  elif user_input.lower() in ["date","what is the date","today's date? ", "what is the date today"]:
    reply =datetime.now().strftime("today is %D-%M-%Y")

  elif user_input.lower() in ["time","what is the time","current time?"]:
    reply= datetime.now().strftime("current time is %H:%M:%S")
  else:
   reply= responses.get(user_input,"sorry I am not programmed that way ! is there any thing i can help you with.")  # .get command is used for searching the query from its knowledge base #
  print(f"bot: {reply}")   # print the reply from the bot #
