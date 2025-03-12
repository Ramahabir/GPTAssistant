from gptChat import get_command_respond
from command import execute_command
from speechtotext import recognize_from_microphone
from txttospeech import text_to_speech


while True:
    # get text
    recognized_text = recognize_from_microphone()

    # get command and response
    cmd, resp = get_command_respond(recognized_text)
    print(f"Command: {cmd}")
    print(f"Response: {resp}")

    if cmd is None or resp is None:
        print("Adinda didn’t understand that.")
        continue  # Skip to the next loop iteration instead of crashing

    # execute command
    execute_command(cmd)

    # text_to_speech
    text_to_speech(resp)


