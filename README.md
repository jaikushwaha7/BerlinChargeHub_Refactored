```
project_root/
│
├── src/
│   ├── app/
│   │   ├── create_heatmap.py          # Main application script for Streamlit (Entry point for the app)
│   │
│   ├── infrastructure/
│   │   ├── core/
│   │   │   ├── HelperTools.py          # Contains helper functions (e.g., reusable tools like performance timing)
│   │   │   ├── methods.py              # Contains logical and reusable data processing methods like merging DataFrames
│   │
│   ├── search_management/
│   │   ├── application/
│   │   │   ├── charging_station_search.py  # Implements search functionality (e.g., SearchService class)
│   │   ├── domain/                      # Folder for domain-level abstractions (if needed for future growth)
│   │
│   ├── rating_management/
│   │   ├── application/
│   │   │   ├── charging_station_rate.py   # Manages station rating functionality (e.g., ChargeStationRating class)
│   │   ├── domain/                      # Folder for domain logic related to rating (optional)
│   │
│   ├── demand_management/
│   │   ├── application/
│   │   │   ├── demand_calculator.py      # Contains DemandCalculator for calculating demand and related formulas
│   │
│   ├── visualization_helper/
│   │   ├── mapping.py                   # Functions responsible for map-specific tasks (e.g., mapping_residents, mapping_stations)
│   │
│   ├── utils/
│   │   ├── logger.py                    # Logger utilities (e.g., @logger_decorator)
│   │   ├── exceptions.py                # Custom exception classes (e.g., SearchException)
│   │   ├── database_utils.py            # Utility functions for database-related tasks (e.g., verify_user function)
│
├── tests/
│   ├── test_create_heatmap.py           # Unit tests for the main heatmap app
│   ├── test_search_management.py        # Tests for SearchService-related methods
│   ├── test_rating_management.py        # Tests for charging station rating functionality
│   ├── test_demand_management.py        # Tests for demand calculation functionality
│   ├── test_visualization_helper.py     # Tests for map-rendering functions
│   ├── test_utils.py                    # Tests for utility functions (e.g., logger, database utilities, exceptions)
│
├── data/
│   ├── population_data.csv              # Example CSV file for population data
│   ├── charging_stations_data.csv       # Example CSV file for charging stations' data
│
├── requirements.txt                     # List of Python dependencies (e.g., streamlit, pandas, folium, etc.)
├── README.md                            # Project documentation
├── .gitignore                           # Git ignored files (e.g., *.pyc, __pycache__, local data files)
```

Notes:

.idea/: Contains IDE-specific settings and configurations.

datasets/: Includes data files such as charging_stations.csv and demand_data.csv.

presentation/EventFlow_SequenceFlow/: Houses presentation materials like event_flow_diagram.png and sequence_flow_chart.pdf.

src/: Main source code directory:

- domain/: Defines core domain logic with modules like models.py, events.py, and exceptions.py.
- application/: Contains application services, e.g., services.py.
- infrastructure/: Manages data access with repositories.py.
- utils/: Utility functions, including data_loader.py.

tests/: Contains test modules such as test_station_search.py and test_demand_indicator.py.

Root Files:

README.md: Project overview and documentation.
config.py: Configuration settings.
.gitignore: Specifies files and directories for Git to ignore.
main.py: Primary executable script.
requirements.txt: Lists project dependencies.
