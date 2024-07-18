# FAT Disk Type Automation Script

This script automates several tasks for FAT disk types. It is designed to analyze and gather important information about partitions within a FAT disk.

## Overview

The script performs the following tasks:

1. **Determine the Type of Each Partition**: Identifies the type of each partition present in the partition table.
2. **Determine the Starting Offset**: Calculates the starting offset for each partition's Volume Boot Record (VBR).
3. **Count the Number of Partitions**: Counts the total number of partitions found in the disk.
4. **Check the Last Partition**: Determines whether the last partition in the partition table is null or not.
5. **Determine Cluster Size**: Retrieves the cluster size used by each partition.
6. **Check Partition Activity**: Verifies whether each partition is active by examining byte number 0.

## Features

- **Automated Analysis**: Streamlines the process of analyzing FAT disk partitions.
- **Detailed Information**: Provides comprehensive details about partitions, including type, offset, and activity status.
- **Easy to Use**: Designed to be user-friendly with straightforward functionality.

## Usage

1. **Download or Clone the Repository**: Obtain the script from this repository.
2. **Run the Script**:
   - Ensure that you have the necessary permissions to execute the script.
   - Execute the script using the appropriate command for your environment.
3. **Review the Output**: The script will generate output detailing the partition information, which you can review for further analysis.

## Example Command

```bash
./your-script-name.sh
