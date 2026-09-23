---
title: Combat Mitigation
type: page
categories:
- Stats
source:
  title: Combat Mitigation
  url: https://eq2.fandom.com/wiki/Combat_Mitigation
  history: https://eq2.fandom.com/wiki/Combat_Mitigation?action=history
  revision: 1994881
  revised: '2026-04-08T22:05:25Z'
  license: CC BY-SA 3.0
---

Now, that's a tough one. Combat Mitigation (CM) is the most shady, hence the most annoying part of current EQ2 Combat Mechanics. This article will help you figure out Encounters' Combat Mitigation values and how it affects your Abilities.

## Detect Weakness

To figure out CM values of any given encounter your character must be a Vah Shir or a Scout with enough AAs to use "[[Detect Weakness (Assassin Subclass Prestige)|Detect Weakness]]" ability. Once used, you will find the following info in your chat box:
![](images/Cm_caith.png)
![](images/Detect_weakness.png)

Now you know Caith's CM and you probably don't want to fight him…

So, what does CM actually do? Well, the more CM the encounter has, the less of your Potency, Crit. Bonus, Fervor & Ability Modifier is really used to calculate damage & healing in combat. This also means debuffs like [[Brittle Armor II|Brittle Armor]] are extremely important when grouping or raiding.
The above is sufficient to understand that undergeared characters are not welcome to some content.  Rule of thumb:
Your Potency should be higher than encounters' Combat Mitigation

## Mechanics

### Damage Formula

The damage your abilities deal unoficially follows this formula:
Damage=spell_value×(1+(Pot-**c**)/100)×((**cb_base**+Cb-**b**)/100)×(1+(Fervor+prof.Fervor-**a**)/100)×
×(1+(**Main_att**/100))+[((**cb_base**+Cb-**b**)/100)×(1+(Fervor+prof.Fervor-**a**)/100)×ABMod]
alternative form:
Damage=[((**cb_base**+Cb-**b**)/100)×(1+(Fervor+prof.Fervor-**a**)/100)]×
×[spell_value×(1+(**Main_att**/100))×(1+(Pot-**c**)/100)+ABMod]]
spell_value is a function of [[Understanding Your Character#Skills|Combat Skills]], but it's a matter of different topic.
**cb_base** changes per adventure class per ability type, mouseover you Crit.Bonus in character window to find it. **Main_att** can be found similarly: mouseover your primary parameter.

0 ≥ **Main_att** < 300
100 ≥ **cb_base** < 150
**a** - mitigated Fervor
**b** - mitigated Crit.Bonus
**c** - mitigated Potency
prof.Fervor includes effectiveness
Examples of effectiveness:
![](images/Eff_mini.png)

### CM and a,b,c

Unfortunately a(CM), b(CM), c(CM) follow some kind of a not yet derived log? formula and also depend on encounter difficulity: Raid/Challenge/Solo

### Finding a,b,c

Finding mitigated values in game requires applying the above formula and having killed [[Victory: The Abandoned Labomination (Challenge)|Labomination]] a few times ^^

![](images/FoV.png)
In order to figure out a,b,c you need to parse a spell/ an ability in-game. This spell/ability shouldn't be modified by ability modifier and have no spread. Second line of damage in sorc's "Flames of Velious" is the best candidate I could find. You can also parse some Combat Arts under "Combat Mastery" effect as an alternative.

The circled yellow is formed by the following part of formula:
Damage=spell_value×(1+(Main_att/100))×
×(1+(Pot-**c**)/100)×((**cb_base**+Cb-**b**)/100)×(1+(Fervor+prof.Fervor-**a**)/100)
Now, approach any encounter to figure out it's  **a**,**b**,**c**:

1. Make sure your character is stripped off AAs/procs that can skew your results
1. Make a hit, remember the damage as Damage_observed_1
1. Keeping else equal, change only one paramater, let's say, you decided to change fervor.
1. Make another hit, remember the damage as Damage_observed_2
- difference in your parameters should be noticeable. Don't change fervor by 0,1 or Potency by 1

You've got 2 equations:

1. Dmg_obs_1=spell_value×(1+(Main_att/100))×(1+(Pot-**c**)/100)×((**cb_base**+Cb-**b**)/100)×(1+(Fervor_1+prof.Fervor-**a**)/100)
1. Dmg_obs_2=spell_value×(1+(Main_att/100))×(1+(Pot-**c**)/100)×((**cb_base**+Cb-**b**)/100)×(1+(Fervor_2+prof.Fervor-**a**)/100)

Divide (1) by (2) as they're part of one system, and cancel out unnecessary parts:
(Dmg_obs_1)/(Dmg_obs_2)=(1+(Fervor_1+prof.Fervor-**a**))/(1+(Fervor_2+prof.Fervor-**a**))
You know every variable in this equation to find "**a**" Do similarly for **b** & **c**:
(Dmg_obs_3)/(Dmg_obs_4)=(**cb_base**+Cb_1-**b**)/(**cb_base**+Cb_2-**b**)

(Dmg_obs_5)/(Dmg_obs_6)=(100+Pot_1-**c**)/(100+Pot_2-**c**))

Now you have all the necessary instruments & info to properly evaluate your stats in combat, not just by the Training Dummy!

### Practical application

Now think about how severely mislead are player when told something like "1Cb ~ 25Potency" out of context. Proper ratios for your character depend on all variables used in [[Combat Mitigation#Mechanics|Formula]]. Let's see some examples, leaving out tiresome calculations.
If you approach Emperor Ssraeshza[Challenge] with provided stats, the following ratios are true for you:
**a**=475;**b**=9280;**c**=307307;  [09/09/21]
400000=Potency; 19000=Crit.Bonus; 700=Fervor; 115=prof.Fervor
1Cb ~ 9,4Potency
1Fervor ~ 22,43Cb
1Fervor ~ 211Potency
However for a Training Dummy ratios are different:
**a**=0;**b**=0;**c**=0; Training Dummy; same stats
400000=Potency; 19000=Crit.Bonus; 700=Fervor; 115=prof.Fervor
1Cb ~ 21Potency
1Fervor ~ 21Cb
1Fervor ~ 441Potency

Context matters!

## Heals & Wards

TBA

### Chaotic Leech

TBA
