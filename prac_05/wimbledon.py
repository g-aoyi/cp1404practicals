filename = "wimbledon.csv"
champions = {}
countries = []

with open(filename, "r", encoding="utf-8-sig") as in_file:
    lines = in_file.readlines()
    for line in lines[1:]:
        info = line.strip().split(",")
        if info[2] in champions:
            champions[info[2]] += 1
        else:
            champions[info[2]] = 1
        if info[1] not in countries:
            countries.append(info[1])
print("Wimbledon Champions:")
for key in champions:
    print(f"{key} {champions[key]}")
print(f"\nThese {len(countries)} countries have won Wimbledon:")
print(", ".join(countries))
