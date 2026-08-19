# print("hello! I am your first programmer")
# name="alex"
# name=input("what is your name")
# print("nice to meet you"+name)
# mood=input("how are you:")
# if mood=="good":
#     print("great to hear")
# else:
#     print("hope it gets better")
# if mood=="good":
#      print("great to hear ")
# else:
#      print("hope yuor day gets better")
# if mood =="good":
#      print("great to hear that")
# elif mood=="sad":
#      print("sorry to hear that. I am hear to chat")
# elif mood=="tired":
#      print("get some rest")
# else:
#      print("thanks for sharing.")
# while True:
#      message=input("you: ")
#      if message=="bye":
#          print("Bot:goodbye!")
#          break
#      print("Bot I heard what you said " +  message)
# print("HI! i am chatbot,what is your name?")
# name=input("you: ")
# print(" Nice to meet you, "+ name+" ! type bye to leave."BYE)
# while True:
#      message=input(name+":")
#      if message=="bye":
#          print("Chatbot:goodbye, "+name+"!")
#          break
#      elif message=="hello":
#          print("Bot:hello there")
#      elif message == "how are you":
#          print("chatbot:I am just code,but i feel great!")
# else:
#         print("Chatbot: I am not sure how to answer that yet.")
# message="0h! hello there friend"
# if "hello" in message:
#     print("greeting is found!")
# elif"how are you " in message:
#     print("Chatbot:I feel great!")
# name="pop"
# message=input(name+":")
# message=message.lower()
import tkinter as tk
window=tk.Tk()
window.title("My ChatBot")
label=tk.Label(window, text="hello! I am your ChatBot.")
label.pack(padx=20,pady=20)
window.mainloop()
