from collections import defaultdict
row1= [75]
row2 = [95,64]
row3 = [17,47,82]
row4 = [18,35,87,10]
row5 = [20,4,82,47,65]
row6 = [19,1,23,75,3,34]
row7 = [88,2,77,73,7,63,67]
row8 = [99,65,4,28,6,16,70,92]
row9 = [41,41,26,56,83,40,80,70,33]
row10 = [41,48,72,33,47,32,37,16,94,29]
row11= [53,71,44,65,25,43,91,52,97,51,14]
row12= [70,11,33,28,77,73,17,78,39,68,17,57]
row13= [91,71,52,38,17,14,91,43,58,50,27,29,48]
row14= [63,66,4,68,89,53,67,30,73,16,69,87,40,31]
row15= [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
text = 'row'

l =  [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

#def findnextpos(lst,prevpos):

total = (l[0])[0]
prevpos = 0
rwcnt = 0
#print(total[0])
while True:
    rwcnt +=1
    if rwcnt == len(l): break

    if l[rwcnt][prevpos] > l[rwcnt][prevpos+1]:
        total = total + l[rwcnt][prevpos]
        print("row", rwcnt, 'number',l[rwcnt][prevpos],'in position',prevpos,'total', total)
    else:
        total = total + l[rwcnt][prevpos+1]
        print("row", rwcnt, 'number',l[rwcnt][prevpos+1],'in position',prevpos+1,'total', total)
        prevpos += 1

print(total)

row1
row2
row3
row4
row5
row6
row7
row8
row9
row10
row11
row12
row13
row14
row15
