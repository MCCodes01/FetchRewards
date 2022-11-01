# FetchRewards
Application for pixel plotting:

Requirements:
Docker

Step 1: 
Make sure Docker is installed

Step 2:
How to run:
(open a terminal and cd into the filepath of the Docker Directory)

Next:
In the Command line Run the following command:
docker build -t fetchrewards . (make sure to add the period and that it is all lowercase)

Step 3:
In the Command line Run the following command:
docker run -it --rm --network host --name fetchrewards-Running fetchrewards

Step4:
Enter the local webaddress and drag "input.html" file into the webpage

Step 5:
You should now have two input boxes displayed "Corners" and "Dimensions"

Step 6:
Enter the input for Corners and Dimensions in the following formatting
Corners: [(X1, Y1), (X2, Y2), (X3, Y3), (X4, Y4)] (must be an array of touples)
Dimensions: (H, W) (touple)

Note: 
The input must be taken as a touple inputting x,y will not work

EX Input:
Corners: [(1,1}, (1,3),(3,1),(3,3)]
Dimensions: (3,3)

Output: [(1,1), (2,1), (3,1), (1,2), (2,2), (3,2), (1,3), (2,3), (3,3)]

Note: 
The input for the Dimensions MUST be an integer, otherwise you will recieve an "internal server error". However the Corners can be a floating point

Note: reccomended to run through a Linux enviroment for optimal success
