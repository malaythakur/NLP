# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:33:58 2022

@author: Malay Thakur
"""

import nltk
nltk.download()
trafficRules = """
1. Do Not Drink and Drive

A statistic reveals that around 19 Indians are killed daily due to drunk-driving road accidents (source)
As per the current law, the blood alcohol limit permissible for driving is up to 0.03%, which is equivalent to 30 mg of alcohol per 100 ml of blood.
If an individual fails to pass this BAC test, he/she can be fined between Rs.2000 and Rs.10000, based on the final blood alcohol limit.
Moreover, such individuals may also be sentenced to a prison term ranging between 7 months and four years.

2. Always Own Valid Car Insurance Policy

According to the Motor Vehicles Act of 1988, all motor vehicles in India need to possess valid third-party insurance coverage at all times.
If you are not careful and the insurance policy lapses, you could be penalised for driving a vehicle without such a protection plan.
The traffic authorities charge a fine of Rs.2000 for a first-time offence of this nature. However, repeat offences can lead to penalties of up to Rs.4000.

3. Wear your seatbelt while Driving a Car

If you are new to driving, get in the habit of securing the seat belt as the first thing you do upon entering your vehicle. Doing so will not only help you avoid traffic violations, but it will also save your life in case of mishaps.
If you are caught driving without this seat belt around your waist and chest, traffic cops can fine you up to Rs.1000 for this violation on the spot.
So, be a hero and wear your seat belt!

4. Riding a Two-Wheeler without a Helmet On

One must wear a helmet at all times while riding a two-wheeler. One distinction to notice here is that the law states that all individuals on a two-wheeler must put on helmets and not just the driver.
Penalties for non-compliance with this rule come in the form of fines of up to Rs.1000.
In serious cases, traffic authorities may decide to suspend your license for a period of up to 3 months as well.

5. Using a Mobile Phone while Riding

As per the new Motor Vehicle rules in effect from Oct 1, 2020, drivers can only use their phones as a navigational tool while on the wheel.
If you are caught using the phone in any other fashion while driving, get ready to pay a fine of up to Rs.5000. A one-year prison sentence also applies to such traffic violators.
Get off your phone for a while and focus on the road!

6. Over Speeding

Drivers should never exceed the recommended speed guidelines on roads, as doing so will draw the ire of traffic cops.
As per a report, 66% of accidents in 2018 were caused due to speeding on Indian roads. (source)
The fine charged for speeding varies as per the size of your vehicle, typically ranging between Rs.1000 and Rs.2000.     

7. Jumping the Red Light

If you do not intend to bear penalties of up to Rs.5000 and a one-year prison sentence, ensure you stick to the various traffic signals during a drive, even if you are in a hurry. Remember the old saying, ‘better late than never.’
These are some of the most basic traffic laws for drivers. As a person behind the wheels, you need to follow several others as well.
Drive safe and adhere to all laws!
"""

#tokenizing sentences

sentences = nltk.sent_tokenize(trafficRules)

word = nltk.word_tokenize(trafficRules)
