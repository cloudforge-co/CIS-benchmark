# CIS-benchmark
Converting CIS benchmark results to CSV format.

## docker-bench
### Running docker-bench

1. Clone the [docker-bench-security](https://github.com/docker/docker-bench-security) repository and run the benchmark directly on the node:

```
git clone https://github.com/docker/docker-bench-security.git
cd docker-bench-security
sudo sh docker-bench-security.sh -l cis-results
```

2. Convert the results to a CSV file:

```
git clone https://github.com/cloudforge-co/CIS-benchmark.git
cd CIS-benchmark
export S3_FILE_NAME="cis-results.json"
python convert-cis.py
```

3. The script prints its output to stdout. The CSV file uses "-ctrl-" special string as delimiter.
