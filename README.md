# RSA Cryptography 🔐

This project was made in collaboration with [Eder](https://github.com/Nxrth-x), [Elida](https://github.com/elidacastro), [Victoria](https://github.com/suzuyay) and [Vinicius](https://github.com/Viniccin) during our second Computer Science semester.  In short: This is a pure Python implementation of the Public Key Encryption Algorithm.

## Features 
- User Interface 📱
- RSA encryption module 🔑
- Implementation of a non linear cypher 👨‍💻

## Dependencies
There are no dependencies/modules you need to install to use this implementation, have fun! 

## RSA module
During our planning, we've decided to make everything as modular as possible. So we agreed in making a separate file for our cryptography, so... Here are some examples on how to use it. 🤠

### Importing in your project
To use it, all you need to do is have the `encrypt_rsa.py` file in the same directory as your project, then you import it as follows:

`import encrypt_rsa as rsa`

> Done, that's it!

### Generating the keys 🗝️
To generate the keys (both public and private) you'll need to use the following method:

`public, private = rsa.generate_new_keys()`

The `generate_new_keys()` method doesn't receive any parameters. 

`** this method returns a tuple (which has a tuple in itself).`

You'll **need both keys**, the `public` is used to encrypt messages and the `private` one is used to decrypt.

### Encrypting messages ✉️
Encrypting messages is simple, you'll need the private key from the example above, then all you have to do is pass both the `message` and the `key` as parameters to the method.

` cipher: str = rsa.encrypt("Hello, world! 👋", public)`

Which will return you something like this: `375a65eg2841033g294f08fg294f08fg10b380eg1e96af2gbad2d7g208a8cag10b380eg480f30g294f08fg19ab37fg30c5a2dgbad2d7g1ad8afb`

### Decrypting messages 📬
To decrypt messages, you'll need to use the `private key` generated before. Just like the encrypting method, you'll need to pass the `message` and the `key`.

`decipher: str = rsa.decrypt(cipher, private)`

Which, in this case, returns the original `Hello, world! 👋`.

## Aknowledgements  👏
Massive thanks to everyone who helped building it. 💖
- [Eder Lima](https://github.com/Nxrth-x)
- [Élida Castro](https://github.com/elidacastro)
- [Victoria Sampaio](https://github.com/suzuyay) 
- [Vinicius Rodrigues](https://github.com/Viniccin) 

### Usefull links 🔗
- [Public Key Cryptography - Computerphile](https://www.youtube.com/watch?v=GSIDS_lvRv4)
- [Secret Key Exchange - Computerphile](https://www.youtube.com/watch?v=NmM9HA2MQGI)
- [SP Networks - Computerphile](https://www.youtube.com/watch?v=DLjzI5dX8jc)
- [RSA Encryption Algorithm - Part 1 - Professor Eddie Woo](https://www.youtube.com/watch?v=4zahvcJ9glg)
- [RSA Encryption Algorithm - Part 2 - Professor Eddie Woo](https://www.youtube.com/watch?v=oOcTVTpUsPQ)
- [Public Key Cryptography - Art of the Problem](https://www.youtube.com/watch?v=wXB-V_Keiu8)