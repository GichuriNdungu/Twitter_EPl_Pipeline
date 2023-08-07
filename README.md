# CSV DATA PIPELINE

This data engineering project aims to create a simple data pipeline that extracts data from a csv source, transforms it, and finally loads into a data warehouse from which further analysis can be made. The project is powered by technological concepts such as:

* Python Pandas
  * Mainly used to transform data by creating fact and dimension tables. Also heavily employed in the extraction and loading of data into the warehouse.

* APIs
  - Used to access static data stored in Google cloud storage.

* Mage.AI
  - This is a modern data orchestration tool used to create, maintain, and monitor data pipelines. In this project, it is used to create and run the pipeline.

* Google Cloud Platform
  - Google cloud storage (For storing static data)
  - Google bigquery (For data warehousing)
  - Google engine (used to run Mage.AI)
## Project Setup
![Project_breakdown](/images/project_visual.png)
The above image demonstrates the overall flow of the entire project.
