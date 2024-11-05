from IPython.display import display, Markdown
import pandas as pd

class ResultAnalyzer:
    @staticmethod
    def display_project_info(project, project_objectives, industry, team_members, project_requirements):
        formatted_output = f"""
        **Project Type:** {project}
        **Project Objectives:** {project_objectives}
        **Industry:** {industry}
        **Team Members:**
        {team_members}
        **Project Requirements:**
        {project_requirements}
        """
        display(Markdown(formatted_output))
    
    @staticmethod
    def calculate_costs(crew):
        """Calculate and return usage costs"""
        return 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
    
    @staticmethod
    def create_results_dataframes(result):
        """Create and return DataFrames for tasks and milestones"""
        result_dict = result.pydantic.dict()
        
        tasks_df = pd.DataFrame(result_dict['tasks'])
        milestones_df = pd.DataFrame(result_dict['milestones'])
        
        return tasks_df, milestones_df