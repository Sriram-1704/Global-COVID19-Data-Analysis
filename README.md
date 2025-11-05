# 🌍 Global COVID-19 Data Analysis using Python and Power BI

### 📊 Overview
This project demonstrates an **end-to-end data analysis workflow** using real-world COVID-19 data.  
The goal is to clean, analyze, and visualize the datasets to uncover trends and insights on the global pandemic using **Python (Pandas)** and **Power BI**.

---

## 🧰 Tools & Technologies
- **Python** → Data cleaning and preprocessing  
- **Pandas, NumPy** → Data manipulation and feature creation  
- **Power BI** → Data visualization and interactive dashboard building  
- **Excel** → Quick data validation and checks  

---

## 📂 Project Structure
Global-COVID19-Data-Analysis/
│
├── covid_data_cleaning.py # Python script used for cleaning and preprocessing
├── Global_COVID19_Dashboard.pbix # Final Power BI dashboard
│
├── Health Related Datasets/
│ ├── Raw Datasets/ # Raw Kaggle datasets
│ │ ├── country_wise_latest.csv
│ │ ├── day_wise.csv
│ │ ├── worldometer_data.csv
│ │
│ └── Cleaned Datasets/ # Cleaned data generated via Python script
│ ├── country_cleaned.csv
│ ├── day_cleaned.csv
│ ├── worldometer_cleaned.csv

---

## ⚙️ Data Cleaning Workflow
Performed in **`covid_data_cleaning.py`** using Pandas:
1. Loaded raw Kaggle datasets  
2. Dropped missing or inconsistent values  
3. Renamed columns for uniformity  
4. Created calculated columns:
   - `recovery_rate = (recovered / confirmed) * 100`
   - `death_rate = (deaths / confirmed) * 100`
5. Exported the cleaned datasets into a new folder for visualization  

---

## 📊 Power BI Dashboard Overview
Built a Power BI report (`Global_COVID19_Dashboard.pbix`) with three interactive pages:

1. **Daily Trends** – Line chart of confirmed, deaths, and recoveries over time  
2. **Country Comparison** – Top 10 countries and a world map visualization  
3. **Global Summary** – KPI cards, bar & pie charts, and key insights  

---

## 💡 Insights
- The USA and Brazil reported the highest total confirmed cases  
- Global average recovery rate is around **47%**  
- Death rate declined steadily post-2021 due to improved healthcare and vaccinations  
- Power BI dashboards provide a clear, interactive understanding of the pandemic trends  

---

## 🧑‍💻 Author
**Sri Ram**  
_Data Analyst | Python | Power BI | SQL_  
📧 [sriramsattiraju2003@gmail.com]  
🔗 [https://www.linkedin.com/in/sri-ram-sattiraju-028349211]

---

