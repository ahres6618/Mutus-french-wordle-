from word_game import list_of_word, starting_word, color_outcome, check_word, random_words
from flask import Flask, render_template, request

app = Flask(__name__)


list_five_letters_words = list_of_word()

print(list_five_letters_words)


wordle = random_words(list_five_letters_words)


word=''
#HERE WORDS LIST AND THE CHOSEN WORD ARE SENT TO THE FIRST AND THE SECOND LINE OF OUR JAVASCRIPT FILE
a_file = open("static/js/script.js", "r")
list_of_lines = a_file.readlines()

list_of_lines[0] = f'var guessList = {str(list_five_letters_words)} \n'
list_of_lines[1] = f'var word = "{str(wordle)}" \n'

a_file = open("static/js/script.js", "w")
a_file.writelines(list_of_lines)
a_file.close()

@app.route('/',methods=['GET','POST'])
def hello_world():

    if request.method=="POST":
        word_=str(request.get_data())
        if not word_:
            resultat='gggg'
            return render_template('base.html', resultat=resultat)
        else:

            word=word_[2:7]
            row=word_[-2]


            print(word)
            print(row)
            resultat = color_outcome(word,wordle , list_five_letters_words)
            print(resultat)
            a=True


            #temp(resultat,a)
    return render_template('base.html')




if __name__ == '__main__':
    app.run()
