

def greeting(greeting="Hello", name="World"):
    "returns a greeting"
    return "%s %s!" % (greeting, name)


print(greeting("Greetings", "Jon"))
print(greeting(name="Dave", greeting="Welcome"))
print(greeting())
