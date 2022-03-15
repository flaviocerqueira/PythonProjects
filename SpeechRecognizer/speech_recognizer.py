import speech_recognition as sr


def listen_mic():

    phrase = None

    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Diga algo: ')
        audio = microfone.listen(source)

    try:
        phrase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + phrase)
    except sr.UnknownValueError:
        print('Não entendi')

    return phrase


listen_mic()
