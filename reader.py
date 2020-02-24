import pandas as pd


class Reader:
    def _read_data(self, url: str):
        self._dataset = pd.read_csv(url)

    def load_data(self, url: str):
        self._read_data(url)
        return self._dataset

    def clean_data(self, dataset: pd.DataFrame):
        self._parse_date(dataset, ["date"])
        self._parse_float(dataset, ["high", "low"])
        self._compute_mid_range_price(dataset)
        return self._dataset

    def _parse_date(self, dataset: pd.DataFrame, list_of_columns: list):
        for col in list_of_columns:
            dataset[col] = pd.to_datetime(dataset[col])

    def _parse_float(self, dataset: pd.DataFrame, list_of_columns: list):
        for col in list_of_columns:
            dataset[col] = dataset[col].str.strip("$").astype("float64")

    def _compute_mid_range_price(self, dataset: pd.DataFrame):
        dataset["mid_range_price"] = dataset[["high", "low"]].mean(axis=1)
