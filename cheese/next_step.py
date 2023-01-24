import os

from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.datastream.execution_mode import RuntimeExecutionMode
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)
settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
t_env = StreamTableEnvironment.create(env, environment_settings=settings)

kafka_jar_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "./",
    "flink-sql-connector-kafka_2.11-1.14.4.jar"
)
t_env.get_config().get_configuration().set_string(
    "pipeline.jars", f"file://{kafka_jar_path}"
)


source_query = """
    CREATE TABLE pb_5_table (
        `algo` STRING METADATA FROM 'value.algo' VIRTUAL,
        `result` STRING METADATA FORM 'value.powerBall.result' VIRTUAL,
        `k_Offset` INT
        `odd_even` STRING METADATA FORM 'value.powerBall.odd_even' VIRTUAL,
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'powerball_5_test',
        'properties.bootstrap.servers' = 'psawesome.xyz:50900',
        'properties.group.id' = 'cheese_next_step',
        'key.format' = 'json',
        'key.fields-prefix' = 'k_',
        'key.fields' = 'k_Offset;k_Key;k_Timestamp',
        'value.format' = 'debezium-json'
        'scan.startup.mode' = 'latest-offset'
    )
"""

t_env.execute_sql(source_query)

def tmp(row):
    if row.odd_even == True:
        pass

pb_table = t_env.from_path("pb_5_table")
pb_table = pb_table.select(pb_table.algo, pb_table.odd_even)
pb_table.map(lambda x: x).alias()
