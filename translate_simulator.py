import os.path


words = []
lan_list = ['english' , 'persian']
choose = 0

def load():        
    if os.path.isfile('translate.txt'):
        myfile = open ('translate.txt' , 'r')
        data = myfile.read()
        data_list = data.split('\n')
        for i in range (len(data_list)-1):
            word_info = data_list[i].split(',')
            word_dict = {'english': word_info[0], 'persian': word_info[1]}
            words.append(word_dict)
    else:
        print ("file does not exist! please enter valid address & restart the program.",'\n')
        exit()
          
def add_word():
    en_word = input("word in english:")
    pe_word = input("word in persian:")
    mydict = { 'english' : en_word , 'persian' : pe_word}
    words.append(mydict)
    print("the word added!")
    save()
    menu()

def translate():
    
    count = ''
    list = []
    a = input()
    
    if '.' in a:
        sentence = a.split('.')
        for i in range(len(sentence)):
            list1 = sentence[i].split(' ')
            list.append(list1)
            flag = 1
        for j in range(len(list)):
            for l in range(len(list[j])):
                for k in range(len(words)):
                    if list[j][l] == words[k][lan_list[0]]:
                        count = count + ' ' + (words[k][lan_list[1]])
                        flag = 0
                if flag == 1:
                    count = count + ' ' + list[j][l]
            count = count + '.'
        print(count)
    else:
        list = a.split(' ')
        for i in range(len(list)):
            for k in range(len(words)):
                if list[i] == words[k][lan_list[0]]:
                    count = count + ' ' + (words[k][lan_list[1]])
                    flag = 0
            if flag == 1:
                count = count + ' ' + list[i]
        count = count + '.'
        print(count)
           
def save():
    f = open('translate.txt', 'w')
    for i in range(len(words)):
        row = words[i]['english'] + ',' + words[i]['persian'] + '\n'
        f.write(row)
    f.close()

def menu():
        print("1-Add new word")
        print("2-Translation English to persian")
        print("3-Translation persian to english")
        print("4-Exit")
        choose = int(input('Select:'))
        if choose == 1:
            add_word()
        elif choose == 2:
            print('enter a world or sentence in English:')
            translate()
        elif choose == 3:
            print('enter a world or sentence in Persian:')
            lan_list[0] , lan_list[1] = lan_list[1] , lan_list[0]
            translate()
        elif choose == 4:
                save()
                exit()
        else:
                print("Wrong input! Try again")
                menu() 
                    
load()
menu()