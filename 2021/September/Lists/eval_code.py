# Code injection attack
# __import__('subprocess').getoutput('start msedge.exe')


def _eval(input_string):
     code = compile(input_string, "<string>", "eval")
     if code.co_names:
         raise NameError("Use of names not allowed")
     return eval(code, {"__builtins__": {}}, {})

l = _eval(input("Enter list: "))

print(l)
