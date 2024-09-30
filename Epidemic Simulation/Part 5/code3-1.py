# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import imageio #製作動圖
import random
#計算距離
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
#輸入邊界x,y座標
m=2
n=2

version = "3-1"

#畫邊界
plt.axes().set_aspect('equal')
for i in range(m):
    for j in range (n):
     x= [0+ 1.2 * i, 1+ 1.2 * i, 1+ 1.2 * i, 0+ 1.2 * i,0+ 1.2 * i]
     y= [0+ 1.2 * j,0+ 1.2 * j,1+ 1.2 * j,1+ 1.2 * j,0+ 1.2 * j]
     plt.plot(x,y,'k')
     
#建立模擬參數
human_number = 100 # 人數
infectious_distance = 0.15 # 傳染辦半徑
infection_rate = 0.05 # 感染率
reinfection_rate = 0.4 # 重複感染率
Travel_rate = 0.02 # 旅遊率


#建立人物
human_x = []
human_y = []
#建立人物區塊編好
mi = []
nj = []
#建立人物移動速度
vx = []
vy = []
#建立人物身體裝況 0:健康者 1:感染者 2:康復者
si=[]
si_days=[]

#隔離
for i in range (m):
 for j in range (n):
  for k in range(human_number): 
   human_x.append(random.randint(10, 90)/100+1.2*i)
   human_y.append(random.randint(10, 90)/100+1.2*j)
   vx.append(random.randint(-30, 30)/1000)
   vy.append(random.randint(-30, 30)/1000)
   si.append(0)
   mi.append(i)
   nj.append(j)
   si_days.append(0)
test = random.randint(0,n*m*human_number-1)
si[test] = 1  

#畫角色
x0,y0 = [],[] #健康者作圖
x1,y1 = [],[] #感染者作圖
x2,y2 = [],[] #康復者作圖

for i in range(n*m*human_number):
    if si[i] ==0:
        x0.append(human_x[i])
        y0.append(human_y[i])
    elif si[i] ==1:
        x1.append(human_x[i])
        y1.append(human_y[i])
plt.plot(x0,y0, 'bo')
plt.plot(x1,y1, 'ro')
plt.axis('off')
#建立圖片
number = 0
plt.savefig(f'out{version}/model_{number}')
plt.close()
S_people = [] #健康者
I_people = [] #感染者
R_people = [] #康復者
day = [] #疫情翻展天數

S_people.append((m*n*human_number-1)/(m*n*human_number))
I_people.append((1)/(m*n*human_number)) 
R_people.append(0)
day.append(0)
SI_people = [S_people[0]+I_people[0]]
plt.bar(day, I_people, width=1,color='tomato', label = 'I')
plt.bar(day, S_people, width=1,color='lightseagreen',bottom=I_people, label='S')
plt.bar(day, R_people, width=1,color='gray',bottom=SI_people, label='R')
plt.xlabel('day')
plt.ylabel('rate')
plt.legend(bbox_to_anchor=(1,1), loc='upper left')
plt.savefig(f'out{version}/model_長條圖_{number}')
plt.close()



#人物移動
#設定如晤移動速度
rx=[]
ry=[]

for i in range(n*m*human_number):
    rx.append(0)
    ry.append(0)

