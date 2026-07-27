# command run when you reduced the line of dataset 
run this command in terminal



python -c "import sys; lines = [sys.stdin.readline() for _ in range(20)]; sys.stdout.writelines(lines)" < NYC.CSV > NYC_short.csv