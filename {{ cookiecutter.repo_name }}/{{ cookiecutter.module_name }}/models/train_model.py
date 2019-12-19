# -*- coding: utf-8 -*-
import click
import logging
import logging.config
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from ..log_config import LOGGING


logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


@click.group()
def main():
    pass


@main.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def split(input_file, output_filepath):
    """
    Splits the `input_file` into a train set and a test set that
    are written to `output_filepath`.
    """
    logger.info("Splitting into train and test set...")
    output_dir = Path(output_filepath)
    dataset = pd.read_csv(input_file)
    logger.info("Dataset has %d lines.", len(dataset.index))
    train, test = train_test_split(dataset)
    logger.info("Train set has %d lines.", len(train.index))
    logger.info("Test set has %d lines.", len(test.index))
    train.to_csv(output_dir / "train.csv", index=False)
    test.to_csv(output_dir / "test.csv", index=False)


if __name__ == "__main__":
    main()
