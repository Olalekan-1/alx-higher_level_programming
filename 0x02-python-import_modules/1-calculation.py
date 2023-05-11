#!/usr/bin/python3

a = 10
b = 5

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)
    print(f"{a:d} + {b:d} = {c:d}")
    print(f"{a:d} - {b:d} = {d:d}")
    print(f"{a:d} * {b:d} = {e:d}")
    print(f"{a:d} / {b:d} = {f:d}")
