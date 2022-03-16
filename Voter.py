class Voter:
    identification_number = -1
    candidate = ''
    validation_number = -1
    ctf_public_key = ''
    voter_private_key = ''

    def __init__(self, identification_number):
        self.identification_number = identification_number 
        pass

    def get_identification_number(self):
        return self.identification_number

    def set_validation_number(self, validation_number):
        self.validation_number = validation_number

    #send (encryppted vote + validation number) + digital signature with ctf public key
    def vote(self):
        if (self.validation_number == -1):
            print("Cannot vote! Need validation number")
        else:
            print('voted')
    
    def get_validation_number(self):
        return self.validation_number

    def encrypt_vote(self):
        print("encrypted")

    def digital_signature(self):
        print("signed")

    def set_ctf_public_key(self, ctf_public_key):
        self.ctf_public_key = ctf_public_key

    def send_vote(self):
        return 'vote'