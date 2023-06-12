# Webscraping-SUKL-reports
This is a Python-based web scraping program that gathers information from SUKL about the availability of drugs on the Czech market. 
Drug Availability Web Scraping Script
This Python script is designed to scrape information from the State Institute for Drug Control (SUKL) website to gather data about the availability of drugs on the Czech market.

## Requirements
- Python 3.x
- Selenium library
- Chrome WebDriver

## Usage
1. Install the required dependencies by running the following command:

```
pip install selenium
```
2. Download and configure the Chrome WebDriver for your operating system.

3. Update the CHROME_PATH constant in the script with the path to your Chrome WebDriver executable.

4. Run the script:

```
python main.py
```
5. The script will prompt you to choose one of the available options for scraping data. Enter the corresponding option and press Enter.
Options:
- placing
```
zahajeni
```
- interruption
```
preruseni
```
- cessation
```
ukonceni
```
- resumption
```
obnoveni
```
6. The script will scrape the data from the SUKL website and save it in a JSON file named data.json.

## Notes
- The script uses Selenium library to automate the web scraping process.
- The script runs in headless mode, meaning it does not open a browser window during the scraping process.
- The scraped data is saved in a JSON file for further analysis or integration with a database.

**Disclaimer: This script is provided for educational and informational purposes only. Please ensure that your usage complies with the website's terms of service and applicable laws and regulations.**
