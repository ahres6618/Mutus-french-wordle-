import unicodedata
import random
import numpy as np



def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


def list_of_word():

    with open('French-Dictionary-master/dictionary/verbs.txt',encoding = "UTF-8") as f:
        verb_lines = f.readlines()
        
    with open('French-Dictionary-master/dictionary/pronouns.txt',encoding = "UTF-8") as f:
        pron_lines = f.readlines()
        
    with open('French-Dictionary-master/dictionary/prepositions.txt',encoding = "UTF-8") as f:
        prepo_lines = f.readlines()
        
    with open('French-Dictionary-master/dictionary/nouns.txt',encoding = "UTF-8") as f:
        nouns_lines = f.readlines()
        
    with open('French-Dictionary-master/dictionary/dictionary.txt',encoding = "UTF-8") as f:
        dict_lines = f.readlines()
        
    with open('French-Dictionary-master/dictionary/determiners.txt',encoding = "UTF-8") as f:
        det_lines = f.readlines()
        
        
    with open('French-Dictionary-master/dictionary/conjunctions.txt',encoding = "UTF-8") as f:
        conj_lines = f.readlines()
        
        
    with open('French-Dictionary-master/dictionary/adverbs.txt',encoding = "UTF-8") as f:
        adv_lines = f.readlines()
        
    with open('French-Dictionary-master/dictionary/adjectives.txt',encoding = "UTF-8") as f:
        adj_lines = f.readlines()


    verbs = []
    pronouns = []
    prepo = []
    nouns = []
    dictio = []
    determ = []
    conj = []
    adv = []
    adj = []

    for line in verb_lines:
        verbs.append(line.split(';')[0])
        
    for line in pron_lines:
        pronouns.append(line.split(';')[0])   
        
    for line in prepo_lines:
        prepo.append(line.split(';')[0])  
        
    for line in nouns_lines:
        nouns.append(line.split(';')[0])
        
    for line in dict_lines:
        dictio.append(line.split(';')[0])
        
    for line in det_lines:
        determ.append(line.split(';')[0])
        
    for line in conj_lines:
        conj.append(line.split(';')[0])
        
    for line in adv_lines:
        adv.append(line.split(';')[0])
        
    for line in adj_lines:
        adj.append(line.split(';')[0])


    full_list = verbs + pronouns + prepo + nouns + dictio + determ + conj + adv + adj
    full_clean = []
    for i in full_list:
        full_clean.append(strip_accents(i.split('\n')[0]))


    good_list = list(set(full_clean))


    list_five_letters_words = []

    for word in good_list:
        if len(word) == 5:
            list_five_letters_words.append(word)

    return list_five_letters_words


def starting_word(user_input,list_five_letters_words):
    if user_input not in list_five_letters_words:
        print("Le premier mot entré n'existe pas")
       # return first_word(list_five_letters_words)
    else:
        letter_one = random.choice(user_input)
        all_words_selected = [word for word in list_five_letters_words if letter_one in word]

        selected_word = np.random.choice(all_words_selected,1)[0]
        return selected_word
selected_words=[]

def random_words(list_five_letters_words):

    selected_word = np.random.choice(list_five_letters_words,1)[0]
    return selected_word



def check_word(word,list_of_word):
    return word  in list_of_word

def color_outcome(user_entries, selected_word, list_five_letters_words):
    color_result = []
    if user_entries not in list_five_letters_words:
        print("Ce mot n'existe pas")
    else:
       
        for i in range(5):
            if user_entries[i] == selected_word[i]:
                color_result.append([user_entries[i],'g'])
            elif (user_entries[i] in selected_word) and (user_entries[i] != selected_word[i]):
                color_result.append([user_entries[i],'y'])
            else :
                color_result.append([user_entries[i],'b'])
        
    return color_result

if __name__ == "__main__":
#    user_input = 'hello'
    list_five_letters_words = list_of_word()
#    selected_word = starting_word(user_input,list_five_letters_words)
#    print(color_outcome(user_input, selected_word ,list_five_letters_words))
