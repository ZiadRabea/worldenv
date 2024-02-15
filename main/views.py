import sys

from django.shortcuts import render
from django.shortcuts import redirect
import importlib
import sys
# Create your views here.
def home(request):
    return redirect("/run/طباعة('أهلاً بالعالم')/Arabic")

def read_code(request, code, lang):
    print(code)
    import main.Tokens
    main.Tokens.set_lang(f"{lang}_KW")
    print(main.Tokens.data_dict)
    from main.Interpreter import run
    result, error = run("<stdin>", str(code))
    if error: print(error.as_string())
    else: print(result)
    import main.Interpreter
    del sys.modules["main.Tokens"]
    del sys.modules["main.Lexer"]
    del sys.modules["main.Parser"]
    del sys.modules["main.RT_result"]
    del sys.modules["main.Interpreter"]
    code = code.replace(" ;", "\n")
    #print(sys.modules)
    return render(request, "page.html", {"code": code, "error": error, "result": result, "lang":lang})
