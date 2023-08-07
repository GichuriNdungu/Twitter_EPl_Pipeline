# CSV DATA PIPELINE
This data engineering project aims to create a simple data pipeline that extracts data from a csv source, transforms it, and finally loads into a data warehouse from which further analysis can be made. 
The project is powered by technological concepts such as;
    1. Python Pandas
        * Mainly used to transform data by creating fact and dimension tables. Also heavily employed in the extraction and loading of data into the warehouse.
    2. API's
        - Used to access static data stored in Google cloud storage. 
    3. Mage.AI
        - This is a modern data orchestration tool used to create, maintain and monitor data pipelines. In this project, it is used to create and run the pipeline. 
    4. Google Cloud Plartform
        - Google cloud storage (For storing static data)
        - Google bigquery (For data warehousing)
        - Google enginet (used to run Mage.AI)
