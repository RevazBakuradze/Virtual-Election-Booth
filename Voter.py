import RSA
from Val_Num_Vote import *

class Voter:
    identification_number = -1
    val_num_vote = ''  # For whom the voter voted for
    validation_number = -1
    ctf_public_key = RSA.get_public_key()

    def __init__(self, identification_number):
        self.identification_number = identification_number 
        pass

    def get_identification_number(self):
        return self.identification_number

    def set_validation_number(self, validation_number):
        self.validation_number = validation_number

    # Gathering vote file that contains encrypted (vote + validation number)    
    def vote(self, candidate):
        if (self.validation_number == -1):
            print("Cannot vote! Need validation number")
        else:
            self.val_num_vote = Val_Num_Vote(candidate, self.validation_number).generate_str()
            
    # Encrypt vote and validation number using the public key of CTF
    def encrypt_vote_and_validation_number(self):
        return RSA.encrypt(b"self.val_num_vote")

    # Sending vote securly
    def send_vote(self):
        print(self.encrypt_vote_and_validation_number())
        return self.encrypt_vote_and_validation_number()