# Data Dictionary

This document describes the columns used in the sales dataset.

| Column | Description |
|---|---|
| Date | Date on which the sales transaction occurred |
| Customer | Name or identifier of the customer |
| Product | Name of the product sold |
| City | City where the sale occurred |
| Quantity | Number of units sold |
| Price | Selling price per unit |
| Cost | Cost per unit of the product |

## Derived Metrics

The following metrics can be calculated from the available columns:

- **Sales** = Quantity × Price
- **Total Cost** = Quantity × Cost
- **Profit** = Sales − Total Cost
