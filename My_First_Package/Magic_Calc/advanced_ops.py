import math

def power(base, exp):
    return math.pow(base, exp)

print(power(2, 3))  # 8.0

def sqrt(number):
    """수의 제곱근을 계산합니다."""
    if number < 0:
        raise ValueError("음수의 제곱근은 계산할 수 없습니다.")
    return math.sqrt(number)

def magic_multiply(number, magic_factor=7):
    """수를 마법의 숫자(기본값 7)로 곱합니다."""
    return number * magic_factor