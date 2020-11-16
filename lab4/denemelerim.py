
def fonksiyon(*args,**kwargs):
    for i in args:
        print(i)
    for v,k in kwargs.items():
        print('anahtar: ',k,'Degerimiz: ',v)
 
fonksiyon(1,2,3, 'args' , deger = 'kwargs')