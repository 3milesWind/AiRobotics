<img src="README.assets/Images.jpg" align="right" width="300" alt="header pic" />

# Artificial Intelligence Algorithms

Code for Ai algorithm 

# Table of Contents

* [What is this?](#What-is-this)
* [Documentation](#Documentation)
* [matplotlib](#matplotlib)
  * [Animation](###Animation)
  * [Text the points](###Text-the-points )

* [Numerical Optimization](#Numerical-Optimization)
  * [Gradient Descent](###Gradient-Descent)

* [Stochastic Search](#Stochastic-Search)
  * [Simulated Annealing](###Simulated-Annealing)


# What is this?

> This is a Python code collection of Artificial Intelligence Algorithms
>
> During Master degree, Try to collect all the Intelligence algrithms I learn
>
> CheckList:
>
> > - [ ]  Stochastic Search
> > - [ ]   Do Numerical Optimization Background doc
> > - [ ]  Classical Search

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

> Newton's method is a powerful technique—in general the [convergence](https://en.wikipedia.org/wiki/Rate_of_convergence) is quadratic: as the method converges on the root, the difference between the root 

<img src="README.assets/newtwonMethod.gif" alt="newtwonMethod" width="400" height="300" style="float: left;" />

* some difficulties: 
  * Only can work on the Positive definite. 

# Stochastic Search 

## Simulated-Annealing 

**The Travelling Salesman Problem ** [code](TravellingSalesman/Simulated_Annealing.py)   [Simple Presentation](TravellingSalesman/Presentation1.pptx) 

> Simulated annealing algorithm is a random algorithm, it has a certain probability to find the global optimal solution

<img src="README.assets/Simuted_annlea.gif" alt="Simuted_annlea" width="400" height="300" style="float: left;"  />
