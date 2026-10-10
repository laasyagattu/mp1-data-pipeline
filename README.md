# MP1 Data Pipeline

This pipeline loads a CSV file, checks that it has the expected structure, cleans it, and saves the result as a new CSV, with all settings controlled by `config/config.yaml`. 

Data moves through four stages: load, validate, process, and save. `pipeline.py` is the entry point: it reads the command-line arguments, checks that the input and config files exist, and calls each stage in order. The modules live in `src/`, where `data_loaders.py` reads CSV, JSON, and YAML files and `data_validator.py` confirms the required columns exist and removes rows with invalid numeric values. `data_processor.py` removes duplicates, missing values, and outliers based on the config, and `data_output.py` saves the cleaned data. `utils.py` holds the logging setup and file validation shared across the pipeline. Because column names and cleaning options come from the config file, the same code can clean a different dataset without any changes to the modules.

## Usage

```bash
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

## Example Output

```text
PASTE YOUR TERMINAL OUTPUT HERE
```