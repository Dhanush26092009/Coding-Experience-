def assign_priority(issue_type):
    issue_type = issue_type.lower()
    if issue_type == "low":
        return 1
    elif issue_type == "medium":
        return 2
    elif issue_type == "high":
        return 3
    else:
        return 0  # Unknown issue type

issue = input("Enter issue type (low/medium/high): ")
priority = assign_priority(issue)
if priority == 0:
    print("Invalid issue type!")
else:
    print(f"Priority level for '{issue}' issue is {priority}")
