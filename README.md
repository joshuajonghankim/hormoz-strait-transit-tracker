# Strait of Hormuz Transit Tracker

https://hormoz-strait-transit-tracker-mgveuu9c3itb5fwylswter.streamlit.app/

A Python-based data analysis tool that tracks and summarizes maritime traffic through the Strait of Hormuz. It utilizes the UN Global Platform's Daily Chokepoints API to provide actionable insights into weekly vessel movements.

## 🚀 Features

- **Automated Data Fetching**: Connects to the ArcGIS FeatureServer to retrieve real-time maritime chokepoint data.
- **Weekly Aggregation**: Automatically groups daily transit counts into ISO weeks for trend analysis.
- **4-Week Summary**: Provides a detailed breakdown of the last 4 weeks, including daily logs and total weekly vessel counts.
- **Data Cleaning**: Handles timestamp conversions and missing data filtering using `pandas`.

## 🛠 Tech Stack

- **Language**: Python 3.x
- **Libraries**:
  - `requests`: For API communication.
  - `pandas`: For data manipulation and time-series grouping.

## 📊 Sample Output

```text
=============================================
📊 Strait of Hormuz: Last 4 Weeks Summary
=============================================

[Week: 2024-W15] (2024-04-08 ~ 2024-04-14)
---------------------------------------------
      date  n_total
2024-04-14       82
2024-04-13       75
...
---------------------------------------------
✅ Weekly Total: 540 vessels
```
