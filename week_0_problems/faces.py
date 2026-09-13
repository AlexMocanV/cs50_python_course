def emoji_face(list_of_words):
    for i, word in enumerate(list_of_words):
        if word == ":)":
            list_of_words[i] = "🙂"
        if word == ":(":
            list_of_words[i] = "🙁"
    
x = input()
y = x.split()

emoji_face(y)

print(*y)