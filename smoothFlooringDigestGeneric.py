import time
from sendEmail import *
import pickle
import datetime
import os
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

funFacts = list()
funFacts.append('\"Carpeted floors in schools and homes contained significantly more dust, proteins, and allergens than smooth floors.\"')
funFacts.append('\"Mite allergen concentrations in dust from carpeted floors were 6 to 14 times higher than in dust from smooth floors.\"')
funFacts.append('\"More house dust mite allergen in dust from carpeted classroom floors than from smooth classroom floors\"')
funFacts.append('\"Higher concentrations of allergens consistently found in carpets compared with smooth floors. Carpet vacuuming seems to remove larger particles but not the allergen-associated smaller particles whereas smooth floor cleaning appears more efficient regarding removal of these smaller particles.\"')
funFacts.append('\"Significantly higher concentrations of allergens from house dust mites have been reported in rooms with carpet floors no matter how the carpets were made compared to hard/smooth floors.\"')
funFacts.append('\"Levels of several antigens were statistically higher on carpet than on hard surfaced flooring. For dog and cat allergens, the differences were clinically significant, with mean levels on hard floors being well below proposed thresholds for allergic sensitization.\"')
funFacts.append('\"Carpeted floor held larger amount of antigens than non-carpeted floor.\"')
funFacts.append('\"Installation of carpets caused an increased exposure to allergens from house dust mites. Removal of carpets significantly reduced the levels of both mite allergens and ergosterol, a cell wall component of molds.\"')
funFacts.append('\"Carpeted floors, upholstered furniture and clothes were important reservoirs and sources of allergens, especially from dust mites and pets.\"')
funFacts.append('\"When comparing the recovery fraction obtained by vacuuming of standardized dust applied to various surfaces, significantly lower amounts were obtained from rough and porous surfaces compared with smooth and hard surfaces and with the lowest recovery from carpets.\"')
funFacts.append('\"The ratio between indoor air and outdoor air amounts of particulate matter (<2.5 mm) was significantly higher for classrooms with carpeted floors compared with classroom without carpet floor. This indicated that carpets may increase the amount of resuspended dust.\"')
funFacts.append('\"For particle size 3.0 to 10.0 µm, carpets exhibited higher resuspension fractions compared with hard floorings. The results support that people sensitive to allergens could select hard floorings to reduce exposure and adverse health outcomes.\"')
funFacts.append('\"Flooring type can significantly impact incremental time-averaged daily exposures to coarse and fine particles and that high-density cut pile carpeting resulted in the highest exposures.\"')
funFacts.append('\"Higher resuspension rates of particles from carpets compared to wood PVC and vinyl materials.\"')

