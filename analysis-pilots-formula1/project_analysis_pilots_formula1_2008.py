
import csv
import os

# Define the points for positions 1 to 8 in the Formula 1 Rank
points_position = {1: 10, 2: 8, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

def specific_stats(driver):

    """
    This function takes the name of a driver as input and returns a list containing:
    - Total points of each driver
    - Number of wins
    - Number of podiums
    """

    input_file = '/content/formula1_data.csv'

    if not os.path.exists(input_file):
        print(f"File not found: please upload 'formula1_data.csv' into the workspace.")
        return

    total_points = 0
    num_podiums = 0
    num_wins = 0
    driver_found = False

    with open(input_file, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['Driver'].lower() == driver.lower():
                driver_found = True
                position = int(row['Position'])

                if position in points_position:
                    points = points_position[position]
                    total_points += points

                    if position <= 3:
                        num_podiums += 1

                    if position == 1:
                        num_wins += 1
                else:
                  total_points += 0

        if not driver_found:
            print(f"Driver {driver} not found in this dataset.")
            return

    print([total_points, num_podiums, num_wins])

driver_name = input("Name of the pilot: ")
specific_stats(driver_name)

def final_rank_drivers():

    """
    This function reads race data from a CSV file, calculates the total points for each driver,
    and saves the drivers' standings in a text file called "Final_rank_Formula1_2008.txt".
    """

    input_file = '/content/formula1_data.csv'

    if not os.path.exists(input_file):
        print(f"{input_file} not found")
        return

    rank_drivers = {}

    with open(input_file, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            driver_name = row['Driver']
            position = int(row['Position'])

            if position in points_position:
                points = points_position[position]
                rank_drivers[driver_name] = rank_drivers.get(driver_name, 0) + points

    rank_drivers_sorted = dict(sorted(rank_drivers.items(), key=lambda item: item[1], reverse=True))

    output_file = '/content/Final_Rank_Formula1_2008.txt'
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('Drivers Standings 2008 Formula 1\n')
        for rank, (driver, points) in enumerate(rank_drivers_sorted.items(), start=1):
            file.write(f"{rank}. {driver}: {points} points\n")

    return rank_drivers_sorted

final_rank_drivers()

def final_rank_teams():
    """
    This function reads the drivers' standings from the txt.file previously generated,
    calculates the total points for each team summing up the points of each driver,
    and returns a dictionary of teams and their total points.
    """
    output_file = '/content/Final_Rank_Formula1_2008.txt'

    if not os.path.exists(output_file):
        print(f"{output_file} not found")
        return

    drivers_teams = {
        'Hamilton': 'McLaren',
        'Massa': 'Ferrari',
        'Raikkonen': 'Ferrari',
        'Kubica': 'BMW',
        'Alonso': 'Renault',
        'Heidfeld': 'BMW',
        'Kovalainen': 'McLaren',
        'Vettel': 'Toro Rosso',
        'Trulli': 'Toyota',
        'Glock': 'Toyota'
    }

    rank_drivers = {}

    with open(output_file, encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
        for line in lines[1:]:
            parts = line.strip().split(': ')
            if len(parts) == 2:
                driver = parts[0].split('. ')[1]
                points = int(parts[1].split()[0])
                rank_drivers[driver] = points

    rank_teams = {}
    for driver, points in rank_drivers.items():
        team = drivers_teams.get(driver)
        if team:
            rank_teams[team] = rank_teams.get(team, 0) + points

    rank_teams_sorted = dict(sorted(rank_teams.items(), key=lambda item: item[1], reverse=True))

    return rank_teams_sorted

final_rank_drivers()
