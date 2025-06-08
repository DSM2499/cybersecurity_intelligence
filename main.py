from crew import CyberThreatIntelCrew
from utils.exa_helpers import search_cyber_threats

def run():
    """Run the Cyber Threat Intel Crew."""
    exa_results = search_cyber_threats("latest cybersecurity threats 2025")
    inputs = {
        'topic': 'Latest cybersecurity threats 2025',
        'exa_results': exa_results,
        # These will be filled by the Crew automatically:
        'threat_summary': '',
        'cve_analysis': '',
        'mitigation_strategies': ''
    }

    CyberThreatIntelCrew().crew().kickoff(inputs = inputs)

if __name__ == "__main__":
    run()
