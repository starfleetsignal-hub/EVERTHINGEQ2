---
title: Cap
type: page
categories:
- Skills
- Stats
- Terms
- User Guides
source:
  title: Cap
  url: https://eq2.fandom.com/wiki/Cap
  history: https://eq2.fandom.com/wiki/Cap?action=history
  revision: 1950500
  revised: '2026-01-05T17:55:56Z'
  license: CC BY-SA 3.0
---

## Stat Caps

Only 2 stats are used.  Stamina is used by all classes and gives you more hit points.  There is no cap on stamina.  In addition, each class has a primary stat that affects its damage output and power pool.  While the other stats may still be listed on your character sheet, they don't affect your character at all.

Fighters use Strength, Scouts use Agility, Mages use Intelligence, Priests use Wisdom

There is no cap on the power pool gained from your primary stat, but there is a soft cap and diminishing return curves on the damage bonus.  From 0 - 1200 on your primary stat, it follows the old diminishing returns curve that's been around since the game first launched.  The characteristics of that curve are that you get a pretty good boost up until 800, and then it flattens out until 1200.  At 1200 it makes a good jump again as it switches to the new curve.  Over 1200, a 30% increase in your primary stat will give you a 10% boost in damage.  As you can see, that gets into diminishing returns pretty quickly.

These numbers are for level 90 characters, I'm not sure how it works sub 90.  I suspect the old diminishing returns are in effect, which means you could potentially have a big gap below 1200 where you are seeing no gain until you get high enough to enter the new curve.

The +hit points and +power gained from stamina and your primary stat is a static amount per point. It scales up to a final amount of 10.0 @ L90.

## Skill Cap

- Skill Cap = 5*  Level
  - **Example:** A level 70 player has a skill cap of 350, which means that anything higher is considered over the cap.  As of GU61 Skills over their cap grant new bonuses.

1. Example1: A level 70 player has a skill cap of (5*70) or 350.
1. Example2: A level 80 player has a skill cap of (5*80) or 400.
1. Example3: A level 90 player has a skill cap of (5*90) or 450.
1. Example4: A level 95 player has a skill cap of (5*95) or 475

There is no hard cap for Crushing, Slashing, Piercing, or Ranged. These skills are contested against the target's defense and parry. The attacker needs 100 more points in their skill than the defender has in their opposing skill to receive the max amount of accuracy or avoidance based on combat skills. A Ranger would need 600 Ranged Skill to receive max benefit against a target with 500 Defense.

As of GU 61, having weapon skill over the cap now increases your minimum damage amount making it closer to the maximum amount.

As of sometime prior to GU66, the skill caps are not 6.5 per level, but 5 per level. I (Dedith) have tested this out on multiple characters as well.  Post on SOE's forums can be found [here](https://forums.station.sony.com/eq2/index.php?threads/help-with-skill-caps-pls.534711/).

|  |
|---|
| Offensive Skill (Over Base) - Variance Reduction Percentage - ToV Update |
| +100 - 2% |
| +1000 - 20% |
| +2500 - 30% |
| +5000 - 40% |
| base = Level x 5; eg. 475 at Level 95 |
| Variance Reduction increases the damage of the "lowest possible" on an ability or auto-attack. The low end is boosted while the high end remains the same. |

## Regen Cap

- In-combat HP Regen Cap = 3*  Level
- In-combat HP Regen Cap (from Items) = 3*  Level*  0.5
- In-combat Power Regen Cap = 1.5*  Level
- In-combat Power Regen Cap (from Items) = 1.5*  Level*  0.5
  - **Example:** A level 60 player is decked out in power regen items and has the equivalent of 50 power regen per tick thanks to her items. She is also in a group that has an Illusionist who is giving her another 50 power regen per tick. Since the cap from her items is 1.5*60*0.5=45, she only receives 45 power per tick from her gear. The cap for total power regen at her level is 1.5*60=90. With the 45 power per tick from her items, she would only receive 45 power per tick from her group buffs as well. Any additional buffs or power regen gear would have no effect on her power regen.

## Mitigation Cap

- Mitigation Cap = 150*  Level = 75%
  - Mitigation increases result in increasing returns until (52.5*  Level) at which point mitigation suffers from diminishing returns.

