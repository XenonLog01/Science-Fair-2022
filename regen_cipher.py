import random
import sys

num = 0

# Every single char, a new seed is generated
# This may be based on the ord of the last
# char, or by some other method. 

def gen_new_num(): 
  global num
  num = random.randint(32, 254)

def encrypt(msg):
  num_start = num
  encoded_msg = ""
  for ch in msg:
    p_ch = chr(ord(ch) + num)
    if ord(p_ch) > 254:
      a = ord(p_ch) - 254
      p_ch = chr(a + 32)
    encoded_msg += chr(num) + p_ch
    gen_new_num()
  
  encoded_msg = f"{encoded_msg}"

  return encoded_msg

def decrypt(msg):
  global num
  decoded_msg = ""
  is_num = True
  for ch in msg:
    if is_num:
      num = int(ord(ch))
      is_num = False
      print(num)
    else:
      p_ch = ord(ch) - num
      if p_ch < 32:
        a = 32 - p_ch
        p_ch = 254 - a
      decoded_msg += chr(p_ch)
      is_num = True

  return decoded_msg

def main(encrypting=True):
  gen_new_num()
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
