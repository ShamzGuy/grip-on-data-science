# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    """
    Runs generic data processing and cleanup scripts to turn raw data
    from (../raw) into interim data that can be further analyzed and aggregated.

    Examples / Ideas:
    - Delete duplicate rows in raw data that are results of a bad SQL
    - Remove columns that are constant
    - Remove columns that only contain technical information and are not
    needed for aggregation (ids)
    """
    logger = logging.getLogger(__name__)
    logger.info("Running generic data processing and cleanup scripts...")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
