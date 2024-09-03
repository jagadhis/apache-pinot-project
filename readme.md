**Commands used**


**- To add table to the pinot cluster** 

`docker run   --name pinot-add-table   --network=apache-pinot-project_default   -v /home/jags/projects/apache-pinot-project:/configs   apachepinot/pinot:1.1.0   AddTable   -schemaFile /configs/scripts/rawdata/electric_vehicles_schema.json   -tableConfigFile /configs/scripts/rawdata/electric_vehicles_table.json   -controllerHost pinot-controller   -controllerPort 9000   -exec`


**- To run the ingestion job**

`docker run --name pinot-ingest --network=apache-pinot-project_default -v /home/jags/projects/apache-pinot-project:/configs -it apachepinot/pinot:1.1.0 LaunchDataIngestionJob -jobSpecFile /configs/job-spec-json.yaml`


**- To just start the container and not the ingestion job**

`docker run --name pinot-ingest --network=apache-pinot-project_default -v /home/jags/projects/apache-pinot-project:/configs -it --entrypoint /bin/sh apachepinot/pinot:1.2.0`


**- To replace NaN with Null in Dataset**

`sed -i 's/NaN/null/g' Electric_Vehicle_Population_Data.json`

**-- for windows**
`(Get-Content Electric_Vehicle_Population_Data.json) -replace 'NaN', 'null' | Set-Content Electric_Vehicle_Population_Data.json`