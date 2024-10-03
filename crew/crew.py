from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.markdown_tools import markdown_validation_tool  # Import the validation tool

# Define the model key to be used (this is the key from the 'models' section in the YAML file)
llm_model_key = 'llama_3_1_8b_instruct_q8_0'

@CrewBase
class MarkdownCrew():
    """Crew configured to review Markdown"""
    
    # Define paths to YAML configuration files (for agents, tasks, and LLM models)
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    models_config = 'config/local_llm.yaml'  # Path to the models configuration file (contains the models section)

    def __init__(self):
        # Reference the LLM model by its key inside the 'models' section in the YAML
        self.llm_config = {
            'models': llm_model_key  # Use the model key defined above
        }

    # Define the agent to validate markdown
    @agent
    def markdown_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['markdown_agent'],
            tools=[markdown_validation_tool],  # Use the markdown validation tool
            llm=self.llm_config['models'],  # Refer to the LLM model inside the 'models' section
            verbose=True
        )

    # Define the task that uses the agent
    @task
    def markdown_task(self, file_path) -> Task:
        return Task(
            config=self.tasks_config['markdown_task'],
            agent=self.markdown_agent(),
            inputs={"file_path": file_path}  # Pass the file path to the task
        )

    # Define the crew to execute the workflow
    @crew
    def crew(self) -> Crew:
        """Creates the crew for Markdown review"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
