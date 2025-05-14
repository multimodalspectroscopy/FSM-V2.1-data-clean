# Data Cleaning and Preprocessing Module

This Python module provides reusable functions for cleaning and preprocessing LED signal data. It includes dark signal subtraction, filtering (high-pass, low-pass, band-pass, median), and visual comparisons using Plotly and Dash.

---

## 📁 File Structure

```

your-repo/
├── data\_cleaning/
│   ├── **init**.py
│   └── data\_cleaning.py
└── README.md

````

---

## 🚀 Features

- 📉 **Dark Subtraction** – Removes background signal from LED data.
- 🎚️ **Filtering Options** – Apply high-pass, low-pass, band-pass, and median filtering.
- 📊 **Visual Comparisons** – View original vs. cleaned data in interactive plots.
- 🧩 **Modular Design** – Each preprocessing step is a separate function.

---

## 📦 Installation

Install required packages:

```bash
pip install pandas numpy scipy plotly dash
````

---

## 🧪 Usage

```python
from data_cleaning import preprocess_and_plot

preprocessing_config = {
    "subtract_dark": True,
    "dark_mapping": {
        "LED_A_808_DET1": "LED_A_DARK_DET1",
        "LED_A_848_DET1": "LED_A_DARK_DET1"
        # Add your full mapping here
    },
    "highpass": {
        "cutoff": 0.1,
        "order": 3,
        "sr": 1000
    },
    "lowpass": {
        "cutoff": 5.0,
        "order": 2,
        "sr": 1000
    },
    "bandpass": {
        "lowcut": 0.5,
        "highcut": 4.0,
        "order": 2,
        "sr": 1000
    },
    "median": {
        "window_size": 5
    },
    "grouped_columns": {
        "Group A Detector 1": ["LED_A_808_DET1", "LED_A_848_DET1"],
        "Group B Detector 2": ["LED_B_808_DET2", "LED_B_848_DET2"]
    }
}

group_flags = {
    "Group A Detector 1": True,
    "Group B Detector 2": False
}

plots = preprocess_and_plot("data/sample_data.xlsx", preprocessing_config, group_flags)

# `plots` is a list of Dash HTML divs containing interactive figures
```

---

## 📄 License

MIT License. You are free to use, modify, and distribute this module.
