x , y , z  = 2 , 5 , 107

numbers = 1 , 5 , 7 , 10 , 6

#1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ? 
ilkSayi = input('İlk sayıyı giriniz: ')
ikinciSayi = input('İkinci sayıyı giriniz: ')
carpim = int(ilkSayi) * int(ikinciSayi)
print('İki sayının çarpımı : ' , carpim)

fark = ( x + y + z ) - (carpim)
print('İki ifadenin farkı : ' , fark)

#2- y'nin x' e kalansız bölümünü hesaplayınız. 

a = y // x 
print(a)

#3- (x,y,z) toplamının mod3'ü nedir ? 

b = (x + y + z) % 3
print(b)

#4- y'nin x.'ci kuvvetini hesaplayınız. 
c = y ** x
print(c)

#5- x, *y , z  = numbers işlemine göre z'nin küpü kaçtır ? 
x, *y , z = numbers 
d = z ** 3
print(d)

#6- x , *y , z = numbers işlemine göre y'nin değerleri toplamı kaçtır ? 
x, *y ,z = numbers 

e = y[0] + y[1] + y[2]


print(e)
