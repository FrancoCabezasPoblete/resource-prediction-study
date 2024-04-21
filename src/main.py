from utils import (
    parse_arguments,
    run_with_strace,
    run_and_monitor_memory,
    run_and_monitor_cpu
)
import os

args = parse_arguments()

if not os.path.exists(args.directory):
    os.makedirs(args.directory)

stdout, stderr = run_with_strace(args.command, os.path.join(args.directory, "strace.txt"))
print(f"STDOUT: {stdout}")
print(f"STDERR: {stderr}")

memory_info, stdout, stderr = run_and_monitor_memory(args.command)
print(f"Memory Info: {memory_info}")
print(f"STDOUT: {stdout}")
print(f"STDERR: {stderr}")

cpu_times, execution_time, stdout, stderr = run_and_monitor_cpu(args.command)

print(f"CPU Times: {cpu_times}")
print(f"Execution Time: {execution_time}")
print(f"STDOUT: {stdout}")
print(f"STDERR: {stderr}")