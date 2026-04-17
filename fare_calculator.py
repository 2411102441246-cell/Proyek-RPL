# Fungsi hitung
def calc(d, t, is_p, v_type):
    # d = distance, t = time
    res = 0
    if v_type == 1: # 1 is goride
        res = (d * 2000) + (t * 500)
        if is_p == True:
            res = res - 5000 # diskon promo 5rb
    elif v_type == 2: # 2 is gocar
        res = (d * 5000) + (t * 1000)
        if is_p == True:
            res = res - 10000 # diskon promo 10rb
            
    print("Total harga adalah: Rp " + str(res))
    return res
