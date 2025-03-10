# 🚗🔋 Reducing EV Range Anxiety  

## **Paper details**

This repository contains datasets and code for our paper:  

[Reducing Electric Vehicle Range Anxiety with Machine Learning Models Incorporating Human Behavior](https://chemrxiv.org/engage/chemrxiv/article-details/67155be0cec5d6c142b80c48)

### Authors 
[Hemanth Neelgund Ramesh](https://nrhemanth.github.io/hemanthnr/about/), Souryadeep Mondal, Xiao Ma, Shuan Cheng, Tristan Angeles, [Shijing Sun](https://www.uwsunlab.com/shijing).  

*Department of Mechanical Engineering, University of Washington*  

Please contact us by email for questions about our paper or code.

hemnr31[at]uw[dot]edu, shijing[at]uw[dot]edu

<br>

## **Repository structure**
```bash
models/                     # Machine learning and Simulink models  
│
datasets/                   # Battery and velocity datasets used in this study  
│ ├── battery_data_processed/  # Processed battery dataset  
│ ├── battery_raw/             # Raw battery dataset  
│ ├── velocity_raw/            # Raw velocity dataset  
│
misc/                      # Miscellaneous files containing data processing notebooks and ML results  
│
dataset_description.md      # Detailed dataset documentation  
|
LICENSE                     # Repository license  
|
path_manager.py             # Manages dataset and script paths
|
pyproject.toml              # Python package dependencies  
|
readme.md                   
```
<br>

## **Dataset details**
You can read more about the dataset in:  
📄 **[dataset_description.md](./dataset_description.md)**

<br>

## **To reproduce results**
### **1. Clone the Repository**
```bash
git clone https://github.com/yourrepo/EV-range-anxiety.git
cd EV-range-anxiety
```

### **2. Install Dependencies**
You can install dependencies from `pyproject.toml` using **Poetry**:
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