# **Log Parsing Project**

## **Overview**
This project involves creating a Python script that reads, parses, and processes log data from standard input (`stdin`). The script is designed to handle logs in a specific format, calculate relevant metrics, and output these metrics after processing a batch of lines or upon receiving a keyboard interrupt (Ctrl+C).

## **Features**
- **Real-time log processing**: Reads log lines from `stdin` and processes them in real-time.
- **Metric Calculation**: Computes and displays the total file size and counts of specific HTTP status codes.
- **Signal Handling**: Gracefully handles keyboard interruptions to print the metrics before exiting.
- **Efficient Parsing**: Utilizes regular expressions to validate and parse log entries efficiently.
- **Performance-Oriented**: Outputs statistics after every 10 lines, ensuring timely updates even with large data streams.

## **Usage**
### **Input Format**
The script expects log entries in the following format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
- **IP Address**: IPv4 address of the client.
- **Date**: Date and time when the request was made.
- **Request**: HTTP method and resource requested (in this project, it's fixed as `GET /projects/260 HTTP/1.1`).
- **Status code**: HTTP status code returned by the server (e.g., 200, 301, 404).
- **File size**: Size of the file returned (in bytes).

### **Example of a Valid Log Entry**
```
123.123.123.123 - [01/Jan/2022:00:00:00 +0000] "GET /projects/260 HTTP/1.1" 200 1024
```

### **Execution**
To run the script, you can use the following command:
```bash
./0-generator.py | ./0-stats.py
```
Here, `0-generator.py` is a log generator script, and `0-stats.py` is the log parsing script. The log generator simulates log entries being written to `stdin`, which are then processed by `0-stats.py`.

### **Script Behavior**
- The script reads each line from `stdin`, parses it, and updates the relevant metrics.
- After every 10 lines, the script outputs:
  - **Total file size**: Cumulative size of all files returned.
  - **Status code counts**: The number of times each HTTP status code was encountered.
- If interrupted by a keyboard interrupt (Ctrl+C), the script will print the current metrics before exiting.

### **Example Output**
```text
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
```

## **Project Structure**
```
0x03-log_parsing/
├── 0-stats.py        # Main script for log parsing
├── 0-generator.py    # Log generator for testing
└── README.md         # Project documentation
```

## **Requirements**
- **Python version**: Python 3.4.3 or later.
- **Operating System**: The script is tested on Ubuntu 20.04 LTS.
- **PEP 8 Compliance**: The script follows the PEP 8 style guide.

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-interview.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 0x03-log_parsing
   ```
3. Ensure that the script is executable:
   ```bash
   chmod +x 0-stats.py
   ```

## **Development**
- **Editors**: Recommended editors are `vi`, `vim`, and `emacs`.
- **Code Style**: The script adheres to PEP 8 guidelines for Python code.

## **License**
This project is licensed under the MIT License. You can find more details in the `LICENSE` file.

## **Acknowledgments**
- **ALX Program**: This project is part of the ALX Software Engineering curriculum.
- **Python Documentation**: For extensive resources on Python programming.

## **Contact**
For any issues or inquiries, please reach out to [gideonphiri032@gmail.com](mailto:gideonphiri032@gmail.com).

---
