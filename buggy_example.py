class PythonCalc:
    def __init__(self, memory=[]): 
        self.memory = memory

    def __call__(self, expression):
        self.memory.append(expression)

        match expression:
            case PythonCalc(): 
                return eval(str(expression)) 
            
            case str() if "calc" in expression:
                context = {"calc": self, "__builtins__": {}}
                return eval(expression, context)
            
            case _:
                return eval(str(expression))

calc = PythonCalc()

print("Начинаем вычисление.")
result = calc("calc(calc)")
print(result)
