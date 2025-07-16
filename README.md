# Observability playground

My objective with this repository is to play around with metrics and
observability tools, and to learn how to use them effectively.

Observability includes several pieces, from metrics, to alert system and
visualization.

For [metrics](./docs/metrics.md), tool selected for this playground is
[Prometheus](https://prometheus.io/). It is a system frequently used in many
projects, which supports distributed installations (native, docker, kubernetes).

Prometheus offers an alerting system, which is
[Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/).

For visualization, I have selected [Grafana](https://grafana.com/), which is a
popular tool for creating dashboards and visualizing metrics from various data
sources, including Prometheus.

## Getting started

A docker compose file is provided to run all the components together. To start
services, run:

```bash
task build
```

To stop and remove the services, run:

```bash
task clean
```

You have a health check for the services, which can be run with:

```bash
task health
```

## Accessing the services

- Prometheus: [http://localhost:9090](http://localhost:9090)
- Push gateway: [http://localhost:9091](http://localhost:9091)
- Alertmanager: [http://localhost:9093](http://localhost:9093)
- Grafana: [http://localhost:3000](http://localhost:3000)

## Concepts

Let's review some of the concepts used in this playground:

- data model: prometheus uses a time series data model, where values are stored
  with timestamps. These entries can be identify by a metric and/or labels.
- metric: a numerical value that represents a measurement of a system or
  application.
  [Metrics can be](https://prometheus.io/docs/concepts/metric_types/) counters
  (increasing values), gauges (numerical value can go up and down), histograms
  (time distribution and percentiles), or summaries (similar to histograms, but
  data cannot be aggregated).
- label: a key-value pair that provides additional context to a metric. Labels
  can be used to filter and group metrics.

## Publish metrics

WIP

## Querying

Prometheus provides a powerful
[query language](https://prometheus.io/docs/prometheus/latest/querying/basics/)
called PromQL, which allows you to perform actions such as filter, group, and
aggregate metrics.

WIP

## Alerting

WIP

## Visualization

WIP
