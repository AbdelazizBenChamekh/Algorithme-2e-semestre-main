ef max_prizes(n):
    prizes = []
    k, total = 0, 0
    while total + k + 1 <= n:
        k += 1
        prizes.append(k)
        total += k
    r = n - total
    if r > 0:
        prizes[-1] += r  # добавляем остаток к последнему числу
    return len(prizes), prizes
n = int(input())
k, prizes = max_prizes(n)
print(k)
print(*prizes)

write_output_file2(file_path2, output_data)
