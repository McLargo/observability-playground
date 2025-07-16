# Observability playground

My objective with this repository is to play around with metrics and
observability tools, and to learn how to use them effectively.

Observability includes several pieces, from metrics, to alert system and
visualization.

For metrics, tool selected for this playground is
[Prometheus](https://prometheus.io/). It is a system frequently used in many
projects, which supports distributed installations (native, docker, kubernetes).

Prometehus offers an alerting system, which is
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
