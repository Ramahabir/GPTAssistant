import os
import azure.cognitiveservices.speech as speechsdk

sp_key = os.environ['sp_key']
sp_region = os.environ['sp_region']

speech_config = speechsdk.SpeechConfig(subscription=sp_key, region=sp_region)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_config.speech_synthesis_voice_name='id-ID-GadisNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

def text_to_speech(text):
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
    

