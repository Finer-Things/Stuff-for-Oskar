class Number:
    def __init__(self, value, primes = []):
        self.value = value
        self.primes = primes

    def get_primes(self):
        if not isinstance(self.value, int):
            return "Not an integer."
        if self.value <= 0:
            return "Not a positive integer"
        dividend = self.value
        divisor = 2
        primes_list = []
        while dividend > 1:
            q, r = divmod(dividend, divisor)
            if r == 0:
                primes_list.append(divisor)
                dividend = dividend//divisor
            else: 
                divisor += 1
        self.primes = sorted(primes_list)

    def print_primes(self):
        primes_list = self.get_primes()
        n = len(primes_list)
        print_string = ""
        for i, prime in enumerate(primes_list[:-1]):
            print_string += str(prime)
            print_string += " * "
        print_string += str(primes_list[-1])
        print(print_string)


my_number = Number(64)
my_number.get_primes()
print(my_number.primes)
# my_number.print_primes()

    