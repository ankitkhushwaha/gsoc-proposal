
project_name/
│── data_pipeline/        # retrieve data from archive  
│── docs/                 # Documentation files  
│── missions/             # Mission-specific functions  
│   ├── nicer/  
│   │   ├── process/         # Processing of observations  
│   │   │   ├── tests/    # Tests for processing  
│   │   │   ├── impl/     # Code for event file reduction  
│   │   ├── extract/  
│   │       ├── spec/     # Spectrum extraction  
│   │       ├── lc/       # Light-curve extraction  
│   │── Nustar/
|
│── frontend/             # GUI components  
│   ├── main_ui/          # main user interface  
│   ├── particular_obs/   # UI for individual observations  
│   ├── retrieve_data_ui/ # UI for data retrieval  
│── tests/                
│── Observation/                
│── ML_pipeline/                
│── data/                 # Sample datasets  
│── README.md             
│── setup.py              
│── requirements.txt      
│── LICENSE               
