from src.utils.data_downloader import DataDownloader

if __name__ == "__main__":
    data_downloader = DataDownloader()
    data_downloader.download_dataset("yasserh/breast-cancer-dataset")