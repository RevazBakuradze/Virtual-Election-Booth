class Central_legitimimation_agency:
    validation_number_recipient = {}

    def __init__(self):
        pass

    def send_validation_number(self, recipient):
        num = self.generate_validation_number()
        # if else to make sure user is not duplicated. If user already requested dont give
        self.store_validation_number(num, recipient)
        print("sending validation number")

    def store_validation_number(self, number, recipient):
        # if else to make sure user is not duplicated
        self.validation_number_recipient[recipient] = number

    def generate_validation_number(self):
        # if else to prevent same # generation
        print("Generating validation number")
        return 12345867585865865

    def valid_nums_list(self):
        return self.validation_number_recipient.keys()