<p align="center">

  <h3 align="center">PolyU ENG1003 AAE Freshman Project Group4</h3>



*Project Objectives:  During this project, students will get not only the valuable practical experience to use computer programming language to design and develop a path planning algorithm for an aircraft operation from scratch but also practical skills of using online collaborating programming platform to work with group members remotely.*

  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Blackground of Path Planning to Aviation Engineering ">Blackground of Path Planning to Aviation Engineering</a>
    </li>
    <li>
      <a href="#Theory of Path Planning Algorithm">Theory of Path Planning Algorithm</a>
    </li>
    <li>
      <a href="#Engineering Tools">Engineering Tools</a>
    </li>
    <li>
      <a href="#Project Goals">Project Goals</a>
    </li>
    <li>
      <a href="#Assignments">Assignments</a>
    </li>
    <li>
      <a href="#Relective Essays">Reflective Essays</a>
    </li>

  </ol>
</details>



<!--Blackground of Path Planning to Aviation Engineering-->
## 01|Blackground of Path Planning to Aviation Engineering
• Path planning (also known as the navigation problem) 
is computational problem to find a sequence of valid configurations 
that moves the object from the source to destination. The term is 
used in aviation, robotics and computer games.

• Private pilots do the path plan before the flight to make sure the navigation aid is available

<img width="790" alt="截屏2021-11-05 12 49 14" src="https://user-images.githubusercontent.com/90884944/140459860-e3de43a0-7a0f-45fd-8a4f-59c5af521601.png">

• For ATC near airports, collaborative path planning is required to make the best use of the crowded airspace

<img width="724" alt="截屏2021-11-05 12 58 35" src="https://user-images.githubusercontent.com/90884944/140460592-c1d3e592-5816-4561-a492-47d51f44c96e.png">

•Commercial pilot follow the path that plan based on different cost index designed by airlines.

<img width="811" alt="截屏2021-11-06 00 09 39" src="https://user-images.githubusercontent.com/90884944/140542278-bfa3454e-8683-4843-ad05-f9e6f6fbb08a.png">







<!-- Theory of Path Planning Algorithm -->
## 02|Theory of Path Planning Algorithm

 

<!-- Programming Tools -->
## 03|Programming Tools

• python

<img width="986" alt="截屏2021-11-08 10 13 51" src="https://user-images.githubusercontent.com/90884889/140674101-c37560ac-9d47-44a4-aa51-354868ae2486.png">


• Github

<img width="986" alt="截屏2021-11-08 10 14 46" src="https://user-images.githubusercontent.com/90884889/140674156-b5e38f67-be97-4173-93f1-86b169baad37.png">


•VS Code

<img width="986" alt="截屏2021-11-08 10 16 05" src="https://user-images.githubusercontent.com/90884889/140674236-f5f072cb-e544-4f17-b4c2-b69532c039be.png">




<!-- Project Goals -->
## 04|Project Goals

• Goal of this project, to select the best aircraft models with an 
optimized route that minimized the cost of the aircraft operation 
under given scenario.

• Design the cost of the aircraft operation

• Design an aircraft model (virtually) with different cost coefficients 
to fly safe and cheapest. 

• Design the path planning algorithm considering 3D, 2D + time, 
scenarios.


<!-- Assignments -->
## 05|Assignments
**Task1:**
In this task, it is needed to find the PolyU aircraft models that achieve the minimum cost for the challenge assigned to your group.

**a.Methodology**
  
  First of all,we obtained the source code from the lecturer.After receiving te code, we follow the image of the task 1 to change the bourdaries of the map.Also, we have changed the time-consuming area and the fuel-consuming area by inputing the cordination and we input the formulae into the code which can let the code to help us to calculate the minimun cost.
  Then, we only need to input the data of different aircraft models and it will run the program.At the same time, it will help us to calculate the minimun cost by using the two given formulae.

  
**b.Results** 

The results of the minimun cost of different aircraft models:

