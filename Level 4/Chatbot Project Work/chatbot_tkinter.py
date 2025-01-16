import tkinter as tk
from tkinter import scrolledtext
import random
import json
import os

class SimpleZyrixAI:
    def __init__(self):
        # Load responses from JSON
        self.load_responses()
        
        # Choose random agent name
        self.agent_name = random.choice(self.responses["agent_names"])
        
        # Create main window
        self.root = tk.Tk()
        self.root.title(f"Chat with {self.agent_name}")
        self.root.geometry("600x700")
        
        # Configure basic colors
        self.root.configure(bg='black')
        
        # Create chat area
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            bg='black',
            fg='white',
            padx=10,
            pady=10
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=20, pady=(20, 10))
        
        # Create input area
        self.entry = tk.Entry(
            self.root,
            font=("Helvetica", 12),
            bg='black',
            fg='white'
        )
        self.entry.pack(fill=tk.X, padx=20, pady=(0, 10))
        
        # Create send button
        self.send_button = tk.Button(
            self.root,
            text="Send",
            command=self.send_message,
            bg='cyan',
            fg='black'
        )
        self.send_button.pack(pady=(0, 20))
        
        # Bind enter key
        self.entry.bind('<Return>', lambda e: self.send_message())
        
        # Display welcome message
        self.display_message(f"{self.agent_name}: Hello! I'm {self.agent_name}. How can I help you today?")

    def load_responses(self):
        try:
            with open('responses.json', 'r') as file:
                self.responses = json.load(file)
        except FileNotFoundError:
            print("responses.json not found!")
            self.root.quit()

    def get_response(self, user_input):
        # Convert input to lowercase for matching
        user_input = user_input.lower()
        
        # Check for keywords
        for keyword, response in self.responses["keywords"].items():
            if keyword in user_input:
                return response
        
        # If no keyword matches, return random default response
        return random.choice(self.responses["default_responses"])

    def send_message(self):
        message = self.entry.get().strip()
        if message:
            # Display user message
            self.display_message(f"You: {message}")
            
            # Get and display AI response
            if message.lower() in ['bye', 'quit', 'exit']:
                self.display_message(f"{self.agent_name}: Goodbye! Have a great day!")
                self.root.after(1500, self.root.quit)
            else:
                response = self.get_response(message)
                self.display_message(f"{self.agent_name}: {response}")
            
            # Clear input field
            self.entry.delete(0, tk.END)

    def display_message(self, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.configure(state='disabled')
        self.chat_area.see(tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleZyrixAI()
    app.run()