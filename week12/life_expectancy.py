with open('life-expectancy.csv') as life:
    print()

    year_of_user = int(input('Enter the year of interest: '))
    print()
    country_of_user = input('Enter a Country of interest: ').capitalize()
    life_expectancy = 0
    max_life_expectancy = 0
    max_life_expectancy_of_year = 0
    max_life_expectancy_of_country = 0
    min_life_expectancy = 1000
    min_life_expectancy_of_year = 1000
    min_life_expectancy_of_country = 1000

    country = ''
    sum_of_year = 0
    sum_of_year_of_country = 0
    data = []
    count = 0
    count_of_country = 0
    n = 0

    for line in life:

        if n == 0:
            n = n+1  # to avoid the header because do not have useful data
        else:
            group = line.split(',')
            life_expectancy = float(group[3].strip())
            life_expectancy_average = float(group[3].strip())
            country = group[0]
            year = int(group[2])
            year_of_average = int(group[2])
            data.append(group)

#   max country and life expectation
            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_country = country
                year_of_max = year
#   min country and life expectation
            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_country = country
                year_of_min = year

#  average
# The average life expectancy across all countries was 54.95
            if year_of_average == year_of_user:
                sum_of_year += life_expectancy_average
                count += 1
# The max life expectancy was in Norway with 73.49
                if life_expectancy_average > max_life_expectancy_of_year:
                    max_life_expectancy_of_year = life_expectancy_average
                    max_country_of_year = country
# The min life expectancy was in Mali with 28.077
                if life_expectancy_average < min_life_expectancy_of_year:
                    min_life_expectancy_of_year = life_expectancy_average
                    min_country_of_year = country


# Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
            if country_of_user == country:
                sum_of_year_of_country += life_expectancy_average
                count_of_country += 1

                if life_expectancy_average > max_life_expectancy_of_country:
                    max_life_expectancy_of_country = life_expectancy_average
                if life_expectancy_average < min_life_expectancy_of_country:
                    min_life_expectancy_of_country = life_expectancy_average

    average = sum_of_year / count

    average_of_country = sum_of_year_of_country / count_of_country

    print()
    print('___________________________________________________________________________________')
    print()

    print(
        f'The overall max life expectancy is: {max_life_expectancy} from {max_country} in {year_of_max}')
    print(
        f'The overall min life expectancy is: {min_life_expectancy} from {min_country} in {year_of_min}')

    print()

    print(
        f'for the year {year_of_user}:')
    print(
        f'The average life expectancy across all countries was {average:.2f}')
    print(
        f'The max life expectancy was in {max_country_of_year} with {max_life_expectancy_of_year}')
    print(
        f'The min life expectancy was in {min_country_of_year} with {min_life_expectancy_of_year}')
    print()

    print(
        f'for the Country {country_of_user}:')
    print(
        f'The average life expectancy in {country_of_user} is {average_of_country:.2f}')
    print(
        f'The max life expectancy  in {country_of_user} is {max_life_expectancy_of_country}')
    print(
        f'The min life expectancy in {country_of_user} is {min_life_expectancy_of_country}')

    print('___________________________________________________________________________________')
    print()
