# Python Weather Tracker

A Python project for retrieving and tracking weather information for a
chosen location. It provides a practical way to practise working with
external weather data, handling API responses, and presenting useful
weather details from Python.

## Features

* **Location-based weather lookup** for a city or supported location.
* **Weather data retrieval** from the configured weather service.
* **Readable output** for the returned weather information.
* **Repeatable checks** by running the script again for updated
conditions.



## Tech Stack

* Python
* HTTP requests to a weather data service
* JSON response handling

## Requirements

* Python 3.9 or later recommended
* Internet connection
* An API key if required by the weather provider used by the code

## Setup

### 1\. Clone the repository

``` bash
git clone https://github.com/Ani-4a4/Python-Weather-Tracker-.git
cd Python-Weather-Tracker-
```

### 2\. Create and activate a virtual environment 

**Windows (PowerShell):**

``` powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

## Usage

Run the project's main Python script from the repository root. 

``` bash
python main.py
```

If the entry-point file has a different name, run that file instead.
Follow any prompts or configuration instructions printed by the program.

## How It Works

1. The program receives or defines a location to check.
2. It requests weather information from the configured data source.
3. It parses the returned response.
4. It displays or records the relevant weather details.

## Notes and Limitations

* Weather data availability and freshness depend on the selected
provider.
* Some providers require an API key and may impose request limits.
* Invalid locations, network errors, or API limits may prevent a
lookup.
* Keep credentials private and check the weather provider's terms of
use.

## Possible Improvements

* Add a multi-day forecast and historical tracking.
* Save readings to CSV or a database.
* Add configurable units and favourite locations.
* Add charts to show changes in temperature or other measurements over
time.

