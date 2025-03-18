import os

from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer, KafkaSourceBuilder
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

souce_query = f"""
  CREATE TABLE powerball_source (
    algo STRING,
    power_result STRING,
    power_section STRING,
    power_under_over STRING,
    basic_result STRING,
    basic_sum STRING,
    basic_section STRING,
    basic_size STRING,
    basic_odd_even STRING,
    basic_under_even STRING
  ) WITH (
    'connector' = 'kafka',
    'topic' = 'powerball_5',
    'properties.bootstrap.servers' = 'localhost:9092',
    'properties.group.id' = 'test-group',
    'format' = 'json',
    'scan.startup.mode' = 'latest-offset'
  )
"""

sink_query = """
  CREATE TABLE sink (
    algo STRING
  ) WITH (
    'connector' = 'print'
  )
"""

t_env.execute_sql(souce_query)
t_env.execute_sql(sink_query)
t_env.from_path("powerball_source").execute().wait()
t_env.execute("flink_kafka_to_kafka_sql")
