def my_function(**kwargs):
    x = kwargs.get('c')
    if x:
        print(x)
    else:
        print(kwargs)

my_function(a=1, b=2, d=3, c=1000, e=4)

# Edson Copque | https://linktr.ee/edsoncopque
