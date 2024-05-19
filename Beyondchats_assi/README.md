
# Citation Fetcher

This Python program fetches citations from a specified API endpoint, identifies matching citations based on similarity ratios, and outputs the relevant sources and links.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)
- Pandas library (`pip install pandas`)

## Setup

1. Clone this repository to your local machine:

```
git clone: https://github.com/DavidChance27/Gen_ai_citation_fetcher/tree/main
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Open the `config.py` file and set the following constants:

- `THRESHOLD`: The similarity threshold for considering citations as a match.
- `WEB_PAGES`: The number of pages to fetch data from the API.

## Usage

Run the program by executing the following command in your terminal:

```
python citation_fetcher.py
```

The program will fetch citations from the specified API, identify matching citations, and output the relevant sources and links.

## Code Structure

- `citation_fetcher.py`: Main Python script containing the citation fetching and matching logic.
- `config.py`: Configuration file containing constants such as threshold and number of web pages.
- `requirements.txt`: List of required Python packages.

## How it Works

1. The program fetches data from the specified API endpoint using the `fetch_api` function.
2. It then iterates over the fetched data, identifying matching citations using the `check_similarity` function.
3. Matching citations are stored in the `citations` list.
4. The program outputs the final list of citations.

## Credits

This program was developed by David Chance.
