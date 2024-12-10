files = open('brothers.txt', 'w') # (w)right, (a)dd, (r)ead
files.write('Théo')
files.write('Mel \n')
# Response: ThéoMelMel

files2 = open('brothers.txt', 'a')
files.write('Edson\n')
files.write('Santos\n')
# Response: Edson | Santos

hd_names = open('new_names.txt', 'w')
while True:
    x = input('Enter a name or 0 to exit: ')
    if x == '0':
        break
    else:
        hd_names.write(x + '\n')
hd_names.close()

# Edson Copque | https://linktr.ee/edsoncopque
