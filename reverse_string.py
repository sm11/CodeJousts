def reverse_char(word, start, end):

    s = list(word)
    while start < end:
        s[start], s[end] = word[end], word[start]
        start += 1
        end -= 1
    s = "".join(x for x in s)
    print (s)
    return s

def reverse(word, start, end):
    while start < end:
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1
    



# def reverse_sentence(sentence):
#     sent = sentence.split()
#     return (" ".join(reverse_char(w,0, len(w)-1) for w in reverse(sent, 0, len(sent)-1)))
    # sent = " ".join(reverse(w, 0, len(w)-1) for w in sentence.split())
    # return reverse(sentence.split(), 0, len(sentence-1))


def reverse_sentence(sentence):
    start = 0
    end = 0

    reverse(sentence, start, len(sentence)-1)
    for idx, val in enumerate(sentence):
        start = end
        if val == " ":          
            end = idx - 1
            reverse(sentence, start, end)
            end += 2
        elif idx == len(sentence)-1:
            end = idx
            reverse(sentence, start, end)
    return "".join (s for s in sentence)

    # sent = sentence.split()
    # return (" ".join(reverse_char(w,0,len(w)-1) for w in reverse(sent, 0, len(sent)-1)))
    

if __name__ == "__main__":
    s = "This is a sentence."
    c = "The quick brown fox jumped over the lazy dog."
    a = "Hello World!"
    print (reverse_sentence(list(a)))
    print (s[::-1])