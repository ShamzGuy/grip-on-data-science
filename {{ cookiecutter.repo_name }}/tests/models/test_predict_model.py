import io
import pandas as pd
import json
from click.testing import CliRunner
from {{ cookiecutter.module_name }}.models.predict_model import main
from {{ cookiecutter.module_name }}.models.model_config import TARGET_NAME
from joblib import dump
from sklearn.linear_model import LinearRegression


CSV_DATA = f"""
OBJECTID,{TARGET_NAME}
0,1
1,1
2,3
3,4
4,1
"""


def test_evaluate():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("dataset.csv", "w") as f:
            f.write(CSV_DATA)
        df = pd.read_csv(io.StringIO(CSV_DATA))
        X, y = df.drop(columns=[TARGET_NAME]), df[TARGET_NAME]
        linreg = LinearRegression()
        linreg.fit(X, y)
        dump(linreg, "linearReg")
        result = runner.invoke(main, ["evaluate", "dataset.csv", ".", "report.json"])
        assert result.exit_code == 0
        with open("report.json", "r") as f:
            report = json.load(f)
        assert "linearReg" in report
