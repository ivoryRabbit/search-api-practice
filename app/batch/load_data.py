import glob
import subprocess
import zipfile
import pandas as pd
from urllib import request


def load_data(root_path: str) -> None:
    """load Movie Lens data"""
    marker = f"{root_path}/_SUCCESS"
    if glob.glob(marker):
        return

    download_url = "https://files.grouplens.org/datasets/movielens/ml-1m.zip"
    request.urlretrieve(download_url, "ml-1m.zip")

    zip_file = zipfile.ZipFile("ml-1m.zip")
    zip_file.extractall()

    schemas = {
        "ratings": ["user_id", "item_id", "rating", "timestamp"],
        "users": ["user_id", "gender", "age", "occupation", "zip_code"],
        "movies": ["item_id", "title", "genres"],
    }

    for dataset, columns in schemas.items():
        source_file_name = f"ml-1m/{dataset}.dat"
        df = pd.read_csv(
            source_file_name,
            delimiter="::", names=columns, engine="python", encoding="ISO-8859-1"
        )

        output_file_name = f"{root_path}/{dataset}.csv"
        df.to_csv(output_file_name, index=False)

    subprocess.check_call("rm ml-1m.zip", shell=True)
    subprocess.check_call("rm -r ml-1m", shell=True)
    subprocess.check_call(f"touch {marker}", shell=True)


if __name__ == "__main__":
    load_data(root_path="data")
