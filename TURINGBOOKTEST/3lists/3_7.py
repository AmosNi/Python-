invitors = ['Amos', 'Blue', 'Mike']
invitors.insert(0, 'David')
invitors.insert(2, 'Jack')
invitors.append('Bluce')
print("Sorry our desk has a problem, we can invite just 2 people")
for i in range(1, 5):
    print('Sorry, ' + invitors.pop() + ' , we may invite you next time.')
for invitor in invitors:
    print('Hi, ' + invitor + '. Please come to my party!')
del invitors[0]
del invitors[0]
print(invitors)
