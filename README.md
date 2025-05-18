End to End ML Project   

Steps
1. Data Ingestion
2. Data Transformation




This code is deployed on AWS ElasticBeanStak

For deploying on AWS EBS
1. it is mandatory to create application.py so that it can understand
2. Need to create a folder with .ebextensions which contains python.config file with options settings configurations
option_settings:
"aws:elasticbeanstalk:container:python":
WSGIPath:application:application
