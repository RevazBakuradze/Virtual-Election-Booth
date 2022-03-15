from Central_legitimization_agency import *
from Central_tabulating_facility import *

#TESTING GROUND
cla = Central_legitimimation_agency()

print(type(cla))



#===========================================#
'''

cla = Central_legitimimation_agency()
candidate_list = {}


print("Hello! Welcome to the elections")

candidates_num_input = input("Please enter the number of candidates in the election\n")
candidates_num = int(candidates_num_input)

candidate_counter = 0
# While loop candidates_num >= candidate_counter
# Check if candidate exists & dont lets them add
candidates_name_input = input("Please enter the name of the candidate number " + (candidate_counter + 1) + "\n")
candidate_list[candidate_counter] = candidates_name_input
candidate_counter += 1


validation_number_list = cla.valid_nums_list()
ctf = Central_tabulating_facility(validation_number_list)   #CLA sends validation numbers to CTF and adds voters to the list
for name in candidate_list:                                 #CTF initializes the names of candidates
    ctf.initialize_candidate_names(name)




voters_num_input = input("Please enter the number of voters")
voters_num = int(voters_num_input)

vote_counter = 0
# While loop voters_num >= vote_counter
voter_name_input = input("Please enter name of the voter number " + (vote_counter + 1) + "\n")








Steps for voting
1. voter requests valiudation # forom cla
2. cla sneds val num & adds votesr to the list
    after all voters are registered
3. cla sends array of val-numbs to ctf
4. voter sned encryppted vote + validation number + signature with ctf public key
5. ctf decrypts & updates the score
'''