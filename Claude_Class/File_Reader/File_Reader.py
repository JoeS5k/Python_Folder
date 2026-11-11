import string

with open("Test2.txt", encoding="utf-8") as file:
    content = file.read()
    word_count = {}
    for word in content.split():
        word = word.lower().strip(string.punctuation)
        if word != "":
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    word_count_sorted = sorted(word_count.items(),  key=lambda x: x[1], reverse = True)
    for word, count in word_count_sorted[:10]:
        print(f"{word}: {count}")