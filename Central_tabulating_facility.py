from Central_legitimization_agency import *
import RSA
from RSA import *
from Val_Num_Vote import *

class Central_tabulating_facility:
    validation_number_list = [] # Expected from CLA
    list_of_voters = [] # Check who voted
    votes = {}  #Tally containing {candidate name : number of votes recieved}
    private_key = RSA.get_private_key()    #For decrypting the incoming votes

    def __init__(self):
        pass

    def update_list_of_voters(self, voter):
        self.list_of_voters.append(voter)

    def set_validation_number_list(self, validation_number_list):
        self.validation_number_list = validation_number_list

    def decrypt_incoming_vote(self):
        # Using RSA decrypt incomming vote
        print("decrypted")

    def initialize_candidate_names(self, name):
        self.votes[name] = 0

    # Publish result
    def get_vote_results(self):
        return self.votes

    # Update the election results
    def vote_for_candidate(self, candidate):
        if (self.votes[candidate].exists()):
            self.votes[candidate] += 1
        else:
            print("The candidate " + candidate + " does not exist")

    #TODO Check validity of candidate here not in terminal
    def recieve_vote_and_validation_number(self, string):
        vote_and_val_num = self.bin_to_str(RSA.decrypt(string, self.private_key))
        print(RSA.decrypt(string, self.private_key))
        print(RSA.decrypt(self.bin_to_str(string), self.private_key))
        print(string)
        print(vote_and_val_num)
        vote = Val_Num_Vote('', -1).get_candidate(vote_and_val_num)
        val_num = Val_Num_Vote('', -1).get_validation_number(vote_and_val_num)

        if (self.validation_number_list.__contains__(val_num)):
            # Count vote
            # Delete from validation_number_list
            # Add to list_of_voters

            # if () # Candidate is valid
            self.vote_for_candidate(vote)
            print("Done")
    
    # From https://www.adamsmith.haus/python/answers/how-to-convert-binary-to-string-in-python
    def bin_to_str(self, binary: str):
        binary_values = binary.split()
        ascii_string = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character
        return ascii_string