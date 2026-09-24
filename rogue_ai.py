# ============================================================
# CMP 131 - ROGUE AI EMERGENCY DIAGNOSTIC SYSTEM
# Team members:
# ============================================================

print("========================================")
print("     ROGUE AI DIAGNOSTIC SYSTEM")
print("========================================")

# LEVEL 1 - TEMPERATURE DIAGNOSTIC
# Ask for the system temperature and make the required decision.
Temperature = int(input("What is your temperature?"))
if Temperature >= 100:
    print("WARNING: SYSTEM OVERHEATING")
else:
    print("Temperature Normal")

# LEVEL 2 - POWER DIAGNOSTIC
# Ask for the battery percentage and make the required decision.
Battery = int(input("What is your battery percentage?"))
if Battery <= 20:
    print("LOW POWER")
else:
    print("Power Normal")

# LEVEL 3 - SECURITY DIAGNOSTIC
# Ask for the security status and make the required decision.
security = input("What is your security status?")

if security == "danger":
    print("SHUTDOWN REQUIERED")
else:
    print("System Secure")


print("========================================")
print("Diagnostic complete.")
print("========================================")
