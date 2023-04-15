"""

3-5 Changing Guest List: 

You just heard one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite

"""

guest = input('Enter the name of the guest 1: \n')
guest_list = []
temp_list = []
i = 1 # flag value

while guest == '-1':
    guest = input('Please enter the name of guest 1 (you need at least one guess): \n')

while guest != '-1':
    i+=1
    guest_list.append(guest)
    guest = input(f'Enter the name of the guest {i} (when finish type: -1): \n')

print()
for guests in guest_list:
    print(guests, end=', ')

if len(guest_list) >= 6:
    print("\n\nPeople who can't make it:\n")
    for j in range(0,3): # for loop that pops and appends items in list to post popped items
        print(guest_list.pop(), end=', ')
    print('\n')
    for i in range(0,3): # for to input name of new guests
        guest = input(f'Enter the name of the new guest {i} (when finish type: -1): \n')
        guest_list.append(guest) 
elif len(guest_list) > 2:
    guest_list.pop()
    guest_list.pop()
elif len(guest_list) == 2:
    guest_list.pop()
elif len(guest_list) == 1:
    guest_list.pop()
    print('The list is empty, please invite more guest!')

print('The new list: ')
for guests in guest_list:
    print(guests, end=', ')


