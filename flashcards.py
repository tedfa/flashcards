import yaml

def yaml_loader(filepath):
    with open(filepath, r) as file_descriptor:
        data = yaml.load(file_descriptor)
        return data

def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

print("Welcome to Flashfacts!")
print("\n")
print("To start new project press 1")
print("to open existing project press 2")
item = input(" ")
print("\n")

print("You selected, ")
print(item)


def new_project():
    proj_name = input("Name your project")



def open_proj():


def add_card():
