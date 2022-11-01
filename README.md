# FetchRewards
Application for pixel plotting:

Requirements:
Docker

How to run:
(go into docker file directory) 
docker build -t fetchrewards . (make sure to add the period)
docker run -it --rm --network host --name FetchRewards-Running FetchRewards

Then open input.html in your browser

Input should be formatted as 

Corners: [(X1, Y1), (X2, Y2), (X3, Y3), (X4, Y4)]
Dimensions: (H, W)
