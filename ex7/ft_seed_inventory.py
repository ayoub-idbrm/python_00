def ft_seed_inventory(seeds, quantity, unity):
    seeds = seeds[0].upper() + seeds[1:]
    if unity == "packets":
        print(f"{seeds} seeds: {quantity} packets available")
    elif unity == "grams":
        print(f"{seeds} seeds: {quantity} grams total")
    elif unity == "area":
        print(f"{seeds} seeds: covers {quantity} square meters")
    else:
        print("error")


ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")
