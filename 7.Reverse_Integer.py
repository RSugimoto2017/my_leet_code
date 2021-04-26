class Solution:
    x = -123
    a = str(x)
    c = []
    #https://stackoverflow.com/questions/780390/convert-a-number-to-a-list-of-integers
    # for for loop converting int into list
    for digit in a:
        c.append(digit)

    #print(c)
    #[取得するリストの始め：取得するリストの終わり：スキップする数+1]
    #[::-1]は逆順になる
    c = c[::-1]
    #print(c)
    #print(c[-1])
    #print(c[1])
    #print(c[3])
    #[-1]は一番最後の意味
    if c[-1] == "-":
        del c[-1]
    separator = ""
    # had to go to https://www.programiz.com/python-programming/methods/string/join
    # リストを一つの変数に合体。区切り文字はseparator("")
    e = separator.join(c)
    #print(isinstance(e, int)) -> False
    if x >= 0:
        e = int(e)
    if x < 0:
        e = int(e) - (2 * int(e))
    if  e >= (2**31)-1 or e <= -(2**31):
        print(0) 
    else:
        print(e)