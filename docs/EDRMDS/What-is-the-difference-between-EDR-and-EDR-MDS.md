# What is the difference between EDR and EDR-MDS

The main difference between EDR and EDR-MDS is the master data aspect. EDR is the obvious choice for data-sources which you have no way of mastering, i.e. 3rd party Business Object sources.

EDR-MDS add the following

- Field and value based mastering (with write-back to all sources)
- Internal *persistance* (via the EDR-MDS backbone)
- Bulk-data dump
- History
  - delayed writeback-queues for handling off-line sources
  - full resynk of sources
  - Object history change and audit log
