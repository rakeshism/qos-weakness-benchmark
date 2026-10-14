# Data

The QWS v2.0 dataset is not redistributed in this repository.

Source: E. Al-Masri and Q. H. Mahmoud, "QoS-based discovery and ranking of web services", Proc. 16th International Conference on Computer Communications and Networks (ICCCN), 2007, pp. 529-534.

Save the file as `data/qws.csv`. It is a comma-separated text file with 2,500 rows and these columns:

ResponseTime, Availability, Throughput, Successability, Reliability, Compliance, BestPractices, Latency, Documentation, ServiceName, WSDLAddress

The notebook adds a `ServiceID` column from the row index. Each record is treated as a separate service. There are 2,377 unique WSDL addresses, and 123 addresses appear twice.
