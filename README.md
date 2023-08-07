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
## Project flow breakdown
![Project_breakdown](/images/project_visual.png)

The above image demonstrates the overall flow of the entire project.
To setup the project, please follow the following steps; 
* Connect to google cloud storage and create a new bucket that will house your csv files. 
    - Having the data stored in google cloud storage aids with easier, online access to the data. 
    - Data stored in this bucket will look as follows;
    ![Google_cloud_bucket](/images/cloud_storage.png)
* Connect and setup Mage.AI for ETL pipeline.
    - setting up a virtual machine in Google cloud engine enables the deployment of mage.AI. Creating an E2 virtual machine on the Google cloud platform is the most convenient route. Similar to the google cloud storage, this machine is setup by clicking on the 'create instance' button, after which, you can be able to set the preffered machine specifications to go with. Below is an image of a virtual machine that was used in the development of this project; 
    ![Google_cloud_engine](/images/e2%20machine.png)
    - After the creation of the E2 machine, you can then be able to access the virtual linux machine through the SSH provided. 
    - Inside the Linux environment, you will need to install mage by running **Pip install Mage-ai**
    - Following the installation, you can start Mage by running **Mage start 'Name_of_your_pipeline'**
* ETL Pipeline through Mage
    - In the previous step, you start mage on the virtual machine. However, you need to write the Extraction, transformation and Loading codes that will be automatically run whenever you start your pipeline. Mage provides a beatiful interface that allows you to visualize how your pipeline looks like. For this, you need to copy the external IP of your virtual machine instance, and add the port that mage is running on (provided when you start mage). The Mage UI will be accessible through the IP + port. Below is an example; 
    ![external_IP](/images/external%20IP%20address%20.png)
    ![mage_running_port](/images/Mage_running_port.png)
    
    In this example, the final IP address would be; http://34.125.227.122:6789/ which would give you access to your pipeline in an interactive Mage UI.
    - Once you are able to access the mage UI, you can then proceed to create your ETL pipeline by simply clickin on the **+New**. 
    - The first process under this particular project is the **Extraction** process which loads data from the Google Cloud Storage through an API link (see the above picture on the data inside the cloud storage)
    - Secondly, the **Transformation** code that transforms the data into fact tables and dimension tables. After these conversions, the data is finally stored in the form of a dictionary. Below is a diagram to demonstrate the data model developed after the transformation process;
    ![data_model](/images/Data_model.png)
    - Lastly, the transformed data is loaded into the Google Bigquery warehouse for further analysis and dashboard creation.
    - Below is the actual ETL pipeline as viewed on Mage.
    ![final_pipeline](/images/Pipeline_on_mage.png)

* Data Dictionary
    - The data that has been used in this project can further be explored through the following links; 
        1. https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
        2. https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page