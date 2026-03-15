import json 
import os 

from AIConfig import AIConfig

def load_user_input():
    config_path = os.path.join( "config", "ai_config_sample.json")
    with open(config_path, "r") as file:
        return json.load(file)
    
def validate_config(input_data):
    try:
        config = AIConfig(**input_data)
        print("✅ Configuration is valid!")
        return config
    except Exception as e:
        print(f"❌ Configuration validation failed: {e}")
        return None

def main():
    user_input = load_user_input()
    config = validate_config(user_input)

    if config: 
        print("Ready to use Azure API with config:") 
        print(config.model_dump())
    else:
        print("Please fix the configuration errors and try again.")

if __name__ == "__main__":
    main()
    