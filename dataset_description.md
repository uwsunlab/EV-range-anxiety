## Dataset Description

The battery and velocity datasets are located in the `dataset/` folder, which contains three subfolders:

- `battery_dataset/` – Raw battery current profile data
- `battery_data(processed)/` – Processed battery current profiles
- `velocity_dataset/` – Drive cycle data used to generate battery current profiles

Each subfolder organizes data into directories for training, testing, and reference (*not validation*).  
Reference data is not used for model validation, it provides insight into typical drive cycles or current profiles.

<br>

#### File Format:
- Velocity data (drive cycles) `.xlsx` format  
- Battery data (current profiles) `.csv` format  

<br>

#### `battery_dataset/ `
*Raw battery current profiles*

`train/` – 102 current profiles (96 original + 6 retests) used for ML training
  - Example: `batch1_method1_assertive_downhill_1` 
    1st driver of batch 1, method 1 charging habit, assertive driving style, downhill terrain
  
`test/` – Test battery current profiles

`reference/` – Reference battery current profiles

<br>

#### `battery_data(processed)/` 
*(Processed battery current profiles – the files you are mostly looking for are in this folder)*  

`train/` – 102 processed current profiles (96 original + 6 retests) used for ML training

`test/` – 12 processed current profiles for testing

`reference/` – 9 processed reference current profiles (not used for validation)

<br>

#### `velocity_dataset/ `
*(Drive cycle data for generating battery profiles)*

`train/` – 16 drive cycles grouped by driving style & batch
  - Example: `assertive_batch1/` contains drive cycles for an assertive driver in batch 1

`test/`– 4 test drive cycles, named by batch & driving style
  - Example: `test_1_def` Test cycle 1 for a defensive driver

`reference/` – 3 reference drive cycles based on trip behavior
  - `brake_once` – A single braking event occurs from max to mean velocity
  - `cons_max_vel` – Constant maximum velocity trip
  - `cons_mean_vel` – Constant mean velocity trip

---

#### Notes
`battery_dataset/` contains raw files, while `battery_data(processed)/` contains processed files
Reference data is only for insight, not for model validation
Battery profiles are generated from velocity (drive cycle) data
The folder structure mirrors the way data is developed