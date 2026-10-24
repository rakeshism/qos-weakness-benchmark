# Data

The QWS v2.0 dataset is not redistributed in this repository: its license does not allow redistribution.

Source: E. Al-Masri and Q. H. Mahmoud, "QoS-based discovery and ranking of web services", Proc. 16th International Conference on Computer Communications and Networks (ICCCN), 2007, pp. 529-534. Download: https://qwsdata.github.io/qws2.html

## Rebuilding the file used in the paper

1. Download `qws2.zip` and unzip `qws2.txt` into the repository folder.
2. Run `python make_qws_2500.py qws2.txt qws.xls`.

The output `qws.xls` is a comma-separated text file with 2,500 rows and these columns:

ResponseTime, Availability, Throughput, Successability, Reliability, Compliance, BestPractices, Latency, Documentation, ServiceName, WSDLAddress

The script checks the SHA-256 fingerprint of the output against the file analysed in the paper.

## Why 2,500 and not 2,507 records

Our copy lacked seven of the 2,507 released records: the first five data rows and the two records whose WSDL address contains a comma. They were lost in conversion to CSV, not removed by any criterion, and the script excludes the same seven records. Repeating the main benchmark on all 2,507 records gives the same detection rates (Section 3.1 of the paper).

The notebook adds a `ServiceID` column from the row index. Each record is treated as a separate service. There are 2,377 unique WSDL addresses, and 123 addresses appear twice.
