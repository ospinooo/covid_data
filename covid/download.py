
from covid.config import Covid19Parameters
import shutil
import os
import subprocess
import datetime

from enum import Enum


def download_daily():

    dt = datetime.datetime.now().strftime("%Y%m%d")

    dir = f'data/{dt}'
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)

    for enum in Covid19Parameters:
        out = subprocess.run(
            ["wget", f"https://opendata.ecdc.europa.eu/covid19/{enum.value}/csv", "-q", "-O", f"{dir}/{enum.value}.csv"])

        print(out)


if __name__ == "__main__":
    download_daily()
