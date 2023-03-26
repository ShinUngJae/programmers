def solution(wallpaper):
    wallpaper_list = []
    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[0])) :
            if wallpaper[i][j] == "#" :
                wallpaper_list.append([i, j])
    height = [i[0] for i in wallpaper_list]
    width = [i[1] for i in wallpaper_list]
    return [min(height), min(width), max(height) + 1, max(width) + 1]