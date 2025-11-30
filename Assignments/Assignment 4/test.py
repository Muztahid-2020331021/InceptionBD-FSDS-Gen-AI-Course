def remove_common_words(text):
    common_words = ["please", "open", "can", "would", "jarvis", "just", "on", "in"]
    for i in common_words:
        if i in text:
            text = text.replace(i, "")
    return text

text = input("Enter text: ")
text = remove_common_words(text)
# search football on google
print(text)