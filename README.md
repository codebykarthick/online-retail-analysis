# Retail Analytics: Inventory Optimisation & Pricing Strategy

This project analyzes the **Online Retail II UCI Dataset** (2009-2011 transactional data) to address two core business objectives: **Inventory Optimisation** via ABC Analysis, and **Pricing Strategy** via Price Elasticity Modeling.

The entire analysis is executed in the `Report.ipynb` Jupyter Notebook.

## Project Setup & Installation

Follow these steps to set up the environment and run the analysis.

### 1\. Prerequisites

You must have Python 3.8+ installed.

### 2\. Install Dependencies

Open your terminal or command prompt in the project directory and run:

```bash
# Recommended: Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate

# Install the required libraries
pip install -r requirements.txt
```

### 3\. Data Acquisition

The notebook is set up to download the data automatically, but if manual download is preferred:

  * **Source:** UCI Machine Learning Repository: [Online Retail II Data Set](https://www.google.com/search?q=https://archive.ics.uci.edu/dataset/501/online%2Bretail%2Bii)
  * **Action:** Download the `.xlsx` file and place it in `data/` directory.

### 4\. Run the Analysis

Launch the Jupyter Notebook environment:

```bash
jupyter notebook Report.ipynb
```

Open the notebook and run all cells sequentially to reproduce the analysis and conclusions.

-----

Executing this analysis from raw data ingestion to final recommendations within an afternoon underscored the efficiency of a **robust, reproducible data pipeline**. The project confirmed the power of leveraging core Python libraries like pandas and scikit-learn to quickly yield critical insights for both **supply chain optimisation** and **revenue strategy** in a large-scale retail environment.