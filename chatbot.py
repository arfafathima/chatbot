import tkinter as tk
from tkinter import scrolledtext


class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("My Tkinter Chatbot")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Store user information
        self.name = ""
        self.age = ""
        self.color = ""
        self.hobby = ""

        # Chat display
        self.chat_area = scrolledtext.ScrolledText(
            root,
            width=55,
            height=25,
            state="disabled",
            wrap=tk.WORD
        )
        self.chat_area.pack(padx=10, pady=10)

        # Input box
        self.input_box = tk.Entry(root, width=45, font=("Arial", 12))
        self.input_box.pack(side=tk.LEFT, padx=(10, 5), pady=10)
        self.input_box.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(
            root,
            text="Send",
            command=self.send_message,
            bg="blue",
            fg="white"
        )
        self.send_button.pack(side=tk.RIGHT, padx=(5, 10), pady=10)

        # Start conversation
        self.step = 0
        self.bot_message(
            "Hello! 👋 I am your chatbot.\n"
            "What is your name?"
        )

    def bot_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, "Bot: " + message + "\n\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    def user_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, "You: " + message + "\n\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    def send_message(self, event=None):
        message = self.input_box.get().strip()

        if not message:
            return

        self.input_box.delete(0, tk.END)
        self.user_message(message)

        # Collect information step by step
        if self.step == 0:
            self.name = message
            self.bot_message(
                f"Nice to meet you, {self.name}! 😊\n"
                "How old are you?"
            )
            self.step = 1

        elif self.step == 1:
            self.age = message
            self.bot_message(
                "Great! 👍 What is your favorite color?"
            )
            self.step = 2

        elif self.step == 2:
            self.color = message
            self.bot_message(
                "That's a nice choice!\n"
                "What is your favorite hobby?"
            )
            self.step = 3

        elif self.step == 3:
            self.hobby = message

            self.bot_message(
                f"Awesome, {self.name}! 🎉\n\n"
                f"Here is what I learned about you:\n"
                f"• Name: {self.name}\n"
                f"• Age: {self.age}\n"
                f"• Favorite color: {self.color}\n"
                f"• Hobby: {self.hobby}\n\n"
                f"I hope you have a great day! 😄"
            )

            self.step = 4

        else:
            self.bot_message(
                "Thanks for chatting with me! 😊"
            )


# Create the main window
root = tk.Tk()

# Create chatbot
chatbot = Chatbot(root)

# Run the application
root.mainloop()


