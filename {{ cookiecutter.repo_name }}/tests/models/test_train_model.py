from click.testing import CliRunner
from {{ cookiecutter.module_name }}.models.train_model import main
from {{ cookiecutter.module_name }}.models.model_config import TARGET_NAME

CSV_DATA = f"""
OBJECTID,{TARGET_NAME}
0,1
1,1
2,3
3,4
4,1
"""


def test_split():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("dataset.csv", "w") as f:
            f.write(CSV_DATA)
        result = runner.invoke(main, ["split", "dataset.csv", "."])
        assert result.exit_code == 0


def test_train():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("dataset.csv", "w") as f:
            f.write(CSV_DATA)
        result = runner.invoke(main, ["train", "dataset.csv", "."])
        assert result.exit_code == 0
