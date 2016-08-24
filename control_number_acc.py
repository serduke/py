'''
Created on 14 апр. 2016 г.

@author: serav
'''

acc = 'KZСС1111111111111891'
cc = 98 - int(acc[4:]+'203500')%97

if cc< 10:
    cc = str('0'+str(cc))
print(cc)


