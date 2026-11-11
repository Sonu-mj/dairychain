# Energy and Operational Analysis


## Purpose
It is for a reader who needs the method without an invented reading.

## In this file
- How much energy is consumed, and how does it change over time?
- Are unusual readings recorded?

## Business question
How much energy is consumed, and how does it change over time?

## Business context
Energy affects dairy processing and storage costs. A trend can show whether consumption follows production, or rises on its own.

## Data required
No sensor readings, energy measurements, equipment names or consumption totals were named in the README. No energy Gold table is listed.

## Analytical approach
When energy data exists: sum consumption by day and by operation or equipment, compare it with production volume for the same period, and flag days that break the pattern. Do not claim predictive maintenance unless it is implemented.

## KPI definitions
Energy per unit of output equals energy consumed divided by finished output in the same period, with the unit stated.


## Direct answer
No energy total, trend or comparison can be given for DairyChain.

## Business interpretation
The two sources differ here, and the README scope is followed.

## Recommendation
Supply energy and sensor records with date, operation or equipment, consumption and unit.

## Business impact
Measured impact: none. Expected benefit: an energy trend would show where consumption is high relative to output.


## Business question
Are unusual readings recorded, and which operations have higher consumption?

## Business context
An unusual reading can be a fault, a data error or a real change in operations. The three need different actions, so the first step is to separate them.


## Analytical approach
Flag readings outside the expected range, check whether the reading is a data error or a real event, and compare consumption by operation only where the operation is identified in the data.

## KPI definitions
No KPI is calculated without the readings and their units.


## Direct answer
No unusual reading can be reported for DairyChain.

## Business interpretation
Do not invent a sensor reading or a high-consumption operation. The method is kept, the answer is left open.

## Recommendation
Supply sensor and energy records with the checks used to flag unusual values.

## Business impact
Measured impact: none. Expected benefit: flagged readings would direct maintenance or data checks.


## Next step / Related files
- Anomaly findings](12_anomaly_and_irregularity_findings.md)
- Production analysis](../04_Business_Analytics/production_analysis.md)
- Data dictionary](../02_System_Architecture/data_dictionary.md)
