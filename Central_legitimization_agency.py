import random

class Central_legitimimation_agency:
    validation_number_recipient = {}

    def __init__(self):
        pass

    # Used for sending validation number to VOTER
    def send_validation_number(self, recipient):
        num = self.generate_validation_number()
        # if else to make sure user is not duplicated. If user already requested dont give
        self.store_validation_number(num, recipient)
        return num

    def store_validation_number(self, number, recipient):
        # if else to make sure user is not duplicated
        self.validation_number_recipient[recipient] = number

    def generate_validation_number(self):
        random_number = random.randint(1000000000, 9999999999)
        if (not self.validation_number_recipient.__contains__(random_number)):
            return random_number
        else:
            return self.generate_validation_number()

    # Send validation numbers to CLA
    def valid_nums_list(self):
        print(self.validation_number_recipient)
        return self.validation_number_recipient.keys()

    #TODO probably take it out. Exposes voters
    def get_validation_number_recipient(self):
        print(self.validation_number_recipient)
        # return self.validation_number_recipient