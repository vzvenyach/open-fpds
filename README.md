# Open FPDS

Enabling Bulk Data Downloads of FPDS data in JSON, because it's 2016.

## Installation

To install, first make sure python 3 is installed. Then:

```
git clone https://github.com/vzvenyach/open-fpds.git
cd open-fpds
pip install -r requirements.txt
```

## Usage

To download a day of FPDS data, simply run:

`python run.py <start_date>`

where the start_date is formatted in the form "YYYY/MM/DD". The data will be saved in the `results` folder.

## Public domain

This project is in the worldwide [public domain](LICENSE.md).
