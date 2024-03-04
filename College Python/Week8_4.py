def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier
closure = multiplier_of(5)
print(closure(3))
