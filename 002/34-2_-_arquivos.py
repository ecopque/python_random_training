file_read = open('brothers.txt', 'r')
with file_read as file_print:
    x = file_print.read()
    print(x)


file_read = open('brothers.txt', 'r')
with file_read:
    x = file_read.read()
    print(x)

# No need to use '.close()'.

# Edson Copque | https://linktr.ee/edsoncopque
