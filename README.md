# veenam_technical_task
We have two simple scripts which can:
Launch a specified process and periodically (with a provided time interval) collect the following data about it:
•	CPU usage (percent);
•	Memory consumption: Working Set and Private Bytes (for Windows systems) or Resident Set Size and Virtual Memory Size (for Linux systems);
•	Number of open handles (for Windows systems) or file descriptors (for Linux systems).
Data collection should be performed all the time the process is running. Path to the executable file for the process and time interval between data collection iterations should be provided by user. Collected data should be stored on the disk. Format of stored data should support automated parsing to potentially allow, for example, drawing of charts.
For script 2 we have:
A program that synchronizes two folders: source and replica. The program should maintain a full, identical copy of destination folder at replica folder.
Requirements:
•	Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;
•	Synchronization should be performed periodically;
•	File creation/copying/removal operations should be logged to a file and to the console output;
•	Folder paths, synchronization interval and log file path should be provided using the command line arguments.

