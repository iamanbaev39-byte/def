def binary_search(royxat, maqsad):
    """
    Saralangan ro'yxat ichidan elementni ikkilik qidiruv usulida topadi.
    Topilsa indeksini, topilmasa -1 qaytaradi.
    """
    boshi = 0
    oxiri = len(royxat) - 1

    while boshi <= oxiri:
        orta = (boshi + oxiri) // 2
        taxmin = royxat[orta]

        if taxmin == maqsad:
            return orta
        elif taxmin > maqsad:
            oxiri = orta - 1
        else:
            boshi = orta + 1

    return -1

# Kodni tekshirib ko'ramiz
if __name__ == "__main__":
    sonlar = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    izlanayotgan_son = 23

    natija = binary_search(sonlar, izlanayotgan_son)

    if natija != -1:
        print(f"Son {natija}-indeksda topildi!")
    else:
        print("Son ro'yxatda topilmadi.")