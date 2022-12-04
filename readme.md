# Attempt to create a beam/flink cluster via podman


## Requirements 

* python installed
* [podman](https://podman.io/) 

## Setup

* run `$ source setup` to create virtual envoirement and install requirements
* run `$ podman-compose up -d ` to start beam/flink cluster with one jobmanager, one taskmanager and one pythonsdk harness worker
* run `$ python pipeline_test.py` to execute pipeline

## Problem

It looks like the sdk-worker is getting stuck. `$ podman logs podman_beam_flink_pythonsdk_1 ` produces:

```
2022/12/04 16:13:02 Starting worker pool 1: python -m apache_beam.runners.worker.worker_pool_main --service_port=50000 --container_executable=/opt/apache/beam/boot
Starting worker with command ['/opt/apache/beam/boot', '--id=1-1', '--logging_endpoint=localhost:45087', '--artifact_endpoint=localhost:35323', '--provision_endpoint=localhost:36435', '--control_endpoint=localhost:33237']
2022/12/04 16:16:31 Failed to obtain provisioning information: failed to dial server at localhost:36435
        caused by:
context deadline exceeded
```

## Sources 

* Flink Cluster and docker-compose.yml from: [Link](https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/resource-providers/standalone/docker/#flink-with-docker-compose)
* SDK Harness worker: [Link](https://beam.apache.org/documentation/runtime/sdk-harness-config/)