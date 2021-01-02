# Amazon Web Scraper
This is a simple python web scraper for Amazon for checking prices of items.

## How to run
Once requirements have been installed, you will need to download the chromedriver for your version of chrome.

* Download the chromedriver [here](https://chromedriver.chromium.org/downloads) and unzip.
* Create an environment variable called CHROMEDRIVER and set it to the absolute path of the chromedriver binary.

Mac/Linux

```console
export CHROMEDRIVER='path/to/chromedriver'
```

Windows

```console
set CHROMEDRIVER='path/to/chromedriver'
```

* Run the program.

```python
python3 scraper.py
```

## Requirements
All requirements can be found in the requirements.txt file.