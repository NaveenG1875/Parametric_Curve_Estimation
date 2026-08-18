Parametric Curve Estimation

Research and Development / AI Assignment


Problem Statement

The objective of this assignment is to find the unknown values of theta, M and X in the given parametric equation of a curve.

The given equations are:

$$
x = t * \cos(\theta) - e^{M|t|} * \sin(0.3t) * \sin(\theta) + X
$$

$$
y = 42 + t * \sin(\theta) + e^{M|t|} * \sin(0.3t) * \cos(\theta)
$$

The unknown variables are:

theta

M

X

The given ranges are:

$$
0^\circ < \theta < 50^\circ
$$

$$
-0.05 < M < 0.05
$$

$$
0 < X < 100
$$

$$
6 < t < 60
$$


Dataset

The given data is provided in the file flam.csv.

It contains x and y coordinates of points belonging to the curve.

I used these points as the reference data and tried to find the values of theta, M and X that produce a curve which is as close as possible to these points.


My Approach

I solved the problem using Python.

First, I loaded the flam.csv file using Pandas and extracted the x and y values from it.

Then I generated equally spaced values of t between 6 and 60 using NumPy.

After that, I implemented the given parametric equations in a Python function.

Since NumPy uses radians for sin() and cos(), I converted theta from degrees to radians using np.radians().


Finding the Unknown Values

There are three unknown values in the equation:

theta

M

X

Instead of manually trying different combinations of these values, I used Differential Evolution from SciPy.

I gave the optimizer the allowed ranges from the assignment:

theta: 0 to 50 degrees

M: -0.05 to 0.05

X: 0 to 100

The optimizer tries different combinations of these values and checks how close the generated curve is to the given data.

The combination that gives the smallest error is selected as the result.


How I Compared the Curves

The points in flam.csv are not necessarily in the same order as the generated points.

Because of this, I used cKDTree from scipy.spatial.

In simple terms, cKDTree helps me quickly find the closest generated curve point to each point from the CSV file.

For each CSV point, I find its closest predicted point and calculate the L1 distance.

The L1 distance between two points is calculated as:

$$
|x_1 - x_2| + |y_1 - y_2|
$$

I add these distances for all the points.

This total value is the error that Differential Evolution tries to minimize.


Code Explanation

The main parts of my code are:

1. Loading the data

I use Pandas to read flam.csv and store the x and y values.

2. Creating t values

I use np.linspace(6, 60, len(x_data)) to create equally spaced values of t between 6 and 60.

3. Creating the curve

The curve() function takes theta, M and X as inputs and calculates the corresponding x and y values using the given equations.

4. Finding the closest points

I create a cKDTree using the generated curve points.

For every point in the CSV data, I find the index of its nearest generated point.

5. Calculating the error

I calculate:

$$
|x_{data} - x_{nearest}| + |y_{data} - y_{nearest}|
$$

for every point and add all the values together.

6. Optimization

The objective() function returns this total error.

Differential Evolution repeatedly calls this function with different values of theta, M and X and searches for the combination that gives the minimum error.

7. Plotting

Finally, I plot the original CSV points and the predicted curve together to visually check how closely they match.


Optimization Result

The optimization produced the following values:

theta = 29.99944510759932 degrees

M = 0.030001202111302153

X = 54.99851837083823

L1 Error = 20.037238358935262


Final Values

The optimized values are very close to simple values:

theta = 30 degrees

M = 0.03

X = 55


Final Fitted Equation

After substituting the final values into the original equations, the fitted curve becomes:

$$
x = t * \cos(30^\circ) - e^{0.03|t|} * \sin(0.3t) * \sin(30^\circ) + 55
$$

$$
y = 42 + t * \sin(30^\circ) + e^{0.03|t|} * \sin(0.3t) * \cos(30^\circ)
$$


Verification

I plotted the given points from flam.csv together with the curve generated using the optimized values.

The two curves overlap very closely in the plot.

This shows that the values found by the optimization give a very good fit to the given data.


Python Libraries Used

NumPy

Used for numerical calculations, generating t values, and calculating sin, cos and other mathematical operations.

Pandas

Used to read the flam.csv file and extract the data.

SciPy

Used for Differential Evolution optimization and cKDTree for finding the nearest curve points.

Matplotlib

Used to plot the given data and the predicted curve.


Files in the Repository

Solution.py

Contains the Python code used to estimate theta, M and X.

flam.csv

Contains the given x and y data points.

README.md

Contains the explanation of the problem, method, results and final equations.


How to Run

Install the required libraries:

pip install numpy pandas scipy matplotlib

Keep Solution.py and flam.csv in the same folder.

Run the program using:

python Solution.py

The program prints the estimated values of theta, M and X, the L1 error, and displays the comparison graph.


Final Answer

theta = 30 degrees

M = 0.03

X = 55
