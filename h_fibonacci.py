'''
Write a function that generates the Fibonacci series up to a specified number of terms.
'''

def fibonacci(n: int) -> list[int]:
    series = []
    if n < 1:
        return series
    elif n == 1:
        series.append(0)
    else:
        series.append(0)
        series.append(1)
        while len(series) < n:
            series.append(series[-1]+series[-2])
    return series

n = int(input("Number of terms: "))
print(f"Fibonacci series: {fibonacci(n)}")
