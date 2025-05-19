from typing import Dict, List, Union

def process_user_data(user_data: Dict, include_history: bool=False):
    user_id = user_data["id"]
    name = user_data["name"]
    
    result: Dict[str, Union[str, List[Dict[str, str]]]] = {
        "display_name": f"User {name}",
        "normalized_id": str(user_id).zfill(8)
    }
    
    if include_history:
        result["history"] = get_user_history(user_id)
    
    return result

def get_user_history(user_id: str) -> List[Dict[str, str]]:
    # Simulate database call
    return [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"}
    ]

# Sample usage
sample_user = {"id": 42, "name": "Alice"}
processed = process_user_data(sample_user, True)
print(processed)
