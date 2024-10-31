capability_content = """
Fitness to practise
- This is about professionalism and the actions expected to protect people from harm. This includes the awareness of when an individual's performance, conduct or health, or that of others, might put patients, themselves or their colleagues at risk.
- Understands the GMC document, "Duties of a Doctor".
- Attends to their professional duties.
- Awareness that physical or mental illness, or personal habits, might interfere with the competent delivery of patient care.
- Identifies and notifies an appropriate person when their own or a colleague's performance, conduct or health might be putting others at risk.
- Responds to complaints or performance issues appropriately.

Maintaining an ethical approach
- This is about practising ethically with integrity and a respect for equality and diversity.
- Awareness of the professional codes of practice as described in the GMC document "Good Medical Practice".
- Understands the need to treat everyone with respect for their beliefs, preferences, dignity and rights.
- Recognises that people are different and does not discriminate against them because of those differences.
- Understands that "Good Medical Practice" requires reference to ethical principles.

Communication and consultation skills
- This is about communication with patients, the use of recognised consultation techniques, establishing patient partnership, managing challenging consultations, third-party consultations and the use of interpreters.
- Develops a working relationship with the patient, but one in which the problem rather than the person is the focus.
- Uses a rigid or formulaic approach to achieve the main tasks of the consultation.
- Provides explanations that are relevant and understandable to the patient, using appropriate language.
- The use of language is technically correct but not well adapted to the needs and characteristics of the patient.
- Provides explanations that are medically correct but doctor-centred.
- Communicates management plans but without negotiating with, or involving, the patient.
- Consults to an acceptable standard but lacks focus and requires longer consulting times.
- Aware of when there is a language barrier and can access interpreters either in person or by telephone.

Data gathering and interpretation
- This is about the gathering, interpretation, and use of data for clinical judgement, including information gathered from the history, clinical records, examination and investigations.
- Accumulates information from the patient that is relevant to their problem.
- Uses existing information in the patient records.
- Employs examinations and investigations that are in line with the patient's problems.
- Identifies abnormal findings and results.

Clinical examination and procedural skills
- This is about clinical examination and procedural skills. By the end of training, the trainee must have demonstrated competence in general and systemic examinations of all of the clinical curriculum areas, this includes the 5 mandatory examinations and a range of skills relevant to General Practice.
- Chooses examinations in line with the patient's problem(s).
- Identifies abnormal signs
- Suggests appropriate procedures related to the patient's problem(s).
- Observes the professional codes of practice including the use of chaperones.
- Arranges the place of the examination to give the patient privacy and to respect their dignity.
- Examination is carried out sensitively and without causing the patient harm
- Performs procedures and examinations with the patient's consent and with a clinically justifiable reason to do so.

Making a decision/diagnosis
- This is about a conscious, structured approach to making diagnoses and decision-making.
- Generates an adequate differential diagnosis based on the information available.
- Generates and tests appropriate hypotheses.
- Makes decisions by applying rules, plans or protocols.
- Is starting to develop independent skills in decision making and uses the support of others to confirm these are correct.

Clinical management
- This is about the recognition and management of patients' problems.
- Uses appropriate management options
- Suggests possible interventions in all cases.
- Arranges follow up for patients
- Makes safe prescribing decisions, routinely checking on drug interactions and side effects.
- Refers safely, acting within the limits of their competence.
- Recognises medical emergencies and responds to them safely.
- Ensures that continuity of care can be provided for the patient's problem, e.g. through adequate record keeping.

Managing medical complexity
- This is about aspects of care beyond the acute problem, including the management of co-morbidity, uncertainty, risk and health promotion.
- Manages health problems separately, without necessarily considering the implications of co- morbidity.
- Identifies and tolerates uncertainties in the consultation.
- Attempts to prioritise management options based on an assessment of patient risk.
- Manages patients with multiple problems with reference to appropriate guidelines for the individual conditions.
- Considers the impact of the patient's lifestyle on their health.

Working with colleagues and in teams
- This is about working effectively with other professionals to ensure good patient care and includes the sharing of information with colleagues.
- Shows basic awareness of working within a team rather than in isolation.
- Understands the different roles, skills and responsibilities that each member brings to a primary health care team.
- Respects other team members and their contribution but has yet to grasp the advantages of harnessing the potential within the team.
- Responds to the communications from other team members in a timely and constructive manner.
- Understands the importance of integrating themselves into the various teams in which they participate.

Maintaining performance, learning and teaching
- This is about maintaining the performance and effective continuing professional development (CPD) of oneself and others. The evidence for these activities should be shared in a timely manner within the appropriate electronic Portfolio.
- Knows how to access the available evidence, including the medical literature, clinical performance standards and guidelines for patient care.
- Engages in some study reacting to immediate clinical learning needs.
- Changes behaviour appropriately in response to the clinical governance activities of the practice, in particular to the agreed outcomes of the practice's audits, quality improvement activities and significant event analyses.
- Recognises situations, e.g. through risk assessment, where patient safety could be compromised.
- Contributes to the education of others.

Organisation, management and leadership
- This is about understanding how primary care is organised within the NHS, how teams are managed and the development of clinical leadership skills.
- Demonstrates a basic understanding of the organisation of primary care and the use of clinical computer systems.
- Uses the patient record and on-line information during patient contacts, routinely recording each clinical contact in a timely manner following the record-keeping standards of the organisation.
- Personal organisational and time- management skills are sufficient that patients and colleagues are not inconvenienced or come to any harm.
- Responds positively to change in the organisation.
- Manages own workload responsibly.

Practising holistically, promoting health and safeguarding
- This is about the ability of the doctor to operate in physical, psychological, socio-economic and cultural dimensions. The doctor is able to take into account patient's feelings and opinions. The doctor encourages health improvement, self-management, preventative medicine and shared care planning with patients and their carers. The doctor has the skills and knowledge to consider and take appropriate safeguarding actions.
- Enquires into physical, psychological and social aspects of the patient's problem.
- Recognises the impact of the problem on the patient.
- Offers treatment and support for the physical, psychological and social aspects of the patient's problem.
- Recognises the role of the GP in health promotion.
- Understands and demonstrates principles of adult and child safeguarding, recognising potential indicators of abuse, harm and neglect, taking some appropriate action.

Community orientation
- This is about the management of the health and social care of the practice population and local community.
- Demonstrates understanding of important characteristics of the local population, e.g. patient demography, ethnic minorities, socio-economic differences and disease prevalence, etc.
- Demonstrates understanding of the range of available services in their particular locality.
- Understands limited resources within the local community, e.g. the availability of certain drugs, counselling, physiotherapy or child support services.
- Takes steps to understand local resources in the community – e.g. school nurses, pharmacists, funeral directors, district nurses, local hospices, care homes, social services including child protection, patient participation groups, etc."""

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
