class InputValidator:
    def __init__(self):
        self.option1 = 1
        self.option2 = 2
        self.valid_inputs = [self.option1, self.option2]

    def get_input(self, question):
        while True:
            user_input = input(question)
            if user_input.isnumeric():
                if int(user_input) in self.valid_inputs:
                    return int(user_input)
                else:
                    print(f"Invalid input. Please enter '{self.option1}' or '{self.option2}'")
            else:
                print(f"Invalid input. Please enter '{self.option1}' or '{self.option2}'")
