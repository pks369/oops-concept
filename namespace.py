class Mobile:
    fp='yes'

    @classmethod
    def show(cls):
        cls.fp
        print(cls.fp)
realme=Mobile() 
redme=Mobile() 
vivo=Mobile() 
moto=Mobile() 
print()
print('realme FP:',realme.fp)
Mobile.fp='Not working'
print('redme FP:',redme.fp)
Mobile.fp='No'
print('vivo FP:',vivo.fp)
moto.fp='some time working'
print('moto FP:',moto.fp)




     