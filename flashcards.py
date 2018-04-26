import yaml

def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
        return data

def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

print("Welcome to Flashfacts!")
print("\n")
filepath = input("What is the name of the card pack you wish to study? ")


data = yaml_loader(filepath)
for x in data:
    print(x)




# def open_proj():
#
#
