# Girilen parola içinde türkçe karakter hatası veriniz.

def check_password(parola):
    turkce_karakterler = 'şçğüöıİ'

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('Parola türkçe karakter içeremez.')
        else:
            pass
    print('geçerli parola')    

parola = input('parola: ')

try:
    check_password(parola)    
except TypeError as err:
    print(err)
