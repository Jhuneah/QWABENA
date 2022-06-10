word=input("Enter a word: ").lower()
cup={}
for letter in word:
    if letter not in cup:
        cup[letter]=1
    else:
        cup[letter]+=1

print(cup.items())

import webbrowser
webbrowser.open_new("www.google.com")