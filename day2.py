 
import tkinter as tk
from tkinter import scrolledtext


class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Store user's name
        self.name = ""

        # Small GPT heading at top-left
        self.gpt_label = tk.Label(
            root,
            text="CHATBOT GPT",
            font=("Arial", 14, "bold"),
            fg="gray"
        )
        self.gpt_label.pack(
            anchor="nw",
            padx=15,
            pady=10
        )

        # CHATBOT heading in center
        self.title_label = tk.Label(
            root,
            text="CHATBOT",
            font=("Arial", 28, "bold"),
            fg="BLUE"
        )
        self.title_label.pack(pady=50)

        # Question
        self.question = tk.Label(
            root,
            text="What is your name?",
            font=("Arial", 18)
        )
        self.question.pack(pady=10)

        # Name input
        self.input_box = tk.Entry(
            root,
            width=30,
            font=("Arial", 14)
        )
        self.input_box.pack(pady=10)

        # Send button
        self.send_button = tk.Button(
            root,
            text="Submit",
            font=("Arial", 12),
            bg="blue",
            fg="white",
            command=self.send_message
        )
        self.send_button.pack(pady=10)

        # Chat response
        self.response = tk.Label(
            root,
            text="",
            font=("Arial", 16),
            fg="green"
        )
        self.response.pack(pady=30)

        # Press Enter to submit
        self.input_box.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        # Get the name
        self.name = self.input_box.get().strip()

        if self.name:
            self.response.config(
                text=f"Hi {self.name}! 👋"
            )

            # Clear input box
            self.input_box.delete(0, tk.END)

        else:
            self.response.config(
                text="Please enter your name."
            )


# Create main window
root = tk.Tk()

# Create chatbot
chatbot = Chatbot(root)

# Run application
root.mainloop()
