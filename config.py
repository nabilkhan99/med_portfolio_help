capability_content = """
Fitness to practise
- Understands GMC document "Duties of a Doctor"
- Attends to professional duties
- Identifies and manages risks to patient care
- Responds appropriately to complaints and performance issues

Maintaining an ethical approach
- Follows GMC "Good Medical Practice"
- Treats everyone with respect for beliefs, dignity and rights
- Avoids discrimination
- Applies ethical principles in practice

Communication and consultation skills
- Develops effective patient relationships
- Uses appropriate consultation techniques
- Provides clear explanations
- Manages challenging consultations
- Works effectively with interpreters

Data gathering and interpretation
- Gathers relevant patient information
- Uses clinical records effectively
- Conducts appropriate examinations
- Identifies abnormal findings

Clinical examination and procedural skills
- Performs appropriate examinations
- Identifies abnormal signs
- Follows professional codes of practice
- Respects patient dignity and privacy

Making decisions/diagnosis
- Generates appropriate differential diagnoses
- Tests clinical hypotheses
- Makes evidence-based decisions
- Develops independent decision-making skills

Clinical management
- Implements appropriate management plans
- Makes safe prescribing decisions
- Refers appropriately
- Manages medical emergencies
- Maintains proper documentation

Managing medical complexity
- Handles co-morbidity
- Manages uncertainty
- Assesses patient risk
- Promotes health improvement

Working with colleagues and teams
- Functions effectively in teams
- Understands team roles
- Communicates well with colleagues
- Integrates into healthcare teams

Maintaining performance, learning and teaching
- Accesses evidence-based resources
- Engages in continuous learning
- Participates in clinical governance
- Contributes to education of others

Organisation, management and leadership
- Understands primary care organization
- Maintains good clinical records
- Manages time effectively
- Adapts to change
- Handles workload appropriately

Practising holistically and promoting health
- Considers physical, psychological and social aspects
- Recognizes impact on patients
- Promotes health improvement
- Implements safeguarding principles

Community orientation
- Understands local population needs
- Knows available services
- Manages resource limitations
- Engages with community resources"""




