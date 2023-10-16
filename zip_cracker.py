import itertools
import zipfile

# ↓↓↓↓↓ Here the file you want to crack. ↓↓↓↓↓
name = 'crackme.zip'

# ↓↓↓↓↓ Here is any information you know that can help to simplify the cracking. ↓↓↓↓↓
# ↓↓↓↓↓ For example: ↓↓↓↓↓
# ↓↓↓↓↓ Does it include numbers? ↓↓↓↓↓
# ↓↓↓↓↓ Does it include any exclamation signs? ↓↓↓↓↓
# ↓↓↓↓↓ ETC ↓↓↓↓↓
# ↓↓↓↓↓ In this case, I know that the password consists of only numbers. ↓↓↓↓↓
chars = '0123456789'

# ↓↓↓↓↓ Here, introduce the quantity of characters the password may have. ↓↓↓↓↓
for guess in itertools.product(chars, repeat=5):
     guess = ''.join(guess)
     print(guess)
     try:
         with zipfile.ZipFile(name,'r') as zip_ref:
             zip_ref.extractall(pwd=guess.encode('utf-8'))
             print(f'El archivo fue extraido con éxito. Contraseña {guess}')
             break
     except Exception as e:
         print(f'Error al extraer el archivo: {e}')