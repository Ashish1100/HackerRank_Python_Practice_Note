#1. Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

x=int(input())
y=int(input())
z=int(input())
n=int(input())

x=[p for p in range(x+1) ]
y=[q for q in range(y+1) ]
z=[r for r in range(z+1) ]

permu=[[i,j,k] for i in x for j in y for k in z ]

required=[l for l in permu if sum(l)!=n ]

print(required)
