import os
import time

def set_volume(level):
    """Convert 0 - 100 to 0 - 65535"""
    volume_value = int((level/100) * 65535)
    os.system(f"nircmd.exe setsysvolume {volume_value}")
    print(f"Volume set to {level}%")

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
    elif "set_volume_50" in command:
        print("Setting Volume to 50%")
        set_volume(50)
    elif "mute" in command:
        print("Mute")
        os.system("nircmd.exe mutesysvolume 1")
    elif "unmute" in command:
        print("Unmute")
        os.system("nircmd.exe mutesysvolume 0")
    elif "open_youtube" in command:
        print("Opening Youtube")
        os.system("start chrome https://www.youtube.com/")
    elif "check_time" in command:
        print("Getting time")
        current_time = time.strftime("%H:%M:%S")
        print(f"Current time is {current_time}")
    elif "stop" in command:
        return "berhenti"
    else:
        print("Unrecognized command")
    