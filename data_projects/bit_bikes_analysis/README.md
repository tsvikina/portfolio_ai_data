# Bit Bikes: Bikesharing Inventory Analysis

## Project Overview

This project analyzes bikesharing trip data for the month of July across three years (2020, 2021, and 2022) using the Divvy Bike system in Chicago. The goal is to forecast the bike inventory needed for July 2023 based on past trends.This project was originally developed as part of an assignment at **Bit Academy** and has been expanded and polished for inclusion in my professional portfolio.


The analysis includes:
- Time series comparison of ride counts per day
- Trend analysis and visualizations
- Recommendations for optimal bike inventory planning

## Dataset

Data is sourced from the official [Divvy Bikes System Data](https://divvybikes.com/system-data) and consists of:
- `202007-divvy-tripdata.csv`
- `202107-divvy-tripdata.csv`
- `202207-divvy-tripdata.csv`

These datasets include ride information such as:
- `started_at`: Timestamp of ride start
- `ended_at`: Timestamp of ride end
- Rider type (member/casual)
- Station locations

Each file contains all rides taken in **July** of the respective year.

## Tools & Technologies

- **Python** (pandas, matplotlib, seaborn)
- **Google Colab** (with Google Drive integration)
- **Jupyter Notebook** for analysis and visualization

## Key Insights

- Ride frequency fluctuates with day-of-week and weather conditions.
- A year-over-year increase in ride volume is observed from 2020 to 2022.
- Peak ridership patterns can guide strategic inventory placement in 2023.

## Business Case

The business goal is to **optimize inventory allocation** by identifying:
- Peak usage times
- Daily ride trends
- Seasonal fluctuations in July

This data-driven approach supports smarter operational planning and customer satisfaction.

## How to Run

1. Open the notebook in Google Colab.
2. Mount your Google Drive.
3. Ensure the required CSV files are placed in the specified directory (e.g., `MyDrive/ColabNotebooks/`).
4. Run all cells to perform the full analysis.
---

