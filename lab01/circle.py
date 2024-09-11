import math
R=input("Enter the length of radius r:")
r=int(R)
perimeter=2*math.pi*r
area=math.pi*(r**2)
print(f"The circle with radius{r:.2f},has an area of{area:.2f},and a perimeter of{perimeter:.2f}")