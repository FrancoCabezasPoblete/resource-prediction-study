from icecream import ic
from utils import (
    parse_arguments,
    syscalls,
    #memory_and_cpu_usage,
    execution_time,
    pc_info
)
import os
import pandas as pd

args = parse_arguments()

def print_std(stdout, stderr):
    if stdout:
        ic(f"STDOUT: {stdout}")
    if stderr:
        ic(f"STDERR: {stderr}")

def add_benchmark_and_pc_info(df, benchmark, pc_info):
    # Add the PC information
    for key, value in pc_info.items():
        df[key] = value
    # Add the benchmark name
    df["benchmark"] = benchmark
    return df

ic(f"Running command: {args.command}")

# Get the PC information
specs = pc_info()

if not os.path.exists("results"):
    os.makedirs("results")

if not os.path.exists(os.path.join("results",specs['arch'])):
    os.makedirs(os.path.join("results",specs['arch']))

stdout, stderr = syscalls(args.command, os.path.join("results",specs['arch'],f"strace_{args.benchmark}.txt"))
print_std(stdout, stderr)

# cpu_records, memory_records, stdout, stderr = memory_and_cpu_usage(args.command)
# if memory_records:
#     memory_df = pd.DataFrame(memory_records)
#     # Get Max, Min, Mean, and Std of the memory usage of each column
#     memory_df = memory_df.describe().T
#     memory_df = add_benchmark_and_pc_info(memory_df, args.benchmark, specs)
#     if os.path.exists(os.path.join("results", "execution_time.csv")):
#         memory_df.to_csv(os.path.join("results", "memory_usage.csv"), mode='a', header=False, index=False)
#     else:
#         memory_df.to_csv(os.path.join("results", "memory_usage.csv"), index=False)
# if cpu_records:
#     cpu_df = pd.DataFrame(cpu_records)
#     # Get Max, Min, Mean, and Std of the CPU usage of each column
#     cpu_df = cpu_df.describe().T
#     cpu_df = add_benchmark_and_pc_info(cpu_df, args.benchmark, specs)
#     if os.path.exists(os.path.join("results", "execution_time.csv")):
#         cpu_df.to_csv(os.path.join("results", "cpu_usage.csv"), mode='a', header=False, index=False)
#     else:
#         cpu_df.to_csv(os.path.join("results", "cpu_usage.csv"), index=False)
# print_std(stdout, stderr)

exec_times = execution_time(args.command, 5)
columns = ["total_time", "total_cpu_usage", "total_memory_usage", "max_ram_usage", "swaps"]
exec_times = [record.strip().split(", ") for record in exec_times]
exec_times = pd.DataFrame(exec_times, columns=columns)

exec_times = add_benchmark_and_pc_info(exec_times, args.benchmark, specs)
# Append to csv if exists 
if os.path.exists(os.path.join("results", "execution_time.csv")):
    exec_times.to_csv(os.path.join("results", "execution_time.csv"), mode='a', header=False, index=False)
else:
    exec_times.to_csv(os.path.join("results", "execution_time.csv"), index=False)