import speech_recognition as sr
listener=sr.Recognizer()
va_name='hey ram'
try:
    with sr.Microphone() as source:
        print('listening.....')
        voice=listener.listen(source)
        command = listener.recognize_google(voice)
        command=command.lower()
        if va_name in command:
            command=command.replace(va_name+' ','')
            print(command)
except:
    print("check your microphone")
