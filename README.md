# Welcome to Hubbub!
Fall 2019, Databases Final Project

### What is Hubbub?<br />
Hubbub is a command line activity selection tool. <br />
When Hubbub is played a series of questions are asked. These questions are used to query a Mongo database that contains many activities which are assigned a list of tags. The answers provided are compared to the various activity tags. After completing a round of Hubbub you are shown a list of activities which best match the answers provided.

### How to control Hubbub<br />
Enter commands based on the bracketed letter.<br />
Example:<br />
Enter p to play Hubbub<br />
When adding an activity, enter activity tags one at a time. When complete enter "a" to add or "q" to cancel adding an activity.<br />

### Features of Hubbub:<br />
Play Hubbub (p on home screen)<br />
View all activities (v on home screen)<br />
Add an activity (a on home screen)<br />
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
Currently number of participants is ignored. Due to the small pool of activities and possibly our filtering technique, using participant count to display activities excluded many activities which should have gotten higher weights (or weights at all). In the future this function should be considered as well as accounting for binary tags -- example an activity that can only happen at night should be impacted more than it currently is -- so things like "watch stars" shouldn't show up if you indicate it is day.
