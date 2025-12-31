def ft_count_harvest_recursive(n):
    if n == 0:
        return
    ft_count_harvest_recursive(n - 1)
    print(f"Day {n}")


ft_count_harvest_recursive(int(input("days until harvest: ")))
print("Harvest time!")
