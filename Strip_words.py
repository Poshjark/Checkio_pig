VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import time

def checkio(text):
    import re
    a = 0
    text = re.split('\W', text)
    template_one = '(.*)?' + ('('+'|'.join(list(VOWELS))+')') * 2 + '(.*)?'
    template_two = '(.*)?' + ('('+'|'.join(list(CONSONANTS))+')') * 2 + '(.*)?'
    for word in text:
        if len(word) > 1:
            vow = re.match(template_one , word, re.IGNORECASE)
            cons = re.match(template_two , word, re.IGNORECASE)
            digits = re.match('.*?[0-9].*?', word)
            #print(vow,cons,digits)
            if vow is None and cons is None and digits is None:
                a += 1
    return a

if __name__ == '__main__':
    start = time.time()
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("1 2 3 12 13") == 0, "0"
    print(time.time()- start)
