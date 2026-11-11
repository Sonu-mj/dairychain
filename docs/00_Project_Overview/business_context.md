# Business Context


## Purpose
This file answers why a dairy business needs DairyChain and how milk moves from supplier to sale. It is for a reader who needs the business workflow before the technical design.

## In this file
- The dairy workflow
- Why separate stages hide losses
- The four areas in business terms
- Who uses the analysis

## The dairy workflow
A dairy business moves milk through connected stages: suppliers, milk procurement, collection centres, quality inspection and acceptance, production batches, raw material consumption, packaging, inventory storage, distribution and sales, then returns and wastage. A problem in one stage shows up as a cost or a loss in a later stage, so the stages must be analysed together.

## Why separate stages hide losses
If procurement is read alone, a low price can look good even when rejection is high. If sales are read alone, high revenue can hide poor fulfilment. If production is read alone, high output can hide a low yield. DairyChain joins the stages so a reader can ask where value is lost, not only where revenue is made.

## The four areas in business terms
- Procurement decides how much milk arrives, from whom, and at what cost.
- Quality decides how much of that milk can be used, and why the rest is rejected.
- Production decides how much finished product comes from the milk that was accepted.
- Sales decides how much of that product reaches customers, is delivered in full, and turns into revenue.

## Who uses the analysis
The intended users are dairy managers and analysts who need supplier, centre, batch, product and daily views. The Gold layer in [../03_Data_Engineering/bronze_silver_gold_layers.md](../03_Data_Engineering/bronze_silver_gold_layers.md) is built for those views: batch, supplier, centre, product and daily.

## Next step / Related files
- Project summary](project_summary.md)
- Objectives and scope](objectives_and_scope.md)
- System architecture](../02_System_Architecture/system_architecture.md)
