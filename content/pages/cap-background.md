---
title: Cap/Background
type: page
categories:
- User Guides
source:
  title: Cap/Background
  url: https://eq2.fandom.com/wiki/Cap/Background
  history: https://eq2.fandom.com/wiki/Cap/Background?action=history
  revision: 507772
  revised: '2010-10-17T16:40:04Z'
  license: CC BY-SA 3.0
---

## What, why and how

[Combat System and Stat Cap Improvements - Official forum post on 9/28/2006](http://forums.station.sony.com/eq2/posts/list.m?topic_id=267128)

As is usually the case when you see me posting about EverQuest II and how it all works internally, for the most part my direct involvement is at the conceptual level.  The "whats" of what we're going after and the "why."  The down and dirty "how" is usually the much more difficult part.

It's easy to help identify a problem and write a sentence.  It's sometimes an excruciating amount of work to make that sentence come true and then communicate it in a way that's relevant to the intended audience.

For the detailed plans, the implementation, as well as the detailed explanations given below, I wanted to make sure that the distinction was made.  What you see below is, as with most of the things I post about, the result of a lot of hard work of some amazingly dedicated people, with whom I'm exceedingly proud to be working.

The message below is something we'll be making a large part of our beta testing for Echoes of Faydwer.  It will eventually impact everyone and it solves a number of issues that people have with combat and progression in EverQuest II

We wanted to make sure the goals and details were made public as soon as possible, as they answer a number of ongoing questions regarding the state of combat in the live game.

In addition to being a part of our beta testing for Echoes, these improvements will also be available on the Test Server, prior to the launch of Echoes of Faydwer.  Rest assured that whether or not you get into EoF beta, you will be able to see these changes firsthand on Test.

- Scott

## Combat System and Statistic Cap Improvements for EoF launch

While working on Echoes of Faydwer, as well as observing and participating on both the Standard and Player vs. Player servers, we've spent time over the past months evaluating many elements of combat in EQ2, with an eye on two things:

- What isn’t working, both from the point of view of the players as well as that of the devs?
- What can we do about them in a way that will enhance the EQ2 experience?

There are many cases where players and devs have been in agreement about what would benefit the most from improvement.  We’d like to talk about some changes coming to a number of these elements, across all zones, not just those in Echoes of Faydwer.

For those who might be a nervous when seeing the words “combat” and “changes,” used in the same sentence, we’d like to assure you that that this is nothing of the scale of what occurred last year where some systems were replaced wholesale and class abilities changed significantly.

What you’ll be reading about below are extensions and improvements to existing systems, and our sincere desire to be as open and forthcoming about them as possible.

Our overall goal is to enhance the long-term enjoyability of the game both for PvE and PvP players alike. This post will provide a brief summary explaining "what" will change, as well as detailed sections for those who prefer to dig into the "how" and "why".

## In Summary: "What are the goals?"

Here are the high-level issues and complaints that we’re looking to address.

- For many moderate players and beyond, the combination of spells and items in EQ2 has led people to reach stat caps early on and then not see improvement from upgrading buffs and equipment, which many view as unsatisfying.
- As people leveled up beyond 50, primarily in groups and raids, the disparity in survivability between plate classes and everyone else progresses in a way that leads to considerably un-fun one-shot death for many classes.
- Caster skill improvements are not as much fun as they could be and do not have as much practical use as they should.
- The PvE issue of NPC mitigation dovetailed with the persistent issue of casters vs. melee on the PvP servers, and both can be addressed with the same system changes.  Mitigation is the word that we use when we refer to both Armor Class and Resistances.  They’re both mitigations, just against different types of damage.

## In Detail: "How are they changing?"

### Damage Mitigation and Resistance

- Maximum mitigation/resistance numbers for current level has been increased from [ Level*  80 ] to [ Level*  150 ]
- Damage mitigated now has diminishing returns, with the break-even point set at 4000 for level 70 players

### Stat Caps

- All stat cap maximums have been increased from [ 7*  Level + 20 ] to [ 15*  level + 20 ]
- Stat benefits are now on a diminishing returns curve
- The maximum benefit that each stat provides, including power pool size, has been increased
- Classes that use multiple stats for power pools have had their maximum power possible increase by up to +25% if they are high enough in both stats. This is to offset the difficulty of having to increase multiple stats

### Avoidance Skill

- Skill caps have increased from [ 1*  Level ] to [ 1.5*  Level ]
- Base Parry chance has been lowered from 10% to 5%
- Base Deflection chance has lowered from 30% to 25%
- Increases to avoidance skills now have diminishing returns similar to the changes made for mitigation/resistance. Players experience more gains in avoidance when further away from the cap, and less gains as they reach closer to the cap

### Casting Skill

- Skill caps have increased from [ 1*  Level ] to [ 1.5*  Level ]
- Uses a diminishing returns curve similar to avoidance skills
- Actual hostile spell resistance modification has increased from -10% to -20% at maximum
- Beneficial spells that use casting skill, mostly affecting ministration, have their power costs reduced with increased skill
- Fizzle nevermore! The entire Fizzle mechanic has been removed

### Focus Skill

- Skill caps have increased from [ 1*  Level ] to [ 1.5*  Level ]
- Focus has a maximum 20% instead of 10% to prevent damage interrupts
- Focus Skill also mitigates the chance of spell based Interrupts, Stifle, and Stun Effects from interrupting a spell that is already casting

### Attack Skill

- Skill caps have increased from [ 1*  Level ] to [ 1.5*  Level ]

### Attackspeed/DPS

- Attack speed and DPS caps have increased to 200%
- Uses a diminishing returns curve to determine the actual amount of attackspeed and DPS modification, which caps out at 125% actual modification when reaching the cap

Creatures will have their damage values adjusted to account for the changes to mitigation.

## In Detail:  "Why these things?"

- Cap issues for avoidance skills, casting skills, mitigation, stats, and haste:
  - Many players spend most of their time with maxed out stats and skills.  This creates a few problems:
    - The game is not as satisfying to play when there is a diminished sense of progression as people gain new and more powerful items and spells.
    - Equipment doesn’t feel as interesting when it’s “just a different way to hit the cap I’m already at.”
    - Encounters have needed to be designed with the expectation that caps are always reached
- Increases in Mitigation and Avoidance as one comes closer to the cap cause characters in that range to become exponentially stronger
  - This created a huge gap between the well-equipped and poorly equipped characters, where small increases in mitigation and avoidance had little impact on the lower end of the spectrum, but made huge leaps in power at the higher end. This causes several other problems:
    - It contributed to the effect that getting better gear does not make much difference in success.
    - It forced raid encounters to have incredibly high damage,output along with special abilities that overcome all mitigations to negate those large gains. This leads to a lot of one-shot kills against classes with low mitigation (mages primarily).
    - It forced named raid encounters to have increased melee attack skills, which unfairly affected classes that rely more on avoidance.
    - Cloth and Leather armor wearers were effectively double penalized because increasing their mitigation values gave less benefit per-point than did Chain/Plate.

- Casting Skill bonuses were not balanced in relative benefit that is granted through Melee and Avoidance Skills
  - Casters did not have as much incentive to increase their casting skills as melee classes because they did not receive as much benefit when reaching their caps. This resulted in bonuses to skills that favored melee classes much more than casters, which is more apparent in raid situations and fighting overcon encounters. Some of the specifics:
    - Offensive casting skill increases were only half as beneficial as the increased chances to hit offered by melee skill increases.
    - Debuffing casting skill was also only half as effective as debuffing melee skills.
    - The Fizzle mechanic filled a gap where beneficial spells did not need a resist check, so Fizzle became a ‘beneficial resist’ chance that could be mitigated with increased skill. It ended up being more of an annoyance than adding any interesting gameplay.
    - Focus skill had very little impact on damage interrupt rates, and the sources of most interrupts were unavoidable in the form of spell interrupts, stifles, and stuns.
    - PvP combat became heavily skewed towards melee classes because of non-damage interruptions, fizzles, and resist mechanics.
  - To address many of these issues, we re-evaluated how mitigation, avoidance, stats, and other systems could be modified for better progression and game balance. Some of the general changes are listed below:
    - Most caps have been increased by 50% to 100%
    - The use of diminishing returns curves has been added instead of using a linear progression. This provides greater benefits at the low end and slows down as the player nears the cap.
    - There was a re-evaluation of what casting skills affect.
    - Characters that have mitigation, stat, or skill values that are around 40% of the new cap will not experience much change for that particular system. That is the typical break-even point where the old linear line and the new diminishing returns curve intersect. Players above the break-even point are often raid equipped and will see less benefit initially, but the new maximum caps yield the potential for achieving even greater benefit than before.
  - A diminishing returns curve is not a ‘soft cap’ because there is no point on the curve where there is a sudden shift in how much benefit is returned. The break-even point can be used as a reference to how these changes will affect your character.

## Example: Mitigation and Longevity

To illustrate how diminishing returns help solve the problem of linear progression for mitigations, take a look at the benefits of two level 70 characters that increase their mitigation by the same amount in the old system:

- Player A increases their mitigation from 2000 to 2600. A change of +600, or +8.5% mitigation
- Player B increases their mitigation from 5000 to 5600. A change of +600, or +8.5% mitigation

Even though it looks like Player A and B received the same amount of benefit, Player B gained more than 3 times as much effective benefit with that same amount. How is that possible?

The change of mitigation Player A experienced granted them 13.6% more length of time to live, which we will refer to as Longevity. The change of mitigation Player B experienced granted them 42.9% additional longevity than they previously had. This is because Longevity is determined by the equation: [ 1 / ( 100 - Mitigation% ) ]

What results is that players that are very well equipped grow exponentially stronger than those that are not as well equipped. This causes these very well-equipped players to solo heroics with relative ease, and raid encounters must be designed to deal incredible amounts of damage that often one-shot kill other players in an area effect that do not have a minimum amount of mitigation for that encounter, especially mage classes.  Cloth-wearers obviously won’t be tanking, but we don’t want them to get crushed if they take a single hit.

Using a diminishing returns curve for mitigation balances it in such a way that players that are further away from the cap receive more benefit per point of mitigation than does a player that is near the cap.

Another way of looking at this from the perspective of a level 70 player after these changes:

A player below 4000 in a mitigation type will experience more benefit than they did before, and a player above 4000 in a resist type will experience smaller gains in their damage reduction than before. 4000 is the level 70 break-even point where the old linear line and the new diminishing returns curve meet that returns the same benefit before and after the changes.

- Player A increases their mitigation from 1000 to 1600. A change of +600, or +9.75% mitigation
- Player B increases their mitigation from 2000 to 2600. A change of +600, or +6% mitigation
- Player C increases their mitigation from 5000 to 5600. A change of +600, or +2.15% mitigation

- Player A = 15.4% increase in changed longevity (this benefits mages a lot more than before)
- Player B = 9.6% increase in changed longevity
- Player C = 6% increase in changed longevity

Generally speaking, 40% of the new cap is roughly the break even point on most of these graphs for all of the new diminishing returns graphs for resists, stats, and skills.

## Finally...

We hope that this background is useful, both for communicating our thoughts on the huge subject that is “Combat in EverQuest II,” and also useful a tool by which you can gauge the changes and continue to provide feedback on what it is that’s coming to the Test Server, in Beta, and beyond.
