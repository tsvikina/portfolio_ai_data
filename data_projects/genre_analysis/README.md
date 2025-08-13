# Cross-Country Analysis of Music Genre Preferences & Profitability
**SQL Project using the Chinook Database**

This project explores commercial music trends across countries, using SQL queries to identify the most purchased and highest-grossing music genres. The analysis helps businesses optimize catalog development and tailor marketing strategies to regional preferences.

## Objectives
- Identify top-selling genres per country.
- Compare revenue contributions of genres across countries.
- Understand genre popularity versus profitability.
- Highlight high-value customers and spending patterns.

## Skills Used
- SQL JOINs and GROUP BY
- Aggregate filtering (HAVING)
- Window functions
- Data summarization
- Data visualization with bar charts, pie charts, and scatter plots

---

## Key Visualizations & Business Insights

### 1. Top Purchased Genre per Country *(Bar Plot)*
Shows the top-selling genre per country based on purchase counts.

**Business Insight:** Align genre promotions with dominant regional preferences.

---

### 2. Revenue Share by Genre Within Country *(Interactive Pie Chart)*
Highlights the share of total revenue per genre within each country.

**Business Insight:** Reveals premium-priced genres and helps inform pricing and bundling strategies.

---

### 3. Purchase Distribution per Genre Across Countries *(Interactive Bar Plot)*
Shows which countries contribute most to a genre’s purchases.

**Business Insight:** Supports region-specific genre marketing and licensing decisions.

---

### 4. Popularity vs. Profitability of Genres *(Scatter Plot with Bubble Size)*
Plots genre popularity (purchases) against revenue, with bubble size representing average revenue per purchase.

**Business Insight:** Guides catalog strategy — which genres to invest in, promote, or phase out.

---

## Bonus Analysis: Top Customers by Spending

### Objective
Identify high-value customers who spend significantly more than average.

- Used `SUM()`, `GROUP BY`, and `HAVING` to filter customers by total purchases.
- Compared individual customer totals to the average across all customers.
- Visualized top 20 customers with a red line showing average total purchases.

**Business Insight:** Useful for loyalty, referral, or VIP targeting programs.

---

## Dataset
The [Chinook Database](https://github.com/lerocha/chinook-database) — a sample database representing a digital media store, with tables for customers, invoices, tracks, albums, genres, and more.

---

## Future Improvements
- Automate data extraction and dashboard creation using Python or Power BI.
- Extend analysis to include time-based trends (seasonal or yearly).
- Create recommendation logic for bundling genres by region.

---

## Contact
**Author:** Teodora Tsvikina  
izpyten@yahoo.com

