# AI-Chatbot
An AI chatbot is a python based project that uses natural language processing and machine learning to simulate human conversation, providing real-time assistance and performing task

## Author: Priyanshu Singh

### Overview
This project includes three Python scripts that demonstrate how to interact with a graphical user interface (GUI) using PyAutoGUI, manage clipboard operations with Pyperclip, and use OpenAI's GPT-3.5-turbo model to generate automated responses based on chat history. The three scripts are as follows:

1. `get_cursor.py`
2. `openai.py`
3. `03_bot.py`

### 1. get_cursor.py
This script captures and prints the current mouse cursor position. This can be useful for determining the coordinates of various GUI elements that you want to interact with.

#### How It Works:
- The script continuously captures the current position of the mouse cursor and prints it to the console.
- It includes a small delay (`time.sleep(1)`) to avoid overwhelming the console with too many position updates.

#### Usage:
```sh
python get_cursor.py
```

### 2. openai.py
This script demonstrates how to use the OpenAI API to generate text completions. It initializes the OpenAI client and tests it with a sample command.

#### How It Works:
- The script initializes the OpenAI client with your API key.
- It sends a sample message to the GPT-3.5-turbo model and prints the response.
- The message prompts the model to respond in the style of a person named HADI who speaks both Urdu and English, is from Pakistan, and is a coder.

#### Usage:
```sh
python openai.py
```

### 3. 03_bot.py
This is the main script that automates GUI interactions to copy chat history, generate a response using OpenAI, and then send the response back through the chat interface.

#### How It Works:
- The script uses PyAutoGUI to click on specific screen coordinates, drag the mouse to select chat text, and copy the text to the clipboard.
- It retrieves the copied text using Pyperclip and checks if the last message is from a specific sender.
- If the condition is met, it uses the OpenAI API to generate a response based on the chat history.
- The generated response is then pasted back into the chat interface and sent.

#### Detailed Steps:
1. Click on the Chrome icon to bring the chat window into focus.
2. Drag the mouse to select the chat history text.
3. Copy the selected text to the clipboard.
4. Retrieve and print the copied chat history.
5. Check if the last message is from a specified sender.
6. If true, generate a response using the OpenAI API.
7. Copy the response to the clipboard.
8. Click on the input area of the chat interface.
9. Paste the response.
10. Press Enter to send the message.

#### Usage:
```sh
python 03_bot.py
```

### Prerequisites
Ensure you have the following Python packages installed:
- `pyautogui`
- `pyperclip`
- `openai`

You can install these packages using pip:
```sh
pip install pyautogui pyperclip openai
```

### Configuration
Before running `03_bot.py`, make sure to replace `"your-api-key-here"` with your actual OpenAI API key.

### Conclusion
This project demonstrates the integration of GUI automation and AI text generation. It can be extended to various use cases where automated interactions and intelligent responses are required. Feel free to modify the scripts to suit your specific needs.

For any questions or support, please contact Priyanshu Singh.
MAIL ME : priyanshusingh231202@gmail.com
