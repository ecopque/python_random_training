import pickle

x = 1

print(type(x))
# Response: <class 'int'>

print(pickle.dumps(x))
# Response: b'\x80\x04K\x01.'

###
y = [1, 2, 3, 4]
b = pickle.dumps(y)
print(pickle.loads(b))
# Response: [1, 2, 3, 4]

###
c = [1, 2, 3, 4]
file_var = open('file.pkl', 'wb')
pickle.dump(c, file_var) # Create file.

file_var = open('file.pkl', 'rb')
return_var = pickle.load(file_var)
print(return_var)
# Response: [1, 2, 3, 4]

# Edson Copque | https://linktr.ee/edsoncopque
