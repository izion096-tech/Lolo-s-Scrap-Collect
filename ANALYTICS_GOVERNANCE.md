# Analytics governance

## Useful operational analytics
- Kilograms and load count by day, source channel, route, material family and grade.
- Estimated purchase spend; add verified resale and processing costs before calculating actual margin.
- Buyer price history, contamination deductions, stock ageing, dispatch reconciliation and grade yield.
- Supplier cadence, repeat supply, average lot size and channel trends using internal references where possible.
- Review queue with an objective reason, reviewer, decision, evidence reference and timestamp.

## Avoid
- Secret or opaque personal risk scores, facial recognition, social graph inference or automated accusations.
- Automatically denying trade or blacklisting people based on a model score.
- Collecting identity data that is not necessary for a lawful purpose.
- Treating a missing field as evidence of wrongdoing.

## Production controls
Use role-based access, least privilege, MFA, retention limits, access logs, tamper-evident audit events, encryption, data-subject request processes, a documented legal basis, and an incident response plan. Review analytics for bias and false positives. Every alert needs an owner and disposition.
