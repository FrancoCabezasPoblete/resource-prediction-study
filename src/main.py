import os

import pandas as pd
from icecream import ic
from utils import (
    execution_time,
    memory_and_cpu_usage,
    parse_arguments,
    pc_info,
    run_callgrind,
    syscalls,
    test_execution,
)

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


# Check if the command uses all the memory
if args.test:
    ic("Checking if the command uses all the memory.")
    if not test_execution(args.command):
        exit()

ic(f"Running command: {args.command}")

# Get the PC information
specs = pc_info()

if args.sys:
    stdout, stderr = syscalls(
        args.command,
        os.path.join("/results", specs["arch"], f"strace_{args.benchmark}.txt"),
    )
    print_std(stdout, stderr)

if args.val:
    run_callgrind(
        args.command,
        os.path.join("/results", "callgrind", f"{args.benchmark}_call.out"),
    )
    # run_massif(args.command, os.path.join("/results", f"{args.benchmark}_mass.out"))

exec_times = execution_time(args.command, 5)
columns = ["total_time", "total_cpu_usage", "max_ram_usage"]
exec_times = [record.strip().split(", ") for record in exec_times]
exec_times = pd.DataFrame(exec_times, columns=columns)

max_time = exec_times["total_time"].astype(float).max()

time_records, cpu_records, memory_records, stdout, stderr = memory_and_cpu_usage(
    args.command, max_time * 1.2
)
if memory_records:
    # from dicts
    memory_df = pd.DataFrame(memory_records)
    memory_df["time"] = time_records
    memory_df = add_benchmark_and_pc_info(memory_df, args.benchmark, specs)
    if os.path.exists(os.path.join("/results", "memory_usage.csv")):
        memory_df.to_csv(
            os.path.join("/results", "memory_usage.csv"),
            mode="a",
            header=False,
            index=False,
        )
    else:
        memory_df.to_csv(os.path.join("/results", "memory_usage.csv"), index=False)
if cpu_records:
    # from dicts
    cpu_df = pd.DataFrame(cpu_records)
    cpu_df["time"] = time_records
    cpu_df = add_benchmark_and_pc_info(cpu_df, args.benchmark, specs)
    if os.path.exists(os.path.join("/results", "cpu_usage.csv")):
        cpu_df.to_csv(
            os.path.join("/results", "cpu_usage.csv"),
            mode="a",
            header=False,
            index=False,
        )
    else:
        cpu_df.to_csv(os.path.join("/results", "cpu_usage.csv"), index=False)
print_std(stdout, stderr)

exec_times = add_benchmark_and_pc_info(exec_times, args.benchmark, specs)
# Append to csv if exists
if os.path.exists(os.path.join("/results", "execution_time.csv")):
    exec_times.to_csv(
        os.path.join("/results", "execution_time.csv"),
        mode="a",
        header=False,
        index=False,
    )
else:
    exec_times.to_csv(os.path.join("/results", "execution_time.csv"), index=False)
