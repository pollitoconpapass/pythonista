# Loading the `.env` file from different subdirectories

Example, if your folder directory is like this: 
```
funcs
|_ retrieval_funcs.py
app.py
.env
```

And you want to load the .env file inside the `retrieval_funcs.py`file. 

Do it like this:
```py
import os
from dotenv import load_dotenv

# Navigate one directory up from retrieval_funcs.py to access .env
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

```

## Deeper Nesting
```
project/
│
├── src/
│   └── modules/
│       └── app.py
├── .env
```

You need to go up 2 levels:
```py
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

```