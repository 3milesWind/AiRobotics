<img src="README.assets/Images.jpg" align="right" width="300" alt="header pic" />

# Artificial Intelligence Algorithms

Code for Ai algorithm 

# Re-design the Repo to the link: https://github.com/3milesWind/Seach_and_Optimization

# Table of Contentsdesign

* [What is this?](#What-is-this)
* [Documentation](#Documentation)
* [matplotlib](#matplotlib)
  * [Animation](###Animation)
  * [Text the points](###Text-the-points )
* [Numerical Optimization](#Numerical-Optimization)
  * [Gradient Descent](###Gradient-Descent)
  * [Newton Method](###Newton-Method)
* [Stochastic Search](#Stochastic-Search)
  * [Simulated Annealing](###Simulated-Annealing)
* [Classic Search](#Classic-Search)
  * 



# What is this?

> This is a Python code collection of Artificial Intelligence Algorithms
>
> During Master degree, Try to collect all the Intelligence algrithms I learn
>
> CheckList:
>
> > - [ ]  Stochastic Search
> > - [x]   Numerical Optimization
> > - [x]  Classical Search

# Documentation
1. Clone this repo.

> git clone https://github.com/3milesWind/AiRobotics.git

2. Install the required libraries.

using conda :

> conda env create -f environment.yml


3. Execute python script in each directory.

4. Add star to this repo if you like it :smiley:.

# matplotlib

> Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python

### Animation

Code: [SimpleAnimation1.py](matplotlib/SimpleAnimation1.py)

<img src="README.assets/Mathplotlib_animitation.gif" alt="Mathplotlib_animitation" width="400" height="300" style="float: left;" />

### Text the points 

###  [code](matplotlib/SimpleMakeTextEachPoint.py)

<img src="README.assets/Screen Shot 2021-11-09 at 1.23.43 AM.png"  width="400" height="300" style="float: left;" />

# Numerical Optimization

> *Numerical Optimization* presents a comprehensive and up-to-date description of the most effective methods in continuous optimization.

### Gradient Descent 

###  [Background](Docs/GradientDescent.md)

> Gradient descent is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function. 

Example Function: <img src="https://render.githubusercontent.com/render/math?math=x_1^2 %2B x_1 * x_2 %2B 3x_2^2 %2B 5">

* With a fixed learning rate    [Code](NumericalOptimization/gradientDescentWithFixedRate.py)

  <img src="README.assets/GradientDecWithFixedRate.gif" alt="GradientDecWithFixedRate" width="400" height="300" style="float: left;" />

* With a Optimal learning rate [Code](NumericalOptimization/gradientDescentWithOptimalRate.py)

  <img src="README.assets/gradient_Decent_Optiomal.gif" alt="gradient_Decent_Optiomal" width="400" height="300" style="float: left;"/>

### Newton Method

Example Function: <img src="https://render.githubusercontent.com/render/math?math=x_1^2 %2B x_1 * x_2 %2B 3x_2^2 %2B 5">

[Code](NumericalOptimization/NewtonMethod.py)

> Newton's method is a powerful technique—in general the [convergence](https://en.wikipedia.org/wiki/Rate_of_convergence) is quadratic: as the method converges on the root, the difference between the root 

<img src="README.assets/newtwonMethod.gif" alt="newtwonMethod" width="400" height="300" style="float: left;" />

* some difficulties: 
  * Can not be singular matrix
  * Derivattive can not be zeros

# Stochastic Search 

## Simulated-Annealing 

**The Travelling Salesman Problem ** [code](TravellingSalesman/Simulated_Annealing.py)   [Simple Presentation](TravellingSalesman/Presentation1.pptx) 

> Simulated annealing algorithm is a random algorithm, it has a certain probability to find the global optimal solution

<img src="README.assets/Simuted_annlea.gif" alt="Simuted_annlea" width="300" height="300" style="float: left;"  /><img src="README.assets/Probability.jpg" alt="Probability" width="350" height="300" style="float: left;" />













# Classic-Search



### Depth-First Search (DFS) 

> The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.         

<img src="README.assets/ezgif.com-gif-maker.gif" alt="ezgif.com-gif-maker" width="400" height="470" style="float: left;" />

### Breadth-first search (BFS)

> It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. Extra memory, usually a queue is needed to keep track of the child nodes that were encountered but not yet explored.

<img src="README.assets/ezgif.com-gif-maker (2)-7201204.gif" alt="ezgif.com-gif-maker (2)" width="400" height="470" style="float: left;" />

### Dijkstra 

> For a given source node in the graph, the algorithm finds the shortest path between that node and every other with cost

<img src="README.assets/ezgif.com-gif-maker (3).gif" alt="ezgif.com-gif-maker (3)" width="400" height="470" style="float: left;" />

### A*

> A* is an informed search algorithm, **or a best-first search**, meaning that it is formulated in terms of weighted graphs: starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost

<img src="README.assets/ezgif.com-gif-maker (4).gif" alt="ezgif.com-gif-maker (4)" width="400" height="470" style="float: left;" />
