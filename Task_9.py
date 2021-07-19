def my_function():
    text = input("Enter a word: ")
    text_reverse = text[::-1]
    if text == text_reverse:
        print("Yes")
    else:
        print("No")
my_function()