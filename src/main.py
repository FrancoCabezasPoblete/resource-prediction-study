from icecream import ic
from utils import (
    parse_arguments,
    syscalls,
    memory_usage,
    cpu_usage,
    execution_time
)
import csv
import os

args = parse_arguments()

if not os.path.exists(args.directory):
    os.makedirs(args.directory)

def print_std(stdout, stderr):
    if stdout:
        ic(f"STDOUT: {stdout}")
    if stderr:
        ic(f"STDERR: {stderr}")

ic(f"Running command: {args.command}")

stdout, stderr = syscalls(args.command, os.path.join(args.directory, "strace.txt"))
print_std(stdout, stderr)

memory_records, stdout, stderr = memory_usage(args.command)
# Write the memory records to a file
if memory_records:
    with open(os.path.join(args.directory, "memory_usage.csv"), "w", newline='') as f:
        fields = memory_records[0].keys()
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for record in memory_records:
            writer.writerow(record)
print_std(stdout, stderr)

cpu_records, stdout, stderr = cpu_usage(args.command)
# Write the CPU records to a file
if cpu_records:
    with open(os.path.join(args.directory, "cpu_usage.csv"), "w", newline='') as f:
        fields = cpu_records[0].keys()
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for record in cpu_records:
            writer.writerow(record)
print_std(stdout, stderr)

exec_time, stdout, stderr = execution_time(args.command, 10)
# Write the execution times to a file
with open(os.path.join(args.directory, "execution_time.csv"), "w") as f:
    f.write("execution_time\n")
    for record in exec_time:
        f.write(f"{record}\n")
print_std(stdout, stderr)