prompt_content = """

I am a GP Trainee. Write a clinical case review for my GP Portfolio based on the case description below. Please structure the response carefully with ALL of the following sections in order:

Case Summary:
[Provide a clear, structured 2-3 paragraph summary of the key points, clinical decisions, and outcomes]

{capabilities}

Reflection: What will I maintain, improve or stop?
[Reflect on:
- What went well and why (to maintain these behaviors)
- What could be improved in future similar cases
- What should be stopped or done differently
- Your emotional response to the case
As per RCGP guidance: "This reflection should include actions required in response to your emotional needs as well as clinical and educational actions i.e. 'how did it make you feel?'"]

Learning needs identified from this event:
[List specific learning needs, knowledge gaps, or skills to develop based on this case]

Here is the case to review:
{case_description}

Please ensure:
- Each section is clearly labeled
- Use professional medical language throughout
- Make specific, actionable points in the reflection and learning needs sections
- Link capabilities to concrete actions and decisions from the case
- Include emotional aspects in the reflection as per RCGP guidance

Here are two examples of good case reviews for reference:

Example 1: 

User input: During a duty day I noticed VH, an elderly gentleman was on the list requesting a call back. The telephone number had a code in front of it. I was aware VH was very hard of hearing. The telephone number took me through a text telephone service. I witnessed the use of the text telephone system and conveyed my questions via an operator. VH in turn answered the questions. VH was concerned he may have had a recurrence of his piles and was keen for something to help. We had a brief conversation on the telephone. I became acutely aware that I needed to ask short and simple questions that could be conveyed via a text. Having never seen VH with a similar problem, nor could I see a recent documentation of treatment for haemorrhoids and that it was harder to communicate over the telephone I arranged to see him to further assess face to face. 

LLM Output:

Capability: Communication and consultation skills Justification [describe how your actions and approach link to the capability]: 
It was interesting to experience the text telephone system.I have now had experience of using a different communication modality. I was able to adapt the language that I used to take into consideration his individual needs. I was able to manage the consultation effectively with the patient through using the text telephone interpreter, which required me to be organized and structured.

Reflection: what will I maintain, improve or stop?
[Look at the word descriptors. Think what you would need to change to demonstrate competence or excellence] When asking questions via an operator it is important to be precise with the questions to. It made me consider the importance of e 3 system as well as improving communication with patients using different modalities. Overall I felt this telephone consultation and the process of the consultation was successful. 

Learning needs identified from this event:
I would like to gain experience of using a translation telephone line (something we don't use regularly in my current practice). I would also like to develop further strategies to communicate effectively with patients who have a loss of hearing – should they present alone, or with a signer. 

Example 2: 

User input: I worked a busy weekend on call covering general psychiatry over several hospital sites. 

LLM Output:

Working with colleagues and in teams Justification (describe how your actions and approach link to the capability): 
I find that during on calls you have to use a very particular type of team working skills, as you have to create a mini, instant team for the on calls without knowing who is going to be in the team in advance. The same doctors do nights and days for the weekend, so you hand over to them at the start and end of the shifts, and this continuity is really helpful for patient care. Since the pandemic, there has been a meeting every night at 21.30 via skype, which includes the SHOs, registrar, consultant and matron or nurse in charge. It is really helpful to have the nursing staff represented at the meeting. In one meeting, I discussed a patient who had just become unwell and the meeting meant that the consultant was able to share an experience of Covid19 presenting in a manner like my patient, and the nursing staff being present meant they could immediately go and put the plan we came up with into place, as well as me phoning the nurse directly after the meeting. It facilitated improved patient care. 

Clinical examination and procedural skills Justification [describe how your actions and approach link to the capability]:
I was attended one of the psychiatric hospitals to review a male patient with abdominal pain. In order to assess him I examined him. At the moment, in a psychiatric hospital, this involves reviewing them in a locked treatment room with a nurse present. I also wear PPE with gloves, a mask and apron. I tried to be sensitive to the fact that I knew he was in a lot of pain and very anxious, and that examining his abdomen was likely to be very uncomfortable, but very important as it meant I could elicit signs such as guarding, which added to my concerns about him needing to go to hospital to rule out serious pathology. 

Organisation, management and leadership Justification [describe how your actions and approach link to the capability]: 
During this busy weekend, I attended Ravenswood Hospital, which is geographically remote and therefore I needed to manage my time well to ensure I did tasks at hospitals which were on my way to Ravenswood. When I arrived, there was a major incident occurring and therefore I could not immediately do the seclusion reviews which I had attended to do. Once I established that there was nothing I could do to help, I asked if there was somewhere I could work, so that whilst I was waiting I could continue to work remotely on my laptop. This allowed me to ensure that the delay did not effect patients which still needed my attention, for example medications prescribing remotely, as I could access their records online and prescribe remotely. 

Reflection: What will I maintain, improve or stop? 
I will continue to improve my time management skills during busy working periods. I feel that every job I have done have been busy in different ways and have required me to juggle tasks and prioritise tasks differently. I am now imminently going to be moving to GP and am excited to see how my skills transfer and what new ones I need to learn. The experience of covering multiple different sites has been unique with this job and is extremely challenging at times, when you cannot be everywhere at once. There will also be a different type of team in GP, which I am looking forward to, especially after having quite minimal contact with a team for much of this rotation. 

Learning needs identified from this event:
I am aware that I need to continue to improve my skills in seeing patients in remote of nonclinical environments, for example on home visits. There are parallels with seeing patients with medical problems OOH in a psychiatric hospital with doing home visits, as psychiatric 5 hospitals are not set up for medical emergencies, and is it very limited in terms of what medical problems can be dealt with. 


"""
