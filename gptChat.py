import os
from openai import AzureOpenAI
    
client = AzureOpenAI(
    api_key= os.environ['GPT_API'],  
    api_version="2025-01-01-preview",
    azure_endpoint = os.environ['GPT_ENDPOINT']
    )
    
deployment_name='gpt-4' #This will correspond to the custom name you chose for your deployment when you deployed a model. Use a gpt-35-turbo-instruct deployment. 

def get_command_respond(user_input):
    messages = [
        {"role": "system", "content":   "You are a smart assistant that translates user requests into actions.\n"
                                        "Always respond in this format:\n"
                                        "Command: <action>\n"
                                        "Response: <natural language reply>\n\n"
                                        "Example:\n"

                                        "User: 'Hey Jarvis, make the volume louder!'\n"
                                        "Command: turn_up_volume\n"
                                        "Response: Okay, turning up the volume.\n\n"
                                        
                                        "User: 'Hey Jarvis, open Chrome!'\n"
                                        "Command: 'open_chrome'\n"
                                        "Response: 'Okay, opening Google Chrome.'\n\n"

                                        "User: 'Hey Jarvis, shut down the computer!'\n"
                                        "Command: 'shutdown'\n"
                                        "Response: 'Alright, shutting down the computer.'\n\n"

                                        "User: 'Hey Jarvis, increase the volume!'\n"
                                        "Command: 'volume_up'\n"
                                        "Response: 'Sure, increasing the volume.'\n\n"

                                        "User: 'Hey Jarvis, decrease the volume!'\n"
                                        "Command: 'volume_down'\n"
                                        "Response: 'Got it, lowering the volume.'\n\n"

                                        "User: 'Hey Jarvis, mute the sound!'\n"
                                        "Command: 'mute'\n"
                                        "Response: 'Muting the system volume.'\n\n"

                                        "User: 'Hey Jarvis, stop'\n"
                                        "Command: 'stop'\n"
                                        "Response: 'stop assisting person'\n\n"

                                        "User: 'Hey Jarvis, unmute the sound!'\n"
                                        "Command: 'unmute'\n"
                                        "Response: 'Unmuting the system volume.'\n\n"},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model=deployment_name, # model = "deployment_name".
        messages=messages,
        max_tokens=50
    )

    output_text = response.choices[0].message.content.strip()

    lines = output_text.split('\n')
    command = None
    response = None

    for line in lines:
        if line.startswith("Command:"):
            command = line.replace("Command:", "").strip()
        elif line.startswith("Response:"):
            response = line.replace("Response:", "").strip()
    
    return command, response
