# Visualization

For visualization, we are using [Grafana](http://localhost:3000/). It is a
powerful tool for creating dashboards and visualizing metrics from various data
sources, like Prometheus as data source (first thing to configure when starting
Grafana).

Queries can be written in PromQL, but Grafana also provides a query builder that
allows you to create queries without writing PromQL directly.

You can create dashboards to gather your panels to visualize different metrics
(a panel can have more than 1 queries.). Several types of panel visualizations
are available, such as graphs, tables, pie charts, histograms, and more.
