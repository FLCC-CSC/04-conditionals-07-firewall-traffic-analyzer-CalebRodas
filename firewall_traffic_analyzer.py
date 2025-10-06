# FILE NAME - firewall_traffic_analyzer.py

# NAME: Caleb Rodas
# DATE: 10/05/2025
# BRIEF DESCRIPTION:  This program analyzes network traffic based on port number and
# data transfer size to assess potential security risks.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########


# Display the header
print("=== Network Traffic Security Analyzer ===\n")

# Prompt user for port number and data transfer size
port_number = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
file_size_mb = int(input("Enter the data transfer size in megabytes (MB): "))

# Analyze the traffic and determine risk level
if (port_number == 22 or port_number == 3389) and file_size_mb >= 100:
    risk_message = "HIGH RISK: Potential unauthorized remote access detected!"
elif port_number == 80 and file_size_mb > 100:
    risk_message = "MEDIUM RISK: Large unencrypted data transfer detected."
elif port_number == 443:
    risk_message = "LOW RISK: Secure encrypted transfer detected."
else:
    risk_message = "UNKNOWN: Unrecognized traffic pattern."

# Display the firewall log
print("\nFIREWALL LOG:")
print(f"Port: {port_number}, Transfer Size: {file_size_mb} MB")
print(f"Risk Assessment: {risk_message}")
print("------------------------")







########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?







'''
