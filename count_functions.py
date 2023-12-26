import sys

print("Welcome!\n This program counts the number of functions in a python program.")


def main():
    python_code = "Please, input a python program \n"
    functs = number_functions(python_code)
    if len(functs) == 0:
        print("No function found")
    elif len(functs) == 1:
        print(f"The only function found is\n {functs}")
    else:
        print(f"Below are the functions found")
        for funct in functs:
            print(funct)

def number_functions(prompt):
    program = input(prompt)
    functions = []
    if program.endswith("py"):
        try: 
            with open(program) as file:
                for line in file:
                    if line.strip().startswith("def"):
                        line = line.lstrip().removeprefix("def ")
                        line = line.rstrip().removesuffix(":")
                        functions.append(line)
                    else:
                        continue

        except FileNotFoundError:
            sys.exit("File does not exist")

    else:
        sys.exit("Not a python file")

    return functions

if __name__ == "__main__":
    main()
