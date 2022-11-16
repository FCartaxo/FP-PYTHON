
string_stop = 'chupacabra'

while True:
    user_word = input("Enter a string:\n")

    if user_word == string_stop:
        print("Your string:", user_word)
        break
    print("Your string:", user_word)

print("Saiste do loop com sucesso!!!")
