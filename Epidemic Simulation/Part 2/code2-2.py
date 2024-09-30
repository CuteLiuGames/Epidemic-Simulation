# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import imageio #製作動圖
import random
#計算距離
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
#輸入邊界x,y座標
x = [0, 1, 1, 0,0]
y= [0,0,1,1,0]

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
for i in range(human_number):
  human_x.append(random.randint(10, 90)/100)
  human_y.append(random.randint(10, 90)/100)
  vx.append(abs(random.randint(-30, 30)/1000))
  vy.append(abs(random.randint(-30, 30)/1000))
  si.append(0)
test = random.randint(0,human_number-1)
si[test] = 1  
#畫邊界
plt.axes().set_aspect('equal')
#畫出圖形
plt.plot(x,y,'k')
#畫角色
x0,y0 = [],[] #健康者作圖
x1,y1 = [],[] #感染者作圖
for i in range(human_number):
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
plt.savefig(f'out2-2/model_{number}')
plt.close()



#人物移動
#設定如晤移動速度
rx=[]
ry=[]

for i in range(human_number):
    rx.append(0)
    ry.append(0)

print('Creating...')
times = 100
for step in range(times):
    #腳色移動
    for i in range(human_number):
      rx[i] = random.randint(-1, 1)
      ry[i] = random.randint(-1, 1)
      if (human_x[i]+vx[i] * rx[i]) >1-0.05 and rx[i] > 0:
         rx[i] = 0
      if (human_x[i]+vx[i] * rx[i]) <0+0.05 and rx[i] < 0:
         rx[i] = 0
      if (human_y[i]+vy[i] * ry[i]) >1-0.05 and ry[i] > 0:
         ry[i] = 0
      if (human_y[i]+vy[i] * ry[i]) <0+0.05 and ry[i] < 0:
         ry[i] = 0
      human_x[i] += vx[i] * rx[i]
      human_y[i] += vy[i] * ry[i]
    test = si
    for i in range(human_number):
        for j in range(human_number):
            if distance(human_x[i], human_y[i], human_x[j], human_y[j]) <= infectious_distance:
                if si[j] ==1 and random.random() <= infection_rate:
                    test[i] = 1
    si = test
    #畫邊界
    plt.axes().set_aspect('equal')
    plt.plot(x,y,'k')
    #畫角色
    x0,y0 = [],[] #健康者作圖
    x1,y1 = [],[] #感染者作圖
    for i in range(human_number):
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
    number = number + 1
    plt.savefig(f'out2-2/model_{number}')
    plt.close()
    
    
#製作動圖
images_ = []
for i in range(number+1):
    image = imageio.imread(f'out2-2/model_{i}.png')
    images_.append(image)
    
imageio.mimsave('out_model_2-2.gif',images_,'GIF',duration=0.05)
print('Done!')