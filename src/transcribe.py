import speech_recognition as sr

def transcribe_local_sphinx(audio_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        
    try:
        text = recognizer.recognize_sphinx(audio_data)
        return text
    except sr.UnknownValueError:
        return "Sphinx could not understand the audio."
    except sr.RequestError:
        return "Sphinx error."
