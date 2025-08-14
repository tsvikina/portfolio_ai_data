# Power BI Projects

This repository showcases interactive Power BI dashboards that explore diverse datasets through visual storytelling and data analysis.

## Projects

### 1. HR Dashboard

A Power BI dashboard tailored for the Human Resources department to monitor hiring quality, work anniversaries, and workforce trends.

**Features:**
- Monthly analysis of new employees with breakdowns by gender and employment type
- Hired/Fired status per year, region, gender, and age group
- Bad hire detection (<60 days)
- Anniversary tracking (40-year milestone)

**Dataset:** 
An anonymized multi-page employee dataset visualized in Power BI.

[date.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/38fe7a67-e318-4ff1-bbf5-f42e2cc7a44c/nl/1/date.csv)

[employee.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/38fe7a67-e318-4ff1-bbf5-f42e2cc7a44c/nl/1/employee.csv)

[manager.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/38fe7a67-e318-4ff1-bbf5-f42e2cc7a44c/nl/1/manager.csv)

---

### 2. IT Salary Dashboard

This Power BI dashboard explores salary data from individuals working in the IT sector. It provides interactive visuals and insights based on factors such as gender, company, years of experience, and job role.

**Features:**

- Filter buttons to quickly select groups such as "All Managers" or "All Engineers"
- Dynamic metrics showing:
  - Total number of people selected
  - Maximum salary in the selection
  - Maximum bonus in the selection
- Comparisons by:
  - Gender
  - Company
  - Job title
  - Years of experience

**Dataset:** The dataset was sourced from a public CSV file:  
[salaries_powerbi.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/8fd0ba12-2e1a-446f-9a73-4f3ee7a97081/nl/1/salaries_powerbi.csv)

---

### 3. Sales Performance Dashboard

An interactive sales dashboard built with Power BI. The dashboard provides insights into sales trends, item performance, store performance, and seasonal patterns based on historical sales data.

**Features:**
- Time-based sales trends
- Top-performing items and categories
- Store-level performance comparison
- Monthly and seasonal breakdown

**Dataset:** 
The analysis is based on a multi-table dataset (star schema).

[district.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/district.csv) 

[item.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/item.csv) 

[sales.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/sales.csv) 

[store.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/store.csv) 

[time.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/time.csv)

---

### 4. Interactive Map of the Netherlands

This dashboard presents a geographic analysis of the Netherlands, highlighting two key indicators by municipality: population density and percentage of surface area covered by water.

**Features:**

- Interactive map with municipalities colored by population density
- Filters for selecting specific provinces or regions
- Tooltip details showing population, area, and water percentage per municipality
- Toggle between key metrics for comparative analysis


**Dataset:** The dataset was sourced from a public CSV file:  
[nederland.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/ec8a5143-e58d-43db-9ea4-2e6f50fe406c/nl/1/nederland.csv)

---

