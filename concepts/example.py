# Sequence of page references
page_references = [5, 7, 7, 5, 1, 7, 1, 1, 1, 4, 3, 4, 1, 2, 3]
# print(page_references[:-1])
delta = 3  # Window size for working set
max_frames = 3  # Maximum frames available

# Variables to track the process
resident_set = []  # Current pages in frames
page_faults = 0  # Count of page faults
page_outs = 0  # Count of page outs
resident_sets_after_each_access = []  # Resident set after each access
access_history = []  # To track the last delta accesses

# Reuse Distance calculation
reuse_distances = []  # To store reuse distance for each access

for i, page in enumerate(page_references):
    # Update access history, keeping only the last delta accesses
    access_history.append(page)
    if len(access_history) > delta:
        access_history.pop(0)
    
    # Calculate reuse distance
    if page in access_history[:-1]:
        rd = len(set(access_history[:-1])) - 1  # Excluding the current page from count
    else:
        rd = len(set(page_references[:i]))
    reuse_distances.append(rd)
    
    # Working set algorithm
    if page not in resident_set:
        page_faults += 1
        if len(resident_set) < max_frames:
            resident_set.append(page)
        else:
            # Page out oldest page not in the current working set
            for old_page in resident_set:
                if old_page not in access_history:
                    resident_set.remove(old_page)
                    page_outs += 1
                    break
            resident_set.append(page)
    resident_sets_after_each_access.append(list(resident_set))

print(page_faults)
print(page_outs)
print(resident_sets_after_each_access)
print(reuse_distances)