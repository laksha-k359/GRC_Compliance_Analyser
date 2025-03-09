#####################################################################################################################################
#To develop a multi-agent based GRC (Governance, Risk, and Compliance) assessment assistant that leverages GenAI  
#to evaluate organization. The system will analyze  the organization based on the input
# and provide insights on risk mitigation strategies. It aims to streamline GRC processes, ensuring compliance 
# and optimizing security frameworks
#####################################################################################################################################

#####################################################################################################################################
#pip install crewai
#pip install questionary
#####################################################################################################################################


from crewai import Agent, Task, Crew, Process
from textwrap import dedent  #Multi line stringindentation
import getpass
import datetime
from typing import Dict, List
import questionary   #interactive CLI questionarie
import os
os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
class GRCAssessment:
    def __init__(self):
        # Initialize agents
        self.policy_agent = Agent(                 #Agent1
            role='Policy Analyst',
            goal='Analyze compliance requirements and policy frameworks',
            backstory=dedent("""
                You are an expert in regulatory compliance and policy frameworks.
                You have extensive experience in analyzing GRC requirements and 
                providing actionable recommendations."""),
            verbose=True,
            allow_delegation=False
        )

        self.risk_agent = Agent(                    #Agent2
            role='Risk Assessor',
            goal='Evaluate risks and provide mitigation strategies',
            backstory=dedent("""
                You are a seasoned risk management professional with expertise in
                identifying, analyzing, and mitigating various types of organizational
                risks."""),
            verbose=True,
            allow_delegation=False
        )

        self.security_agent = Agent(               #Agent3
            role='Security Expert',
            goal='Recommend and evaluate security controls',
            backstory=dedent("""
                You are a cybersecurity expert specializing in designing and
                implementing security controls. You have deep knowledge of
                security frameworks and best practices."""),
            verbose=True,
            allow_delegation=False
        )

    def gather_input(self) -> Dict:
        """Gather user input through interactive questionnaire"""
        print("\n=== GRC Assessment Questionnaire ===")

        # Organization context
        org_type = questionary.select(
            "What type of organization are you assessing?",
            choices=[
                "Financial Services",
                "Healthcare",
                "Technology",
                "Retail",
                "Manufacturing"
            ]
        ).ask()

        # Assessment area
        assessment_area = questionary.select(
            "What area would you like to assess?",
            choices=[
                "Data Protection",
                "Information Security",
                "Operational Risk",
                "Third Party Risk",
                "Business Continuity",
                "Regulatory Compliance"
            ]
        ).ask()

        # Specific scenario
        scenario = questionary.text(
            "Please describe the specific scenario or concern(Ex:Third party Vendor, Sensitive Data, Bankruptcy):"
        ).ask()

        # Risk factors
        likelihood = questionary.select(
            "What is the likelihood of this risk occurring?",
            choices=["Low", "Medium", "High"]
        ).ask()

        impact = questionary.select(
            "What would be the impact if this risk materializes?",
            choices=["Low", "Medium", "High"]
        ).ask()


        return {
            "org_type": org_type,
            "assessment_area": assessment_area,
            "scenario": scenario,
            "likelihood": likelihood,
            "impact": impact,
        }

    def create_tasks(self, input_data: Dict) -> List[Task]:
        """Create tasks for each agent based on user input"""
        
        # Policy analysis task
        policy_task = Task(             #Task1
            description=dedent(f"""
                Analyze compliance requirements for {input_data['assessment_area']} in 
                {input_data['org_type']} organization.
                Scenario: {input_data['scenario']}
                
                Provide:
                1. Relevant regulatory frameworks
                2. Key compliance requirements
                3. Required policy updates
                4. Compliance action items
            """),
            expected_output="A summary of relevant compliance frameworks, key policy requirements, and recommended updates.",
            agent=self.policy_agent
        )

        # Risk assessment task
        risk_task = Task(           #Task2
            description=dedent(f"""
                Evaluate risks for {input_data['assessment_area']} scenario:
                {input_data['scenario']}
                
                Risk Factors:
                - Likelihood: {input_data['likelihood']}
                - Impact: {input_data['impact']}
                
                Provide:
                1. Risk level assessment
                2. Detailed risk analysis
                3. Mitigation strategies
                4. Monitoring requirements
            """),
            expected_output="A structured risk assessment report detailing risk levels, potential impacts, and recommended mitigations.",
            agent=self.risk_agent
        )

        # Security assessment task
        security_task = Task(           #Task3
            description=dedent(f"""
                Recommend security controls for:
                Area: {input_data['assessment_area']}
                Scenario: {input_data['scenario']}
                
                Provide:
                1. Required security controls
                2. Technical recommendations
                3. Implementation priorities
                4. Security metrics
            """),
            expected_output="A list of security controls with implementation priorities and relevant technical recommendations.",
            agent=self.security_agent
        )

        return [policy_task, risk_task, security_task]

    def run_assessment(self):
        """Run the full GRC assessment"""
        # Gather input
        input_data = self.gather_input()

        # Create tasks
        tasks = self.create_tasks(input_data)

        # Create and run the crew
        crew = Crew(
            agents=[self.policy_agent, self.risk_agent, self.security_agent],
            tasks=tasks,
            verbose=True,
            process=Process.sequential
        )

        # Execute the assessment
        result = crew.kickoff()
        print(result)

def main():
    print("Welcome to the Crew AI GRC Assessment System!")

    # Create and run assessment
    assessment = GRCAssessment()
    assessment.run_assessment()


if __name__ == "__main__":
    main()