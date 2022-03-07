import pathlib

import uvicorn

# https://github.com/Razor-Sec/HighLevel-Architecture-APP
if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
