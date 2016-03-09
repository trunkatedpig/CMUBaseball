# CMUBaseball
This repository holds code for the future website of CMU Baseball.
To preview the website on your linux machine, run the following code from the directory you cloned into:
```
pip install virtualenv
virtualenv baseball
source baseball/bin/activate
cd CMUBaseball
pip install flask
pip install jinja
python app.py
```

Then, simply type in http://0.0.0.0:8000/ into your browser.


To preview the website again, simply go to the directory you cloned into and enter the following commands:
```
source baseball/bin/activate
cd CMUBaseball
python app.py
```

If you do not have pip installed, you can go to https://pip.pypa.io/en/stable/installing/ for download and installation instructions.
