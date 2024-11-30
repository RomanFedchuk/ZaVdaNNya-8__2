import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції '{func.__name__}': {execution_time:.6f} секунд")
        return result
    return wrapper


@measure_time
def sample_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


def test_measure_time():
    print("Тест 1: Обчислення суми перших 10 чисел")
    sample_function(10)

    print("\nТест 2: Обчислення суми перших 1000 чисел")
    sample_function(1000)

    print("\nТест 3: Обчислення суми перших 100000 чисел")
    sample_function(100000)


if __name__ == "__main__":
    test_measure_time()