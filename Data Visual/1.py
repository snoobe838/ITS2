import matplotlib.pyplot as plt

x=['Virat', 'MSD', 'Rohit', 'Sachin']
y=[25566,9681,14687,32458]


'''
pl1=[]
run1 =[]
for i in range(len(x)):
    if y[i]>25000:
        pl1.append(x)
        run1.append(y)4

'''        

#x1=[2,10,9,13,20,20]
#y1=[10,15,9,28,26,28]

#creating axis
plt.xlabel('Players')
plt.ylabel('Runs')

#plt.scatter(x,y, marker='*', color= 'red', s = 120, label = 'soil')
#plt.scatter(x1,y1, label = 'water')
#plt.legend()


plt.grid()

#plt.plot(x,y)
#plt.plot(x1,y1)



plt.bar(x,y)
plt.show()