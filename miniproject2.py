import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calc_mean_erp(trial_points_file, ecog_data_file):
    # Load and process the trial points data
    column_names = ["start", "peak", "finger"]  # Define column names
    trial_points = pd.read_csv(trial_points_file, header=None, names=column_names)  # Load without header, add names

    try:
        trial_points = trial_points.astype(int)  # Convert to integers
    except ValueError as e:
        raise ValueError("The trial_points file contains non-integer values. Please check the data.") from e

    # Load the ECOG data
    ecog_data = pd.read_csv(ecog_data_file, header=None).squeeze("columns")

    # Initialize output matrix
    fingers_erp_mean = np.zeros((5, 1201))

    # Process each finger
    for finger_id in range(1, 6):
        # Get indices for the current finger
        finger_trials = trial_points[trial_points["finger"] == finger_id]

        # Initialize storage for the current finger's ERP data
        finger_data = []

        for _, row in finger_trials.iterrows():
            start_idx = row["start"]
            # Extract 1201 data points: 200ms before, 1ms around, 1000ms after
            block = ecog_data.iloc[start_idx - 200: start_idx + 1001]
            if len(block) == 1201:
                finger_data.append(block.values)

        # Compute the mean ERP for this finger
        if finger_data:
            fingers_erp_mean[finger_id - 1, :] = np.mean(finger_data, axis=0)

    # Plot the ERPs for each finger
    time = np.linspace(-200, 1000, 1201)  # Time in ms
    plt.figure(figsize=(10, 6))
    for finger_id in range(1, 6):
        plt.plot(time, fingers_erp_mean[finger_id - 1, :], label=f"Finger {finger_id}")
    plt.title("Mean ERP for Each Finger")
    plt.xlabel("Time (ms)")
    plt.ylabel("Brain Response (ECOG Signal)")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(fingers_erp_mean)
    return fingers_erp_mean

# Main 
trial_points = r"mini_project_2_data\events_file_ordered.csv"
ecog_data_file = r"mini_project_2_data\brain_data_channel_one.csv"
fingers_erp_mean = calc_mean_erp(trial_points, ecog_data_file)