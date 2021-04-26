class Solution:
    s = "III"

    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    dic_key = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    strlist = list(s)
    answer = 0
    
    for i in range(0, len(strlist)):
        if len(strlist)-1 < i+1:
            answer += dic[strlist[i]]
        elif dic_key.index(strlist[i]) >= dic_key.index(strlist[i+1]):
            answer += dic[strlist[i]]
        else:
            answer -= dic[strlist[i]]
            i += 1 
    print(answer)