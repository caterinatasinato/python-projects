# Formula 1 Analysis Project

This project implements the following 3 functions, importing a CSV file called `formula1_data.csv`:

1. **Driver Statistics Function:**
   - Takes as input the name of a driver.
   - Returns a list containing:
     - The driver's total points.
     - The number of wins (how many times the driver finished first).
     - The number of podiums (how many times the driver finished in the top three).

2. **Drivers Standings Function:**
   - Does not take any parameters as input.
   - Returns a dictionary consisting of key-value pairs:
     - Key: A string containing the driver's name.
     - Value: An integer representing the total points the driver has accumulated by the end of the World Championship.
   - Saves the standings in a txt file called `Final_Rank_Formula1_2008.txt`.

3. **Constructors Standings Function:**
   - Does not take any parameters as input.
   - Returns a dictionary consisting of key-value pairs:
     - Key: A string containing the name of the constructor (Team).
     - Value: An integer representing the total points the constructor has accumulated by the end of the World Championship.
   - The points accumulated by a constructor (Team) are the sum of the points that the drivers racing for the constructor have accumulated during the year.
   - Uses the data saved in the previously created txt file.

## Data

The data used in this project is sourced from a CSV file named `formula1_data.csv`.

## Usage

1. Ensure you have the CSV file `formula1_data.csv` in the project directory.
2. Implement the functions as described above.
3. Run the functions to analyze the Formula 1 data and generate the standings.

## Example

```python
# Example usage of the functions

# Import the necessary functions
from formula1_analysis import get_driver_statistics, generate_drivers_standings, generate_constructors_standings

# Get statistics for a specific driver
driver_name = "Lewis Hamilton"
statistics = get_driver_statistics(driver_name)
print(statistics)

# Generate and save drivers standings
drivers_standings = generate_drivers_standings()
print(drivers_standings)

# Generate and save constructors standings
constructors_standings = generate_constructors_standings()
print(constructors_standings)
