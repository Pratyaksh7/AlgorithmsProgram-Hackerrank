def main():
    for _ in range(int(input())):
        n = int(input()) - 1

        q = n // 3
        total_3 = q * q
        q -= 1
        sum_of_series = (q * (q + 1)) // 2
        sum_of_3 = (total_3 - sum_of_series) * 3

        q = n // 5
        total_5 = q * q
        q -= 1
        sum_of_series = (q * (q + 1)) // 2
        sum_of_5 = (total_5 - sum_of_series) * 5

        q = n // 15
        total_15 = q * q
        q -= 1
        sum_of_series = (q * (q + 1)) // 2
        sum_of_15 = (total_15 - sum_of_series) * 15

        print((sum_of_3 + sum_of_5) - sum_of_15)


main()