# Vendor Performance Analysis

## Overview
End-to-end data analysis project using Python, SQL, and Tableau to evaluate vendor performance.

## Objectives
- Identify top-performing vendors  
- Detect low-performing vendors  
- Analyze the impact of profit and freight cost

## Tools Used
- Python (Pandas)
- SQL
- Jupyter Notebook
- Tableau


**Correlation Heatmap**

This heatmap highlights relationships between key variables such as purchase price, sales quantity, profit margin, and stock turnover. Strong correlations indicate operational efficiency, while weak or negative correlations reveal areas where pricing and profitability are not aligned.

![Correlation Heatmap](images/correlation_Heatmap.png)

Purchase Price vs. Total Sales Dollars & Gross Profit  
Weak correlation (-0.012 and -0.016), indicating that price variations do not significantly impact sales revenue or profit.  

Total Purchase Quantity vs. Total Sales Quantity  
Strong correlation (0.999), confirming that inventory purchased is almost directly converted into sales, indicating efficient demand fulfillment and minimal overstocking.  

Profit Margin vs. Total Sales Price  
Negative correlation (-0.179), suggesting that higher selling prices are not translating into better margins, likely due to increased costs or competitive pricing pressures.  

Stock Turnover vs. Gross Profit & Profit Margin  
Weak negative correlation (-0.038 & -0.055), indicating that faster inventory movement does not guarantee higher profitability, implying inefficiencies in cost control or pricing strategy.  




**Vendor Contribution Pie Chart**

This chart shows how total sales are distributed across vendors. A significant portion is concentrated among a few top vendors, while the majority fall under "Other Vendors," indicating a highly skewed dependency on key contributors.

![Vendor Contribution](images/vendor_contribution.png)

The top vendor group contributes approximately 34–35% of total sales alone, while the remaining vendors individually contribute much smaller shares (mostly below 10%). This highlights a concentration risk, where business performance is heavily reliant on a limited number of vendors, making the supply chain vulnerable to disruptions from these key contributors.


**Profit vs Sales Analysis**

This scatter plot visualizes the relationship between total sales and profit margin. Vendors highlighted in red represent high-margin targets, while the distribution of blue points shows varying performance levels, helping identify candidates for pricing or promotional strategies.

![Profit vs Sales](images/profit_vs_sales.png)

A cluster of vendors with very low sales but high profit margins (highlighted in red) indicates underutilized high-margin opportunities. Meanwhile, a large number of vendors generate moderate to high sales but operate within lower profit margin ranges (20–40%), suggesting that revenue is not being efficiently converted into profit. This reveals an opportunity to either scale high-margin vendors or improve cost efficiency among high-sales vendors. 

## Key Business Insights
- Top 10 vendors contribute a significant percentage of total sales, indicating heavy dependency on a small group of vendors.
- Several vendors generate high revenue but have low profit margins due to high freight costs and operational expenses.
- Freight cost has a noticeable negative impact on profitability for certain vendors, reducing overall margins.
- A group of vendors shows consistently low sales and profit, indicating potential inefficiencies or underperformance.
- Profit margins vary significantly across vendors, suggesting inconsistent pricing or cost management strategies.
- Some vendors maintain balanced performance with both high sales and strong profit margins, making them ideal for long-term partnerships.
- Data analysis revealed opportunities to optimize vendor selection by focusing on high-margin and low-cost vendors.
- Outlier vendors with unusually high costs or low returns were identified, which may require further investigation.
