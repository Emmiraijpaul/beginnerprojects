import random
def main():
    level = get_level()
    count = 0
    total = 0
    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        question = (input(str(x) + ' + ' + str(y) + '= '))
        if question == str(x+y):
            total += 1
        else:
            try:
                int(question)
            except ValueError:
                print("EEE")
            else:
                print("EEE")
            trial = 0
            while trial < 2:
                question = (input(str(x) + ' + ' + str(y) + '= '))
                if question == str(x+y):
                    total += 1
                    break
                else:
                    try:
                        int(question)
                    except ValueError:
                        print("EEE")
                        trial += 1
        
                    else:
                        print("EEE")
                        trial += 1
                
                    if trial == 2:
                        print(f"correct answer is {x+y}")
                        break
        count += 1
        if count == 10:
            print(f"Total score is {total}")



def get_level():
    while True:
        ask = (input("Level: "))
        if ask not in ['1','2','3']:
            continue
        else:
            return ask
        

def generate_integer(ask):

    try:
        valid_entry = int(ask)
    except ValueError:
        print("Invalid Level")
    else:
        level1 = 10 
        level2 =  50
        level3 = 100
        
        if valid_entry == 1:
            return random.randint(1, int(level1))
        elif valid_entry == 2:
            return random.randint(10, int(level2))
        else:
            return random.randint(50, int(level3))
    


if __name__ == "__main__":
    main()
