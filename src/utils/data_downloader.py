import os
import sys
import json
from kaggle import KaggleApi

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DataDownloader:
    """
    This class provides methods for downloading datasets from Kaggle.
    """

    def __init__(self, kaggle_json_path=None):
        """
        This method initializes the KaggleApi object and authenticates the user.

        Args:
            kaggle_json_path (str): The path to the Kaggle API credentials JSON file.
        """
        
        self.api = KaggleApi()

        if kaggle_json_path:
            with open(kaggle_json_path, 'r') as f:
                creds = json.load(f)
            os.environ['KAGGLE_USERNAME'] = creds['username']
            os.environ['KAGGLE_KEY'] = creds['key']

        self.api.authenticate()

    def download_dataset(self, dataset_name):
        """
        This method downloads a dataset from Kaggle.

        Args:
            dataset_name (str): The name of the dataset to download.

        Returns:
            None
        """

        download_path = f"./data/{dataset_name.split('/')[-1]}"
        os.makedirs(download_path, exist_ok=True)
        self.api.dataset_download_files(dataset_name, path=download_path, unzip=True)

