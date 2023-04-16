

''' 
Alejandro Z -> @

3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner. 

'''

'''
1. Limit list to maximum 10 guests


'''

guest = input('Enter the name of the guest 1: \n')
guest_list = []
i = 1 # Counter

while guest == '-1':
    guest = input('Please enter the name of guest 1 (you need at least one guess): \n')

while guest != '-1' and i < 11:
    i+=1
    guest_list.append(guest)
    guest = input(f'Enter the name of the guest {i} (when finish type: -1): \n')

print('The new list: ')
for guests in guest_list:
    print(guests, end=', ')


