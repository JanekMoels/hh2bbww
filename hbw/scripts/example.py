"""
An example how to run tasks via python.
"""

from columnflow.tasks.selection import SelectEvents

import awkward as ak
# awkward not in conda environment -> source sandbox before calling this file:
# source $HBW_BASE/modules/columnflow/sandboxes/venv_columnar_dev.sh

task = SelectEvents(version="v1", dataset="tt_sl_powheg", walltime="1h") #, remove_output = "3ay")
task.law_run()

outp = task.output()["collection"]
inp = task.input()
print(type(outp))
print(outp)

print(type(inp))
for key, item in inp.items():
    print(key, item)

# check outputs of task and print fields of all parquet files
for branch in outp.keys():
    for key, item in outp[branch].items():
        print("=============== Output:", key)
        if "parquet" in item.fn:
            events = ak.from_parquet(item.fn)
            print("========== Fields:", events.fields)
            for f in events.fields:
                print("=====", f"{f}:", events[f].type)


# Debugger
from IPython import embed
# embed()
