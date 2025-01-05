from pathlib import Path

#dir paths
ROOT_DIR = Path(__file__).parent
DATASET_DIR = ROOT_DIR / 'datasets'
MISC_DIR = ROOT_DIR / 'misc'
MODELS_DIR = ROOT_DIR / 'ML_and_simulink_models'
PLOT_DIR = ROOT_DIR / 'plots'

#specific folder paths
BATT_DATA_DIR = DATASET_DIR / 'battery_dataset'
VEL_DATA_DIR = DATASET_DIR / 'velocity_dataset'
CURRENT_MODEL_DIR = MODELS_DIR /'current_based_ML_models'
FORECAST_MODEL_RESULT_DIR = CURRENT_MODEL_DIR / 'forecast_model_results'
VEL_MODELS = MODELS_DIR / 'velocity_based_ML_models'

##specific notebook file paths
FORECAST_DATA_NB = MISC_DIR / 'forecast_data_create.ipynb'
REF_NB = MISC_DIR / 'Cons_brk_tests.ipynb'
TRAIN_DATA_NB = MISC_DIR / 'Database_create.ipynb'
TEST_DATA_NB = MISC_DIR / 'Test_data_create.ipynb'
