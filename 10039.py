'''
Path

10039 - Railroads

 she is looking for the train which gets her to Darmstadt as early as possible. However, she dislikes to get to the station too early, so if there are several schedules with the same arrival time then she will choose the one with the latest departure time.

Input
 The very first line of the input gives the number of scenarios. Each scenario consists of three parts.  Part one lists the names of all cities connected by the railroads. It starts with a number 1 < C ≤ 100, followed by C lines containing city names. These names consist of letters.  Part two describes all the trains running during a day. It starts with a number T ≤ 1000 followed by T train descriptions. Each of them consists of one line with a number ti ≤ 100 and ti more lines with a time and a city name, meaning that passengers can get on or off the train at that time at that city.  Part three consists of three lines: Line one contains the earliest journey’s starting time, line two the name of the city where she starts, and line three the destination city. The two cities are always different.

Output
 For each scenario print a line containing “Scenario i”, where i is the number of the scenario starting at 1.  If a connection exists then print the two lines containing zero padded timestamps and locations as shown in the sample. Use blanks to achieve the indentation. If no connection exists on the same day (i.e., arrival before midnight) then print a line containing “No connection”.  After each scenario print a blank line.
'''