## Ability Modifier Cap

- Ability Modifier Cap depending on the damage/heal amount of the spell/ca/heals adds 50% of maximum damage
  - The ideal amount of Ability Modifier is equal to about 100% of the highest value of your highest spell/ca/heal. If you have more than that, it doesn't effect your spells/ca/heals any further (it is capped there), however note that many skills now have an unmodified (by AM) damage max of over 2 million, so reaching the 1 million AM cap may be tough in that case.
  - The damage shown in the tool tips when you hover the mouse over the spell or CA includes any Ability Mod that you have. To get the actual damage range of the spell/CA, subtract any Ability Mod that you have.
  - The maximum effective Ability Mod will be 100% of the highest value shown in the tool tip when your AM is not buffed by gear or anything else.
  - AOE spells only get a 33% maximum boost from Ability Mod.
  - Although Ability Mod affects Ascension Skills, the cap for those is currently astronomical (summer 2017), so calculate the cap from your highest non-Ascension skill.
  - See [[Ability Modifier]]

## Crit Chance Cap

- 100% Crit Chance = it will at least crit 100% of the time (not contested vs level)
- At 100% Crit, you will have a 1% chance to get a Legendary critical hit.
- At 500% Crit, you will have a 1% chance to get a Fabled critical hit.
- At 700% Crit, you will have a very small chance to get a Mythical critical hit.
- 1200% Crit Chance = Softcap of the Crit chance. (This "softcap" claim needs a reference because running in raid with 2K+ Crit Chance works well for Assassin DPS).
  - many will be legendary crit
  - some fabled crit
  - a few mythical Crit
- 6000% Crit chance = Hardcap?

- A Legendary Critical hit takes the damage you would have had with a normal one and increases it by 25%.
- A Fabled Critical hit takes the damage you would have had with a normal one and increases it by <s>100%</s> 65%.
- A Mythical Critical hit takes the damage you would have done with a normal one and increases it by <s>200%</s> 100%.

*Note change with [[Planes of Prophecy]] : To decrease the erratic spike damage we have increased the chance of obtaining a higher critical type, but decreased the higher critical bonus multiplier. The new multipliers are Legendary: 1.25 (unchanged), Fabled: 1.65 (down from 2), Mythical: 2 (down from 3).*

## Avoidance Cap

- Avoidance Cap = 80%
  - Base = 80%
  - Blocking = 70%
  - Parry = 70%
  - Deflection = 70%

Block (Non-Brawlers): A Block is based on the player's shield. The higher the protection rating, the higher chance to block. All block that is used by a non-Brawler class is uncontested, meaning it is a straight percentage chance to avoid an incoming attack.

Block (Brawlers): Brawlers have two types of Block. Contested block which is based on their Deflection Skill and level difference and Uncontested Block which is based off of their "Minimum Deflection Chance."

Parry: A parry is generally a contested roll based on the defender's parry skill and level compared against the attacker's weapon skill and level.

Riposte: There is a chance that any Parry will turn into a Riposte. A Riposte is a parry that also deals damage to the attacker. The base chance for a Parry to convert to a Riposte is 20%.

Dodge: A dodge is generally a contested roll based on the defender's defense skill and level compared against the attacker's weapon skill and level.

*The formula for determining avoidance based on the three subsets of avoidance is unknown at this time.*

## DPS / HASTE / FLURRY

