# Використовуйте модуль часу, щоб порівняти продуктивність «ефективного» методу пошуку простих чисел
# із простою реалізацією  (без перерв, тестування за всіма числами тощо).
# Перевірте кілька діапазонів пошуку простих чисел (наприклад, до 100, до 1000 і т.д.)
# Ефективний метод - будь-який математично визначиний підхід обрахунку.
import math
import time
# [2,n] - діапазон в якому шукаємо прості числа

def simple_prime_search(n):
    simple_numbers = []
    for i in range(2,n+1):
        count = 0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            simple_numbers.append(i)
    return simple_numbers # список простих чисел

# print(simple_prime_search(100))

# Метод Решето Ератосфена
def sieve_eratosthenes(n):
    prime = [True] * n
    prime[0], prime[1] = False, False  # 0 та 1 не є простими
    for i in range(2, math.ceil(math.sqrt(n))):  # від 2 до квадратного кореня з n
        if prime[i]:  # якщо просте видаляємо всі числа кратні до нього
            j = i * i  # для i=2,j будуть такі значення 4,6,8,10,12... для i=3 j — 9,12,15,18,21...
            while j < n:
                prime[j] = False
                j += i
    simple_numbers=[]
    for k in range(0,len(prime)):
        if prime[k]:
            simple_numbers.append(k)
    return simple_numbers  # список простих чисел

# print (sieve_eratosthenes(100))

def measure_time(func,*args):
    start_time=time.time()
    result=func(*args)
    end_time=time.time()
    print(f"Time of the {func.__name__} function: {end_time-start_time:.10f} sec.")
    return  result

# measure_time(simple_prime_search, 100)
# measure_time(sieve_eratosthenes, 100)
print(measure_time(simple_prime_search, 100))
print(measure_time(sieve_eratosthenes, 100))