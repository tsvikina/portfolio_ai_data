# Sales Performance Dashboard

This Power BI dashboard provides a comparative analysis of product category sales across multiple cities. The report is based on joined datasets including sales, city, and district information.

## Key Features

- **Sales breakdown by product category**: Visualized per city, enabling quick performance comparison.
- **Interactive filtering**:
  - Filter by sales **Period**.
  - Filter by **District** (e.g., FD-01, LI-02).
- **Insights by category**:
  - Track top-performing product lines (e.g., Home, Womens, Shoes).
  - Identify cities with the highest category sales.

## Visuals

- **Clustered Bar Chart**: Displays total sales by city, segmented by product category.
- **Slicers**: Allow users to dynamically filter the dashboard by time period and district.

## Tools Used

- **Power BI Desktop**
- Data Preparation: Dataset joins and transformations performed in Power BI
- **CSV files** 
The analysis is based on a multi-table dataset (star schema).

[district.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/district.csv) 
[item.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/item.csv) 
[sales.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/sales.csv) 
[store.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/store.csv) 
[time.csv](https://prod-jarvis-public.s3.eu-west-1.amazonaws.com/3b69a5ce-4e3a-400e-b48e-f31ac386d2bb/nl/1/time.csv)

## Screenshot

![Sales Analysis Dashboard](./sales_analysis.png)

---

This project helps regional sales and inventory teams monitor product category performance and target underperforming cities or periods with promotions and stock adjustments.
