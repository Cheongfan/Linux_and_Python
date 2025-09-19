import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    start = time.time()
    yield
    end = time.time()
    print(f"{name} 耗时: {end-start:.4f}秒")

with timer("计算斐波那契数列"):
    n = 20000
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print(f"斐波那契数列第{n}项: {a}")

