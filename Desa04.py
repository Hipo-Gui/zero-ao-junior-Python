import math
# 1
def fator(n):
    if n == 0:
    # Quando 'n' for igual a '1' o programa terá que retornar '2'.
        return 1  
    else:
        return n * fator(n - 1)
# Se N não for igual a 1, então ele irá fazer n * Fator, depois n - 1.
 
# print(fator(5))
result = fator(5)
c = 1.0
d = 3 
f = c + d 
print(result, f)
