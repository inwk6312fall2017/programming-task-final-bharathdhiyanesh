open_file = open("Book1.txt", 'r')
    words_list =[]
    contents = open_file.readlines()
    for i in range(len(contents)):
         words_list.append(contents[i].strip('\n'))
    return words_list    
    open_file.close()  

for word in words_list:
        if lalen<len(word):
            lalen=len(word)
            laWord=word
print "The longest word in the list is %s." % laWord


fin= open("Book2.txt", 'r')
    words_lists =[]
    content = fin.readlines()
    for i in range(len(content)):
         words_lists.append(content[i].strip('\n'))
    return words_lists    
    fin.close()  

for word in words_lists:
        if lalen<len(word):
            lalen=len(word)
            laWord=word
print "The longest word in the words_lists is %s." % laWord


f = open("Book1.txt", 'r')
    word_list =[]
    cont = f.readlines()
    for i in range(len(cont)):
         word_list.append(cont[i].strip('\n'))
    return word_list    
    f.close()  

for word in word_list:
        if lalen<len(word):
            lalen=len(word)
            laWord=word
print "The longest word in the word_list is %s." % laWord


