# Mean ERP Calculation

This repository contains a Python script to compute the mean Event-Related Potential (ERP) from brain signals recorded using ECOG electrodes. The calculation links brain data with finger movement events and provides insights into brain responses.

## Overview
The `calc_mean_erp` function processes two input files:
1. **Trial Points File:** Contains the starting point, peak point, and finger number for each movement.
2. **ECOG Data File:** Contains time-series brain signal data recorded using an ECOG electrode.

### Key Features
- Defines ERP for each finger movement as 200ms before, 1ms during, and 1000ms after the movement.
- Computes a 5x1201 matrix where:
  - Each row represents the average ERP for one finger.
  - Each column represents a time point relative to the movement.
- Plots the averaged brain responses for all five fingers.

## Input Data Format
### Trial Points File (`trial_points.csv`)
A CSV file with three columns:
- **start:** Starting point of each movement.
- **peak:** Peak of each movement.
- **finger:** Finger number (1-5).

### ECOG Data File (`ecog_data.csv`)
A CSV file with a single column containing the ECOG signal time series.

## Function Usage
### Syntax
```python
calc_mean_erp(trial_points_file, ecog_data_file)
```
### Parameters
- `trial_points_file`: Path to the trial points CSV file.
- `ecog_data_file`: Path to the ECOG data CSV file.

### Returns
A NumPy array of shape (5, 1201) containing the mean ERP for each finger.

### Example
```python
# Example usage
fingers_erp_mean = calc_mean_erp('trial_points.csv', 'ecog_data.csv')
print(fingers_erp_mean)
```

### Plot Output
The function generates a plot showing the averaged brain response for each finger over time.

## Error Handling
- If the `trial_points.csv` file contains non-integer values, the function raises a `ValueError` with a descriptive message.
- Ensures all indices used to extract ECOG data are within range of the time series.

## Dependencies
- Python 3.7+
- NumPy
- Pandas
- Matplotlib

Install required libraries with:
```bash
pip install numpy pandas matplotlib
```

## File Structure
```
├── calc_mean_erp.py      # Main script containing the function
├── trial_points.csv      # Example trial points file (not provided)
├── ecog_data.csv         # Example ECOG data file (not provided)
└── README.md             # This file
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or contributions, please contact [your email or GitHub profile].

