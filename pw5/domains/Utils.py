from fileinput import fileno
from zipfile import ZipFile
import json
import os

class Utils:
    # Ask the user to input a number
    def input_number(unit):
        return int(input(f"Enter the number of {unit} in this class: "));

    # Display a list of items
    def display(dct):
        for i, item in enumerate(dct.values()):
            print(str(i+1) + ".", end=" ")
            print(item)

    # Ask the user to enter an integer to select an option
    def select(option_range, input_message="Choose an option: "):
        selection = input(input_message)
        if not selection.isnumeric():
            return -1
        selection = int(selection)
        if selection not in option_range:
            return -1
        return selection

    # Pause the program
    def pause():
        input("Press Enter to continue...")

    def save(filename, obj_list):
        with open(filename, "w") as f:
            for obj in obj_list:
                f.write(repr(obj))
    
    def load(filename):
        data = ""
        try:
            with open(filename, "r") as f:
                data = f.readlines()
        except FileNotFoundError:
            pass
        return data
    
    def load_json(filename):
        data = {}
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        return data
    
    def save_json(filename, data):
        with open(filename, "w") as f:
            f.write(json.dumps(data))
    
    def zipfiles(zipname, files):
        try:
            with ZipFile(zipname, 'w') as z:
                for file in files:
                    z.write(file)
            print(f"All files are zipped in {zipname} successfully!")
        except FileNotFoundError:
            pass
    
    def extract(zipname):
        try:
            with ZipFile(zipname, 'r') as z:
                z.extractall()
        except FileNotFoundError:
            pass
    
    def remove_file(filename):
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass