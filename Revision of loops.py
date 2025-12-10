# printing 1 - 10 (for loop)
for x in range (1,11,1):
  print (x)
# printing 1 - 10 (while loop)
x=1
while x<=10:
  print (x)
  x+= 1 
# printing from 30-3 (by 3's) for loop
for y in range (30,2,-3):
  print (y)
# printing from 30-3 (by 3's) while loop
y = 30 
while y>=3:
  print (y)
  y-= 3
# multiplication table for 4 x all the way until 10 (for loop)
z=4
for i in range(1,11,1): 
  print ("{} x {} = {}".format(z,i,z*i))
# multiplication table for 4 x all the way until 10 (while loop)
i = 1
while i<=10:
  print ("{} x {} = {}".format(4,i,4*i))
  i+=1