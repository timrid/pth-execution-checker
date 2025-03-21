# .pth file execution checker
This package is for checking if .pth files are automatically processed at startup by `site.py`. 

## Installation
```
pip install git+https://github.com/timrid/pth-execution-checker@main
```

## Usage
After the whole interpreter is startet and the main script is running, you can check if the .pth file is processed like this:

```python
import pth_execution_checker
if not pth_execution_checker.pth_executed:
    raise RuntimeError(".pth file not processed...")
```
