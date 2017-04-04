# CloudAssignment4

In this assignment, we built mapper and reducer scripts to analyze the traffic data of New York City and yield summary counts for each vehicle that
describe the total count, per vehicle type, that the vehicle type was involved in an incident.

**Running the analysis**

1. Clone the repository in CSCloud
1. Run the command *hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/varanasa/mapper.py  -mapper /home/varanasa/mapper.py -file /home/varanasa/reducer.py   -reducer /home/varanasa/reducer.py -input /data/nyc/nyc-traffic.csv  -output /user/varanasa/myoutput*
 - This gives the logs while running Mapper and Reducer scripts.
1. Then run the command *hadoop fs -cat /user/varanasa/myoutput/**
 - This gives the output, that is the summary count of the vehicle types involved.
 
**Summary Counts**
 
AMBULANCE 3713 <br>
BICYCLE 24153 <br>
BUS 25871 <br>
FIRE TRUCK  1333 <br>
LARGE COM VEH(6 OR MORE TIRES) 27981 <br>
LIVERY VEHICLE  17775<br>
MOTORCYCLE      10029<br>
OTHER   51360<br>
PASSENGER VEHICLE 1005161<br>
PEDICAB 123<br>
PICK-UP TRUCK 26281 <br>
SCOOTER 534<br>
SMALL COM VEH(4 TIRES)  30048<br>
SPORT UTILITY / STATION WAGON   363210<br>
TAXI    63892<br>
UNKNOWN 105481<br>
VAN     51666<br>

