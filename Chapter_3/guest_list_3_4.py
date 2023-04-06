

''' 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner. '''

guest = input('Enter the name of the guest 1: \n')
guest_list = []
i = 1 # flag value
while guest != '-1':
    i+=1
    guest_list.append(guest)
    guest = input(f'Enter the name of the guest {i}: \n')

print(guest_list)



