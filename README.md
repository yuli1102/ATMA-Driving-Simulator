# Citation
If you use this repository, please cite the following paper:

Li, Y., Wang, B., Li, W., & Qin, R. (2023). Simulation Study of Passing Drivers’ Responses to the Autonomous Truck-Mounted Attenuator System in Road Maintenance. Transportation Research Record, 0(0).

~~~~  
@article{li2023simulation,
  title={Simulation Study of Passing Drivers’ Responses to the Autonomous Truck-Mounted Attenuator System in Road Maintenance},
  author={Li, Yu and Wang, Bill and Li, William and Qin, Ruwen},
  journal={Transportation Research Record},
  pages={03611981221144281},
  year={2023},
  publisher={SAGE Publications Sage CA: Los Angeles, CA}
  doi = {10.1177/03611981221144281},
}
~~~~

# ATMA-Driving-Simulator
ATMA: autonomous truck-mounted attenuator
This driving simulator was designed and developed for the ATMA study. In this study, out team aim to discover how drivers passing through road maintenance areas perceive, understand, and react to the ATMA system.

This gif shows What are the passing drivers supposed to do:
<p align="center">
  <img src="https://github.com/yuli1102/ATMA-Driving-Simulator/blob/main/expection-edit.gif" width="40%" />
</p>

Concerns include:
(1) Fail to change lane in time; (2) Cut into the ATMA system; (3) Drivers may fail to recognize the connected vehicles and autonomous driving technologies implemented in the ATMA.
<p align="center">
  <img src="https://github.com/yuli1102/ATMA-Driving-Simulator/blob/main/fail%20change%20lane-edit.gif" width="30%" />
  <img src="https://github.com/yuli1102/ATMA-Driving-Simulator/blob/main/cut-in-edit.gif" width="30%" /> 
</p>


## Simulator Design and Development
### Road
We simulated a segment of the interstate highway in New York state with a speed limit of 65 mph. Here is a comparison between our simulation and the real-world map on Google Maps. This road segment includes a rest area. In our experiment, participants started on the right side of the road and were asked to exit the highway and reach the rest area to complete the experiment.
![image](https://user-images.githubusercontent.com/44143351/232259101-9e0c412c-9c02-4726-91b7-a267a6d6f136.png)
### Views
We designed two views for our driving simulator: the driver's view and the experiment coordinator's view. The driver's view includes a front view, rear views from the side mirrors, and a dashboard with the vehicle's speedometer and tachometer, as well as turn signal indicators. The experiment coordinator's view provides a bird's-eye view on the right side, which allows experiment coordinator to observe the experiment in progress and easily control the experiment settings from another monitor.
![image](https://user-images.githubusercontent.com/44143351/232259147-b9d4ea28-3440-466a-a863-75c27a68d51b.png)




(1) Driving data collected from the driving simulation. 

"Raw Data"-> participant xx -> "experiment 1" is the low traffic volume data, "experiment 2" is collected in high traffic volume. 

(2) Gaze data collected from Tobii eye tracking.

"Raw Data"-> participant xx -> "Eye_tracker_Data_Px_xxxx.xlsx". 

(3) Code of data processing can be found in "Data Process" folder.  

(4) The processed and combined data can be found in release. Name is "Driving_Simulation_Experiment_Data_All_0723.csv". 

(5) A demo of designed driving simulation. Download "Demo.zip" in release, click "HighwayI90.exe" to start the simulator.

This demo is only support keyboard. Some function keys are listed following:
w --> accelerator;
s --> brake;
a,d --> wheel;
q,e -->left/right indicator;
B --> change to backing mode;

More videos and details can be found in my website:https://sites.google.com/view/yuli1102/projects/driving-simulation/atma-driving-simulation-study

Contact me if you need the source code for the simulation.

