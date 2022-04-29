import speech_recognition as sr

rec_1 = sr.Recognizer()

with sr.Microphone() as source: 
	print('Say something......')
	audio = rec_1.listen(source)

	try:
		text = rec_1.recognize_google(audio)
		print("Recognized Speech: {}".format(text))
	except:
		print("Sorry could not recognize your voice")

