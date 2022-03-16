#!/usr/bin/env python3

import random
from Central_legitimization_agency import *
from Central_tabulating_facility import *
from Voter import *

#TODO check input in terminal

voters_list = []
voter_identification_number = {}   
def generate_voter_identification_number():
    random_number = random.randint(1000000000, 9999999999)
    if (not voter_identification_number.__contains__(random_number)):
        voter_identification_number[random_number] = True
        return random_number
    else:
        return generate_voter_identification_number()


cla = Central_legitimimation_agency()
candidate_list = []

print("Hello! Welcome to the elections")

candidates_num_input = input("Please enter the number of candidates in the election\n")
candidates_num = int(candidates_num_input)

candidate_counter = 0
while (candidates_num > candidate_counter):
    candidates_name_input = input("Please enter the name of the candidate number " + str(candidate_counter + 1) + "\n")
    candidates_name = str(candidates_name_input)
    if (candidate_list.__contains__(candidates_name)):
        print("Candidate " + candidates_name + " has already been registered")
    else:
        candidate_list.append(candidates_name)
        candidate_counter += 1

print("List of candidates are: ")
print(candidate_list)

  
ctf = Central_tabulating_facility()             #CLA sends validation numbers to CTF and adds voters to the list
for name in candidate_list:                                 #CTF initializes the names of candidates
    ctf.initialize_candidate_names(name)


#=================================

voters_num_input = input("Please enter the number of voters\n")
voters_num = int(voters_num_input)

vote_counter = 0
# While loop voters_num >= vote_counter
while(voters_num > vote_counter):
    voter_name_input = input("Please enter name of the voter number " + str(vote_counter + 1) + "\n")

    #Making sure there is no double vote
    if (voters_list.__contains__(str(voter_name_input))):
        print("Voter " + str(voter_name_input) + " has already voted")
    else:
        voters_list.append(str(voter_name_input))
        voter_id_number = generate_voter_identification_number()
        voter = Voter(voter_id_number)
        
        # Generates validation number for voter and stores it with identification number
        voter_validation_number = cla.send_validation_number(voter_id_number)   
        voter.set_validation_number(voter_validation_number)
        print(str(voter_validation_number)) # TODO DELETE IMMIDIATLY

        print(voter_name_input + " has the ideantification number " + str(voter.get_identification_number()) + "\n")

        print(candidate_list)
        vote_input = input("Voter " + str(voter.get_identification_number()) + ", please enter the full name of the desired candidate\n")

        vote = str(vote_input)
        if (candidate_list.__contains__(vote)):
            vote_counter += 1
            voter.send_vote() #TODO implemnt vote
        else:
            print("Candidate is not in the list")

    
    # at pressing some key "stop", voting process stops break

validation_number_list = cla.valid_nums_list()
ctf.set_validation_number_list(validation_number_list)
print(ctf.validation_number_list)
print("Validation numbers has been successfully sent")
# print(cla.send_validation_number())

#==========================


'''
Steps for voting
1. voter requests valiudation # forom cla
2. cla sneds val num & adds votesr to the list
    after all voters are registered
3. cla sends array of val-numbs to ctf
4. voter send encryppted vote + validation number + signature with ctf public key
5. ctf decrypts & updates the score
'''