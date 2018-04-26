import yaml

def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
        return data

def yaml_dump(filepath, data): # Don't actually need this function
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

#def dict_parser(data):


print("Welcome to Flashfacts!")
print("\n")
filepath = input("What is the name of the card pack you wish to study? ")


data = yaml_loader(filepath)


question_list = []
ans_list = []

for values in data.values():
    ans_list.append(values)

for items in data:
    question_list.append(items)

print(question_list)
print(ans_list)


