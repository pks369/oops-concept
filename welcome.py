# import sys
# print('a',sys.argv[0])

# import collections
# s="John Deo"
# freqency=collections.Counter(s)
# print(freqency)
# repeated={}
# for key,value in freqency.items():
#     if value >1:
#            repeated[key]=value
# print(repeated)
    #  print(key,value )

import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



   
    