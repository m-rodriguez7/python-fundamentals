
sentence = input("Enter a sentence: ").replace(" ","").strip()

result = {"Upper case":0,"Lower case":0,"Punctuation":0,"Total chars":0}

result["Total chars"] = len(sentence)

for char in sentence:
    if(char.isupper()):
        result["Upper case"] += 1
    elif(char.islower()):
        result["Lower case"] += 1
    elif(not char.isalpha()):
        result["Punctuation"] += 1

for key,value in result.items():
    print(key + ':',value)
