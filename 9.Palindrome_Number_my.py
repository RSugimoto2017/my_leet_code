import itertools
class Solution:
    x = 5
    strx = str(x)
    listx = list(strx)
    print(listx)
    #for i,j in itertools.product(range(0,len(listx)-1,1), range(len(listx)-1,-1,-1)):
    if(len(listx) > 1):
        for i in range(0, len(listx)-1):
            for j in range(len(listx)-1,-1,-1): 
                print(i, j)
                if i <= j:
                    if listx[i] != listx[j]:
                        #print(listx[i])
                        #print(listx[j])
                        print("False")
                        break
                else:
                    print("True")
                    break
                i += 1
            else:
                continue
            break
    else:
        print("True")