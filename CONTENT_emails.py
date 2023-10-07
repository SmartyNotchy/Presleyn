from imports import *


class WelcomeToClementeEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Welcome to RCMS!"
    self.sender = "Golden Hawks Team"
    self.contents = '''\
Welcome to RCMS! We hope you make the most of your
learning experience and stay.

Some classrooms are not open to instruction as of
this moment, unfortunately. Please do not attempt
to enter these classrooms. All locked classrooms
will have a "Locked" sign on their door!'''

    self.starred = starred
    self.unread = unread
    
class NursesOfficeEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Healing Opportunities"
    self.sender = "The School Nurse"
    self.contents = '''\
Feeling sick after losing a spell battle?
Counselors can help with the emotional trauma,
but for a low, low ticket price, the Nurse's
Office can dispell any physical injuries you
might suffer!

Pricing:
Health Lost / 5 + 20 (Rounded Down)
Additional 50 ticket tax if healthcare has been
administered previously without charge.
'''

    self.starred = starred
    self.unread = unread


class IEDOverdoseEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Oh Noes, IED Overdose!"
    self.sender = "Pilliam Wark"
    self.contents = '''\
Welcome to the IED classroom! I hope you are excited to 
learn about all your favorite topics such as tonal 
shading, 3D modeling in OnSpace, and how to use a dial 
caliper. Make sure that all your answers on every test 
are accurate, they don't have to be precise. As a 
reminder, whenever there is a big project spanning 
multiple weeks, make sure to enhance the likelihood of 
getting a good grade by dressing up your project as a 
certain member of the Animalia kingdom.
'''

    self.starred = starred
    self.unread = unread

class PoolesvilleAcceptanceEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "SMCS Acceptance Letter"
    self.sender = "Pilliam Wark"
    self.contents = '''\
Congratulations, you just got accepted to Poolesville!

Never gonna give you up,
Never gonna let you down,
Never gonna run around,
(...)
'''

    self.starred = starred
    self.unread = unread

class MESAEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Sproglet MESA"
    self.sender = "Poorvi Deshpande"
    self.contents = '''\
Please submit the electronic display board for the 
MESA project. I don't want another late assignment.
'''

    self.starred = starred
    self.unread = unread

class MESAFollowUpEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Sproglet MESA (Follow Up)"
    self.sender = "Poorvi Deshpande"
    self.contents = '''\
Sorry, that previous email wasn't ment for you. Please 
ignore it, Goran still hasn't fixed his email software.
'''

    self.starred = starred
    self.unread = unread

class RainbowHawksEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Rainbow Hawks Meet TODAY!"
    self.sender = "No Reply"
    self.contents = '''\
The Rainbow Hawks (RCMS' Gender and Sexuality Alliance) 
will meet today, Wednesday, May 3rd. The Rainbow Hawks 
club is open to any student,  whether they are a member 
of the LGBTQ+ community or an ally. We plan for exciting 
school events, offer a fun and safe space, and also 
educate our community on LGBTQ+ issues. The Rainbow 
Hawks will continue to meet on the first Wednesday of 
the  month after school. We look forward to seeing you 
there! Please see Mr. Spinach with any questions.  
'''

    self.starred = starred
    self.unread = unread

class CodeHSAnswersEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Gib me codehs answers"
    self.sender = "Henry Pu"
    self.contents = '''\
Please gib me codehs answers
my comp sci grad suffr
i no want bad grade in comp sci
tank you
'''

    self.starred = starred
    self.unread = unread

class AssignmentGradedEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "AG: Inheritance Coding(10)"
    self.sender = "Ms. Ramasamy - Computer Science"
    self.contents = '''\
Your assignment PA - Inheritance Coding(10) has been 
graded.

graded: May 2 at 1:59am
score: 9.5 out of 10.0
comments: "At least you aren't Katherine... who cares 
about a measly 0.5pts."
'''

    self.starred = starred
    self.unread = unread

class BrainSTEMOrderEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "BrainSTEM Order"
    self.sender = "Anna Zhou"
    self.contents = '''\
Dear Peter Zhao,

This is your confirmation email that your order to sacrifice 
the local oprhanage has been received.

ORDER ID: 17
STATUS: PENDING
Please expect further details to be sent out no later than 
11:59 PM, February 31st, 2023 (EST).

Thank you for working with brainSTEM.
'''

    self.starred = starred
    self.unread = unread

class BrainSTEMOrderFollowUpEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Sorry man."
    self.sender = "Anna Zhou"
    self.contents = '''\
Oh oops I sent that email to the wrong person.
Please ignore man, thank you.
'''

    self.starred = starred
    self.unread = unread

class RCMSLoreEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "RCMS Lore Updates"
    self.sender = "Jerry Wong"
    self.contents = '''\
Canonically in the RCMS lore, Jashlee is Anna's sister.

Just in case you wanted to know.

- Sherry Wang (Pen Name: Jerry Wong)
'''

    self.starred = starred
    self.unread = unread

class WantedCriminalEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Wanted Criminal"
    self.sender = "Erin Presley"
    self.contents = '''\
If you have any insight on a certain individual that
goes by the name of 'Jerry Wong', please contact me or any
team leader. They've been on the loose for tax evasion by
avoiding paying SGA funds to license songs from the 
Korean Boyband, BTS, during the school dance.
'''

    self.starred = starred
    self.unread = unread

class BaldastanEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Baldastan"
    self.sender = "Akshaj Eruventi"
    self.contents = '''\
Shareef Ganesh

<Mirza Sayf Baig Responded To This Email:>

  Bro Akshaj, stop sending these useless emails.
'''

    self.starred = starred
    self.unread = unread

class NameChangeEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Legal Name Change"
    self.sender = "Anna Zhou"
    self.contents = '''\
I have legally changed my name to Katherine, now 
I am Katherine Zhou.

<Katherine Xu Responded To This Email:>

    Excuse me?

    <Anna Zhou Responded To This Reply:>

      Why are all my emails sending to everyone?!?! 
      Goran, your email software sucks!
'''

    self.starred = starred
    self.unread = unread
    
class MagnetCohortEmail(Email):
  def __init__(self, starred, unread):
    self.subject = "Grapefruit Extravaganza"
    self.sender = "Ms. Tangerine"
    self.contents = '''\
Every year, in the spring, the grade 8 magnet cohort
has always endangered the lives of fellow Clemente 
students/teachers.

This time, they hoarded up grapefruits in the cafetaria
and launched them at unsuspecting teachers, resulting
in a huge mess.

We won't reveal the names of the students who 
participated in the act... AHEM... TYLER AND CHRIS.

Sincerely,
  Ms. Tangerine
'''

    self.starred = starred
    self.unread = unread
    


