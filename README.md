---
title: Hormuz Transit Summary
description: "An interactive Streamlit app that fetches and summarizes the Strait of Hormuz transit data over the last 4 weeks."
date: "2026-05-05"
published: true
---

A Python-based tool that tracks and summarizes maritime traffic through the Strait of Hormuz. It utilizes the UN Global Platform's Daily Chokepoints API to provide actionable insights into weekly vessel movements.

### 🚀 Interactive App

> **Note for GitHub viewers:** The interactive iframe below may not render on GitHub. You can access the live app directly here: [Strait of Hormuz Transit Tracker](https://hormoz-strait-transit-tracker-mgveuu9c3itb5fwylswter.streamlit.app/)

<iframe
  src="https://hormoz-strait-transit-tracker-mgveuu9c3itb5fwylswter.streamlit.app/?embed=true"
  width="100%"
  height="600"
  style={{
    border: "none",
    borderRadius: "8px",
    backgroundColor: "transparent",
  }}
></iframe>

### 🚀 Features

- **Automated Data Fetching**: Connects to the ArcGIS FeatureServer to retrieve real-time maritime chokepoint data.
- **Weekly Aggregation**: Automatically groups daily transit counts into ISO weeks for trend analysis.
- **4-Week Summary**: Provides a detailed breakdown of the last 4 weeks, including daily logs and total weekly vessel counts.
- **Data Cleaning**: Handles timestamp conversions and missing data filtering using `pandas`.

### 🛠 Tech Stack

- **Language**: Python 3.x
- **Libraries**:
  - `requests`: For API communication.
  - `pandas`: For data manipulation and time-series grouping.

### 📊 Sample Output

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

### � Source Code

> **Note:** You can also view the full source code directly on GitHub.

<iframe
  src="https://emgithub.com/iframe.html?target=https://github.com/joshuajonghankim/hormoz-strait-transit-tracker/blob/main/hormuz.py&style=github-dark&type=code&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"
  width="100%"
  height="600"
  style={{ border: "none", borderRadius: "8px" }}
></iframe>
