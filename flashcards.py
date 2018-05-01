import yaml
import random

def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
        return data

def yaml_dump(filepath, data): # Don't actually need this function
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

def meta_flag_checker(meta_list):
    for i in meta_list:
        if meta_list[i] == False:
            return 1

print("Welcome to Flashfacts!")
print("\n")
filepath = input("What is the name of the card pack you wish to study? ")

# loads user chosen yaml file in to dict
data = yaml_loader(filepath)

# creates lists that the yaml file will be sorted in to
question_list = []
ans_list = []

# sorts questions and answers in to their own lists
for values in data.values():
    ans_list.append(values)

for items in data:
    question_list.append(items)

# allows randomization of both lists but they keep the same relative order
zipped = list(zip(question_list, ans_list))
random.shuffle(zipped)

# unzip previous list
rand_question, rand_answer = zip(*zipped)

# list to hold flag that determines if an answer has been answered correctly.
meta_list = []
# sets all values in meta_list to False.
for i in range(len(question_list)):
    meta_list.append(False)


flag = True
while flag:
    for i in range(len(question_list)):
        if meta_list[i] == False:
            answer = input(rand_question[i])
            if answer == rand_answer[i]:
                print("correct")
                meta_list[i] = True
            else:
                print("incorrect")
                print(rand_answer[i])
                meta_list[i] = False
    #i = 0
    if meta_flag_checker(meta_list) != 1:
        flag = False

meta_list = []