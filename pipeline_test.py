import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import logging

def main():
    options = PipelineOptions([
        "--runner=FlinkRunner",
        "--flink_version=1.14",
        "--flink_master=localhost:8081",
        "--environment_type=EXTERNAL",
        "--environment_config=pythonsdk:50000",
        "--sdk_worker_parallelism=1"
    ])

    #options = PipelineOptions([
    #    "--runner=FlinkRunner",
    #])
    
    with beam.Pipeline(options=options) as pipeline:
        lines = pipeline | 'ReadFromText' >> beam.io.ReadFromText('input.txt') | beam.io.WriteToText('output', file_name_suffix='.txt')
    
if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)

    main()