# Risk assessment for the entire complete system.

## A fitness and health website.

### Categories:

### Physical:
- Something happening to team members, their computers, gitlab servers explode!

### Technical:
- gitlab delete, wrong merge, corrupted data, DB goes down, skynet takes over.

### Nature:
- Phenomenon in nature, earthquakes, pandemic, super storms freeze the planet.
    
### Business:
- direct financial loss, damage to brand or reputation, violation of customer or
- regulatory constraints, potential liability, and increase in development costs.

### Likelihood scale 1-10:
- 1 = almost never happens
- 10 = most certainly will happen

### Impact scale 1-10
- 1 = almost no impact at all
- 10 = website needs reworking from the ground up.

### Here are a couple of guidelines that can help quantifying likelihood, impact, prevention, mitigations:

### Likelihood:     	
- How likely is it that the risk will happen? Do you think that the chance is remote, or very likely to happen?

### Impact:     	
- What is the negative impact if the risk does occur? Is there general discomfort for the team, or is it back to the drawing board for some significant rework?

### Preventions:
- Have backups for data loss, have well documented code if another team member has to continue other members gode.

### Mitigations:
- What is the best allocation of resources?


### Example:

**Risk:** Team member gets sick (normal sick)
**Category:** Physical
**Likelihood and scale [3]:** It’s not uncommon for people to get sick.
**Impact and scale[3]:** One team member is off for a few days is not that big of a deal.
**Preventions:** daily stand-ups, well documented progress, clear and clean code, code properly committed to the repo
**Mitigations:** workload from the sick member need to be distributed evenly among the others, depending on the workload.

Template:

**Risk:** 
**Category:**
**Likelihood and scale [x]:**
**Impact and scale[x]:** 
**Preventions:**
**Mitigations:**

----------------------------------------------------------------------------------------------------------------------------
1.
- **Risk:** Team member leaves the team.
- **Category:** Physical 
- **Likelihood and scale [3]:** not too likely that a team member leaves the team.
- **Impact and scale[4]:** depends on the size of the team, since we are a team of 8, the impact will be noticeable.
- **Preventions:** have group meetings and often or daily to see the morale of the group
- **Mitigations:** don’t have people in very specialized jobs so they can’t be replaced, if that happens have a well documented “how to” for each job.

2.
**Risk:** Database gets deleted 
**Category:** Technical
**Likelihood and scale [3]:** Highly unlikely but in the case of accident or bug this can happen.
**Impact and scale[8]:** If this happens all the customers lose their data everything they have created so far on the website. If not handled within the day this can ruin the reputation of the website
**Preventions:** Have inplace checks for if any deletion is performed on the database, even only let one or two individuals have the power to delete from the database.
**Mitigations:** Have 12 even 6 hour backups for the database so that they can be set up right away. 



3.
**Risk:** website uptime is below 99.9%
**Category:** Technical
**Likelihood and scale [1]:** The website being hosted on a server farm with backups this is very unlikely
**Impact and scale[8]:** The cost for a few minutes unscheduled downtime can be immense and website can get a bad reputation if this happens repeatedly 
**Preventions:** Have inplace load balance on the website so if there is too much traffic, DDoS prevention. Tag team of servers, one is hosting and the other is ready to boot if the other goes down.
**Mitigations:** If there is an unscheduled downtime, a backup of the whole system is saved and stored in a very secure location. Backup server is booted up with the backup data from the downed one.

4.
**Risk:** Pandemic
**Category:** Nature
**Likelihood and scale [2]:**  Worldwide pandemics are few and very far between (100 years or so) Ironic that we are in the middle of one right at this moment in time.
**Impact and scale[3-5]:** People working from home should make that much impact but it will be noticeable, people getting sick or even dying has more impact and needs major actions.
**Preventions:** As individuals, we all need to take care of ourselves and stay home. Wash our hands and don’t go outside unless you have to. Follow whatever rules are given out by the  health organization.
**Mitigations:** Workload needs balancing and deadlines need pushed back to give room for changes in surroundings.

5.
**Risk:** Sponsors that want to place ads on the website, cancel.
**Category:** Business
**Likelihood and scale [3]:** likelihood is not very high, fitness brands want to place ads on highly active websites
**Impact and scale[2-3]:** Smaller bands will not have that much impact and others can be put in their place. Bigger brands are impactful and other brands need to be contacted.
**Preventions:** Clear communication with brands and set amount of rules from the contract need to be met at all times.
**Mitigations:** Capital needs to be saved for those times when and if a big brand pulls out.






6.
**Risk:** User data leaked
**Category:** Technical
**Likelihood and scale [1]:** The data that is collected from users is minimal but it's important nonetheless. Banking information is never to be public.
**Impact and scale[7]:** The reputation after such a breach is hard to recover and will take months to build up again. To gain the public's trust again will take time and effort. 
**Preventions:** All data under GDPR will be held to the highest standards
**Mitigations:** Major PR, and a public apology is the only course of action. Going beyond GDPR standard.

