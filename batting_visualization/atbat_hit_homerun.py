import matplotlib.pyplot as plt

#korean font
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#player = [name, position, atbat, hit, double, triple, homerun, bb, ops, advance ability...]
player = [['최경철', '2', 32, 10, 2, 0, 2, 3, 0.973, ' 0.0 ', ' 0.0 ', ' 33.3 ', ' 100.0 ', ' 50.0 ', ' 100.0 '],
          ['러프', '3', 515, 162, 38, 0, 31, 60, 0.965, ' 14.3 ', ' 31.0 ', ' 45.5 ', ' 53.6 ', ' 81.8 ', ' 42.9 '],
          ['구자욱', '9', 564, 175, 39, 10, 21, 63, 0.91, ' 9.0 ', ' 38.6 ', ' 42.4 ', ' 36.6 ', ' 69.2 ', ' 29.4 '],
          ['이승엽', '3', 472, 132, 30, 5, 24, 47, 0.864, ' 12.1 ', ' 33.3 ', ' 51.7 ', ' 41.4 ', ' 80.0 ', ' 33.3 '],
          ['배영섭', '7', 218, 66, 11, 1, 6, 19, 0.81, ' 7.9 ', ' 36.8 ', ' 40.0 ', ' 19.1 ', ' 41.7 ', ' 50.0 '],
          ['최영진', '5', 20, 4, 0, 2, 1, 1, 0.788, ' 33.3 ', ' 0.0 ', ' 0.0 ', ' 100.0 ', ' 100.0 ', '  '],
          ['조동찬', '4', 353, 102, 23, 0, 10, 22, 0.783, ' 9.1 ', ' 31.8 ', ' 41.2 ', ' 29.4 ', ' 75.0 ', ' 25.0 '],
          ['박한이', '7', 118, 31, 9, 0, 4, 13, 0.774, ' 15.4 ', ' 16.7 ', ' 50.0 ', ' 16.7 ', ' 25.0 ', ' 0.0 '],
          ['이원석', '5', 411, 109, 20, 1, 18, 34, 0.773, ' 16.0 ', ' 32.4 ', ' 38.1 ', ' 20.0 ', ' 61.5 ', ' 0.0 '],
          ['김성훈', '4', 151, 48, 4, 2, 0, 12, 0.741, ' 18.8 ', ' 54.6 ', ' 75.0 ', ' 0.0 ', ' 50.0 ', ' 0.0 '],
          ['박해민', '8', 570, 162, 25, 8, 7, 50, 0.731, ' 12.1 ', ' 37.0 ', ' 50.0 ', ' 26.3 ', ' 50.0 ', ' 0.0 '],
          ['김헌곤', '7', 356, 94, 13, 2, 9, 29, 0.719, ' 10.6 ', ' 29.2 ', ' 37.5 ', ' 26.9 ', ' 35.7 ', ' 50.0 '],
          ['권정웅', '2', 99, 21, 3, 0, 6, 8, 0.702, ' 11.8 ', ' 0.0 ', ' 0.0 ', ' 33.3 ', ' 100.0 ', ' 50.0 '],
          ['안주형', '6', 10, 3, 1, 0, 0, 0, 0.7, '  ', ' 100.0 ', ' 0.0 ', ' 100.0 ', '  ', '  '],
          ['강한울', '6', 412, 125, 9, 3, 0, 26, 0.684, ' 20.0 ', ' 48.0 ', ' 25.0 ', ' 7.9 ', ' 16.7 ', ' 50.0 '],
          ['김상수', '6', 144, 38, 7, 0, 3, 5, 0.666, ' 7.7 ', ' 40.0 ', ' 33.3 ', ' 22.2 ', ' 50.0 ', ' 100.0 '],
          ['김정혁', '5', 84, 23, 5, 0, 0, 4, 0.652, ' 25.0 ', ' 50.0 ', ' 66.7 ', ' 16.7 ', ' 75.0 ', ' 33.3 '],
          ['최원제', '3', 18, 4, 3, 0, 0, 0, 0.611, ' 20.0 ', ' 0.0 ', '  ', ' 0.0 ', '  ', ' 50.0 '],
          ['이지영', '2', 302, 72, 10, 2, 0, 20, 0.579, ' 9.8 ', ' 34.6 ', ' 57.1 ', ' 14.3 ', ' 70.0 ', ' 40.0 '],
          ['정병곤', '6', 74, 16, 0, 0, 2, 4, 0.572, ' 11.1 ', ' 0.0 ', ' 0.0 ', ' 33.3 ', ' 0.0 ', '  '],
          ['김성윤', '7', 12, 1, 0, 0, 1, 2, 0.547, ' 33.3 ', ' 0.0 ', ' 0.0 ', '  ', '  ', '  '],
          ['나원탁', '2', 23, 5, 1, 0, 0, 0, 0.478, ' 0.0 ', ' 0.0 ', '  ', '  ', '  ', '  '],
          ['이현동', '7', 16, 3, 1, 0, 0, 0, 0.438, ' 0.0 ', '  ', '  ', '  ', '  ', '  '],
          ['김민수', '2', 21, 3, 1, 0, 0, 1, 0.372, ' 0.0 ', ' 33.3 ', ' 50.0 ', ' 0.0 ', ' 0.0 ', ' 100.0 '],
          ['나성용', '7', 11, 2, 0, 0, 0, 0, 0.364, ' 0.0 ', '  ', '  ', '  ', '  ', '  '],
          ['이성규', '4', 17, 2, 0, 0, 0, 1, 0.329, ' 25.0 ', ' 0.0 ', ' 0.0 ', '  ', '  ', '  '],
          ['백상원', '4', 46, 6, 0, 0, 0, 3, 0.31, ' 0.0 ', ' 33.3 ', ' 50.0 ', ' 0.0 ', ' 0.0 ', '  '],
          ['성의준', '5', 6, 0, 0, 0, 0, 1, 0.143, ' 0.0 ', '  ', '  ', '  ', '  ', '  '],
          ['우동균', '7', 12, 0, 0, 0, 0, 1, 0.077, ' 0.0 ', ' 0.0 ', '  ', '  ', '  ', '  '],
          ['이영욱', '8', 4, 0, 0, 0, 0, 0, 0.0, ' 0.0 ', ' 0.0 ', '  ', '  ', '  ', '  '],
          ['문선엽', '9', 4, 0, 0, 0, 0, 0, 0.0, ' 0.0 ', '  ', '  ', '  ', '  ', '  ']]


#screen size
fig = plt.figure(figsize = (150,100), facecolor = 'w')


#screen adjust
def plotCircle(x,y,radius,color, alphaval):
    circle = plt.Circle((x,y), radius = radius, fc = color, alpha = alphaval)
    fig.gca().add_patch(circle)
    nofcircle = plt.Circle((x,y), radius = radius, ec = color, fill = False)
    fig.gca().add_patch(nofcircle)


x=[]
y=[]
r=[]

#atbat, hit, homerun 표시
for j in range(len(player)):
    x.append(player[j][2]) #atbat
    y.append(player[j][3]) #hit
    r.append(player[j][6]) #homerun



for i in range(len(x)):
    plotCircle(x[i], y[i], r[i],'b', 0.1)

plt.title('Samsung Lions Atbat & Hit (Radius : Homerun)')
plt.xlabel('# of Atbat')
plt.ylabel('# of Hit')
plt.axis('scaled')
plt.show()


