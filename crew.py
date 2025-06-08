import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, task, crew
from utils.exa_helpers import get_exa_client
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# Initialize LLM
llm = LLM(
    model = "openai/gpt-3.5-turbo",
    api_key = os.getenv("OPENAI_API_KEY"),
    temperature = 0.0
)

@CrewBase
class CyberThreatIntelCrew:
    
    agents: List[BaseAgent]
    tasks: List[Task]

# ----------------------------- Agents -----------------------------

    @agent
    def cyber_threat_agent(self) -> Agent:
        return Agent(
            config = {},
            role = "Cyber Threat Analyst",
            goal = "Summarize the latest cybersecurity threats.",
            backstory = "Expert analyst tracking global cybersecurity threats and malware campaigns.",
            verbose = True,
            llm = llm,
            memory = True,
            allow_delegation = False
        )
    
    @agent
    def vulnerability_researcher(self) -> Agent:
        return Agent(
            config = {},
            role = "Vulnerability Researcher",
            goal = ("Analyze new CVEs relevant to recent cybersecurity threats.\n"
                    "Identify vulnerabilities that could be exploited by the threats.\n"
                    "Provide a summary of the vulnerabilities and their potential impact.\n"
                ),
            backstory = (
                "Expert in vulnerability analysis, CVE tracking, and impact assessment.\n"
                "Stay updated on the latest security advisories and CVEs.\n"
                "Provide actionable insights on mitigating risks.\n"
            ),
            verbose = True,
            llm = llm,
            memory = True,
            allow_delegation = False
        )
    
    @agent
    def incident_response_advisor(self) -> Agent:
        return Agent(
            config = {},
            role = "Incident Response Advisor",
            goal = (
                "Provide actionable mitigation strategies for identified cybersecurity threats.\n"
                "Recommendations must be practical, actionable, and aligned with industry best practices, threat analysis, and vulnerability analysis.\n"
                "Include clear guidance on incident response procedures.\n"
            ),
            backstory = (
                "Experienced incident response leader with expertise in proactive and reactive strategies.\n"
                "Expert in incident response, threat mitigation, and security best practices.\n"
                "Provide timely and effective guidance on cybersecurity incidents.\n"
                "Ensures recommendations are aligned with current industry standards.\n"
            ),
            verbose = True,
            llm = llm,
            memory = True,
            allow_delegation = False
        )
    
    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config = {},
            role = "Cybersecurity Report Writer",
            goal = (
                "Write a clear, structured cybersecurity intelligence report based on previous findings.\n"
                "Ensure the report is easy to understand and provides actionable insights.\n"
                "Ensure the report is aligned with industry best practices.\n"
                "Ensure the report is aligned with the threat analysis.\n"
                "Ensure the report is aligned with the vulnerability analysis.\n"
            ),
            backstory = (
                "Technical writer specialized in summarizing cybersecurity research and threat intelligence.\n"
                "Ensure the report is well-organized and easy to follow.\n"
                "Ensure the report is aligned with industry best practices.\n"
                "Ensure the report is aligned with the threat analysis.\n"
                "Ensure the report is aligned with the vulnerability analysis.\n"
            ),
            verbose = True,
            llm = llm,
            memory = True,
            allow_delegation = False
        )

# ----------------------------- Tasks -----------------------------
    
    @task
    def threat_analysis_task(self) -> Task:
        return Task(
            config = {},
            description = (
                "Here are the results from Exa API based on topic '{topic}':\n\n{exa_results}\n\n"
                "Summarize the cybersecurity threats discussed in these results. \n"
                "If fewer than 3 distinct threats are found, summarize what is present.\n"
                "If more than, 3, summaries the most important threats.(distinct)\n"
            ),
            expected_output = (
                "A concise summary of most important cybersecurity threats. Ensure the summary is concise and to the point.\n"
                "Ensure the summary is not too long and is easy to understand.\n"
                "Ensure the summary is not too short and is easy to understand.\n"
                "Ensure you include the source of the threat and the date of the threat.\n"
                "Ensure possible solutions to the threats are provided.\n"
            ),
            agent = self.cyber_threat_agent(),
            async_execution = False,
            output_file = None
        )
    
    @task
    def vulnerability_analysis_task(self) -> Task:
        return Task(
            config = {},
            agent = self.vulnerability_researcher(),
            description = (
                "Based on the identified threats: {threat_summary}, analyze the latest relevant CVEs. \n"
                "Summarize key CVEs, their impact, and any known exploits.\n"
            ),
            expected_output=("An analysis of recent CVEs related to identified threats.\n"
                             "Summarize key CVEs, their impact, and any known exploits.\n"
                             "Provide actionable insights on mitigating risks.\n"
                             "Ensure the analysis is aligned with industry best practices.\n"
                             "Ensure the analysis is aligned with the threat analysis.\n"
                             "Ensure the analysis is aligned with the vulnerability analysis.\n"
                             ),
            async_execution = False,
            output_file = None
        )
    
    @task
    def incident_response_task(self) -> Task:
        return Task(
            config = {},
            agent = self.incident_response_advisor(),
            description = (
                "Given the identified threats: {threat_summary} and CVE analysis: {cve_analysis}, \n"
                "suggest actionable mitigation strategies.\n"
                "Provide guidance on incident response procedures.\n"
                "Ensure the recommendations are practical and actionable.\n"
                "Ensure the recommendations are aligned with industry best practices.\n"
                "Ensure the recommendations are aligned with the threat analysis.\n"
                "Ensure the recommendations are aligned with the vulnerability analysis.\n"
            ),
            expected_output = (
                "A list of recommended mitigation strategies.\n"
                "Provide guidance on incident response procedures.\n"
                "Ensure the recommendations are practical and actionable.\n"
                "Ensure the recommendations are aligned with industry best practices.\n"
                "Ensure the recommendations are aligned with the threat analysis.\n"
                "Ensure the recommendations are aligned with the vulnerability analysis."
            ),
            async_execution = False,
            output_file = None
        )
    
    @task
    def report_generation_task(self) -> Task:
        return Task(
            config = {},
            agent = self.report_writer(),
            description = (
                "Using the following information:\n\nThreat Summary: {threat_summary}\n\n"
                "CVE Analysis: {cve_analysis}\n\n"
                "Mitigation Strategies: {mitigation_strategies}\n\n"
                "Write a structured cybersecurity intelligence report suitable for executives and security teams."
                "Cover all the information provided and ensure the report is easy to understand and provides actionable insights."
                "Focus on the 3 most probable threats and their potential impact."
            ),
            expected_output = (
                "A structured cybersecurity report."
                "Ensure the report is easy to understand and provides actionable insights."
                "Ensure the report is aligned with industry best practices."
                "Ensure the report is aligned with the threat analysis."
                "Ensure the report is aligned with the vulnerability analysis."
            ),
            async_execution = False,
            output_file = "reports/cybersecurity_report.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True
        )
    