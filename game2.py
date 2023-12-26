import random as r

print("Welcome to the word challenge game.\n Do you want to add to the word bank or play the game?\n Input 'Add' or 'Play'")
welcome = input("Response: ").strip().lower()
if welcome == 'add':
    try:
        while True:    
            word =str(input("Welcome! Please input words from 4 letters upwards: "))
            if len(word) <= 6:
                with open("six_letter.txt", 'a') as file1:
                    file1 = file1.write(f"{word}\n")

            elif len(word) <= 10:
                with open("ten_letter.txt", "a") as file2:
                    file2 = file2.write(f"{word}\n")

            else:
                with open("complex_word.txt", "a") as file3:
                    file3 = file3.write(f"{word}\n")
                    
    except EOFError as e:
        print(e)

elif welcome == "play":
    def main():
        word = get_level()
        count = 0
        total = 0
        while count < 10:
            one_word = r.choice(word)
            listed_word = [char for char in one_word]
            r.shuffle(listed_word)
            shuffled = ""
            for i in listed_word:
                shuffled += i
            question = input(str(shuffled) + " = ").lower()
            try:
                str(question)
            except ValueError:
                print("Invalid answer")
            else:
                if question == one_word:
                    print("Well done English Guru")
                    total += 1                   
                else:
                    trial = 0
                    while trial < 2:
                        question = input(str(shuffled) + " = ").lower()
                        if question == one_word:
                            print("Well done English Guru")
                            total += 1
                            break
                        else:
                            try:
                                str(question)
                            except ValueError:
                                print("Invalid answer")
                                trial += 1
                            else:
                                trial += 1
                        if trial == 2:
                            print(f"Right answer is {one_word}")
                            break
            count += 1
            if count == 10:
                print(f" Total score is {total}")
        


    def get_level():
        while True:
            level = input("Please input a level: ")
            try:
                int(level)
            except ValueError:
                print("Not valid entry")
                continue
            else:
                words = []
                if level == '1':
                    with open("six_letter.txt") as file1:
                        for line in file1:
                            words.append(line.rstrip().lower())
                elif level == '2':
                    with open("ten_letter.txt") as file2:
                        for line in file2:
                            words.append(line.rstrip().lower())
                elif level == '3':
                    with open("complex_word.txt") as file3:
                        for line in file3:
                            words.append(line.rstrip().lower())   
                else:
                    continue
            return words
        
        
    if __name__  == "__main__":
        main()

else:
    print("Not the right response")
    