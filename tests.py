import time
import random
import encrypt_rsa as rsa

def generate_random_word():
     return "".join([chr(random.randint(1, 55294)) for i in range(random.randint(16, 255))])

#Tests
if __name__ == '__main__':

     tests: int = 0

     #Execution
     start: float = time.perf_counter()

     for i in range(64):
          #Keys
          public, private = rsa.generate_new_keys()

          #Errors
          error = False

          #Test
          for j in range(1, 65):

               #Encryption-Decryption
               message = generate_random_word()
               encrypted = rsa.encrypt(message, public)
               decrypted = rsa.decrypt(encrypted, private)
               tests+=1

               #Error checking
               error = (decrypted!=message)

               if(error):
                    break
          if(error):
               break

     #Execution
     finish: float = time.perf_counter()

     #Log
     print(f"\nTEST LOG\nErrors on execution? {error}\nExecution time: {finish-start:.2f}s\nTests: {tests}\n")