import os
import yaml
from dotenv import load_dotenv

class ConfigLoader:
    @staticmethod
    def load_environment():
        """Load environment variables"""
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        model_name = os.getenv('OPENAI_MODEL_NAME')
        
        if not api_key or not model_name:
            raise ValueError("Missing required environment variables")
            
        return api_key, model_name

    @staticmethod
    def load_yaml_configs():
        """Load YAML configuration files"""
        files = {
            'agents': 'config/agents.yaml',
            'tasks': 'config/tasks.yaml'
        }
        
        configs = {}
        for config_type, file_path in files.items():
            try:
                with open(file_path, 'r') as file:
                    configs[config_type] = yaml.safe_load(file)
            except FileNotFoundError:
                raise FileNotFoundError(f"Configuration file not found: {file_path}")
                
        return configs['agents'], configs['tasks']