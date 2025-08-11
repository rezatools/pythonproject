import polars as pl


def test_polars_sum() -> None:
    df = pl.DataFrame({"x": [1, 2, 3]})
    assert df.select(pl.col("x").sum()).item() == 6