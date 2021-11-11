kalimat=str(input("masukan kalimat: "))
kata=str(input("masukan kata untuk dihitung: "))
list_kata=kalimat.split(" ")
hitung_kata=0
for i in range(0,len(list_kata)):
    if list_kata[i]==kata:
        hitung_kata=hitung_kata+1
    else:
        pass
print ("ada %s buah kata %s"%(hitung_kata,kata))    
