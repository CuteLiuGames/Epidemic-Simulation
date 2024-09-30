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

#畫邊界
plt.axes().set_aspect('equal')
for i in range(m):
    for j in range (n):
     x= [0+ 1.2 * i, 1+ 1.2 * i, 1+ 1.2 * i, 0+ 1.2 * i,0+ 1.2 * i]
     y= [0+ 1.2 * j,0+ 1.2 * j,1+ 1.2 * j,1+ 1.2 * j,0+ 1.2 * j]
     plt.plot(x,y,'k')
     
#建立模擬參數
human_number = 100
infectious_distance = 0.1
infection_rate = 0.05


#建立人物
human_x = []
human_y = []
#建立人物移動速度
vx = []
vy = []
#建立人物身體裝況 0:健康者 1:感染者 2:康復者
si=[]
for i in range (m):
 for j in range (n):
  for k in range(human_number): 
   human_x.append(random.randint(10, 90)/100+1.2*i)
   human_y.append(random.randint(10, 90)/100+1.2*j)
   vx.append(random.randint(-30, 30)/1000)
   vy.append(random.randint(-30, 30)/1000)
   si.append(0)
test = random.randint(0,n*m*human_number-1)
si[test] = 1  


#畫角色
x0,y0 = [],[] #健康者作圖
x1,y1 = [],[] #感染者作圖
for i in range(n*m*human_number):
    if si[i] ==0:
        x0.append(human_x[i])
        y0.append(human_y[i])
    else:
        x1.append(human_x[i])
        y1.append(human_y[i])
plt.plot(x0,y0, 'bo')
plt.plot(x1,y1, 'ro')
plt.axis('off')
#建立圖片
number = 0
plt.savefig(f'out2-3/model_{number}')
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
      total+=1
      human_x[total] += vx[total]
      human_y[total] += vy[total]
      if human_x[total] >1+1.2*i-0.05 or human_x[total] <0+1.2*i+0.05:
         vx[total]*=-1 
      if human_y[total] >1+1.2*j-0.05 or human_y[total] <0+1.2*j+0.05:
         vy[total]*=-1 
  test = si
  for i in range(n*m*human_number):
        for j in range(n*m*human_number):
            if distance(human_x[i], human_y[i], human_x[j], human_y[j]) <= infectious_distance:
                if si[j] ==1 and random.random() <= infection_rate:
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
  total = -1
  for i in range (m):
    for j in range (n):
     for k in range(human_number):
        total+=1
        if si[total] == 0:
            x0.append(human_x[total])
            y0.append(human_y[total])
        else:
            x1.append(human_x[total])
            y1.append(human_y[total])
  plt.plot(x0,y0, 'bo')
  plt.plot(x1,y1, 'ro')
  plt.axis('off')
    #建立圖片
  number = number + 1
  plt.savefig(f'out2-3/model_{number}')
  plt.close()
    
    
#製作動圖
images_ = []
for i in range(number+1):
    image = imageio.imread(f'out2-3/model_{i}.png')
    images_.append(image)
    
imageio.mimsave('out_model_2-3.gif',images_,'GIF',duration=0.05)
print('Done!')