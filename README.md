# Covid Data Dashboard

## Introduction

This project is a Covid Data dashbord that outputs up to date covid data and outputs the latest News Articles, it also can schedule updates and is a fully interactive dashboard.

### Prerequisites

this project can be run in any version of python 3 but the ideal is **Python 3.8.1**

### Installation

pip install pkg-luishidalgogt2003==0.0.1

#### installation required

- **py -m pip install Cov19API**
- **py -m pip install flask**

### How to use the project

Inside the folder src you will find the folder package with all the files needed to run the dashboard for every module and each function in each module.
The Dashboard is divided in three python modules:

- **covid_data_handler.py**
- **covid_news_handling.py**
- **covid_user_interface.py**
  
each of the modules performs a task required to run the dashboard.
In each module there is clear instructions in the function created on how it works and how to run it.

### Data Required

For the project you will need to include details to the **config.json** file so it can be customised with what you want to update or search. All of the values except API key are default and can be used to run the application:

- **Api Key**
- **Location for the covid data**
- **Search Terms for the News Articles**

### Testing

To test the code before running it there will be various test modules inside the file directory **tests**, where there will be three files each including tests for there specific module, such as

- **test_covid_data_handler**
- **test_news_data_handling**
- **test_covid_user_interface**  

### Running

To run the code run **covid_user_interface.py** and search **"http://127.0.0.1:5000/"** in any browser

### File Management

- Covid Data Dashboard
  - dist
  - src
    - package
      - static
        - images
          -mask.png
      - templates
        - index.html
      - init.py
      - covid_data_handler.py
      - covid_news_handling.py
      - covid_user_interface.py
      - test_covid_data_handler.py
      - test_news_data_handling.py
      - test_covid_user_interface.py
  - config.json
  - covid_dashboard.log
  - LICENSE.txt
  - nation_2021-10-28.csv
  - pyproject-toml
  - README.md
  - setup.py

## Details

- Project Created by **Luis Hidalgo Gutierrez De Tovar**,
- Licence in file: **LICENSE.txt**
- source code in dist folder: **pkg-luishidalgogt2003-0.0.1.tar.gz**,

### Acknoledgements

file acknoledgments to Module Leader **Matt Collison** for the template **index.html**
