# Day 1: Project Alignment & Architecture Planning

## Overview
This folder contains the alignment activities, dataset verification, and initial application architecture planning for the Customer Segmentation Streamlit dashboard. On Day 1, previous outputs from model development (Module 6) and business insights (Module 8) were reviewed to design a deployment-ready web application.

## Key Files
| File Name | File Type | Description |
| :--- | :--- | :--- |
| [proj.ipynb](file:///D:/Machine%20Learning/Machine%20Learning/Internship/Day%201/proj.ipynb) | Jupyter Notebook | Notebook containing checks for model assets, feature list identification, and planning out the Streamlit dashboard structure. |
| [Final Dataset.csv](file:///D:/Machine%20Learning/Machine%20Learning/Internship/Day%201/Final%20Dataset.csv) | CSV Dataset | The final client customer dataset including engineered features ready for visualization and predictive segmentation. |
| [Deployment_Readiness_App_Design_Report.pdf](file:///D:/Machine%20Learning/Machine%20Learning/Internship/Day%201/Deployment_Readiness_App_Design_Report.pdf) | PDF Document | Technical report detailing the app design specification, page navigation, widgets, and layout. |
| [AI_Lab_99_Deployment_Readiness_Poster.pdf](file:///D:/Machine%20Learning/Machine%20Learning/Internship/Day%201/AI_Lab_99_Deployment_Readiness_Poster.pdf) | PDF Document | Visual poster showcasing the design framework and deployment readiness of the system. |

## Activities & Processes
1. **Review of Past Project Artifacts**: Analyzed model files (`kmeans_model.pkl`, `standard_scaler.pkl`) and features list from Module 6, as well as the segments and marketing findings from Module 8.
2. **Feature Mapping & Selection**: Identified the 10 core features required by the K-Means clustering algorithm for deployment: `Income`, `Total_spending`, `Recency`, `Customer_Tenure`, `Family_size`, `Total_Children`, `Total_Campaign`, `NumWebPurchases`, `NumStorePurchases`, and `NumCatalogPurchases`.
3. **Cluster Labeling Mapping**: Established business labels for the segments:
   - **Cluster 0** $\rightarrow$ **High-Value Elite** (High Income, High Spending, Smaller Family, Offline Purchases)
   - **Cluster 1** $\rightarrow$ **Value/Frugal Buyers** (Lower Income, Low Spending, Larger Family, Web & Discount Purchases)
4. **App Architecture Blueprinting**: Designed the multi-page structure for the Streamlit dashboard (Home, Dashboard, Segments, Search, Prediction, Visualizations, Marketing, and Download).
