"""

3-5 Changing Guest List: 

You just heard one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite

"""

guest = input('Enter the name of the guest 1: \n')
guest_list = []
i = 1 # flag value
while guest != '-1':
    i+=1
    guest_list.append(guest)
    guest = input(f'Enter the name of the guest {i}: \n')

print(guest_list)
print(len(guest_list))
if len(guest_list) >= 6:
    guest_list.pop()
    guest_list.pop()
    guest_list.pop()
elif len(guest_list) > 2:
    guest_list.pop()
    guest_list.pop()
elif len(guest_list) == 2:
    guest_list.pop()
elif len(guest_list) == 1:
    guest_list.pop()
    print('The list is empty')


print(guest_list)

