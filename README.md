# QoS weakness benchmark

Code for the paper **"Hidden weaknesses in QoS-based service ranking: a known-answer benchmark of normalization and aggregation choices"** (Kumar, Kumari, Mohapatra, Jyotish, Kumar).

The benchmark adds services with planted weaknesses of known type and severity to the 2,500 services of QWS v2.0, then varies normalization and aggregation one at a time under fixed weights.

## Requirements

- Python 3.11 or newer (NumPy 2.3.5 requires it)
- Packages pinned in `requirements.txt`

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The experiments in the paper were run on a laptop (Intel Core i7-14650HX, 16 GB RAM, 64-bit Windows, no GPU).

## Data

The QWS v2.0 dataset is not redistributed here. Obtain it from its original authors (Al-Masri and Mahmoud, ICCCN 2007) and save it as `data/qws.csv`. See `data/README.md` for the expected columns.

## How to run

1. Place the data file as described above.
2. Open `benchmark_experiments.ipynb` in Jupyter.
3. Choose Kernel > Restart & Run All.

The BWM judgments (best criterion, worst criterion, and the two comparison vectors) are set in the notebook's BWM step. They are the values reported in Appendix A of the paper: best = Reliability, worst = Documentation, A_B = (4, 3, 5, 3, 1, 4, 5, 4, 7), A_W = (4, 5, 3, 5, 7, 4, 3, 4, 1) in the order ResponseTime, Availability, Throughput, Successability, Reliability, Compliance, BestPractices, Latency, Documentation.

## Random seeds

Each run uses `numpy.random.default_rng(seed)`.

| Analysis | Seeds |
|---|---|
| Main benchmark, severity grid, weight robustness | 0-19 |
| Held-out replication | 100-119 |
| Independent benchmark | 200-219 |



## License

MIT. See `LICENSE`.

## Citation

See `CITATION.cff`. A DOI will be added after the first archived release.
