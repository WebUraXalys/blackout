import re


def validate(buildings):
    validated = []
    for b in buildings:
        b = re.sub('[-,. ]', "", b)  # Remove following characters, space included
        length = len(b)
        if length > 3:
            letters = 0
            for char in b:
                if char.isalpha(): letters += 1
                if letters > 2: break
            if letters < 2:
                b = b.lower()
                validated.append(b)
        elif length >= 1:
            b = b.lower()
            validated.append(b)
    return validated
