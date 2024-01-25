def solve(numheads, numlegs):
    for num_chikens in range(numheads + 1):
        num_rabbits = numheads - num_chikens
        solution = 2 * num_chikens + 4 * num_rabbits

        if solution == numlegs:
            return num_chikens, num_rabbits

    return None


heads = 35
legs = 94
solution = solve(heads, legs)
if solution is not None:
    num_chikens, num_rabbits = solution
    print(f"We have {num_chikens} chikens and {num_rabbits} rabits")
else:
    print("No solution found")



