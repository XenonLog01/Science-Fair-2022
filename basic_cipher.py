# Essentially, a random number from 1 - 255 is generated.
# That number acts as a base for encryption, and is used to
# shift characters. Every character, it is shifted as well.
# Eg. number = 4, message = "hello!"
# The message is cyphered, then the number is appended onto the
# beginning.

import random
import sys   # Only used for getting files.

# 32 is the minimum visible ASCII character,
# and 254 is the maximum.
num = random.randint(32, 254)

def encrypt(msg):
  # Used for decryption
  num_start = num
  # The variable which will be appended 
  # to with the output message.
  encoded_msg = ""

  for ch in msg:
    p_ch = ord(ch) + num
    if p_ch > 254:
      looped = p_ch - 254
      p_ch = looped + 32
    encoded_msg += chr(p_ch)
  
  encoded_msg = f"{chr(num_start)}{encoded_msg}"

  return encoded_msg

def decrypt(msg):
  global num
  num = int(ord(msg[0]))
  msg = msg[1:]
  decoded_msg = ""
  for ch in msg:
    p_ch = ord(ch) - num
    if p_ch < 32:
      a = 32 - p_ch
      p_ch = 254 - a
    decoded_msg += chr(p_ch)

  return decoded_msg

def main(encrypting=True):
  file = None
  with open(sys.argv[2], "r", encoding="utf-8") as f:
    file = f.read()

  if encrypting:
    with open(sys.argv[3], "w", encoding="utf-8") as f:
      f.write(encrypt(file))
  else:
    with open(sys.argv[3], "w", encoding="utf-8") as f:
      f.write(decrypt(file))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1].lower() == "e" or sys.argv[1].lower() == "encrypt":
      main()
    elif sys.argv[1].lower() == "d" or sys.argv[1].lower() == "decrypt":
      main(encrypting=False)
    else:
      print("?")
  else:
    print("?")
