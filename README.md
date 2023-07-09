# xss_and_sqli_scanner
python script for recersive crawling URL to find list of endpoints and paramters 
then scan found endpoints with paramters using https://github.com/s0md3v/XSStrike.git and sqlmap

so
1. download XSStrike in same directory using `git clone https://github.com/s0md3v/XSStrike.git`
2. downaload sqlmap using normal download using `git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev`
3. modify header.txt to what u want (add cookie, more HTTP headers)
   
finally run `python3 main.py -u 'http://testphp.vulnweb.com/' --header_file header.txt `
