alas_atap=float(input("masukan alas atap: "))
tinggi_atap=float(input("masukan tinggi atap: "))
tinggi_tembok=float(input("masukan tinggi tembok: "))
luas_rumah=((alas_atap*tinggi_atap)/2)+(tinggi_tembok**2)
semen=((luas_rumah)/5)
print("rumah tersebut membutuhkan %s sak semen"%semen)
