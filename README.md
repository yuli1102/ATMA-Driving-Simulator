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
<p align="center">
  <img src="https://user-images.githubusercontent.com/44143351/232259101-9e0c412c-9c02-4726-91b7-a267a6d6f136.png" width="60%" />
</p>

### Views
We designed two views for our driving simulator: the driver's view and the experiment coordinator's view. The driver's view includes a front view, rear views from the side mirrors, and a dashboard with the vehicle's speedometer and tachometer, as well as turn signal indicators. The experiment coordinator's view provides a bird's-eye view on the right side, which allows experiment coordinator to observe the experiment in progress and easily control the experiment settings from another monitor.
<p align="center">
  <img src="https://user-images.githubusercontent.com/44143351/232259147-b9d4ea28-3440-466a-a863-75c27a68d51b.png" width="60%" />
</p>

### Vehicles and the Traffic Volume
Our simulation includes three types of vehicles: the ego vehicle (i.e., the driver's own vehicle), ATMA (which consists of two trucks with a gap of about 100 feet), and some background vehicles. We designed two different traffic volume scenarios for our experiment by setting different gaps between the background vehicles: a high traffic volume scenario and a low traffic volume scenario. This figure is a schematic diagram of the vehicle deployment at the beginning of simulation and in the high traffic volume scenario.
<p align="center">
  <img src="https://user-images.githubusercontent.com/44143351/232259199-a6c542b3-6d99-43d0-b10c-53d1b12673c4.png" width="60%" />
</p>

### Interface Between Participants and the Ego Vehicle
We use a Logitech G29 wheel and floor pedals to control the ego vehicle. Operations such as the brake, accelerator, and left-right turn signals are designed for the wheel and pedals. Additionally, a screen-based eye tracker is used to capture participants' eye movements. Here is a picture that shows how our participants performed the experiment.
<p align="center">
  <img src="https://user-images.githubusercontent.com/44143351/232259325-06755426-9882-4991-9fe6-16232d179925.png" width="50%" />
</p>


## Data Collection 
### Simulation Data Collection
During the experiment, we collect three different types of data from the simulation: the first one is the driving operation data, such as the brake, speed; and the second one is the position data, including the distance from ego vehicle to the exit and to the ATMA; third type data is the 2-dimension coordinates of the ATMA on the screen as shown as this following figure.  This will be used to compare with the participant’s gaze data. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/44143351/232259504-ae0b327e-f7fe-4f77-8ade-f470d97cc3ab.png" width="50%" />
</p>
The raw data can be found: "Raw Data"-> participant xx -> "experiment 1" is the low traffic volume data, "experiment 2" is collected in high traffic volume. 

### Gaze Data Collection
Participants' gaze data is collected in 2-dimensional coordinates on the screen using a Tobii screen-based eye tracker. Based on the gaze point coordinates and the eye's position, we also collect the fixation coordinates. A fixation refers to a group of continuous gaze points. In addition to the coordinate data, we also collect data on the participants' pupil diameters. More details of these variable definations can be found from Tobii website.

The raw data can be found: "Raw Data"-> participant xx -> "Eye_tracker_Data_Px_xxxx.xlsx". 

### Questionnaire Data Collection
In addition to the simulation and gaze data, we also ask participants to complete a questionnaire to obtain their subjective responses. The questionnaire includes questions related to participants' backgrounds, such as age, gender, and driving experience, as well as questions about their recall of the driving experience during the experiment, such as whether they remember the speed limit and why they changed lanes. The important part of the questionnaire consists of three questions related to participants' recognition of the ATMA, including whether they remember what the truck looks like, whether they know the follower truck is unmanned, and whether they understand the entir
<p align="center">
  <img src="https://user-images.githubusercontent.com/44143351/232259504-ae0b327e-f7fe-4f77-8ade-f470d97cc3ab.png" width="50%" />
</p>
![image](https://user-images.githubusercontent.com/44143351/232259663-08f5b3ce-08df-4a3b-b9ce-23452f1c3b7f.png)



# Others

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
