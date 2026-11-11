# Outlet Analysis


## Purpose
This file lists the Gold tables DairyChain uses for sales analysis. It is for a reader who must not import an outlet count or an outlet ranking from another project.

## In this file
- Question
- Why it matters
- Data used
- Method
- Result
- What it means
- What to do next

## Question
Which outlets generate the most revenue and profit, and which outlets need management attention?

## Why it matters
An outlet can have high sales and low profit if rent, salaries, wastage and returns are high. Outlet profit needs revenue, COGS, returns, wastage and operating expenses at outlet level.

## Data used
The Gold tables are batch, supplier, centre, product and daily.

## Method
When outlet data exists, the method is: revenue minus returns, minus COGS, minus outlet operating expenses, at outlet level, then margin by outlet. Do not assume a fixed number of outlets. Confirm the count from the records first.

## Result
No outlet result is reported.

## What it means
DairyChain must not borrow outlet details from RetailIQ or any other project.

## What to do next
Supply outlet records, if outlets are part of the project, with revenue, COGS, returns, wastage, rent, salaries and other operating costs per outlet. Then calculate outlet profit and margin, and add the outputs here.

## Next step / Related files
- Q and A outlets](../05_Business_Questions_and_Answers/03_outlet_performance.md)
- Expense analysis](expense_analysis.md)
- Data dictionary](../02_System_Architecture/data_dictionary.md)
