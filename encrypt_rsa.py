# Dependencies
import random
from math import gcd

#Variables
with open("./primes.txt", "r") as file:
     primes = file.readlines()

#Functions
def define_e(phi_n: int) -> int:
     while(True):
          e = random.randint(2, phi_n-1)
          if(gcd(e, phi_n)==1):
               return e

def define_d(e: int, phi_n: int) -> int:
     phi_aux = phi_n

     x, old_x = 0, 1
     y, old_y = 1, 0

     while(phi_n != 0):
          quotient = e // phi_n
          e, phi_n = phi_n, e - quotient * phi_n
          old_x, x = x, old_x - quotient * x
          old_y, y = y, old_y - quotient * y

     return old_x if old_x >= 0 else old_x + phi_aux

def generate_new_keys() -> tuple:
     p: int = int(primes[random.randint(671, len(primes)-1)])
     while(True):
          q = int(primes[random.randint(671, len(primes)-1)])
          if(p!=q):
               break
     n: int = p * q
     phi_n: int = (p-1)*(q-1)

     e: int = define_e(phi_n)
     public = (e, n)

     d: int = define_d(e, phi_n)
     private = (d, n)

     return public, private

def encrypt(message: str, key: list) -> str:
     try:
          return "g".join([hex(pow(ord(letter), int(key[0]), int(key[1])))[2:] for letter in message])
     except:
          return "Error!"

def decrypt(message: str, key: list) -> str:
     try:
          arr: list = message.split("g")
          message: str = "".join([chr(pow(int(element, 16), int(key[0]), int(key[1]))) for element in arr])
          return message    
     except:
          return "Error!"


if __name__ == '__main__':
     public, private = generate_new_keys()
     message: str = 'Hello, world! 👋'
     cifer: str = encrypt(message, public)
     decipher: str = decrypt(cifer, private)
     print(cifer, decipher)