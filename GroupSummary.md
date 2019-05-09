## A concise description of the project (including goals)

Hubbub is a command line activity selection tool. 
When Hubbub is played a series of questions are asked.
These questions are used to query a Mongo database that contains many activities which are assigned a list of tags.
The answers provided are compared to the various activity tags. 
After completing a round of Hubbub you are shown a list of activities which best match the answers provided.
Our main goal was to create a tool that would ask users a series of questions and respond with a list of activities most similar to the answers they provided, which we did.
After we met that goal we added new goals like being able to add and remove activities through the tool, which we also did.

## An abstract representation of the data model(s) used (if appropriate)

Data was imported and can be inserted using JSON format. Each activity entry contains: a name, the minimum and maximum number of participants, and a list of activity tags.
We have a 'counter', not part of the actual database, that ticks up everytime a question is answered an matched to a tag. 
This is used to 'weigh' activities higher than one another.

## Goals achieved and goals not achieved

Our main goal was to create a tool that would ask users a series of questions and respond with a list of activities most similar to the answers they provided, which we did.
After we met that goal we added new goals like being able to add and remove activities through the tool, which we also did.
We originally had the idea of creating an Angular application, which we didn't as it was outside the scope of time and would not add really anything to the database side of the project.

## Potential for future work

The database could always be populated with more activities. We would like to implement the min and max participants. When we tried to use this filter in a similar way to other tags it filtered out too many activities that still could make sense. We must implement this better in the future, possibly with more activities to minimize overfiltering.

## Overall reaction

We are both very happy with the project and what we ended up creating. It is in a complete state and could be used or continued to be worked on if persons wanted to.
