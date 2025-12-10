import json
import operator
import os

# Map operator strings to actual Python functions
OP_MAP = {
    '==': operator.eq,
    '!=': operator.ne,
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le
}

def transform_data(
    input_file: str,
    output_file: str,
    filters: dict = None,
    field_mapping: dict = None,
    sort_by: str = None
) -> int:
    """
    Loads JSON data, filters, transforms fields, sorts, and saves to a new JSON file.

    Returns:
        Number of records in output.
    """
    try:
        # 1. Load JSON from file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_file}' not found.")
        return 0
    except json.JSONDecodeError:
        print(f"❌ Error: Input file '{input_file}' is not valid JSON.")
        return 0

    processed_data = []

    # 2. Filter records based on criteria and 3. Transform/rename fields
    for record in data:
        # Check Filters
        is_filtered = False
        if filters:
            for field, (op_str, value) in filters.items():
                if field in record:
                    op_func = OP_MAP.get(op_str)
                    if op_func is None:
                        raise ValueError(f"Invalid operator '{op_str}' in filter.")
                        
                    # Apply filter condition
                    if not op_func(record.get(field), value):
                        is_filtered = True
                        break
                # If filter field doesn't exist, we assume the record fails the filter
                else:
                    is_filtered = True
                    break
        
        if is_filtered:
            continue  # Skip this record if it failed any filter

        # Apply Transformation
        new_record = {}
        # Copy and rename fields
        for old_key, new_key in (field_mapping or {}).items():
            if old_key in record:
                new_record[new_key] = record[old_key]
        
        # Copy remaining fields that were not mapped
        all_keys = set(record.keys())
        mapped_keys = set((field_mapping or {}).keys())
        
        for key in (all_keys - mapped_keys):
            new_record[key] = record[key]

        processed_data.append(new_record)

    # 4. Sort by specified field
    if sort_by and processed_data:
        # Ensure the sort_by key exists in the transformed records
        if any(sort_by in record for record in processed_data):
            processed_data.sort(key=lambda x: x.get(sort_by), reverse=False)
        else:
            print(f"⚠️ Warning: Sort field '{sort_by}' not found in any processed records. Skipping sort.")


    # 5. Save to new JSON file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=4)
        print(f"✅ Success: {len(processed_data)} records saved to '{output_file}'.")
        return len(processed_data)
    except IOError:
        print(f"❌ Error: Could not write to output file '{output_file}'.")
        return 0

# --- SIMULATION AND TEST SETUP ---

# 1. Create a simulated input file (users.json)
INPUT_FILE_NAME = 'users.json'
OUTPUT_FILE_NAME = 'active_adults.json'

sample_data = [
    {"user_id": 101, "user_name": "Alice", "age": 25, "status": "active", "user_email": "alice@example.com"},
    {"user_id": 102, "user_name": "Bob", "age": 17, "status": "active", "user_email": "bob@example.com"},
    {"user_id": 103, "user_name": "Charlie", "age": 30, "status": "active", "user_email": "charlie@example.com"},
    {"user_id": 104, "user_name": "David", "age": 22, "status": "active", "user_email": "david@example.com"},
    {"user_id": 105, "user_name": "Eve", "age": 16, "status": "inactive", "user_email": "eve@example.com"}
]

try:
    with open(INPUT_FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=4)
    print(f"Simulated input file '{INPUT_FILE_NAME}' created.")

    # 2. Example usage (The original prompt's test case)
    record_count = transform_data(
        INPUT_FILE_NAME,
        OUTPUT_FILE_NAME,
        filters={'age': ('>=', 18), 'status': ('==', 'active')},
        field_mapping={'user_name': 'name', 'user_email': 'email'},
        sort_by='name'
    )

    print(f"\nFinal count returned: {record_count}")
    
    # 3. Print the content of the newly created output file
    if os.path.exists(OUTPUT_FILE_NAME):
        with open(OUTPUT_FILE_NAME, 'r', encoding='utf-8') as f:
            output_content = json.load(f)
        print("\n--- Output File Content (active_adults.json) ---")
        print(json.dumps(output_content, indent=4))
        print("-------------------------------------------------")

finally:
    # Clean up simulated files
    if os.path.exists(INPUT_FILE_NAME):
        os.remove(INPUT_FILE_NAME)
    if os.path.exists(OUTPUT_FILE_NAME):
        os.remove(OUTPUT_FILE_NAME)