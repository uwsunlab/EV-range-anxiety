# 🚗🔋 Reducing EV Range Anxiety  

## **Paper details**

This repository contains datasets and code for our paper:  

[Reducing Electric Vehicle Range Anxiety with Machine Learning Models Incorporating Human Behavior](https://chemrxiv.org/engage/chemrxiv/article-details/67155be0cec5d6c142b80c48)

### Authors 
Souryadeep Mondal,[Hemanth Neelgund Ramesh](https://nrhemanth.github.io/hemanthnr/about/), Xiao Ma, Shuan Cheng, Tristan Angeles, [Shijing Sun](https://www.uwsunlab.com/shijing).  

*Department of Mechanical Engineering, University of Washington*  

Please contact us by email for questions about our paper or code.

hemnr31[at]uw[dot]edu, shijing[at]uw[dot]edu

<br>

## **Repository structure**
```
sample_data/              # Sample time-series velocity and battery performance data
|__sample_battery_data(processed).csv
|__sample_velocity_data.xlsx
|
models/                     # Machine learning and Simulink models   
│
misc/                      # Miscellaneous files containing data processing notebooks and ML results   
|
LICENSE                     
|
path_manager.py             # Manages dataset and script paths
|
pyproject.toml              # Python package dependencies  
|
readme.md                   
```
<br>

## **Dataset details**
The dataset will be uploaded upon publication; sample battery and velocity data can be accessed from the dataset folder.

<br>

## **To reproduce results**
### **1. Clone the Repository**
```bash
git clone https://github.com/uwsunlab/EV-range-anxiety.git
cd EV-range-anxiety
```

### **2. Install Dependencies**
Dependencies can be installed from `pyproject.toml` using Poetry:
```bash
poetry install
```
*(Use Python 3.11.6)*

<br>

## **Citation**
If you use our dataset or models in your research, please cite us:  

### **BibTeX**
```bibtex
@article{Mondal2024,
  author    = {Mondal, Souryadeep and Neelgund Ramesh, Hemanth and Ma, Xiao and Cheng, Shuan and Angeles, Tristan and Sun, Shijing},
  title     = {Reducing Electric Vehicle Range Anxiety with Machine Learning Models Incorporating Human Behavior},
  journal   = {ChemRxiv},
  year      = {2024},
  doi       = {10.26434/chemrxiv-2024-ztnx9}
}
```
<br>

## **License**
This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.
