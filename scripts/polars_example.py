import polars as pl


def main() -> None:
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    summed = df.with_columns((pl.col("a") + pl.col("b")).alias("a_plus_b"))
    print("a_plus_b column:")
    print(summed.select("a_plus_b"))
    print("column sums:")
    print(df.sum())


if __name__ == "__main__":
    main()