#program 1
message=input(">")
def function():
    words=message.split(" ")
    emojis={
    ":)": "😊",
    ":(": "😔"
    }
    output=""
    for word in words:
        output += emojis.get(word,word) +" "
    print(output)

function()

#program2
def emoji_converter(message):
    words=message.split(" ")
    emojis={
    ":)": "😊",
    ":(": "😔"
    }
    output=""
    for word in words:
        output += emojis.get(word,word) +" "
    return output

message=input(">")
print(emoji_converter(message))