![图像2021-11-6 13 20](https://user-images.githubusercontent.com/90884944/140782485-7e380935-d8ca-4596-a74f-11f4bd7ddca0.jpg)



The path plan is as shown below:

![IMG_2209](https://user-images.githubusercontent.com/90884944/140782513-9060e38b-057d-4d11-b995-964d509e4115.GIF)


**c.Discussion**


The result above shows that the aircrft model of PolyU-A380 has the lowest cost in our path plan.After studying the formulae and the result,we have found that if the trip fuel or the time related cost per minute of flight increase,the total cost also increase.The trip fuel or the time related cost per minute of flight are positive proportional to the total cost.


**Task2:**

**Task2.1**


**a.Methodology**

<img width="381" alt="截屏2021-11-09 00 46 44" src="https://user-images.githubusercontent.com/90884944/140783651-65c96f9a-bd7c-4622-a752-2e00a3bf1812.png">




<img width="381" alt="截屏2021-11-09 00 51 43" src="https://user-images.githubusercontent.com/90884944/140784093-c9563d2a-2cfc-4c96-aad4-2cc65ba9872e.png">


**c.Discussion**

We find that to minimize the cost of paths for Cf and CT would have to be 20 each. This shows that if we changed two variables, the difference of cost can be significant. However, in reality, it is much more complicated. There will not be only two unknowns. There will be more formulas that affect each other. There will not be nice integer for the most efficient setup.


**Task2.2**

**a.Methodology**

<img width="391" alt="截屏2021-11-09 00 55 25" src="https://user-images.githubusercontent.com/90884944/140785032-b221394f-0c74-417f-90c2-2dd5ea0d9b9f.png">

By the Excel’s solver, we get:

<img width="356" alt="截屏2021-11-09 00 59 05" src="https://user-images.githubusercontent.com/90884944/140785241-02a5cb3e-d674-4300-af1c-0dc90103ea8a.png">


**c.Discussion**

Even though we use the Excel find the lowest possible setup we can find, we are not sure about our answer. Since this setup or those formulas are for all 10 groups. In other words, we did not customize our setup for our route. Every route has its own setup, and it is not the same to others. We expect there will be more efficient setup than we have now. However, we tried and cannot be found. We are still struggling. We did not where is the problem. Therefore, we still stick our answer.

No matter what the answer is. This task is much closer to the reality. It is much complicated and vague. The actual answer is harder to be find. Also, we can see the importance of calculator and programming. As we use manual calculation, we would waste lots of time and may found incorrect answer. Computer can finish the work instinctly.



**Task3:**


**a.Methodology**

<img width="308" alt="截屏2021-11-09 01 02 26" src="https://user-images.githubusercontent.com/90884944/140785866-04c8100f-95fc-42f5-8687-7b58cb866f1e.png">
<img width="305" alt="截屏2021-11-09 01 02 47" src="https://user-images.githubusercontent.com/90884944/140785915-71073b85-6cfb-4a2e-8dad-5d5254326d3a.png">


**b.Results**

Comparing to Task 1 of A380, it is reduced from 2373.092 to 1922.014. It is 19% cheaper.



**c.Discussion**

From the results, we can see that why airlines tries to find the lowest cost route. As adding one factor, the cost reduces almost 20%. However, in real life situation, there is so much more factors to be considers. For instance, weather, air traffic and altitude. Just to name a few. Finding the lowest or the most efficient cost setup for an airplane is much complicated. At least, it is not simple as task 3. Works are much work to be done in real life. 


<!-- Reflective Essays -->
## 06|Reflective Essays


**AAE Chan Ho Man (21079126D)**


**AAE Chan Ching Long (21110937D)**


**AAE Yang Zi Xi (21107424D)**


**AAE Li Zhehang (21106296D)**

In this ENG course, I gained a lot. First of all, I learned about the basic application of Github and Python, the practical application of digital technology in the field of aviation engineering, and understood the importance of cross-field cooperation in the digital era. Detailed said, python is an easy to learn, simple programming language, grammar is very suitable for non-professional, learn from the programming and application to his specialty, so as to realize interdisciplinary cooperation and making is a very convenient team site, share and edit code make team work more simple and effective, It saves a lot of manpower and material costs. Combining the two, it can help the informatization development in the field of aviation engineering. Secondly, ENG is a team cooperation course. In the last two months, THIS course made me deeply realize the importance of team cooperation. The biggest advantage of team cooperation is that we can divide the work and cooperate, so as to give full play to the advantages of everyone, thus improving the efficiency and quality of the task.


**AAE Kwok Yan Yiu (21084939D)**





