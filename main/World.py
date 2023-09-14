import Interpreter
import json
import os
import sys
if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))

while True:
    text = input('World >> ')
    if text == "libman":
        path = app_path.replace('\\', '/')
        result, error = Interpreter.run('<stdin>', f"world('{path}/libman.world')")
        if error:
            print(error.as_string())
        elif result:
            print(u"{}".format(result))
    elif text == "langman":
        path = app_path.replace('\\', '/')
        result, error = Interpreter.run('<stdin>', f"world('{path}/langman.world')")
        if error:
            print(error.as_string())
        elif result:
            print(u"{}".format(result))
    elif text == "ai":
        print("It seems like you're using the educational of World Language, please make sure to download the practical version : https://cszido.github.io/worldlang")
    else:
        result, error = Interpreter.run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            print(u"{}".format(result))
