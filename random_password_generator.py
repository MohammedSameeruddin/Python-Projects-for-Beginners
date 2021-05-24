##generating random password using random module

import random
passlength=int(input("Please enter your random password length: "))
cipher_text="abskkdkvmdkopfmfdkmcfmfkknkfkfnf01234567889089nmfkffmfjudy847799494";
random_password="".join(random.sample(cipher_text,passlength))
print(random_password);

##another method
import random
p=int(input(“Length of password:- “))
s=’abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?’
m=””
for i in range(p):
m=m+random.choice(s)
print(m)
