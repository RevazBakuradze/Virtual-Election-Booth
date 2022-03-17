class Val_Num_Vote:
    candidate = ''
    validation_number = -1

    def __init__(self):
        pass

    def __init__(self, candidate, validation_number):
        self.candidate = candidate
        self.validation_number = validation_number
        pass

    # Getter method for CTF to update tally
    def get_candidate(self, string: str):
        arr = []
        arr = string.split("#")
        return arr[0] 

    # Getter mathod for CTF to make the list of voters
    def get_validation_number(self, string):
        arr = []
        arr = string.split("#")
        return int(arr[1])

    def generate_str(self):
        return str(self.candidate) + "#" + str(self.validation_number)