def main():
    all_entered_values = []
    
    while True:
        year = int(input("Enter the year (or -1 to stop): "))
        if year == -1:
            break
        state = input("Enter the name of the state: ")
        population = int(input("Enter the population: "))
        all_entered_values.append([year, state, population])
    
    year_to_sum = int(input("Enter the year for which to sum the population: "))
    
    sum_population_for_year(all_entered_values, year_to_sum)

def sum_population_for_year(all_entered_values, year_to_sum):
    total_population = 0
    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            total_population += entry[2]
    
    print(f"Total population for the year {year_to_sum}: {total_population}")

if __name__ == '__main__':
    main()
