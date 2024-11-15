def amigas(x,y):
    num,total = 0,0
    for i in str(x):
        if x[i] == y[i] :
                num += 1
                total += 1
        else:
             total += 1
    percent = (num/total)*100
    if percent >= 90 :
        return True
    else:
        return False
