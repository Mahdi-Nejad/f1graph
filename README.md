# f1graph

A knowledge graph of Formula 1 history. Drivers, teams, circuits, and
races are pulled from public APIs and turned into a queryable graph.
Every relation links back to the record it came from.

## Status

Early. Setting up the pipeline. Nothing runs end-to-end yet.

## Data sources

- [Jolpica F1](https://github.com/jolpica/jolpica-f1) — historical race
  data. CC BY-NC-SA 4.0.
- [F1DB](https://github.com/f1db/f1db) — engines and constructor
  history. CC BY 4.0.

## Layout

```
src/f1graph/     package code
  io/            data loading
  graph/         graph construction
  api/           HTTP API
data/raw/        downloaded data (not committed)
data/processed/  cleaned outputs (not committed)
scripts/         one-off runnable scripts
tests/           tests
```

## Running

Not ready yet.
