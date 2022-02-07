import shutil
import os
import subprocess
from glob import glob
import datetime

inputs_path = '/data/inputs'
outputs_path = '/data/outputs/'

os.chdir(inputs_path)

subprocess.call('/src/HBV.exe')

shutil.copytree(glob(os.path.join(inputs_path, 'Output*'))[0], outputs_path, dirs_exist_ok=True)

title = os.getenv('TITLE', 'HBV-UK output')
description = ' '
geojson = {}

metadata = f"""{{
  "@context": ["metadata-v1"],
  "@type": "dcat:Dataset",
  "dct:language": "en",
  "dct:title": "{title}",
  "dct:description": "{description}",
  "dcat:keyword": [
    "hbv"
  ],
  "dct:subject": "Environment",
  "dct:license": {{
    "@type": "LicenseDocument",
    "@id": "https://creativecommons.org/licences/by/4.0/",
    "rdfs:label": null
  }},
  "dct:creator": [{{"@type": "foaf:Organization"}}],
  "dcat:contactPoint": {{
    "@type": "vcard:Organization",
    "vcard:fn": "DAFNI",
    "vcard:hasEmail": "support@dafni.ac.uk"
  }},
  "dct:created": "{datetime.datetime.now().isoformat()}Z",
  "dct:PeriodOfTime": {{
    "type": "dct:PeriodOfTime",
    "time:hasBeginning": null,
    "time:hasEnd": null
  }},
  "dafni_version_note": "created",
  "dct:spatial": {{
    "@type": "dct:Location",
    "rdfs:label": null
  }},
  "geojson": {geojson}
}}
"""
with open(os.path.join(outputs_path, 'metadata.json'), 'w') as f:
    f.write(metadata)

