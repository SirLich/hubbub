# Welcome to Hubbub!
Fall 2019, Databases Final Project

#### Authors:
Liam Koehler, David Chong 

### What is Hubbub?<br />
Hubbub is a command line activity-selection tool. <br />

Hubbub contains the following functionality:
 - **Play**: The classic game 
 - **View**: View all available activities
 - **Add:** Add a new activity 
 - **Delete:** Delete an activity 
 
The classic version of hubbub is played by pressing p on the main menu. The game will ask the user a series of questions. These questions are used to generate a list of activity-tags for the user. For each tag, the mongoDb is queried, and the returned results are built into a weighted map of activities. After completing a round of Hubbub you are shown a list of activities, based on the weighted map.

### How to control Hubbub<br />
Enter commands based on the bracketed letter.<br />
Example:<br />
Enter p to play Hubbub<br />
When adding an activity, enter activity tags one at a time. When complete enter "a" to add or "q" to cancel adding an activity.<br />

### Hidden features:<br />
Hidden delete activity mode (delete on home screen)<br />
Hidden dev mode to view weights of activities after playing Hubbub (d on home screen)<br />
Hidden beans mode (beans on home screen)<br />

### Available tags:<br />
outside<br />
inside<br />

winter<br />
summer<br />
spring<br />
fall<br />

day<br />
night<br />

active<br />
relaxing<br />

local<br />
remote<br />

productive<br />
recreational<br />

### Additional notes:<br />
Currently, the number of participants is ignored. Due to the small pool of activities and possibly our filtering technique, using the participants count to display activities excluded many activities which should have gotten higher weights (or weights at all). In the future this function should be considered as well as accounting for binary tags -- example an activity that can only happen at night should be impacted more than it currently is -- so things like "watch stars" shouldn't show up if you indicate it is day.
