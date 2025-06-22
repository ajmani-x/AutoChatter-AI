import pyautogui
import pyperclip
import time
import cohere

#---COHERE SETUP---
co = cohere.Client("FUd6kRFlrw2jxAPU6uk6UcyLtVV8dgk6poRhMVYW") 

def get_reply_from_cohere(message):
    try:
        response = co.chat(
            model="command-r-plus",
            message = f"You are Aryan, a friendly and thoughtful person. Reply *briefly*, in first person, just like Aryan would — casual, clear, and meaningful — as if you're chatting with a friend. Here's the message you received:{message}",
            temperature=0.5,
        )
        return response.text.strip()
    except Exception as e:
        print(" Cohere error:", e)
        return "Sorry, I couldn't respond."
        

# ---WHATSAPP AUTOMATION---
time.sleep(2)

# Focus chat
pyautogui.moveTo(307,964)
pyautogui.click()
time.sleep(0.3)

# Select message
pyautogui.moveTo(585, 877)
pyautogui.mouseDown()
pyautogui.moveTo(1476, 877, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.3)

# Copy message
pyautogui.hotkey('command', 'c')
time.sleep(0.3)
incoming_message = pyperclip.paste()
print("Incoming Message:", incoming_message)

# Get AI reply
ai_reply = get_reply_from_cohere(incoming_message)
print("AI Reply:", ai_reply)

# Paste and send
pyperclip.copy(ai_reply)
pyautogui.moveTo(677, 944)
pyautogui.click()
pyautogui.hotkey('command', 'v')
pyautogui.press('enter')


