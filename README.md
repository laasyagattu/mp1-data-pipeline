# MP1 Data Pipeline

This pipeline loads a CSV file, checks that it has the expected structure, cleans it, and saves the result as a new CSV, with all settings controlled by `config/config.yaml`. 

Data moves through four stages: load, validate, process, and save. `pipeline.py` is the entry point: it reads the command-line arguments, checks that the input and config files exist, and calls each stage in order. The modules live in `src/`, where `data_loaders.py` reads CSV, JSON, and YAML files and `data_validator.py` confirms the required columns exist and removes rows with invalid numeric values. `data_processor.py` removes duplicates, missing values, and outliers based on the config, and `data_output.py` saves the cleaned data. `utils.py` holds the logging setup and file validation shared across the pipeline. Because column names and cleaning options come from the config file, the same code can clean a different dataset without any changes to the modules.

## Usage

```bash
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

## Example Output

```text
00:48:09 DEBUG    __main__ — Arguments parsed: input= fixtures/sample_data.csv, output= output/clean.csv, config= config/config.yaml
00:48:09 INFO     src.utils — Input file validated: fixtures/sample_data.csv
00:48:09 INFO     src.utils — Input file validated: config/config.yaml
00:48:09 INFO     src.data_loaders — Loaded CSV file: fixtures/sample_data.csv
00:48:09 INFO     src.data_loaders — Loaded YAML file: config/config.yaml
00:48:09 WARNING  src.data_validator — Invalid numeric value in rating at row 94: 'not_available'
00:48:09 WARNING  src.data_validator — Invalid numeric value in rating at row 95: 'error'
00:48:09 WARNING  src.data_validator — Removed 2 rows with invalid numeric values in rating
00:48:09 DEBUG    src.data_validator — Validation: 100 -> 98 rows
00:48:09 INFO     __main__ — Validation complete: 100 -> 98 rows
00:48:09 DEBUG    src.data_processor — Removed 2 rows with duplicate data
00:48:09 DEBUG    src.data_processor — Removed 2 rows with missing data
00:48:09 DEBUG    src.data_processor — rating: method = iqr, threshold = 1.5, lower = 43.625, upper = 106.625, rows removed = 2
00:48:09 INFO     __main__ — Processing complete: removed 6 rows, removed 0 columns
00:48:09 DEBUG    src.data_output — Saved 92 rows to output/clean.csv
00:48:09 INFO     __main__ — Saved cleaned data to: output/clean.csv
Cleaning Report: {'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
```