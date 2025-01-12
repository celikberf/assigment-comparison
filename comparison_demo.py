#1- Girilen 2 sayıdan hangisi büyüktür ? 
"""
    a = input('İlk sayı : ')
b = input('İkinci sayı : ')

result = (a > b)
print(f"a : {a} b : {b} den büyüktür : {result}")
"""
#2- Kullanıcıdan 2vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. 
# Eğer ortalama 50 ve üstüyse geçti değilse kaldı yazdırın.

"""
ilkVize = float(input('1.Vize notu : '))
ikinciVize = float(input('2.Vize notu : '))
final = float(input('Final notu : '))

ortalama = ((ikinciVize + ilkVize) * 0.6) + (final * 0.4)


print(f"not ortalamanız : {ortalama} ve dersten geçme durumunuz {ortalama >= 50}")
"""

#3- Girilen bir sayının tek mi çift mi olduğunu yazdırın
"""
x = int(input('Bir sayı giriniz : '))
tekcift = (x % 2 == 0)
print(f"Girilen sayının çift olma durumu {tekcift}")
"""

#4- Girilen bir sayının negatif posizitif durumunu yazdırın . 

"""
sayi = int(input('sayi : '))
pozneg = (sayi > 0) == True

print(f"Sayının pozitif olma durumu : {pozneg}")
"""

#5- Parola ve email bilgisini isteyip doğruluğunu kontrol edin. (email : celikberf@hotmail.com , password : abc123) 


girilenEmail = str(input('email : '))
girilenParola = str(input('parola : '))

email = 'celikberf@hotmail.com'
parola = 'abc123'

print(f"Girilen bilgiler doğru : {parola == girilenParola} {email == girilenEmail}")

