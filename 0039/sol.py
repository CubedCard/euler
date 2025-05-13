def find_right_angled_triangles(p):
    return [(a, b, p - a - b) for a in range(1, p // 2) for b in range(a, (p - a) // 2) if a**2 + b**2 == (p - a - b)**2]

best_perimeter = max(range(12, 1001), key=lambda p: len(find_right_angled_triangles(p)))

print(best_perimeter)
