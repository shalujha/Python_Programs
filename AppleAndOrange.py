house=[]
location=input().split(" ")
house.append(int(location[0]))
house.append(int(location[1]))
fruits=input().split(" ")
apple=fruits[0]
orange=fruits[1]
x=input().split(" ")
y=input().split(" ")
z=input().split(" ")
appleLocation=[]
orangeLocation=[]
for i in range(int(x[0])):
    appleLocation.append(int(y[i]))
for j in range(int(x[1])):
    orangeLocation.append(int(z[j]))
countApple=0
for k in range(len(appleLocation)):
    if appleLocation[k]+int(apple)>=house[0] and appleLocation[k]+int(apple)<=house[1]:
        countApple+=1
print(countApple)
countOrange=0
for l in range(len(orangeLocation)):
    if orangeLocation[l]+int(orange)>=house[0] and orangeLocation[l]+int(orange)<=house[1]:
        countOrange+=1
print(countOrange)

