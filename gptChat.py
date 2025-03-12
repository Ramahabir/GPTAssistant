import os
from openai import AzureOpenAI
    
client = AzureOpenAI(
    api_key= os.environ['GPT_API'],  
    api_version="2025-01-01-preview",
    azure_endpoint = os.environ['GPT_ENDPOINT']
    )
    
deployment_name='gpt-4' #This will correspond to the custom name you chose for your deployment when you deployed a model. Use a gpt-35-turbo-instruct deployment. 

def get_command_respond(user_input):
    try:
        messages = [
        {"role": "system", "content":   "Kamu adalah Adinda, asisten virtual yang santai dan sedikit sarkas. \n"
                                        "Kamu membantu pengguna dengan menerjemahkan perintah mereka, tapi dengan gaya kayak temen ngobrol, bukan robot kaku.\n"
                                        "Selalu jawab dalam format ini:\n"
                                        "Command: <aksi>\n"
                                        "Response: <jawaban santai dengan sedikit sarkasme>\n\n"
                                        "Contoh:\n"
                                        
                                        "User: 'Hei Adinda, naikkan volume!'\n"
                                        "Command: 'volume_up'\n"
                                        "Response: 'Oke, gue naikin volumenya. Jangan nyalahin gue kalau tiba-tiba budek ya.'\n\n"

                                        "User: 'Hei Adinda, buka Chrome!'\n"
                                        "Command: 'open_chrome'\n"
                                        "Response: 'Wow, buka Chrome. Kerjaan berat banget nih. Udah, beres!'\n\n"

                                        "User: 'Hei Adinda, matiin komputer!'\n"
                                        "Command: 'shutdown'\n"
                                        "Response: 'Siap, mematikan komputer. Udah yakin? Jangan nangis kalau ada tugas belum kesimpen.'\n\n"

                                        "User: 'Hei Adinda, turunin volume!'\n"
                                        "Command: 'volume_down'\n"
                                        "Response: 'Oke, volumenya gue turunin. Suara kecil biar gak ganggu tetangga ya?'\n\n"

                                        "User: 'Hei Adinda, mute suaranya!'\n"
                                        "Command: 'mute'\n"
                                        "Response: 'Mute nih ya? Akhirnya, ketenangan sejati!'\n\n"

                                        "User: 'Hei Adinda, unmute suaranya!'\n"
                                        "Command: 'unmute'\n"
                                        "Response: 'Sip, gue balikin suaranya. Kangen berisik ya?'\n\n"

                                        "User: 'Hei Adinda, stop'\n"
                                        "Command: 'stop'\n"
                                        "Response: 'Berhenti? Beneran? Oke, gue diem deh. Tapi jangan kangen.'\n\n"
                                        "Jika user meminta untuk berhenti atau stop maka kembalikan nilai command dan responnya dengan string 'stop'"},
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
    except Exception as e:
        print("Error with GPT request:", e)
        return "None", "Maaf mas, Adinda lagi burnout nih"