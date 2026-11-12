print("---LATIHAN OPERATOR---")


print("==Operator Aritmatika==")
a = 2
b = 6
c = 10
d = 16
a = 8
penjumlahan = a + c + d
pengurangan = d - a - b
pembagian = d / a
perkalian = a * c
sisa_bagi = d % c
pembagian_bulat = d // a
pangkat = a ** b
print(f"Hasil Penjumlahan {a} + {c} + {d} = {penjumlahan}")
print(f"Hasil Pengurangan {d} - {a} {b} = {pengurangan}")
print(f"Hasil Pembagian {d} / {a} = {pembagian}")
print(f"Hasil Perkalian {a} * {c} = {perkalian}")
print(f"Sisa Bagi {d} mod {c} = {sisa_bagi}")
print(f"Hasi Pembagian Bulat {d} // {a} = {pembagian_bulat}")
print(f"Hasil Pangkat {a} ** {b} = {pangkat}")

print("==Operator Assignment==")
e = 13
f = 5
g = 7
h = 21
g **= 4
e += 5
h %= 2
f *= 6
print(g)
print(e)
print(h)
print(f)

print("==Operator Perbandingan==")
i = 35
j = 4
k = 9
l = 3
m = 4
print(j == m)
print( k != l)
print(i >= k)
print(k < m )

print("==Operator Logika==")
n = 11
o = 2
p = 12
q = 45
print(o > n and q == p)
print(q != p or o < n)
print(not(p < q))