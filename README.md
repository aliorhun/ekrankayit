# Ekran Kayıt

# Kurulum:
> sudo cp kayitet.py /usr/local/bin/kayit

> chmod +x /usr/local/bin/kayit

# Kullanım:
## Kayıt Başlat
> kayit record

## Manuel Kayıt Başlat
> kayit recorddir

## Kayıt Bitir ve FTP ile yolla
> kayit stop

# Cython ile derlemek için:
> cython3 --embed -o kayitet.c kayitet.py 

> gcc -v -Os -I /usr/include/python3.7m/ -L /usr/lib/x86_64-linux-gnu/  -o kayitet kayitet.c  -lpython3.7m  -lpthread -lm -lutil -ldl

> sudo cp kayitet /usr/local/bin/kayit

> chmod +x /usr/local/bin/kayit
