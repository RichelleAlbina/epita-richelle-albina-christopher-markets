# EPITA Financial Markets CLI Tool (TP2)

A Python CLI application built for the EPITA Engineering Tools lab (TP2). It provides environment isolation, API integration, interactive rich dashboards, and a robust build pipeline using modern tooling like `uv`.

## 🚀 Features

* **`uv` Environment Isolation**: Uses `uv` for dynamic, reproducible environment management without manual shell activation.
* **Rich Dashboard**: Terminal interface powered by `rich` to fetch and render market data.
* **SemVer & Dependency Locking**: Strictly declared constraints in `pyproject.toml` with reproducible builds via `uv.lock`.
* **Clean Code & Debugging**: Resolved runtime type errors and validated telemetry aggregations.

## 🛠️ Requirements & Setup

Make sure you have [`uv`](https://github.com/astral-sh/uv) installed on your system.

### Installation

Clone the repository and install dependencies:

```bash
git clone [https://github.com/RichelleAlbina/epita-richelle-albina-christopher-markets.git](https://github.com/RichelleAlbina/epita-richelle-albina-christopher-markets.git)
cd epita-richelle-albina-christopher-markets
uv sync
