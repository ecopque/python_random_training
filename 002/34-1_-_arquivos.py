files = open('brothers.txt', 'w') # (w)right, (a)dd, (r)ead
files.write('Théo')
files.write('Mel \n')
# Response: ThéoMelMel

files2 = open('brothers.txt', 'a')
files.write('Edson\n')
files.write('Santos\n')
# Response: Edson | Santos

###
hd_openw = open('new_names.txt', 'w')
while True:
    x = input('Enter a name or 0 to exit: ')
    if x == '0':
        break
    else:
        hd_openw.write(x + '\n')
hd_openw.close()

hd_openr = open('new_names.txt', 'r')
hd_read = hd_openr.read()
print(hd_read)
print()

for i in hd_read:
    print(i)

# Edson Copque | https://linktr.ee/edsoncopque
