
#Initialising the varibles and arrays
pupilnames = []
pupilprices = []
startingPrice = 3.00


'{:<12}{:<11}'

groupName = input("What is your group's name? ")

NoOfPupils = float(input("How many pupils are in your group: "))

wholeNoCheck = (NoOfPupils - int(NoOfPupils) == 0)

#Input Validation for the number of pupils
while NoOfPupils <4 or NoOfPupils >10 or not NoOfPupils.is_integer():
  print ("You have either too many pupils or too little pupils to continue. Please try again. ")
  NoOfPupils = float(input("How many pupils are in your group? "))

NoOfPupils = int(NoOfPupils)

#For loop for the number of pupils in the group
for x in range(NoOfPupils):
  name = input("What is the pupil's name? ")

  pupilnames.append(name)

  preorder = input("Would you like to pre-order a photo : Y/N ")

  #Input Validation so the user picks a valid option
  while preorder != "yes" and preorder != "Yes" and preorder != "y" and preorder != "Y" and preorder != "no" and preorder != "No" and preorder != "n" and preorder != "N":
    print ("That is not a valid input")
    preorder = input("Would you like to pre-order a photo : Y/N ")


  if preorder == "yes" or preorder == "Yes" or preorder == "y" or preorder == "Y":
    fulltotal = startingPrice + 1.99

    pupilprices.append(fulltotal)

  if preorder == "no" or preorder == "No" or preorder == "n" or preorder == "N":
    total = startingPrice

    pupilprices.append(total)

#Prints the group name, name of pupils and price they have to pay to display
print ("Group Name: ", groupName)

print ("Number of pupils in group: ", NoOfPupils)

print ('{:12}{:11}'.format('Name:','Price:'))

for x in range(NoOfPupils):
        print ('{:<12}{:<11}'.format(pupilnames[x],pupilprices[x]))