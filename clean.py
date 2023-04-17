# Opening the disk image
file = open('FatFolder/dfr-01-fat.dd', 'rb')

# setting the value for master boot record which are the very first 512bytes
mbr = file.read(512)

# parition table is located at the  offset 446 to 509
partition_table = mbr[446:510]

# Loop through partitions (16 bytes each)
num_partitions = 0  # Counter 
for i in range(0, 64, 16): #looping fro; 0 to 64 for each partition
    # extracting one byte from each partion
    partition_entry = partition_table[i:i+16]
    # extracting what each byte inside the partition table means
    partition_type = partition_entry[4]
    boot_indicator = partition_entry[0]
    partition_size_bytes = partition_entry[8:12]
    partition_size_insectors = int.from_bytes(partition_size_bytes, byteorder='little')
    is_bootable = boot_indicator == 0x80
    # delecting partition type
    file_system = None
    if partition_type == 0x01:
        file_system = "FAT12"
    elif partition_type == 0x04 or partition_type == 0x06:
        file_system = "FAT16"
    elif partition_type == 0x0B:
        file_system = "FAT32"
    elif partition_type == 0x83:
        file_system = "ext2/ext3/ext4"
    
    # Output
    num_partitions += 1 #incrementing the counter
    partition_size_inKBS = (partition_size_insectors * 512) / 1024
    print("Partition " + str(num_partitions) + ": File System: " + str(file_system))
    print("Active: " + ("Yes" if is_bootable else "No"))
    print("Partition size is " + str(partition_size_inKBS) + " KB")
    # Output the hex value for the fourth partition to see if its empty
    if num_partitions == 4:
        print("Hex Value for Fourth Partition: " + hex(partition_type))
        
    if file_system in ["FAT12", "FAT16", "FAT32"]:
        #cluster size from mbr
        vbr = file.read(512)
        cluster_size = vbr[13]
        vbr_offset = int.from_bytes(partition_entry[8:12], byteorder='little') * 512 #calculating the offset for the vbr from the values 8 to 11 in parition table and multiplying it by sector size
        print("Cluster Size " + str(cluster_size))
        # Show the location of VBR for the partition
        print("VBR Location for " + file_system + " partition: Offset " + hex(vbr_offset))
        
# Display total number of partitions
print("Total Partitions: " + str(num_partitions))

# Close the file
file.close()
