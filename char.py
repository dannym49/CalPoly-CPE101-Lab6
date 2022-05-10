def is_lower_101(c):
   if 97 <= ord(c) <= 122:
      return True
   else:
      return False

def char_rot_13(c):
   decode = ''
   for char in c:
      pos = ord(char)
      if ord('a') <= pos <= ord('z'):
         if pos > ord('m'):
            pos -= 13
         else:
            pos += 13
      elif ord('A') <= pos <= ord('Z'):
         if pos > ord('M'):
            pos -= 13
         else:
            pos += 13
      decode += chr(pos)
   return decode
