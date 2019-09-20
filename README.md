# ekrankayit

# Kullanım:
## Kayıt Başlat
kayit record

## Kayıt Bitir ve FTP ile yolla
kayit stop

# Cython ile derlemek için:
cython3 --embed -o kayitet.c kayitet.py 

gcc -v -Os -I /usr/include/python3.7m/ -L /usr/lib/x86_64-linux-gnu/  -o kayitet kayitet.c  -lpython3.7m  -lpthread -lm -lutil -ldl