print('Creating...')
times = 100
for step in range(times):
    #腳色移動
  total = -1
  for i in range (m):
   for j in range (n):
    for k in range(human_number):
      #角色移動=>改變human_x,humax_y
      total+=1
      human_x[total] += vx[total]
      human_y[total] += vy[total]
      if human_x[total] >1+1.2*mi[total]-0.05 or human_x[total] <0+1.2*mi[total]+0.05:
         vx[total]*=-1 
      if human_y[total] >1+1.2*nj[total]-0.05 or human_y[total] <0+1.2*nj[total]+0.05:
         vy[total]*=-1 
     
  #旅遊=>改變mi,nj
  total = -1
  for i in range (m):
    for j in range (n):
     for k in range(human_number):
       total+=1
       if random.random() <= Travel_rate:
           test_mi = random.randint(0, (m-1))
           test_nj = random.randint(0, (n-1))
           while(test_mi == mi[total] and test_nj == nj[total]):
               test_mi = random.randint(0, (m-1))
               test_nj = random.randint(0, (n-1))
           mi[total] = test_mi
           nj[total] = test_nj
           human_x[total] = (random.randint(10, 90)/100+1.2*mi[total])
           human_y[total] = (random.randint(10, 90)/100+1.2*nj[total])
   
   #傳染=>改變si
  test = si
  for i in range(n*m*human_number):
         for j in range(n*m*human_number):
             if distance(human_x[i], human_y[i], human_x[j], human_y[j]) <= infectious_distance :
                 if si[j] ==1 and random.random() <= infection_rate:
                    if si[i]!=2:
                       test[i] = 1
                    elif si[i] == 2 and random.random()<=reinfection_rate:
                       test[i] = 1
  si = test
    #畫邊界
  plt.axes().set_aspect('equal')

  for i in range(m):
        for j in range (n):
         x= [0+ 1.2 * i, 1+ 1.2 * i, 1+ 1.2 * i, 0+ 1.2 * i,0+ 1.2 * i]
         y= [0+ 1.2 * j,0+ 1.2 * j,1+ 1.2 * j,1+ 1.2 * j,0+ 1.2 * j]
         plt.plot(x,y,'k')
    #畫角色
  x0,y0 = [],[] #健康者作圖
  x1,y1 = [],[] #感染者作圖
  x2,y2 = [],[] #康復者作圖
  S_people.append(0)
  I_people.append(0)
  R_people.append(0)
  day.append(step+1)
  total = -1
  for i in range (m):
    for j in range (n):
     for k in range(human_number):
        total+=1
        if si[total] == 0:
            x0.append(human_x[total])
            y0.append(human_y[total])
            S_people[step+1] += ((1)/(m*n*human_number))
        elif si[total] == 1 and si_days[total]<=19:
            si_days[total] += 1
            x1.append(human_x[total])
            y1.append(human_y[total])
            I_people[step+1] += ((1)/(m*n*human_number))
        elif si_days[total]>19 or si[total] == 2:
            si[total] = 2
            si_days[total] = 0
            x2.append(human_x[total])
            y2.append(human_y[total])
            R_people[step+1] += ((1)/(m*n*human_number))
  plt.plot(x0,y0, 'bo')
  plt.plot(x1,y1, 'ro')
  plt.plot(x2,y2, 'go')
  plt.axis('off')
    #建立圖片
  number = number + 1
  plt.savefig(f'out{version}/model_{number}')
  plt.close()
  
  SI_people.append(S_people[step+1]+I_people[step+1])
  plt.bar(day, I_people, width=1,color='tomato', label = 'I')
  plt.bar(day, S_people, width=1,color='lightseagreen',bottom=I_people, label='S')
  plt.bar(day, R_people, width=1,color='gray',bottom=SI_people, label='R')
  plt.xlabel('day')
  plt.ylabel('rate')
  plt.legend(bbox_to_anchor=(1,1), loc='upper left')
  plt.savefig(f'out{version}/model_長條圖_{number}')
  plt.close()
    
    
#製作動圖
Outname = 'out_model_' + version + '.gif'
Outname2 = 'out_model_長條圖_' + version + '.gif'
images_ = []
for i in range(number+1):
    image = imageio.imread(f'out{version}/model_{i}.png')
    images_.append(image)
    
imageio.mimsave(Outname ,images_,'GIF',duration=0.05)
images_ = []
for i in range(number+1):
    image = imageio.imread(f'out{version}/model_長條圖_{i}.png')
    images_.append(image)
    
imageio.mimsave(Outname2,images_,'GIF',duration=0.05)
print('Done!')