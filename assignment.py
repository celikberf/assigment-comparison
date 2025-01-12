# x = 5
# y = 10
# z = 20

x , y, z = 5, 10 ,20

# x,y = y,x =>x'i y'ye , y'yi x'e atadık

x += 5 # (x = x + 5) ile aynı ifadedir
x -= 5 # (x = x - 5) ile aynı ifadedir
x *= 5 # (x = x * 5) ile aynı ifadedir 
x /= 5 # (x = x / 5) ile aynı ifadedir
x %= 5 # (x = X % 5) ile aynı ifadedir


values = 1, 2, 3 , 4 ,5 # tuple
print(type(values))

x , y , *z = values 



# eğer atama yaparken 3 elemanlı bir tuple'ı 3 elemanlı olmayan bir yere ata yapıyorsak , hata verir. fakat '*' koyarsak 
#olan elemandan sonrasını dizi içerisine alır komple . Yukarıda z için bir liste olusturdu . 

print(x,y,z)