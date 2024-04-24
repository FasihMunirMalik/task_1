import matplotlib.pyplot as plt
from functions import angle_between_hands

def find_minima():
    angles = []
    for hour in range(12):
        for minute in range(60):
            angle = angle_between_hands(hour, minute)
            angles.append((hour, minute, angle))

    minima = []
    for i in range(720):
        if (angles[i][2] < angles[(i-1) % 720][2]) and (angles[i][2] < angles[(i+1) % 720][2]):
            minima.append(angles[i])

    return minima, angles

# Find all minima
minima, angles = find_minima()

# Display the number of minima
print("Number of minima:", len(minima))

# Display the range of input values
print("Range of input values: Hour: [0, 11], Minute: [0, 59]")

# Display the range of output values (angles)
print("Range of output values (angles): [0, 180] degrees")

# Display all solutions
print("All minima:")
for minimum in minima:
    print("Hour:", minimum[0], ", Minute:", minimum[1], ", Angle:", minimum[2], "degrees")


# for visual observation of function behavious (angles difference across time).
# Extract angles values for plotting
angles_values = [angle for _, _, angle in angles]

# Plot angle across time
plt.plot(range(720), angles_values)
plt.xlabel('Time (minutes)')
plt.ylabel('Angle (degrees)')
plt.title('Angle between hands of a clock across time')
plt.grid(True)

# Save the plot as a PDF figure
plt.savefig('angle_vs_time.pdf')

# Display the plot
plt.show()
