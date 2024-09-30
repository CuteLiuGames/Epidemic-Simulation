# Epidemic Simulation
###Epidemic Simulation using Python
This program uses the variables set in program to simulate the spreading of disease, giving an animated image about the simulation and the proportion of infected population.
A person (show as dots) will move inside a square area, with straight or random (Brownian motion) moving options.
There will be one infected person at the start, and will recover after a while. However there's a chance for reinfection.
In the traveling experiment, a person will teleport to other areas after moving for a while.
In the quarantine experiment, after being infected for a while, it will be sent to a quarantine zone (mark as red square), and cannot travel until recovery. At that time, the recovered person can travel again.
In the simulation, healthy people are marked blue, infected people are marked red and recovered people are marked green.
In the bar chart, the green blue portion means healthy people, the orange portion means infected people and the gray portion means recovered people.


利用Python程式將設定的參數進行疫情模擬後，得到模擬圖及染疫比例圖。
人(以點點表示)會在一個框框內移動，可為直線或布朗運動。
在模擬中會有一個染疫者，且依照設定的傳染率進行傳染。染疫後一段時間會康復，不過康復後仍會有一定的機率會再次染疫。
在旅遊的實驗中，移動一段時間後會瞬移至其他的框框內。
在隔離的實驗中，染疫後一段時間，會被隔離在隔離區(標示為紅色的框框)，且無法旅遊。康復後該康復者會解隔離，此時康復者離開隔離區且可以進行旅遊。
在模擬圖中，未染疫者標示為藍色的點點，染疫者標示為紅色的點點，康復者標示為綠色的點點。
在染疫比例圖中，綠藍色代表未染疫者，橘色代表染疫者，灰色代表康復者。
