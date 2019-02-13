# coding: utf-8


print (u"åäö")
  
def doit():
    for i in range(1114111):
        a = chr(i)
        if a != '𔮦':
            try:
                print('i=', i, a)
            except UnicodeEncodeError as msg:
                print(f'Exception, msg={msg}')