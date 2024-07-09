import pyautogui
import time
import pyperclip
import openai

# Initialize OpenAI client
openai.api_key = "your-api-key-here"  # Write your API key here

def is_last_message_from_sender(chat_log, sender_name="Rehman"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("\n")
    if messages:
        last_message = messages[-1]
        return sender_name in last_message
    return False

# Step 1: Click on the Chrome icon at coordinates (1226, 1046)
pyautogui.click(1226, 1046)
time.sleep(1)  # Wait for 1 second to ensure the click is registered

while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (841, 283) to (847, 908) to select the text
    pyautogui.moveTo(841, 283)
    pyautogui.dragTo(847, 908, duration=2.0, button='left')  # Drag for 2 seconds

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 2 seconds to ensure the copy command is completed

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    if is_last_message_from_sender(chat_history):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named HADI who speaks Urdu as well as English. You are from Pakistan and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)."},
                {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rehman:"},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message["content"]
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1808, 1328)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')