funFacts.append('\"Personnel in schools with wall-to-wall carpet reported increased prevalence of eye and airway symptoms, face rashes, headache and abnormal tiredness compared with those in schools with hard floors. Removal of carpets caused several symptoms to decrease. Frequency of airway symptoms remained increased in the carpet group.\"')
funFacts.append('\"Floor covering, the shelf factor and the fleece factor were among several factors associated with the prevalence of symptoms (work-related mucosal irritation and work related general symptoms).\"')
funFacts.append('\"Pollution source was a 20 years old carpet. Removal of pollution source resulted in increased satisfaction with perceived indoor air, reduced prevalence of headaches and significantly faster typing of text. Reducing the pollution load was effective in improving comfort, health and productivity.\"')
funFacts.append('\"Carpets used as pollution source. Overall productivity increased with increased ventilation. Results show that maintaining good indoor air quality by controlling indoor pollution sources and ensuring adequate ventilation important for comfort, health and productivity.\"')
funFacts.append('\"An increase in adverse health effects was observed in offices where carpet was the main type of floor covering.\"')
funFacts.append('\"The risk of asthma was related to the presence of plastic wall materials and wall-to-wall carpet at work, the latter in particular in the presence of mold problems (adjusted OR = 4.64, 95% CI: 1.11, 19.4).\"')
funFacts.append('\"Cockroaches, carpet, pets, and in-utero exposures to ETS affected the timing of early-onset asthma.\"')
funFacts.append('\"Childhood respiratory infections associated with increased risk of asthma, chronic bronchitis and chronic cough. Several factors including wall-to-wall carpets were associated with increased risk of frequent childhood respiratory infections.\"')
funFacts.append('\"Individuals with early childhood asthma more likely to have lived in a house with carpet and more likely to report suffering a serious chest illness before the age of two compared to those with later asthma onset. Carpet exposure and suffering a serious chest illness concurrently before age two increased the individual risk even more.\"')
funFacts.append('\"Carpeted floors in the bedroom associated with increase in asthma readmissions (OR = 4.07, 95% CI 1.03 to 16.06).\"')
funFacts.append('\"Prevalence of wheeze was influenced by several factors where carpet covered floor in the child\'s bedroom was one.\"')
funFacts.append('\"Bedroom carpets were one of several indoor factors associated with higher prevalence of respiratory symptoms.\"')
funFacts.append('\"Wall to wall carpets in the bedroom was negatively associated with cough with phlegm, chronic cough, and attacks of dyspnoea.\"')
funFacts.append('\"Workers developed skin and/or airway problems after renewal of offices (new furniture and carpets). Removal of carpets significantly improved symptoms. Workers were examined in 2009 and re-examined in 2013. Chemicals from glued carpets suspected as trigger.\"')
funFacts.append('\"Carpet flooring may act as a “sink” for microorganisms resulting in a higher inflammatory potency of floor dust\"')

signOffs = list()
signOffs.append("Something to ponder")
signOffs.append("Something to consider")
signOffs.append("Food for the mind")
signOffs.append("Thoughts to chew on")
signOffs.append("Brain food")
signOffs.append("Ideas to reflect on")
signOffs.append("Something to muse over")
signOffs.append("Points to ponder")
signOffs.append("Thoughts to keep in mind")
signOffs.append("A morsel of wisdom")

sendDateTimeFileName = 'dateTimeFile.pickle'
sendTime = datetime.time(7,00,00)
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "senderEmail@example.com"
password = "enter password for sender email here"
receivers = ['reveiverEmail1@example.com','reveiverEmail2@example.com']# enter list of receivers

print('script started, waiting to send emails to: ' + ", ".join(receivers))

while True:
    setSendDate = True
    currentDateTime = datetime.datetime.now()
    if os.access(sendDateTimeFileName, os.R_OK):
        sendDateTimeFile = open(sendDateTimeFileName,'rb')
        fileLoadTestSucceeded = True
        try:
            sendDateTime = pickle.load(sendDateTimeFile)
        except:
            fileLoadTestSucceeded = False
        if fileLoadTestSucceeded and sendDateTime.time() == sendTime:
            deltaTime = sendDateTime - currentDateTime
            if deltaTime.total_seconds() > 0:
                if (deltaTime.total_seconds()/3600) <= 24:
                    setSendDate = False 
            else:
                funFact = random.choice(funFacts) #pick a random string from array of fun facts
                signOff = random.choice(signOffs) #pick a random signOff
                Body = 'Did you know?\n\nAccording to Norwegian Institute of Public Health,\n\n' + funFact + '\n\nMore information about the benefits of smooth flooring are available here: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5858259/\n\n' + signOff
                send_email(receivers, "Your Smooth Flooring Digest",Body,smtp_server,smtp_port,username,password) #send mail
                print('email Sent at ' + currentDateTime.ctime())                
        sendDateTimeFile.close()
    if setSendDate: #if setSendDate is True
        sendDateTimeFile = open(sendDateTimeFileName,'wb')
        today = currentDateTime.date()
        sendDateTime = datetime.datetime.combine(today,sendTime)
        if (currentDateTime - sendDateTime).total_seconds() > 0:
            sendDateTime = sendDateTime + datetime.timedelta(days = 1)
        pickle.dump(sendDateTime,sendDateTimeFile)
        print('saved datetime for: ' + sendDateTime.ctime())
        sendDateTimeFile.close()
    time.sleep(5)