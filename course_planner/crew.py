from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class CoursePlanner:
    """CoursePlanner crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def course_curriculum_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["course_curriculum_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def learning_timeline_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["learning_timeline_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def resource_curator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["resource_curator_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def project_recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["project_recommendation_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def skill_assessment_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["skill_assessment_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def career_pathway_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["career_pathway_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def prerequisites_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["prerequisites_analysis_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def study_strategy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["study_strategy_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def community_engagement_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["community_engagement_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def certification_guidance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["certification_guidance_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @task
    def course_curriculum_task(self) -> Task:
        return Task(
            config=self.tasks_config["course_curriculum_task"],
            output_file="output/curriculum.md",
        )

    @task
    def learning_timeline_task(self) -> Task:
        return Task(
            config=self.tasks_config["learning_timeline_task"],
            output_file="output/timeline.md",
        )

    @task
    def resource_curation_task(self) -> Task:
        return Task(
            config=self.tasks_config["resource_curation_task"],
            output_file="output/resources.md",
        )

    @task
    def project_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config["project_recommendation_task"],
            output_file="output/projects.md",
        )

    @task
    def skill_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config["skill_assessment_task"],
            output_file="output/assessments.md",
        )

    @task
    def career_pathway_task(self) -> Task:
        return Task(
            config=self.tasks_config["career_pathway_task"],
            output_file="output/career_pathway.md",
        )

    @task
    def prerequisites_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["prerequisites_analysis_task"],
            output_file="output/prerequisites.md",
        )

    @task
    def study_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["study_strategy_task"],
            output_file="output/study_strategy.md",
        )

    @task
    def community_engagement_task(self) -> Task:
        return Task(
            config=self.tasks_config["community_engagement_task"],
            output_file="output/communities.md",
        )

    @task
    def certification_guidance_task(self) -> Task:
        return Task(
            config=self.tasks_config["certification_guidance_task"],
            output_file="output/certifications.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )