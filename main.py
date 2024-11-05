from src.config_loader import ConfigLoader
from src.crew_setup import CrewSetup
from src.utils import ResultAnalyzer
from src.models import ProjectInputs

def main():
    # Load configurations
    api_key, model_name = ConfigLoader.load_environment()
    agents_config, tasks_config = ConfigLoader.load_yaml_configs()
    
    # Setup project inputs
    project_inputs = ProjectInputs(
        project_type="Website",
        project_objectives="Create a website for a small business",
        industry="Technology",
        team_members="""
        - John Doe (Project Manager)
        - Jane Doe (Software Engineer)
        - Bob Smith (Designer)
        - Alice Johnson (QA Engineer)
        - Tom Brown (QA Engineer)
        """,
        project_requirements="""
        - Create a responsive design that works well on desktop and mobile devices
        - Implement a modern, visually appealing user interface with a clean look
        - Develop a user-friendly navigation system
        - Include essential pages and features
        """
    )
    
    # Display project information
    analyzer = ResultAnalyzer()
    analyzer.display_project_info(
        project_inputs.project_type,
        project_inputs.project_objectives,
        project_inputs.industry,
        project_inputs.team_members,
        project_inputs.project_requirements
    )
    
    # Setup and run crew
    crew_setup = CrewSetup(agents_config, tasks_config)
    crew = crew_setup.setup_crew()
    result = crew.kickoff(inputs=project_inputs.dict())
    
    # Analyze results
    costs = analyzer.calculate_costs(crew)
    tasks_df, milestones_df = analyzer.create_results_dataframes(result)
    
    print(f"Total costs: ${costs:.4f}")
    return tasks_df, milestones_df

if __name__ == "__main__":
    tasks_df, milestones_df = main()