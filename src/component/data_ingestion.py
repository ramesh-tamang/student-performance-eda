import os
import pandas as pd
from sklearn.model_selection import train_test_split
import logging

# Temporary CustomException
class CustomException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

# Config class
class DataIngestionConfig:
    raw_data_path: str = os.path.join('data', 'raw', 'data.csv')
    train_data_path: str = os.path.join('data', 'processed', 'train.csv')
    test_data_path: str = os.path.join('data', 'processed', 'test.csv')

# Main ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Data Ingestion started...")

        try:
            # Read dataset
            df = pd.read_csv('data/student_performance.csv')  # dataset path
            logging.info("Dataset loaded successfully")

            # Create directories if not exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved")

            # Split into train and test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train-test split completed")

            logging.info("Data Ingestion completed successfully ✅")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e)

# Run if main
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    print("Data Ingestion Completed!")
    print(f"Train Data Path: {train_data}")
    print(f"Test Data Path: {test_data}")
