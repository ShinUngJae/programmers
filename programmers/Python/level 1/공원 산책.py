def solution(park, routes):
    height = len(park)
    width = len(park[0])
    X_list = []
    routes_list = {"E" : [0, 1], "W" : [0, -1], "S" : [1, 0], "N" : [-1, 0]}
    for i in range(len(park)) :
        for j in range(len(park[0])) :
            if "S" == park[i][j] :
                dog = [i, j]
            if "X" in park[i][j] :
                X_list.append([i, j])
    temp = dog.copy()

    for k in range(len(routes)) :
        for s in range(int(routes[k].split()[1])) :

            temp[0] += routes_list[routes[k].split()[0]][0]
            temp[1] += routes_list[routes[k].split()[0]][1]
            print(k, s, temp)
            if (temp[0] < 0) or (temp[0] >= height) or (temp[1] < 0) or (temp[1] >= width) or (temp in X_list) :
                temp = dog.copy()
                break
        else :
            dog = temp.copy()

    return dog