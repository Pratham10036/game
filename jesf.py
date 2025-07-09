import random
import string
import math
from datetime import datetime, timedelta

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def random_prime(start=2, end=100):
    primes = [x for x in range(start, end) if is_prime(x)]
    return random.choice(primes)

def random_float():
    return round(random.uniform(1.0, 100.0), 2)

def print_random_data():
    for _ in range(10):
        print(f"String: {random_string()}, Prime: {random_prime()}, Float: {random_float()}")

def generate_dates():
    start = datetime(2020, 1, 1)
    end = datetime(2023, 12, 31)
    dates = [random_date(start, end) for _ in range(5)]
    for d in dates:
        print("Random date:", d.strftime("%Y-%m-%d"))

def main():
    print("Random Data Samples:")
    print_random_data()
    print("\nRandom Dates:")
    generate_dates()

if __name__ == "__main__":
    main()