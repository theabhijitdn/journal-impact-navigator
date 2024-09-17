# Journal Impact Navigator

An interactive Streamlit application for exploring and filtering scientific journal data based on various metrics including Impact Factor, Quartile, Publisher, Category, Region, and Country.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Source](#data-source)
- [Contributing](#contributing)
- [License](#license)

## Overview

Journal Impact Navigator is a web-based tool designed to help researchers, academics, and publishers explore and analyze scientific journal data. It provides an intuitive interface for filtering journals based on multiple criteria, allowing users to quickly find relevant publications in their field of interest.

## Features

- Dynamic filtering of journal data based on:
  - Impact Factor Range
  - Quartile
  - Publisher
  - Category
  - Region
  - Country
- Real-time updates of filtered results
- Interactive data display using Streamlit
- Efficient data handling with pandas

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
git clone https://github.com/yourusername/journal-impact-navigator.git
cd journal-impact-navigator


2. Install the required dependencies:
pip install -r requirements.txt


## Usage

To run the application:

1. Ensure you're in the project directory.
2. Run the Streamlit app:
streamlit run app.py

3. Open a web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

## Data Source

The application uses a dataset named 'combined_final.csv'. This file should contain information about scientific journals, including columns for Impact Factor (IF), Quartile (Q), Publisher, Category, Region, and Country.

## Contributing

Contributions to improve the Journal Impact Navigator are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push to your fork and submit a pull request.

Please ensure your code adheres to the project's coding standards and include tests for new features when applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""
