from char import *
def str_rot_13(string):
   pos = []
   for s in string:
      pos.append(char_rot_13(s))
   return ''.join(pos)



def str_translate_101(string, old, new):
   translate = []
   for i in range(len(string)):
      if string[i] == old:
         translate.append(new)
      else:
         translate.append(string[i])
   return ''.join(translate)

