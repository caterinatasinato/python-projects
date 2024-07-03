# Formula 1 Analysis Project

This project implements the following 3 functions, importing a CSV file called `formula1_data.csv`:

1. **Driver Statistics Function:**
   - Function: `specific_stats(driver)`
   - Takes as input the name of a driver.
   - Returns a list containing:
     - The driver's total points.
     - The number of wins (how many times the driver finished first).
     - The number of podiums (how many times the driver finished in the top three).

2. **Drivers Standings Function:**
   - Function: `final_rank_drivers()`
   - Does not take any parameters as input.
   - Reads race data from a CSV file.
   - Calculates the total points for each driver.
   - Returns a dictionary consisting of key-value pairs:
     - Key: A string containing the driver's name.
     - Value: An integer representing the total points the driver has accumulated by the end of the World Championship.
   - Saves the standings in a txt file called `Final_Rank_Formula1_2008.txt`.

3. **Constructors Standings Function:**
   - Function: `final_rank_teams()`
   - Does not take any parameters as input.
   - Reads the drivers' standings from the previously generated txt file.
   - Calculates the total points for each constructor by summing up the points of the drivers racing for the constructor.
   - Returns a dictionary consisting of key-value pairs:
     - Key: A string containing the name of the constructor (Team).
     - Value: An integer representing the total points the constructor has accumulated by the end of the World Championship.

## Data

The data used in this project is sourced from a CSV file named `formula1_data.csv`.

### Dataset Structure

The dataset `formula1_data.csv` contains the results of the 2008 Formula 1 World Championship season. It consists of 180 rows and the following 5 columns:

1. **Driver:** Name of the Driver
2. **Team:** Constructor for which the driver races
3. **Race:** City where the Grand Prix was held
4. **Country:** Country where the Grand Prix was held
5. **Position:** A number between 0 and 8 representing the driver's position in the race (0 means the driver did not finish in the top 8).

## Usage

1. Ensure you have the CSV file `formula1_data.csv` in the project directory.
2. Implement the functions as described above.
3. Run the functions to analyze the Formula 1 data and generate the standings.

## Example

```python
# Import the necessary functions
from formula1_analysis import specific_stats, final_rank_drivers, final_rank_teams

# Get statistics for a specific driver
driver_name = input("Name of the pilot: ")
specific_stats(driver_name)

# Generate and save drivers standings
drivers_standings = final_rank_drivers()
print(drivers_standings)

# Generate and save constructors standings
constructors_standings = final_rank_teams()
print(constructors_standings)