|  |
|---|
| Damage Per Second - Damage Multiplier - Tears of Veeshan Update |
| 100 - 2x |
| 200 - 3x |
| 300 - 4x |
| 400 - 5x |
| 500 - 6x |
| 600 - 7x *Soft Cap* |
| 1000 - 8x |
| 1600 - 9x |
| 2300 - 10x *Hard Cap (as of Blood of Luclin, there is no hard cap* |

|  |
|---|
| Attack Speed - Flurry Chance - Tears of Veeshan Update |
| 100 - 100% faster |
| 200 - 125% faster *Hard Cap for faster attack, beyond converts into Flurry* |
| 300 - 6.8% *Flurry - as of Blood of Luclin, haste no longer converts to flurry* |
| 500 - 13.4% |
| 700 - 19.6% |
| 900 - 25.6% |
| 1200 - 31.4% |

Flurry Cap = 100%

## Multi Attack

|  |
|---|
| Multi-Attack Chance - Extra Swing Percentage - Tears of Veeshan Update |
| 10 - 12% |
| 20 - 22% |
| 30 - 33% |
| 40 - 43% |
| 50 - 52% |
| 60 - 61% |
| 70 - 69% |
| 80 - 77% |
| 90 - 84% |
| 100 - 91% |
| 110 - 97% |
| 120 - 100% + 2% |
| 130 - 100% + 7% |
| 140 - 100% + 11% |
| 150 - 100% + 15% |
| 160 - 100% + 18% |
| 170 - 100% + 21% |
| 180 - 100% + 23% |
| 190 - 100% + 24% |
| 200 - 100% + 25% |
| 300 - 100% + 35% |
| 500 - 100% + 45% |
| 700 - 100% + 55% |
| 900 - 100% + 65% |
| 1200 - 100% + 75% |
| 3400 - 100%  + 100% |

## AE Auto Attack

- Caps out at 100% = hitting multiple mobs 100% of the time when auto attack occurs.
- Main hand and offhand procs Ae Auto Attack.
- AE Autoattack hits up to 4 additional targets in front of you

## Hate Transfer

- Caps at 50%

## Hate Gain

- The cap for hate gain modifiers is 100%. => will be 300% once [[Renewal of Ro]] goes live
- The hate decrease modifier cap is 50%. => will be 150% once [[Renewal of Ro]] goes live

## Casting Speed - Doublecast Chance

|  |
|---|
| Casting Speed - Doublecast Chance convert |
| 100% - abilities/combat arts/spell will have their cast time halfed. *Hard Cap, beyond this converts to double cast chance - as of Blood of Luclin, spell doublecast is mostly removed and casting speed no longer converts* |
| 200% - 7.5% *double cast chance - prior to December 2019 update* |
| 400% - 15% |
| 600% - 22.5% |
| 800% - 30% |
| 1100% - 37.5% *Hard Cap ? - prior to December 2019 update* |

Doublecast Chance: 100% *Hard Cap - see following notes*

- Ability doublecast gives a percent chance for spells and CAs to deal damage twice.
- Spell doublecast gives a percent chance for spells (but not CAs) to deal damage twice.
  - Some abilities lists on the CA knowledge tab are affected by spell doublecast
  - Spell doublecast was mostly removed from the game in December 2019
- Neither doublecast allows procs to deal damage twice, even procs from class abilities
- Ability doublecast and spell doublecast are contested by mobs ability doublecast avoidance and spell doublecast avoidance, introduced with Planes of Prophecy expansion.
  - For example, Blood of Luclin solo instance mobs have 30% ability doublecast avoidance and 500% spell doublecast avoidance.

## Casting and Reuse of CA/Spells

The Speed Cap is 50% no matter if AA, Item or Buff it can't be less then 50% before modifiers of the base casting speed / reuse speed

- A spell or ca has a casting time of 10 seconds => Cap is 5 seconds as casting time
- A spell or ca has a recast time of 20 seconds => Cap is 10 seconds as reuse time
- The only known way to lower this Cap are certain AAs and abilities that affect the base casting speed or reuse speed.
  - For example, the Warden Epic 2.0 spell [[Nature's Grace]] which "Reduces the base reuse timer of all Combat Arts to 2 seconds."

Caps in detail:

- **Reuse Speed**
  - Spell and CA Reuse has a Cap of 100% Reuse speed

- **Casting Speed**
  - As of December 2019, spells and CA's have a casting speed Cap of 100%
  - Prior to December 2019, spells had a hard cap of 1100%, which granted 50% of the base cast speed (e.g. a spell of 2 seconds is reduced to 1 second cast time) plus 37.5% spell double attack no Cap, it can't be cast faster than 50% of the original speed but you gain Spell Double Attack Chance when your casting speed is greater than 100%

- **Recovery Speed**
  - Spell and CA Recovery has a Cap of 100% Recovery speed
  - Base recovery speed is commonly 0.5 seconds. The Cap is at 0.25 seconds

- **Amount of Triggers of Reactive spells**
  - Cap is +1 (before AA and Focus effects)
    - Reactive spells can't be Double Cast like DD or DoT, instead they gain +1 trigger but only if they haven't got +1 trigger already from AA or Focus effects
    - *Note: Most important for Coercer, they get 3 AA to add triggers to Hostage, Spell Curse and Destructive Mind which means double cast doesn't add an additional trigger because they are over the Cap allready*

## Note

- [[Cap/Background]] - A post from the offical forum about the last change
- [LU29 EOF Update notes](http://forums.station.sony.com/eq2/posts/list.m?topic_id=253135)

My cast time and reuse skyrockets with timewarp and UT running and i am over cap base stat buffs near double,i recomend researching and revising it may have a small return every so many points over.

## Game update 61

- Many stats now provide additional benefits to other stats!  See below for details:
  - Having parry skill over the level cap now gives a bonus to uncontested parry and uncontested riposte.
  - Having defense skill over the level cap now gives a bonus to uncontested dodge.
  - Having haste over the cap now gives a bonus to flurry.
  - Having weapon skill over the cap now increases your minimum damage amount making it closer to the maximum amount.
  - Having weapon skill over the cap now gives a bonus to riposte damage.
  - Having spell and combat art skills over cap now increases the minimum damage of those spells and combat arts making it closer to the maximum amount.
  - DPS is now a rating that translates into the actual increase to your melee damage with no cap. Mouse over the DPS stat in your persona window to see the actual percent increase to your damage.
  - Having spell casting speed over the cap now gives you a slight bonus to double cast spells.
  - Multi Attack is now a rating rather than a straight percent chance for additional attacks.  Mouse over the Multi Attack stat in your persona window to see how many extra attacks you get, and your chance for an additional attack on top of those.

### Overcap Stat Conversions

On 7/28/2012, designer Xelgad posted the following clarification to the conversion rates for the "overcap" stats:

**Parry Skill to Extra Parry Chance:**

- +200: 0.5%
- +400: 1%
- +600: 1.5%
- +800: 2%
- +1000: 2.5%

**Parry Skill to Extra Riposte Chance:**

- +200: 0.5%
- +400: 1%
- +600: 1.5%
- +800: 2%
- +1000: 2.5%

**Defense Skill to Extra Dodge Chance:**

- +200: 1%
- +400: 2%
- +600: 3%
- +800: 4%
- +1000: 5%

**Weapon and Spell Skills Increase to Minimum Damage Amount:**

- +100: 2%
- +200: 4%
- +300: 6%
- +400: 8%
- +500: 10%
- +600: 12%
- +700: 14%
- +800: 16%
- +900: 18%
- +1000:20%

**Focus Skill Enabling Casting While Moving:**

- +100: 5% Movement Speed
- +200: 10%
- +300: 15%
- +400: 20%
- +500: 25%
- +600: 30%
- +700: 35%
- +800: 40%
- +900: 45%
- +1000:50%

## Crit Bonus

Crit Bonus has a "soft" cap of 4.000 - *since [[Kunark Ascending]]*

- The "plain" critbonus stat can go only up to 4k
- The Crit Bonus OverCap stat allows you to that given amount over the cap of 4k

## Potency

Potency has no cap

## Weapon Damage Bonus

Weapon Damage Bonus has an unmodified hard cap of 300. - *since [[Terrors of Thalumbra]]*
Weapon Damage Overcap allows a character to exceed the hard cap by the amount of overcap but does not grant weapon damage bonus

- "Spell Weapon Damage Bonus" got merged into Weapon Damage Bonus

Weapon Damage Bonus has no hard cap with Blood of Luclin release.

## Base Auto-Attack Multiplier

No known cap
Mercenaries seem to have a high inherent base auto-attack multiplier.

## Fervor

Cap of Fervor is 200

- The Fervor OverCap stat allows you to that given amount over the cap of 200

**Disruption to Damage:**
(From Kander at http://forums.station.sony.com/eq2/index.php?threads/screwed-up-mage-gear-still-need-attention.4397/#post-47488)
<blockquote>
If your disruption is higher than your “cap”, which for a level 95 player is 475, then for every 100 disruption over that cap you get a 2% increase to the minimum damage of your spells, up to 20%. So if you have 1475, you’ll be capped at 20% min spell damage increase.

If you had 100%, you would always hit for max damage.
</blockquote>
