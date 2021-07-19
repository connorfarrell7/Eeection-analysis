# Election Analysis

## Overview

Tom works for the Colorado Board of Elections. I have been asked to help him do an elections audit for a congressional district. I was asked to create an automated process of finding the total votes, vote percentages, and winning candidate. Tom and Seth (Tom's boss), would also like to know the amount of voters that turned out in each of the three counties being audited, as well as the county which had the largest turnout. Using my python skills, I created a script to find all the desired values very quickly. If successful, this algorithm can be used for many other elections in the future.

### Election Audit Results

Using the algorithm that I made, I was able to determine the following:

- There was a total of 369,711 votes cast across the three counties. (fig 1)

![figure 1](https://user-images.githubusercontent.com/86024575/126096848-ff68ebf4-fb09-4dc6-8c58-6657a61cf416.png)
*figure 1*

- Arapahoe County had the smallest turnout with 24,801 voters, or 6.7% of the total. (fig 2)
- Jefferson County had 38,855 voters, or 10.5% of the total. (fig 2)

![figure 2](https://user-images.githubusercontent.com/86024575/126096911-fde3f82d-248f-4349-9b72-6b8ec7f36e19.png)
*figure 2*

-	Denver County had by far the largest turnout with 306,055 voters, or 82.8% of the total. (fig 3)

![figure 3](https://user-images.githubusercontent.com/86024575/126096953-3d0abbe6-059c-45c8-9714-a23b4ba2dfca.png)
*figure 3*

-	Raymon Anthony Doane had the smallest number of votes, with 11,606, or 3.1% of the total. (fig 4)
-	Charles Casper Stockham had 85,213 votes, or 23% of the total. (fig 4)

![figure 4](https://user-images.githubusercontent.com/86024575/126096971-1073dabc-b3f9-442c-8f6d-381114211444.png)
*figure 4*

-	The Winner of the election, Diana Degette, had a whopping 272,892 votes, giving her 73.8% of the total votes cast. (fig 5)

![figure 5](https://user-images.githubusercontent.com/86024575/126097004-467b6404-cf61-4370-9144-427203ac9187.png)
*figure 5*

#### Election Audit Summary

This script can be used for many different applications, namely for other elections of this magnitude. If this algorithm were going to be used for a presidential election, an additional "for" loop could be added to iterate through each state first, followed by the "for" loop iterating through each county in the respective state. Furthermore, if we wanted to add a vice president candidate, we could add an "if" statement to determine which vice president won based on which president was elected.
