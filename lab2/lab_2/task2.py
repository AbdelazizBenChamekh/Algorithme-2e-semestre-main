def simulate(n, A, B):
    """Вычисляет min высоту при заданном B."""
    h = [0.0] * n
    h[0] = A
    h[1] = B  # начальное предположение о h[n-1]
    # h_i = 2*h_{i-1} - h_{i-2} + 2  (из формулы рекуррентности)
    # h[i] = 2*h[i-1] - h[i-2] + 2
    h = [0.0] * n
    h[0] = A
    # Нормируем: при h[n-1] = B, решаем линейную систему
    # Используем суперпозицию: h = alpha*f + beta*g
    # f: f[0]=1, f[1]=0; g: g[0]=0, g[1]=1; h[i]=2h[i-1]-h[i-2]+2
    f = [0.0]*n; f[0]=1.0; f[1]=0.0
    g = [0.0]*n; g[0]=0.0; g[1]=1.0
    p = [0.0]*n; p[0]=0.0; p[1]=0.0
    for i in range(2, n):
        f[i] = 2*f[i-1]-f[i-2]
        g[i] = 2*g[i-1]-g[i-2]
        p[i] = 2*p[i-1]-p[i-2]+2
    # h[i] = A*f[i] + B_coeff*g[i] + p[i]
    # h[0]=A: A*f[0]=A -> ok; h[n-1]=B: A*f[n-1] + B_coeff*g[n-1] + p[n-1] = B
    # -> B_coeff = (B - A*f[n-1] - p[n-1]) / g[n-1]
    B_coeff = (B - A*f[n-1] - p[n-1]) / g[n-1]
    return min(A*f[i]+B_coeff*g[i]+p[i] for i in range(n))
lo, hi = 0.0, 1e9
for _ in range(200):
    mid = (lo + hi) / 2
    if simulate(n, A, mid) < 0:
        lo = mid
    else:
        hi = mid
print(f"{hi:.8f}"
