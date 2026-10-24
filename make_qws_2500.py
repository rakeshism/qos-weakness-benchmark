"""Rebuild the 2,500-record QWS v2.0 file used in the paper from the official release.

1. Download qws2.zip from https://qwsdata.github.io/qws2.html and unzip qws2.txt.
2. Run:  python make_qws_2500.py qws2.txt qws.xls
The output is the CSV used by the notebook (header + 2,500 records).

Our copy lacked seven of the 2,507 released records: the first five data rows
and the two records whose WSDL address contains a comma. They are excluded here
so that the output matches the data analysed in the paper exactly.
"""
import sys, hashlib

HEADER = ("ResponseTime,Availability,Throughput,Successability,Reliability,"
          "Compliance,BestPractices,Latency,Documentation,ServiceName,WSDLAddress")
EXPECTED_SHA256 = "009c22498bd8fcd78af2e9fbbcee91424bd1f5a9e982ddf6ce0d2a146be767bf"

def main(src, dst):
    with open(src, encoding="latin-1") as f:
        rows = [l.rstrip("\r\n") for l in f if not l.startswith("#") and l.strip()]
    assert len(rows) == 2507, f"expected 2,507 records in the release, found {len(rows)}"
    keep = [r for i, r in enumerate(rows)
            if i >= 5                      # first five data rows were missing from our copy
            and r.count(",") == 10]        # WSDL address containing a comma (2 records)
    assert len(keep) == 2500, len(keep)
    text = HEADER + "\r\n" + "\r\n".join(keep) + "\r\n"
    with open(dst, "w", encoding="latin-1", newline="") as f:
        f.write(text)
    sha = hashlib.sha256(text.encode("latin-1")).hexdigest()
    print(f"wrote {dst}: 2,500 records; sha256 {sha}",
          "(matches the paper)" if sha == EXPECTED_SHA256 else "(CHECK: differs from the paper)")

if __name__ == "__main__":
    main(*(sys.argv[1:3] if len(sys.argv) >= 3 else ("qws2.txt", "qws.xls")))
