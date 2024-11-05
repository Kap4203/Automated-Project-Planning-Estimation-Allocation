# Automated Project Planning, Estimation, and Allocation

This project utilizes the CrewAI library to automate the process of project planning, estimation, and resource allocation. It takes in high-level project requirements and generates a detailed project plan with task estimates and milestone information.

## Features

- Loads project details from configuration files and environment variables
- Creates agents for project planning, task estimation, and resource allocation
- Orchestrates the execution of tasks to generate a comprehensive project plan
- Analyzes the results and provides cost estimates, task details, and milestone information
- Presents the output in a user-friendly format using Pandas DataFrames and Markdown


## Getting Started

### Project structure
```
project_root/
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── config_loader.py
│   ├── crew_setup.py
│   └── utils.py
├── main.py
├── .env
└── requirements.txt
```

### Prerequisites

- Python 3.10 or higher
- Conda (recommended) or pip for managing dependencies

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/Automated-Project-Planning-Estimation-Allocation.git
   ```

2. Create a new conda environment (recommended):
   ```
   conda create -n project-env python=3.10
   conda activate project-env
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   1. Create a `.env` file in the project root directory.
   2. Add your OpenAI API key and model name:
      ```
      OPENAI_API_KEY=your-api-key-here
      OPENAI_MODEL_NAME=gpt-4-turbo-preview
      ```

5. Run the application:
   ```
   python main.py
   ```

## Usage

The project consists of the following main components:

1. **Configuration Layer**:
   - Loads environment variables and YAML configuration files
   - Manages all the required configurations for the application

2. **Data Models Layer**:
   - Defines Pydantic models for structured data, such as tasks, milestones, and project plans

3. **CrewAI Layer**:
   - Sets up agents for different tasks (planning, estimation, resource allocation)
   - Creates and manages the Crew that coordinates the execution of tasks

4. **Analysis Layer**:
   - Processes the generated project plan
   - Calculates costs and creates Pandas DataFrames for tasks and milestones
   - Displays the results in a user-friendly format

To customize the application, you can modify the following:

- Update the `.env` file with your own OpenAI API key and model name
- Modify the YAML configuration files (`agents.yaml`, `tasks.yaml`) to change agent and task settings
- Adjust the `ProjectInputs` model in `src/models.py` to match your specific project requirements
- Extend the `ResultAnalyzer` class in `src/utils.py` to add more analysis or visualization capabilities

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [GNU General Public License](LICENSE).