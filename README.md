# 🛒 ReserveBar Product Scraper

A Python-based web scraper to extract product information—such as name, price, and fulfillment details—from ReserveBar.

## 📄 Overview

This script automates the process of collecting product data from ReserveBar. It utilizes Selenium WebDriver to navigate the website and extract relevant details, which are then saved into CSV and Excel files for further analysis.

## 🛠️ Tech Stack

-   **Programming Language:** Python
-   **Automation:** Selenium WebDriver
-   **Data Handling:** pandas
-   **Output Formats:** CSV, Excel

## 📦 Installation

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/Irfan-Ahmad-byte/reservebar_scraping_proj.git](https://github.com/Irfan-Ahmad-byte/reservebar_scraping_proj.git)
    cd reservebar_scraping_proj
    ```

2.  **Install Dependencies**

    ```bash
    pip install -r req.txt
    ```

3.  **Download WebDriver**

    Ensure you have the appropriate WebDriver (e.g., ChromeDriver) installed and added to your system's PATH.

## 🚀 Usage

1.  **Run the main scraping script:**

    ```bash
    python reservebank.py
    ```

    The extracted data will be saved as:

    -   `reservebank_products.csv`
    -   `reservebank_products.xlsx`
    -   `reservebank_products_links.csv`

## 📌 Notes

-   The script is configured to scrape product names, prices, and fulfillment information.
-   Ensure compliance with ReserveBar's terms of service when using this scraper.

## 👨‍💻 Author

Developed by [Irfan Ahmad](!https://github.com/irfan-ahmad-byte)