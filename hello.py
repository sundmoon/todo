def main():
    print("Hello from todo!")


if __name__ == "__main__":
    main()
    def fib_tail(n, a=0, b=1):
        if n == 0:
            return a
        if n == 1:
            return b
        return fib_tail(n-1, b, a+b)

    def fibonacci(n):
        if n < 0:
            raise ValueError("n must be non-negative")
        return fib_tail(n)
    
    print(fibonacci(180))