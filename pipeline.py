"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys

from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)


logger = logging.getLogger(__name__)


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Data Processing Pipeline")
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the input file"
    )
    parser.add_argument(
        "--config", "-c",
        required=True,
        help="Path to a YAML configuration file"
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Path to the output file"
    )
    parser.add_argument(
        "--verbose", "-v", 
        action="store_true", 
        help="Enable verbose logging"
    )
    args = parser.parse_args()
    return args


def main():
    """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(f"Arguments parsed: input= {args.input}, output= {args.output}, config= {args.config}")
    if not validate_input(args.input):
        sys.exit(1)
    if not validate_input(args.config):
        sys.exit(1)

    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)

    required_columns = config["validation"]["required_columns"]
    numeric_columns = config["validation"]["numeric_columns"]

    try:
        validated = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)
    logger.info(f"Validation complete: {len(data)} -> {len(validated)} rows")


    original = validated.copy()
    try:
        cleaned = process_data(validated, config)
    except ValueError:
        sys.exit(1)

    report = create_cleaning_report(data, cleaned)
    logger.info(f"Processing complete: removed {report["rows_removed"]} rows, removed {report["columns_removed"]} columns")
    
    output_path = save_data(cleaned, args.output)
    logger.info(f"Saved cleaned data to: {output_path}")

    print(report)

if __name__ == "__main__":
    main()
