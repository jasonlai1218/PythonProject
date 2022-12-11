from pyspark.sql import SparkSession
import pandas as pd
from libs.cpaContractTypeConverter import convert_all_missing_type_as_none, OverallContractTypeConverter
from libs.cpaType import ContractDataFrameMagicValue, ContractDataFrameColumn


if __name__ == '__main__':
    spark = SparkSession.builder.appName("jason-test").master("local").config("spark.driver.host", "127.0.0.1").getOrCreate()
    # p = "/Users/al02027975/Downloads/example_1.json"
    # df = spark.read.json(p)
    # pdf = pd.DataFrame({
    #     "x": [1, None], "y": [None, "foo"],
    #     "z": [pd.Timestamp("20120101"), pd.Timestamp("NaT")]
    # })
    # df = spark.createDataFrame(pdf)
    df = spark.createDataFrame([(1, float('nan'), '{"a":"test", "b":"test2"}'), (None, 1.0, '{"a":"test3", "b":"test4"}')], ("aa", "bb", "operation_log"))
    df.printSchema()
    df.show(truncate=False)

    # handle NaN
    # df = convert_all_missing_type_as_none(df)
    # df.printSchema()
    # df.show(truncate=False)

    df = OverallContractTypeConverter(df).convert()
    # df = df.replace(to_replace=ContractDataFrameMagicValue.INT_AS_NULL.value,
    #                 value=None, subset=[ContractDataFrameColumn.USER_UPPER_LIMIT.value])
    df.printSchema()
    df.show(truncate=False)