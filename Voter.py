class Voter:
    identification_number = -1
    candidate = ''  # For whom the voter voted for
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

    # Gathering vote file that contains encrypted (vote + validation number) with digital signature on top of it
    def vote(self):
        if (self.validation_number == -1):
            print("Cannot vote! Need validation number")
        else:
            print('voted')
    
    def get_validation_number(self):
        return self.validation_number

    # Encrypt vote and validation number using the public key of CTF
    def encrypt_vote_and_validation_number(self):
        self.get_validation_number()
        self.set_ctf_public_key()
        print("encrypted")

    # Creating a digital signature of the document
    def digital_signature(self):
        print("signed")

    def set_ctf_public_key(self, ctf_public_key):
        self.ctf_public_key = ctf_public_key

    # Sending vote securly
    def send_vote(self):
        return self.vote()