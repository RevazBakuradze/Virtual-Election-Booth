# Virtual-Election-Booth

Final Project - MATH450/CS483
	We work in a group of three including Linh Dao, Revaz Bakuradze and David Xu
For the final project, we want to create a voting system that is secured and meets these requirements:
1.	Only authorized voters can vote.
2.	No one can vote more than once.
3.	No one can determine for whom anyone else voted.
4.	No one can duplicate anyone else's votes.
5.	No one can change anyone else's vote without being discovered.
6.	Every voter can make sure that his vote has been taken into account in the final tabulation.
7.	Everyone knows who voted and who didn't.

The system we created uses Central Tabulating Facility and Central Legitimization Agency. 
The process of voting goes as follows. The voter will send a request to the CLA for a validation number. 
The CLA will generate a validation number. To prevent an attacker from guessing a valid validation number, 
we want to make the pool much larger than the actual population, which makes the possibility to guess a functioning validation number much smaller. 
The CLA will keep a list of validation numbers and send it to the CTF for later authorization. 
Voters now generate an identification number for themselves and then encrypt the validation number, identification number, and vote using AES. 
Also, to make sure that the message is secure and from the right person, the voters need to include a digital signature by RSA. 
Using AES encryption and a digital signature will ensure the integrity of the message and make sure that no one can know and duplicate other people’s votes.
The CTF will decrypt the message from the voter and check with the list of validation numbers provided by the CLA to make sure that it is a first-time voter. 
Then, the CTF will add one to the tally and add the identification number under a particular candidate’s voter area. 
This way, when the CTF publishes the result, everyone can see who they voted for. This method ensures two things. 
It ensures that nobody can know who voted for who since the identification number is meaningless to anybody else rather than the voters themselves,
and there is no way to alter somebody’s vote since the voter can just check for their identification number and realize something is wrong. 
The CTF cannot change the outcome number in the tally either since the CLA also has a list of validation numbers, 
and the number of votes needs to be matched by the number of given validation numbers. 

The first step of our program will ask for the number of candidates. 
Then the program is going to ask for the candidates’ names and assign them with a letter so that it is easier for the voter. 
The program will proceed to ask for the number of voters. When you enter the number of voters and start to vote, 
the program is going to ask for the name of the voters and then proceed to generate a validation number. 
If a voter enters their name twice, the CLA will not generate a validation number, which ensures everyone only votes once. 
The CLA also updates a list of validation numbers to CTF. Finally, after the voters made their decision, 
the program will automatically generate an identification number and encrypt it along with the vote and the validation number. 
Then the program will digitally sign the message and then send it to the CTF. The CTF will decrypt the message, check for integrity,
and add one to the tally. After all voters have made their votes, the CTF will publish the results.
