This project implements the following three functions from a cvs.file called "formula1_data.csv:

1) A function that takes as input the name of a driver and returns a list containing the driver's total points, the number of wins (how many times the driver finished first), and the number of podiums (how many times the driver finished in the top three).
2) A function that does not take any parameters as input and returns a dictionary consisting of key-value pairs, where the key is a string containing the driver's name, and the associated value is an integer representing the total points the driver has accumulated by the end of the World Championship. It then saves the standings in a txt file in the following format:
   
Drivers Standings 2008 Formula 1
Name1: Points
Name2: Points
...

3) A function that does not take any parameters as input and returns a dictionary consisting of key-value pairs, where the key is a string containing the name of the constructor (Team), and the associated value is an integer representing the total points the constructor has accumulated by the end of the World Championship. The points accumulated by a constructor (Team) are the sum of the points that the drivers racing for the constructor have accumulated during the year. To achieve this, it uses the data saved in the previously created file.
