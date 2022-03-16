from Central_legitimization_agency import *

class Central_tabulating_facility:
    validation_number_list = [] # Expected from CLA
    list_of_voters = [] # Check who voted
    votes = {}  #Tally containing {candidate name : number of votes recieved}
    private_key = ''    #For decrypting the incoming votes

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