# Chatbot with Tkinter GUI

A simple Python chatbot with a dark-themed GUI interface built using Tkinter. This chatbot provides campus-related information and responds to user queries using a customizable knowledge base.

## Features

- 🌙 Modern dark theme interface
- 💬 Real-time chat interaction
- 🎯 Keyword-based responses
- 🤖 Random agent name assignment
- ⌨️ Enter key support for sending messages

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python installation)

## File Structure

```
chatbot-tkinter/
│
├── chatbot_tkinter.py
├── responses.json
├── README.md
└── .gitignore
```

## Setup and Running

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatbot-tkinter.git
cd chatbot-tkinter
```

2. Ensure both files are in the same directory:
   - `chatbot_tkinter.py`
   - `responses.json`

3. Run the chatbot:
```bash
python chatbot_tkinter.py
```

## Customizing Responses

Modify the `responses.json` file to customize the chatbot's responses:

```json
{
    "keywords": {
        "coffee": "The campus coffee bar is open from 8 AM to 8 PM.",
        "library": "The library is open from 9 AM to 10 PM."
    },
    "default_responses": [
        "I'm sorry, I didn't quite catch that.",
        "Can you rephrase your question?"
    ],
    "agent_names": [
        "Alex",
        "Jamie",
        "Taylor"
    ]
}
```

## Usage Examples

Try asking about:
- Campus facilities: "What are the library hours?"
- Food services: "Tell me about the coffee shop"
- Parking: "Where can I park?"
- Sports: "What sports facilities are available?"

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Future Enhancements

- [ ] Add support for multiple languages
- [ ] Implement more advanced response matching
- [ ] Add conversation logging
- [ ] Include more customization options

## Support

For support, please open an issue in the GitHub repository.
