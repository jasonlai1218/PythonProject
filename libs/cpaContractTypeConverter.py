from pyspark.sql.functions import when, isnan, col, from_json
from pyspark.sql import DataFrame
from pyspark.sql.types import MapType, StringType

from libs.cpaType import TestDataFrameColumn, ContractDataFrameColumn


def convert_all_missing_type_as_none(df: DataFrame) -> DataFrame:
    for c in df.columns:
        df = df.withColumn(
            c, when(isnan(col(c)), None).otherwise(col(c))
        )

    return df


def tuplize_enum_class_values(enum_class):
    """
        - Exmaple:
        >>> from enum import Enum
        >>> class CandidateAppType(Enum):
        ...     HistoricalLowPrice = "historical_low_price"
        ...     RecentLowPrice = "recent_low_price"
        >>> tuplize_enum_class_values(CandidateAppType)
        ('historical_low_price', 'recent_low_price')
    :param enum_class: an instance of Enum
    :return: tuple
    """
    from enum import Enum

    # check enum_class is Class(Enum) Type
    if isinstance(enum_class, Enum):
        raise TypeError("Wrong Enum class type - but got {}".format(type(enum_class)))
    return tuple(k.value for k in enum_class)


def convert_json_string_to_map(df: DataFrame, col: str) -> DataFrame:
    """Will return DataFrame of keys and values both with string types"""
    return df.withColumn(col, from_json(df[col], MapType(StringType(), StringType())))


class OverallContractTypeConverter:
    def __init__(self, df: DataFrame):
        self.df = convert_all_missing_type_as_none(df)

    def convert(self):
        """
        Note
        ----
        - Be careful the placeholders e.g., NaN / NaT or Inf in Pyspark
        Dataframe
        Ref
        ---
        - https://stackoverflow.com/questions/50992713/pyspark-replace-nan-with-null
        """
        BaseContractColumnTypeConverter.meet_condition_pre(self.df)

        for sub_cls in BaseContractColumnTypeConverter.__subclasses__():
            instance = sub_cls(self.df)
            self.df = instance.convert()

        return self.df


class BaseContractColumnTypeConverter:
    def __init__(self, df: DataFrame):
        self.df = df

    @staticmethod
    def meet_condition_pre(df: DataFrame) -> None:
        essential_columns = tuplize_enum_class_values(TestDataFrameColumn)
        # print(f'essential_columns:{essential_columns}')
        # print(f'df.columns:{df.columns}')
        print(f'set(essential_columns):{set(essential_columns)}')
        print(f'set(df.columns):{set(df.columns)}')

        missing_columns = set(essential_columns).difference(set(df.columns))
        print(f'missing_columns:{missing_columns}')
        print(f'len(missing_columns):{len(missing_columns)}')
        assert len(missing_columns) == 0, f"Missing columns {missing_columns}"

    def convert(self):
        return NotImplemented


class OperationLogTypeConverter(BaseContractColumnTypeConverter):
    def convert(self) -> DataFrame:
        self.df = convert_json_string_to_map(self.df, ContractDataFrameColumn.OPERATION_LOG.value)
        return self.df