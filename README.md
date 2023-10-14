# Milkrun ETA Prediction
## Overview
Regression based models to estimate arrival time for milk runs. Milk run logistics are a type of delivery system where shipments are delivered to multiple locations in one trip.

## Installation Instructions
##### Step 1: Clone
Clone this git repository using:
```bash
git clone https://github.com/raashidsalih/milkrun-eta.git
```

##### Step 2: Configure
- Replace the content of ```input_source.csv``` with the data you want predictions for.
- Change the model you want to use (if needed) by modifying ```model_path``` in ```main.py```. You can refer to available models in the section below.
- If you'd like to use another location for the ```input_source.csv```, you can do so by changing ```model_path``` in ```main.py```

##### Step 3: Define Python Virtual Environment [Optional]
I suggest running the program in a Python venv for stability and reproducibility. Although optional, it is highly recommended to avoid potential dependency related issues. Navigate to the cloned directory and create a Python virtual environment using the following command *[Windows]:*
```bash
python -m venv myenv
```
Activate your Python venv using:
```bash
myenv\Scripts\activate
```
If you get a permission error with regards to not being able to run scripts, use this command first:
```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```
It'll not enforce restrictions for the rest of the session.

##### Step 4: Install Requirements
Install the dependencies for the program to run via the handy requirements.txt:
```bash
pip install -r requirements.txt
```

##### Step 5: Ready To Go
All the requirements have been satisfied, and you are now ready to use the program. Just run ```main.py``` from a CLI or using an IDE of your choosing. The results should be present in ```results.csv```.


