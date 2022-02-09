# HBV on DAFNI


[![release](https://img.shields.io/github/v/release/openclim/hbv-dafni)](https://github.com/OpenCLIM/hbv-dafni/releases/latest)
[![build](https://github.com/OpenCLIM/hbv-dafni/actions/workflows/build.yml/badge.svg)](https://github.com/OpenCLIM/hbv-dafni/actions/workflows/build.yml)

This DAFNI model runs an HBV simulation using preprocessed input data.

## Usage 
```
docker build -t hbv-dafni .
docker run -v "<absolute_path_of_data_directory>:/data" --name hbv-dafni hbv-dafni
```
or
```
python run.py
```
## Documentation
[hbv-dafni.md](docs/hbv-dafni.md)

To build the documentation:
```
cd docs
python build_docs.py
```