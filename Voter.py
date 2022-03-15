class Voter:
    identification_number = -1
    candidate = ''
    validation_number = -1
    ctf_public_key = ''

    def __init__(self, identification_number):
        self.identification_number = identification_number 
        pass

    def set_validation_number(self, validation_number):
        self.validation_number = validation_number

    def vote(self):
        if (self.validation_number == -1):
            print("Cannot vote! Need validation number")
        else:
            print('voted')

    def vote_and_val_num(self):
        if (self.validation_number == -1):
            print("Cannot vote! Need validation number")
        else:
            print("")

    def digital_signature(self):
        if (self.validation_number == -1):
            print("Cannot vote! Need validation number")
        else:
            print("Make digital signature")