import hashlib, json, subprocess, urllib.request

local_blob = subprocess.check_output(
    ["git", "rev-parse", "HEAD:pandas/sales_analysis.ipynb"], text=True
).strip()

url = "https://raw.githubusercontent.com/polymathicneo/ML-Foundations/main/pandas/sales_analysis.ipynb"
raw = urllib.request.urlopen(url, timeout=60).read()
remote_blob = hashlib.sha1(b"blob %d\0" % len(raw) + raw).hexdigest()

nb = json.loads(raw)
print("local  git blob:", local_blob)
print("remote git blob:", remote_blob)
print("match:", local_blob == remote_blob)
print("valid notebook JSON: nbformat", nb["nbformat"], nb["nbformat_minor"])
print("cells:", len(nb["cells"]), "| executed:", sum(1 for c in nb["cells"] if c["cell_type"] == "code" and c["execution_count"]))
print("bytes on GitHub:", len(raw))
