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

### Converting the results
1. Convert the results to a CSV file:

```
git clone https://github.com/cloudforge-co/CIS-benchmark.git
cd CIS-benchmark
export S3_FILE_NAME="cis-results.json"
python docker-convert.py
```

2. The script prints its output to stdout. The CSV file uses "-ctrl-" special string as delimiter.

## kube-bench
### Running kube-bench
1. Obtain the desired release of the kube-bench binary from [aquasecurity repository](https://github.com/aquasecurity/kube-bench/releases)

2. Prepare kube-bench's configuration via its config file:

```
cat ${kube-bench-folder}/cfg/config.yaml
```

3. Run the benchmark as root user:

```
./kube-bench --config-dir `pwd`/cfg --config `pwd`/cfg/config.yaml --version 1.25 --noremediations --json > cis-results.json
```

### Converting the results
1. Convert the results to a CSV file:
```
git clone https://github.com/cloudforge-co/CIS-benchmark.git
cd CIS-benchmark
export S3_FILE_NAME="cis-results.json"
python kube-convert.py
```
