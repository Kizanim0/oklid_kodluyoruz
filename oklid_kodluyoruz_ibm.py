import math

while True:
    try:
        n = int(input("Kaç tane nokta gireceksiniz? "))
        if n > 0:
            break
        else:
            print("Lütfen pozitif bir tam sayı girin.")
    except ValueError:
        print("Hatalı giriş! Lütfen sadece bir tam sayı girin.")

points = []
for i in range(n):
    while True:
        try:
            x, y = map(float, input(f"{i+1}. noktanın (x, y) değerlerini girin (örn: 3 4): ").split())
            points.append((x, y))
            break
        except ValueError:
            print("Hatalı giriş! Lütfen iki sayı girin, aralarında bir boşluk olmalı.")


def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktayı tekrar hesaplamamak için
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances) if distances else None  # Tek nokta girilirse hata almamak için

print("Tüm nokta çiftleri arasındaki mesafeler:", distances)
print("Minimum Öklid mesafesi:", min_distance if min_distance is not None else "Yeterli nokta girilmedi.")
