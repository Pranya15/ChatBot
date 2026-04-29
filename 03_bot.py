import pyautogui
import time
import pyperclip
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get last valid (non-empty) message
def get_last_message(chat_log):
    lines = [l for l in chat_log.split("\n") if l.strip()]
    return lines[-1] if lines else ""

pyautogui.FAILSAFE = True

print("Starting in 3 seconds...")
time.sleep(3)

# Step 1: Focus chat
pyautogui.click(800, 500)
time.sleep(1)

last_processed = ""

while True:
    # Step 2: Select all
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)

    # Step 3: Copy
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.8)

    # Step 4: Deselect (safe)
    pyautogui.press('right')

    # Step 5: Get chat
    chat_history = pyperclip.paste()
    print(chat_history[:100])

    # Step 6: Extract last message
    last_message = get_last_message(chat_history)

    # Skip if empty
    if not last_message:
        time.sleep(2)
        continue

    # Avoid duplicate replies
    if last_message == last_processed:
        time.sleep(2)
        continue

    # Avoid replying to yourself (basic check)
    if last_message.lower().startswith("you:"):
        time.sleep(2)
        continue

    # Optional: stop condition
    if "exit_bot" in last_message.lower():
        print("Stopping bot...")
        break

    # Step 7: Generate AI reply
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are Pranya, an Indian coder who speaks Hindi and English casually."
            },
            {
                "role": "user",
                "content": last_message
            }
        ]
    )

    response = completion.choices[0].message.content
    pyperclip.copy(response)

    # Step 8: Click input box
    pyautogui.click(855, 955)
    time.sleep(0.7)

    # Step 9: Paste
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

    # Step 10: Send
    pyautogui.press('enter')

    # Step 11: Update last processed message
    last_processed = last_message

    # Step 12: Wait before next loop
    time.sleep(3)