def min_cost_printing(N, A):
    # Размеры пакетов
    batches = [1, 10, 100, 1000, 10000, 100000, 1000000]
    # Нормализуем: крупный пакет не может быть дороже мелкого
    for i in range(1, 7):
        # стоимость за 1 лист через тариф i vs через тариф i-1
        if A[i] > A[i-1] * batches[i] // batches[i-1]:
            A[i] = A[i-1] * batches[i] // batches[i-1]
    total_cost = 0
    remaining = N
    for i in range(6, -1, -1):  # от крупного к мелкому
        if remaining <= 0:
            break
        count = remaining // batches[i]
        total_cost += count * A[i]
        remaining -= count * batches[i]
    if remaining > 0:  # округление вверх при необходимости
        total_cost += A[0] * remaining
    return total_cost
