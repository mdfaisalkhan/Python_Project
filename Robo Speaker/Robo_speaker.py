import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Enter text to speak (or type 'exit' to end):")
while True:
    try:
        s = input()

        if s.lower() == 'exit':
            speaker.Speak("Exiting code")
            break

        if s.strip():  
            speaker.Speak(s)
        else:
            print("Please enter some text.")
    except Exception as e:
        print(f"An error occurred: {e}")
