# Data Engineering Portfolio Project - Yale Endowment Portfolio Analysis

This project focuses on analyzing the Yale Endowment Portfolio returns over the past 5 years using various technologies such as Python, Amazon S3, AWS Glue, SQL, Amazon Athena, and Amazon QuickSight.

## Project Breakdown

1. Data Ingestion & Storage Script:
   - Retrieve and ingest data from relevant sources.
   - Transform the data and store it in a pandas DataFrame.
   - Create an S3 bucket along with read and write subfolders.
   - Upload the transformed data to the S3 bucket as CSV files.

2. Custom Database & Tables (AWS Glue Crawler):
   - Set up a custom database for storing the portfolio data.
   - Define tables and their schemas using AWS Glue Crawler.

3. Data Upload to Database & Tables (AWS Glue Job):
   - Configure the necessary IAM permissions for the AWS Glue ETL job, including Amazon S3 and AWS Glue permissions.
   - Use the AWS Glue Visual Editor to configure the ETL job:
     - Set Amazon S3 as the data source.
     - Apply necessary transformations to the data (preview transformations if required).
     - Specify Amazon S3 as the target to write the transformed data.
   - Save and run the AWS Glue ETL job to upload the transformed data to the specified S3 location.

4. Data Availability in Amazon Athena:
   - The uploaded data is now available in the Amazon Athena database, allowing SQL queries to be performed on the dataset.

5. Connect Dataset to Amazon QuickSight for Visualization:
   - Utilize Amazon QuickSight to connect to the dataset stored in Amazon Athena.
   - Perform visualizations and gain insights from the Yale Endowment Portfolio data.

## Prerequisites

- Python
- Amazon Web Services (AWS) account with access to Amazon S3, AWS Glue, Amazon Athena, and Amazon QuickSight.

## Project Setup

1. Clone the project repository.
2. Set up the required AWS services (S3, AWS Glue, Amazon Athena, and Amazon QuickSight).
3. Configure the necessary AWS credentials on your local development environment.
4. Run the Data Ingestion & Storage Script to retrieve, transform, and upload the data to the S3 bucket.
5. Set up the custom database and tables using AWS Glue Crawler.
6. Configure and run the AWS Glue ETL job to upload the data to the database.
7. Perform SQL queries using Amazon Athena on the uploaded data.
8. Connect the dataset to Amazon QuickSight for data visualization.

## Additional Notes

- Make sure to review and adjust the configurations, permissions, and file paths as per your specific environment and requirements.
- Refer to the official AWS documentation for detailed instructions on setting up and using AWS services mentioned in this project.