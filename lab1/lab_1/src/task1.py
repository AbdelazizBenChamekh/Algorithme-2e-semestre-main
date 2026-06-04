def collect_signatures(segments):
    segments.sort(key=lambda x: x[1])  # сортировка по правому концу
    points = []
    i = 0
    while i < len(segments):
        x = segments[i][1]  # берём правый конец
        points.append(x)
        # пропускаем все отрезки, покрытые точкой x
        while i < len(segments) and segments[i][0] <= x:
            i += 1
    return points
n = int(input())
segs = [list(map(int, input().split())) for _ in range(n)]
pts = collect_signatures(segs)
print(len(pts))
print(*pts)
