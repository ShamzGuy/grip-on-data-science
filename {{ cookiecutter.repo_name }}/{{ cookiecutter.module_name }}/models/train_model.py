# -*- coding: utf-8 -*-
import click
import logging
import logging.config
from pathlib import Path
from sklearn.model_selection import train_test_split
from ..log_config import LOGGING
from ..utils import read_file, to_file


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
    dataset = read_file(input_file)
    logger.info("Dataset has %d lines.", len(dataset.index))
    train, test = train_test_split(dataset)
    logger.info("Train set has %d lines.", len(train.index))
    logger.info("Test set has %d lines.", len(test.index))
    to_file(train, output_dir / "train.csv")
    to_file(test, output_dir / "test.csv")


if __name__ == "__main__":
    main()
