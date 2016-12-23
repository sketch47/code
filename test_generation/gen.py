import os
import random
zone_array=[]

zone1=[
    "1",
    "2",
    "3"
    ]
zone2=[
    "4",
    "5",
    "6"
]
zone_array.append(zone1)
zone_array.append(zone2)

i=0
a=0
j=0
while a!=3:
     if(i==2):
         i=i-2
         while j!=3:
            zone1[j]=random.randint(0, 9)
            j=j+1
     print(zone_array[i])
     a=input()
     i=i+1
