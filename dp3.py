import numpy as np

def tateyoko(lst,ans,calc,iMax,jMax):
    ans[0][0][0] = ans[0][0][1] = -1
    for cnt in range(jMax-1):
        calc[cnt+1][0] = calc[cnt][0] + lst[cnt+1][0]
        ans[cnt+1][0][1] = cnt
    for cnt in range(iMax-1):
        calc[0][cnt+1] = calc[0][cnt] + lst[0][cnt+1]
        ans[0][cnt+1][0] = cnt

def min_route(i,j,lst,calc,ans):
    route1 = calc[j-1][i-1] + 2*lst[j][i]
    route2 = calc[j][i-1] + lst[j][i]
    route3 = calc[j-1][i] + lst[j][i]

    if (route3 >= route2 >= route1 or route2 >= route3 >= route1):
        calc[j][i] = route1
        ans[j][i][0] = i-1
        ans[j][i][1] = j-1
    elif (route3 >= route1 >= route2 or route1 >= route3 >= route2):
        calc[j][i] = route2
        ans[j][i][0] = i-1
        ans[j][i][1] = j
    else:
        calc[j][i] = route3
        ans[j][i][0] = i
        ans[j][i][1] = j-1


def ans_route(clac,ans,iMax,jMax,lst):
    i = j = itmp = jtmp = 1     # NOT 0(Zero) by line 40
    route =[[iMax-1,jMax-1]]
    flg = 0

    itmp = iMax-1
    jtmp = jMax-1
    i = int(ans[jtmp][itmp][0])
    j = int(ans[jtmp][itmp][1])
    while (itmp != 0 or jtmp != 0):   #i and j == 0 -> loop
        route.insert(0,[i,j])
        itmp = i
        jtmp = j
        i = int(ans[jtmp][itmp][0])
        j = int(ans[jtmp][itmp][1])
    return route


def main(lst,iMax,jMax):
    i = j = 0
    calc = np.zeros((jMax,iMax))    #calc result
    ans = np.zeros((jMax,iMax,2))   #record route-cordinate
    distance = 0

    calc[0][0] = lst[0][0]
    tateyoko(lst,ans,calc,iMax,jMax)
    flag = False

    while(i < iMax-1 and j < jMax-1):   #for making-map
        if(flag == True):   #i or j == Max -> end
            break
        if (i < (iMax-1)):
            i += 1
        else:
            flag = True
        if (j < (jMax-1)):
            j += 1
        else:
            flag = True

        itmp = i    #reset row
        while (i < iMax):
            min_route(i,j,lst,calc,ans)
            i += 1
        i = itmp

        jtmp = j    #reset column
        while (j < jMax):
            min_route(i,j,lst,calc,ans)
            j += 1
        j = jtmp

    route = ans_route(calc,ans,iMax,jMax,lst)
    distance = calc[jMax-1][iMax-1]

    return distance, route
