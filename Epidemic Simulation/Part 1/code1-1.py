# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import imageio #製作動圖


#輸入邊界x,y座標
x = [0, 1, 1, 0,0]
y= [0,0,1,1,0]
#畫出圖形


human_x = 0.5
human_y = 0.5
#畫邊界
plt.axes().set_aspect('equal')
plt.plot(x,y,'k')
#畫角色
plt.plot(human_x,human_y, 'bo')
plt.axis('off')
#建立圖片
number = 0
plt.savefig(f'out1-1/model_{number}')
plt.close()



#人物移動
#設定如晤移動速度
vx=0.01
vy=0.02
print('Creating...')
times = 500
for step in range(times):
    #腳色移動
    human_x += vx
    human_y += vy
    if human_x >1-0.05 or human_x <0+0.05:
       vx*=-1 
    if human_y >1-0.05 or human_y <0+0.05:
       vy*=-1 
    #畫邊界
    plt.axes().set_aspect('equal')
    plt.plot(x,y,'k')
    #畫角色
    plt.plot(human_x,human_y, 'bo')
    plt.axis('off')
    #建立圖片
    number = number + 1
    plt.savefig(f'out1-1/model_{number}')
    plt.close()
    
    
#製作動圖
images_ = []
for i in range(number+1):
    image = imageio.imread(f'out1-1/model_{i}.png')
    images_.append(image)
    
imageio.mimsave('out_model_1-1.gif',images_,'GIF',duration=0.05)
print('Done!')