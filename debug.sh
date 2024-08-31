#!/bin/bash
echo "Listing /opt/pinot/data:"
ls -l /opt/pinot/data
echo "Content of job-spec-json.yaml:"
cat /opt/pinot/data/job-spec-json.yaml
echo "Attempting to read schema file:"
cat /opt/pinot/data/electric_vehicles_schema.json