7.
**Risk:** Office space rent doubles
**Category:** Business
**Likelihood and scale [4]:** Renting an office space should be pretty easy but when real estate moguls buy and sell office buildings they sometimes will raise the rent.   
**Impact and scale[6]:** Doubling in rent as severe financial impact on the company  
**Preventions:** Contracts that state that raise in rent can never be more than 10-15% per year. Contracts can be made void so having a backup office in sight is a valuable thing.
**Mitigations:** Special fund made for this, have other office spaces lined up 

8.
**Risk:** Less than careful CFO takes company money
**Category:** Business
**Likelihood and scale [4]:** This is very unlikely as there is not going to that much money to take but if not careful with appointing CFO this is a real possibility
**Impact and scale[8]:** Depending how much money is lost this could mean the office rent cant be paid or ever hosting service or housing for servers. 
**Preventions:** Don't have a CFO, let bigger financial companies handle the money side of the business. The power to take money from the company is spread to its founders, at least two people.
**Mitigations:** Very good relation with our bank of choice and ask for a loan.

9. 
**Risk:** Volcano
**Category:** Nature
**Likelihood and scale [5]:** Volcano is a very common occurrence in Iceland, a volcano erupts roughly every 10 years but, their magnitude varies. 
**Impact and scale[3-8]:** It really depends on where the volcano erupts and how much ash it spreads. Ash could get into the cooling system for the datacenter and overheat the servers. Ash is a very fine dust so it could easily clogg the airflow filters. Molten lava could enter the buildings. Large numbers of people might migrate so less employees.
**Preventions:** Store the data in multiple locations.
**Mitigations:** Backup the data and rent space in another datacenter. 

10.
**Risk:** Earthquake
**Category:** Nature
**Likelihood and scale [6]:** Earthquakes, like in the “volcano” stated above, are a very common occurrence here in Iceland.
**Impact and scale[2-5]:** Earthquakes here in Iceland are most of the time below 5 on the richter scale so the impact will be low. But now and then a large scale earthquake occurs.
**Preventions:** The workplace and datacenter should be built with strong rebar concrete to minimize impact. The datacenter could also have some sort of a spring or airbag foundation to capture the shaking.
**Mitigations:** Backup the data and tell employees to move to a doorway or hide under something.

11.
**Risk:** Malware, ransomware
**Category:** Technical
**Likelihood and scale [4]:** Blackhat hacker groups and individuals are always trying to break into databases to steal data. But, antivirus software is very efficient nowadays so it happens rarely.
**Impact and scale[9]:** Total shutdown of the website and databases. Employee and user personal data might be compromised, possible lawsuits. 
**Preventions:** Good antivirus software and keep some systems and or data isolated to minimize impact. Regular updates.
**Mitigations:** Contact law enforcement if it is a ransom issue. Do a full system analysis to check where the breach happened and check what was stolen and or corrupted.

12.
**Risk:** Cancel culture
**Category:** Business
**Likelihood and scale [1-3]:** A company has to make a really bad political decision and that rarely happens but always a possibility if the company doesn’t follow the “social rules” and or trends.
**Impact and scale[8]:** Social media will quickly spread the word of what was said and what happened and encourage others to boycott the company. Users, investors and sponsors will leave and if the company is public, the stocks will crash. 
**Preventions:** Hire a PR department and review every announcement and or public statement the company gives. If an employee does something considered bad or risky for the company, have a solid contingency plan in place.
**Mitigations:** Either hope for the media storm to blow over and assess the damage or prepare a public apology and fix the issue regarding the “cancel”.





13.
**Risk:** Food poisoning  
**Category:** Physical 
**Likelihood and scale [2]:** This would likely be a small company so is very unlikely for it to have a cafeteria with hot food but, it might hold some sort of a work party with food or employees gathering to go out and grab food from the same place.  
**Impact and scale[3-5]:** If the food served in the work party is bad, it might affect many employees, so the company will be short on staff. It might lower the production dramatically. 
**Preventions:** Be sure to get the food from a respected institution and follow basic hygiene rules around food.
**Mitigations:** Get the sick employees the help they need, to get them well as soon as possible and consider hiring temporary workers to fill in.

14.
**Risk:** Bad future investments
**Category:** Business
**Likelihood and scale [3]:** Risky investments are rare for a company of this size but it might make some drastic changes on the website for the worse.
**Impact and scale[3-8]:** If the investment involves money in stocks or in some merger, it might lead to the company having to file for bankruptcy or sell for well below market value. If the investment involves a change in policy or website functionality, it could lead to a drop in revenue but it’s easy to change back to the original look or policy.
**Preventions:** Always do a full risk assessment on any investment and if it’s some sort of a change to the website, beta test it. Have some sort of a special fund made for this.
**Mitigations:** If it involves money, use the backup funds and consider getting some sort of a loan. If the beta test fails, cancel the update. 

15.
**Risk:** Bug in the code
**Category:** Technical
**Likelihood and scale [1-10]:** Human error can happen at any time and the smallest bugs can have the largest repercussions  
**Impact and scale[1-10]:** This small or large bug or security flaw can be a misspelling of a name or something that makes the site not work at all.
**Preventions:** Code review is very important and should be done by multiple people as should tests be performed before merging with the release branch
**Mitigations:** have the ability to rollback the release version easily so that the bug can be found and worked on
