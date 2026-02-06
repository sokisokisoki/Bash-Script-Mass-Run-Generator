'''
run script input amount of parameters
then put different options needed to be added to the bash script
i.e:
    python3 massRunScript.py
    Name of executable: [name]
    Amount of fields; [num]
    Options for field x: [opt1, opt2, opt3, ...]
    Options for field y: [opt1, opt2, opt3, ...]
    ...
    Bash Script Name: [name (no .sh)]
'''

def product(*args):
    if not args:
        return iter(((),)) # yield tuple()
    return (items + (item,) 
            for items in product(*args[:-1]) for item in args[-1])


print("Welcmoe to Parallel Programming Mass Run Script")

# Can lowkey start the bash script with a compile so you can all in one?

execName = str(input("What do you want to name your nvcc executable: "))
fieldCount = int(input("How many fields does the program require: "))
fieldOpt = []


for i in range(fieldCount):
    currFieldOpts = str(input(f"Options for field {i+1}: "))
    # split csv values into a list and add to fieldOpt list
    sepList = [item.strip() for item in currFieldOpts.split(',')]

    fieldOpt.append(sepList)

scriptName = str(input("What do you want to name your bash script: "))


if scriptName[-3:] != ".sh":
    scriptName += ".sh"

trackIdfk = 0
with open(scriptName, "w") as script:
    perms = product(*fieldOpt)
    for item in perms:
        sep = ' '
        script.write(f"./{execName} {sep.join(item)}\n")
        trackIdfk+=1

print(f"\n{trackIdfk} commands written!\n\nFile '{scriptName}' succesfully created!\n\nNow use 'chmod +x {scriptName}' to run.")

# option to add a pipe into an output file/files
# >> out.tx
# >> run1.txt
# >> run2.txt
# ...
# >> runN.txt
