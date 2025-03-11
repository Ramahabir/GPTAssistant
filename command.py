import os

def execute_command(command):
    if "open_chrome" in command:
        print("Opening Chrome")
        os.system("start chrome")
    elif "shutdown" in command:
        print("Shutting down")
        os.system("shutdown /s /t 1")
    elif "volume_up" in command:
        print("Volume up")
        os.system("nircmd.exe changesysvolume 2000")
    elif "volume_down" in command:
        print("Volume down")
        os.system("nircmd.exe changesysvolume -2000")
    elif "mute" in command:
        print("Mute")
        os.system("nircmd.exe mutesysvolume 1")
    elif "unmute" in command:
        print("Unmute")
        os.system("nircmd.exe mutesysvolume 0")
    elif "stop" in command:
        return "stop"
    else:
        print("Unrecognized command")
    