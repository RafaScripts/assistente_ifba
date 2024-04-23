import threading
import speech_recognition as sr
from nltk import word_tokenize, corpus
from src.executate import exec_cmd_open, exec_cmd_close, suspend
import json

LANGUAGE_CORPUS = "portuguese"
LANGUAGE_SPEECH = "pt-BR"
CONFIG_PATH = "/Users/rafael/Desktop/inteArti/iaavaliativa/src/config.json"

def init():
    global recognizer
    global stop_words
    global assistent_name
    global actions

    inited = False

    recognizer = sr.Recognizer()
    try:
        stop_words = set(corpus.stopwords.words(LANGUAGE_CORPUS))

        with open(CONFIG_PATH, "r") as config:
            config = json.load(config)
            assistent_name = config["nome"]
            actions = config["acoes"]

        inited = True
    except:
        inited = False

    return inited, recognizer, stop_words, assistent_name, actions

def listen():
    global recognizer

    comand = None
    have_speach = False

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        print('Escutando...')

        speech = recognizer.listen(source, timeout=5)

        try:
            comand = recognizer.recognize_google(speech, language=LANGUAGE_SPEECH)
            have_speach = True
        except sr.UnknownValueError:
            pass

        return have_speach, comand

def process_sound_test(source_file, recognizer):
    have_speach = False

    with sr.AudioFile(source_file) as source:
        speach = recognizer.listen(source)

        try:
            comand = recognizer.recognize_google(
                speach, language=LANGUAGE_SPEECH
            )
            have_speach = True
        except:
            ...

    return have_speach, comand

def process_sound(comand_source):
    global recognizer

    comand = None
    have_comand = False

    with sr.AudioFile(comand_source) as source:
        speach = recognizer.listen(source)

        try:
            comand = recognizer.recognize_google(speach, language=LANGUAGE_SPEECH)
            have_comand = True
        except sr.UnknownValueError:
            pass

    return have_comand, comand

def process_text(tokens):
    global stop_words

    tokens_flitred = []

    for token in tokens:
        if token not in stop_words:
            tokens_flitred.append(token)

    return tokens_flitred

def tokenize(comand):
    global assistent_name

    name, action, object = None, None, None

    tokens = word_tokenize(comand, LANGUAGE_CORPUS)
    if tokens:
        tokens = process_text(tokens)

        if len(tokens) >= 3:
            if assistent_name == tokens[0].lower():
                name = tokens[0].lower()
                action = tokens[1].lower()
                object = tokens[2].lower()

    return name, action, object



def validate_command(action, object):
    global actions

    valid = False

    if action and object:
        for actionSign in actions:
            if action == actionSign["nome"]:
                if object in actionSign["objetos"]:
                    valid = True
                    break

    return valid

def exec_command(action, object):
    print("Executando " + action, object)
    works = False
    ac = object.split(" ")
    if action == "abrir":
        executed = exec_cmd_open(ac[2])

        if executed:
            works = True
    elif action == "fechar":
        executed = exec_cmd_close(ac[2])
        if executed:
            works = True
    elif action == "acionar":
        executed = suspend()
        if executed:
            works = True

    return works

def command_processor():
    while True:
        try:
            have_speach, command = listen()

            print(f"Processing command: {command}")

            if have_speach:
                if command:
                    name, action, object = tokenize(command)
                    valid = validate_command(action, object)
                    if not valid:
                        print(f"Invalid command: {command}")
                    else:
                        works = exec_command(action, command)
                        if not works:
                            print(f"comando não executado: {command}")

        except KeyboardInterrupt:
            print('Foi sem querer querendo')
            break

if __name__ == "__main__":
    init()

    # Iniciando o processador de comandos em uma thread separada
    command_thread = threading.Thread(target=command_processor)
    command_thread.start()

    # Esperando a thread do processador de comandos terminar
    command_thread.join()
