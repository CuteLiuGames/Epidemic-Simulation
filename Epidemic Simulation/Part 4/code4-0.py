import matplotlib.pyplot as plt
import random
S_people = [] #健康者
I_people = [] #感染者
R_people = [] #康復者
day = [] #疫情翻展天數


for i in range(100):
    day.append(i+1)
    S_people.append(random.randint(2, 99))
    I_people.append(random.randint(1, 100 - S_people[i]))
    R_people.append(100-S_people[i]-I_people[i])
    
SI_people = [i+j for i,j in zip(S_people, I_people)]
    
plt.bar(day, I_people, width=1,color='tomato', label = 'I')
plt.bar(day, S_people, width=1,color='lightseagreen',bottom=I_people, label='S')
plt.bar(day, R_people, width=1,color='gray',bottom=SI_people, label='R')
plt.xlabel('day')
plt.ylabel('rate')
plt.legend(bbox_to_anchor=(1,1), loc='upper left')