# Analog Clock Angle Calculator

This project includes Python scripts to calculate the angle between the hour and minute hands of an analog clock for a given time, find the minima of the angle function, and visualize the angle difference across time.

## Files

1. **functions.py**: This file contains the `angle_between_hands` function, which takes a time in hours and minutes (in 24-hour format) as input and calculates the angle between the hour and minute hands of an analog clock.

2. **minima.py**: This file contains the `find_minima` function, which finds the local minima of the angle function across all possible times. It also includes code to visualize the angle difference across time and save the plot as a PDF figure.

3. **test_functions.py**: This file contains test cases to verify the correctness of the `angle_between_hands` function.

## Usage

1. Clone the repository or download the project files to your local machine.

2. Ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/) if you haven't already.

3. Open a terminal or command prompt and navigate to the directory where the project files are located.

4. Install the dependencies, either by manually installing dependencies as noted in the **requirements.txt** file or run the following command

```bash
pip install -r requirements.txt
```
5. To calculate the angle between the hour and minute hands of an analog clock for a given time, run the following command (make sure to replace hours and minuites based of 24 hr time format):
```bash
python functions.py hour minutes
```
example usage
```bash
python functions.py 11 30
```
6. to test the `angle_between_hands` function run the **test_functions.py** file either directly or run the following command in the terminal:
```bash
pytest
```
7. to find all the minima of the function run the **minima.py** file either directly or run the following command in the terminal:
```bash
python minima.py
```
## Observations and considerations
1. The function's input range spans from 0 minutes to infinity, yet, considering the cyclic nature of an analog clock where one cycle repeats every 12 hours, the input range is refined to one cycle, encompassing hours from 0 to 11 and minutes from 0 to 59 within each hour.
2. The function's output range varies from 0 to 180 degrees, reflecting the minimum difference when the hands overlap, such as at 12:00, and the maximum difference when they are on opposite ends of the clock.
3. The function's minimum value occurs when the hour and minute hands overlap, resulting in an angle of zero degrees.
4. The function's minimum value, where the hour and minute hands overlap, occurs approximately every 65.45 minutes.
5. However, due to the discrete nature of our calculations, the exact point where the minimum is reached, i.e., 0 degrees, lies between the 65th and 66th minute in practice.
6. The function exhibits a total of 11 minima within a 12-hour cycle, where the hour and minute hands overlap, all occourences are printed when the **minima.py** file is run .
6. Both from the graph depicting the difference of angle versus time and through mathematical calculations, it is evident that the function behaves as a piecewise linear function.
7. The minimum is found at the endpoint of a linear segment, as illustrated in the graph.
8. For a closed-loop solution, to find an extremum, the partial derivatives of the function with respect to each of the two inputs must be equal to 0.
9. However, in this case, the minimum exists at a point where the partial derivatives on the right and left sides are not equal due to being on the edge of a linear segment.
10. Hence, it can be concluded that finding a closed-loop solution for this function is not straightforward.