from flask import Flask, render_template
import random

root = Flask(__name__)


answer = ''
definition = ''

@root.route("/")
def home():
    global answer, definition
    def_file = open(r'Vocab_Helper\Word_List\definitions.txt', 'r')
    word_file = open(r'Vocab_Helper\Word_List\words.txt', 'r')

    word_list = []
    definition_list = []
    while True:
        w = word_file.readline()[:-1]
        d = def_file.readline()[:-1]
        if w == '':
            break
        word_list.append(w)
        definition_list.append(d)

    word_file.close()
    def_file.close()
    words = []
    num = random.randint(0, len(definition_list) - 1)
    definition = definition_list[num]
    i = num
    print(num, definition)
    while len(words) < 3:
        if word_list[num] not in words:
            words.append(word_list[num])
        num = random.randint(0, len(word_list) - 1)
    random.shuffle(words)
    print(words)
    answer = word_list[i]

    return render_template("index.html", 
        definition=definition, word1=words[0], word2=words[1], word3=words[2], answer=answer)

@root.route("/correct")
def correct():
    return render_template("correct.html")

@root.route("/wrong")
def wrong():
    global answer, definition
    print(answer)
    print(definition)
    return render_template("wrong.html", answer=answer, definition=definition)

if __name__ == "__main__":
    root.run(debug=True)
