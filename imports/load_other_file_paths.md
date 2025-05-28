# Load the file path of a specific document

For when you need the path of a document for it's analysis.

Examples:
- CSV analysis
- Write or edit a file
- Read credentials or data from a file

You **SHOULD NOT** copy the exact path, because that will only exist on your machine. 

Instead try: 
```py
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "placas_carros.csv"
```

This will work for any machine, as long as the folder structure is the same.
