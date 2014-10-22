"""Find a template"""
def __getTemplate( name, input=""):
    startIndex = input.lower().find("{{" + name.lower()) + 2 + len(name)
    length = len(input)
    braces = 0
    result = ""
    for i in range(startIndex, length):
        c = input[i]
        if (c == "{"):
            braces += 1
        elif (c == "}" and braces > 0):
            braces -= 1
        elif (c == "["):
            braces += 1
        elif (c == "]" and braces > 0):
            braces -= 1
        elif (c == "<" and input[i+1] == "!"):
            braces += 1
        elif (c == ">" and braces > 0 and input[i-1] == "-"):
            braces -= 1
        elif (c == "}" and braces == 0):
            result = result.strip()
            parts = result.split("|")
            dict = {}
            counter = 0
            for part in parts:
                part = part.strip()
                kv = part.split("=")
                key = kv[0].strip()
                if (len(key) > 0):
                    val = ""
                    if (len(kv) > 1):
                        val = kv[1].strip().replace("%!%!%", "|").replace("%@%@%", "=")
                    else:
                        val = key;
                        key = counter
                        counter += 1
                    dict[key] = val
            return dict
        elif (c == "|" and braces > 0):
            c = "%!%!%"
        elif (c == "=" and braces > 0):
            c = "%@%@%"
        result += c
