import shutil
from pathlib import Path

STAGING_MODEL = Path("models/staging/model.txt")
PRODUCTION_MODEL = Path("models/production/model.txt")

def promote():
    if not STAGING_MODEL.exists():
        raise RuntimeError("No staging model found. Train before promotion.")

    PRODUCTION_MODEL.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(STAGING_MODEL, PRODUCTION_MODEL)

    print("Model successfully promoted from staging to production")

if __name__ == "__main__":
    promote()

