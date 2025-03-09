# GRC_Compliance_Analyser Using CrewAI

Problem Statement: 
To develop a multi-agent-based GRC (Governance, Risk, and Compliance) assessment 
assistant that leverages GenAI to evaluate the organization. The system will analyze the 
organization based on the input and provide insights into risk mitigation strategies. It aims to 
streamline GRC processes, ensuring compliance and optimizing security frameworks 
 
Command to run on terminal: 
python .\GRC_Agent_Assistant.py 
 
Sample Input: 
Enter your OpenAI API key: sk ************************************ 
Welcome to the Crew AI GRC System! 
=== GRC Assessment Questionnaire === 
? What type of organization are you assessing? Healthcare 
? What area would you like to assess? Data Protection 
? Please describe the specific scenario or concern(Ex:Third party Vendor, Sensitive Data, 
Bankruptcy): Sensitive Customer Data 
? What is the likelihood of this risk occurring? High 
? What would be the impact if this risk materializes? High 
 
Sample Output: 
 
# Agent: Policy Analyst 
## Task:  
Analyze compliance requirements for Data Protection in  
Healthcare organization. 
Scenario: Sensitive Customer Dat 
# Agent: Policy Analyst 
2 
 
## Final Answer: 
1. **Relevant Regulatory Frameworks**: 
   - **Health Insurance Portability and Accountability Act (HIPAA)**: This federal law sets 
standards for the protection of sensitive patient health information. Key aspects include the 
Privacy Rule and the Security Rule. 
   - **General Data Protection Regulation (GDPR)**: If the healthcare organization operates in 
the EU or deals with the data of EU citizens, they must comply with GDPR, which governs the 
collection, storage, and processing of personal data. 
   - **Health Information Technology for Economic and Clinical Health (HITECH) Act**: This 
act promotes the adoption and meaningful use of health information technology. It strengthens 
the privacy and security protections established under HIPAA. 
   - **California Consumer Privacy Act (CCPA)**: Relevant for organizations operating in 
California, this law provides guidelines on the collection and use of personal information, 
including healthcare data. 
   - **The Federal Information Security Management Act (FISMA)**: This act applies to federal 
agencies and highlights the need for protecting government information systems, impacting 
healthcare organizations that work with federal data. 
 
2. **Key Compliance Requirements**: 
   - **Data Encryption**: Encrypting sensitive data both at rest and in transit to protect against 
unauthorized access. 
   - **Access Controls**: Implementing strict access controls to ensure that only authorized 
personnel can access sensitive data. 
   - **Training and Awareness**: Regular training programs for employees on data protection 
principles and organizational policies. 
   - **Incident Response Plan**: Developing and maintaining an incident response plan to 
address data breaches or other security incidents expeditiously. 
   - **Data Minimization**: Limiting the collection and retention of personal data to what is 
necessary for the intended purpose. 
   - **Audit Controls**: Establishing mechanisms to record and examine system activity to 
ensure compliance and detect issues. 
…………………………………………………………………………………………. 
…………………………………………. 
………………………………………….
