from scraper import Scraper


def get_input():
    answer = input("What data do you want to fetch? \n"
                   "Type 'zahajeni', 'preruseni', 'ukonceni', 'obnoveni': ").lower()
    return answer


def valid_input(input):
    if input in ['zahajeni', 'preruseni', 'ukonceni', 'obnoveni']:
        return True


input = get_input()


if valid_input(input):
    my_scraping = Scraper(input)
    my_scraping.initialize_driver()
    my_scraping.scrape_data()
    my_scraping.save_json()
else:
    print(f"Your input {input} is not valid!")
