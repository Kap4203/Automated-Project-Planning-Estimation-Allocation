from crewai import Agent, Task, Crew
from src.models import ProjectPlan  # Changed from .models to src.models

class CrewSetup:
    def __init__(self, agents_config, tasks_config):
        self.agents_config = agents_config
        self.tasks_config = tasks_config
        
    def create_agents(self):
        """Create and return all required agents"""
        return {
            'project_planning': Agent(config=self.agents_config['project_planning_agent']),
            'estimation': Agent(config=self.agents_config['estimation_agent']),
            'resource_allocation': Agent(config=self.agents_config['resource_allocation_agent'])
        }
        
    def create_tasks(self, agents):
        """Create and return all required tasks"""
        return [
            Task(
                config=self.tasks_config['task_breakdown'],
                agent=agents['project_planning']
            ),
            Task(
                config=self.tasks_config['time_resource_estimation'],
                agent=agents['estimation']
            ),
            Task(
                config=self.tasks_config['resource_allocation'],
                agent=agents['resource_allocation'],
                output_pydantic=ProjectPlan
            )
        ]
        
    def setup_crew(self):
        """Create and return the configured crew"""
        agents = self.create_agents()
        tasks = self.create_tasks(agents)
        
        return Crew(
            agents=list(agents.values()),
            tasks=tasks,
            verbose=True
        )