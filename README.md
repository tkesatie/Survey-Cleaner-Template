# Legacy Data Pipeline Modernization (SPSS to Python)

## 1. Project Overview
This repository demonstrates a modular framework for migrating legacy research data workflows from proprietary software (SPSS) to an open-source Python/Pandas environment. 

The primary objective was to eliminate license dependencies and improve processing efficiency for recurring annual data events while maintaining 100% data integrity.

## 2. Technical Architecture
The utility is built using a Class-based structure to ensure scalability and reusability across different survey types. 

### Key Modules:
* **Schema Standardization:** A regex-powered engine that transforms inconsistent, non-standardized survey headers into database-ready `snake_case`.
* **Data Preservation:** Implements an automated "Original State" backup upon ingestion to facilitate validation.
* **Logic Parity Validation:** A framework designed to cross-reference modernization outputs against legacy system results to ensure zero logic drift during the transition.

## 3. Business Impact
* **Cost Reduction:** Facilitated the transition away from proprietary license fees.
* **Efficiency:** Automated the "Copy-Paste" formatting phase, reducing project setup time.
* **Reliability:** Established a "Dual-Run" validation protocol to satisfy strict research audit requirements.

## 4. Usage
```python
from survey_pipeline import SurveyPipeline

# Initialize and transform
pipeline = SurveyPipeline('messy_survey_data.csv')
standardized_df = pipeline.standardize_schema()

# Validate against legacy output
is_valid = pipeline.validate_parity(legacy_spss_df)