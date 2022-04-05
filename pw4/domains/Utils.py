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
