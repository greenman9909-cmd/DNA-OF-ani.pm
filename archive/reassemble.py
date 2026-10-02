#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib

root = Path(__file__).resolve().parent
parts = root / "core"
encoded = "".join((parts / f"chunk-{i:03d}.b64").read_text().strip() for i in range(4))
data = base64.b64decode(encoded)
out = root / "ani-core.zip"
out.write_bytes(data)
print("Wrote:", out)
print("SHA256:", hashlib.sha256(data).hexdigest())
