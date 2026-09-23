---
title: 'Solusek''s Eye: The Calling (Raid)'
type: instance
expansion: Blood of Luclin
release: '[[Blood of Luclin]]'
levels: 128+
access: Raid
difficulty: x4
entered_from: '[[Lavastorm]]'
entrance: '{{waypoint -327, 84, -153}}'
players: 6 days 12 hours-14 days
categories:
- Blood of Luclin
- Blood of Luclin Instances
- IZone pages that need EQ2MAP uid
- Instances
- Lavastorm Instances
- Persistent Instances
- Raid x4 Zones
- Zones
source:
  title: 'Solusek''s Eye: The Calling (Raid)'
  url: https://eq2.fandom.com/wiki/Solusek's_Eye:_The_Calling_(Raid)
  history: https://eq2.fandom.com/wiki/Solusek's_Eye:_The_Calling_(Raid)?action=history
  revision: 1636600
  revised: '2023-01-06T00:55:04Z'
  license: CC BY-SA 3.0
---

## Note

- In this zone timing of curing is for some special curses very very important. Any **mistake will be punished** with immediate death (at least of the cursed) and increase your deathcounter of your encounter.<br>So it is **strongly suggested to have a macro** like "/gsay CURE {my Name} NOW, pls" & "/raid CURE {my Name} NOW, pls".
- The zone has following resolve-sections:
  - Resolve 3740 for the 1. to 5. encounters
  - Resolve 3865 for the 6. to 9. encounters
  - Resolve 4030 for the 10. to 13. encounters (including the p.i.t.a.-encounter.no13)
  - Resolve 4135 for the zone-boss (14. encounter and quiet easy...as you will have trained all required actions by defeating the previouse encounters)
- In the zone you have a porter-network (cogs on the floor). Based on your progress in the zone, the accoriding porters are activated. Following ports are available:![Cog of the porternetwork at the entrance](images/PorterCogAtEntrance.jpg)
  - Entrance {{waypoint 18, 14, -44}}
  - The Speaker's Demise {{waypoint 86, -358, 197}}
  - Fire Gigant Bararacks {{waypoint -300, -511, 216}}
  - The Gong of Ro {{waypoint -414, -589, -160}}

## Walkthrough

This zone has following sections:

- 1. to 5. encounters: Resolve of 3740;
- 6. to 9. encounters: Resolve 3865
- 10. to 13. encounters: Resolve 4030;
- 14. encounter: Resolve 4135;

### Walkthrough - Section 1 (Resolve 3740)

1. Defeat [[The Iron Widow (Epic)]] standing at {{waypoint 44, -13, 213}}  (1st encounter)
   - Effects:
     - [[Obsidian Guard I (Epic)]] (Resolve 3740 etc)
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil I]] (Deathcount 30 etc.): Starts with the beginning of the encounter.
     - [[Mechnamagnetica]]
   - Detrimentals etc:
     - [[Unyielding Onslaught I (Epic)]] (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
     - [[Spinning Cogs]] (Powerdrain-DOT, Poison-DD, Poison-DOT, Pot-Debuff) ![Epic version of the Spinning Cogs effect](images/Effect_SpinningCogs_%28Epic%29.jpg)
   - During the fight also adds named [[A widow maker]] spawn and start to significantly heal [[The Iron Widow]]. Defeat them ASAP...
   - [[The Iron Widow]] stands on its magnetic platform (see also its effect [[Mechnamagnetica]]) and is at the begin of the fight immune to any damage. The platform has on each side three colored pedestal (see picture).![The Plattform of The Iron Widow (Epic) with it's colored pedestals](images/TheIronWidow_Plattform.jpg)<br>During the fight [[The Iron Widow]] switches states by informes you on screen (see picture as the text ends in diffrent colored words!) and in GUI-Massage (narrative)-type![Three examples of the "colored" massage of The Iron Widow (Epic)](images/Text_threeExamplesOfTheIronWidowMessages.jpg).<br>Each effect starts with 4 incremants, which can be reduced by standing on the according collored plates at the 4 sides of the platform. Sometimes you have to mix the required color by standing on different colored plates.<br>**Note**: It looks like, that everybody has to stand on the according collored plates to mitigate the detrimentals of the states [[The Iron Widow]] will have during the fight (by now only the detrimental of the green-state is documented).<br>The state-switch-script does:
     1. **Gas Leak** "RED": Distribute everybody only on the red plates on all 4 sides of the platform to mitigate the detrimental  and reduce the increments of this state-effect:![Gas Leak effect](images/01_TheIronWidow_effect_GasLeak.jpg)
        - [[The Iron Widow]] can only get damage if it stands on the platform.
        - Each increment of the effect reduces 25% of the incomming damage to [[The Iron Widow]]...and provides to it bonuses to the outgoing damage.
     1. **Burning Gas** "ORANGE": Distribute everybody only on the red+green plates on all 4 sides of the platform to mitigate the detrimental  and reduce the increments of this state-effect:![Burnign Gas effect](images/01_TheIronWidow_effect_BurningGas.jpg)
        - [[The Iron Widow]] can only get damage if it stands on the platform.
        - Each increment of the effect increases 25% of the damage reduction of [[The Iron Widow]]...and provides to it bonuses to the outgoing damage.
     1. **Cracked Seals** "BLUE": Distribute everybody only on the blue plates on all 4 sides of the platform to mitigate the detrimental  and reduce the increments of this state-effect:![Cracked Seals effect](images/01_TheIronWidow_effect_CrackedSeals.jpg)
        - [[The Iron Widow]] can only get damage if it stands on the platform.
        - Each increment of the effect reduces 25% of the incomming damage to [[The Iron Widow]]...and provides to it bonuses to the outgoing damage.
     1. **Burning Oil** "PURPLE": Distribute everybody only on the red+blue plates on all 4 sides of the platform to mitigate the detrimental  and reduce the increments of this state-effect:![Burning Oil effect](images/01_TheIronWidow_effect_BurningOil.jpg)
        - [[The Iron Widow]] can only get damage if it stands on the platform.
        - Each increment of the effect increases 25% of the damage reduction of [[The Iron Widow]]...and provides to it bonuses to the outgoing damage.
     1. **Coolant Leak** "YELLOW": Distribute everybody only on the yellow plates to mitigate the detrimental  and reduce the increments of this state-effect:![Coolant Leak effect](images/01_TheIronWidow_effect_CoolantLeak.jpg)
        - [[The Iron Widow]] can only get damage if it stands on the platform.
        - Each increment of the effect increases 25% of the damage reduction of [[The Iron Widow]]...and provides to it bonuses to the outgoing damage.
     1. **Blown Gasket** "GREEN": Distribute everybody only on the green plates on all 4 sides of the platform to mitigate the detrimental [[Dirty Particulas]] and reduce the increments of this state-effect:![Blown Gasket effect](images/01_TheIronWidow_effect_BlownGasket.jpg)
        - [[The Iron Widow]] can only get damage if it stands on the platform.
        - Each increment of the effect increases 25% of the damage reduction of [[The Iron Widow]]...and provides to it bonuses to the outgoing damage.
        - [[Dirty Particulas]]: **Does not apply to targets standing on the GREEN plates.** All others are damaged (DD & DOTs), stifled and dazed in Area (max Range ).
     1. **Overloaded Core** "WHITE" (red + yellow + blue):  Distribute everybody only on the red+green+blue plates on all 4 sides of the platform to mitigate the detrimental  and reduce the increments of this state-effect:![Overloaded Core effect](images/01_TheIronWidow_effect_OverloadedCore.jpg)
        - [[The Iron Widow]] can only get damage if it stands on the platform.
        - Each increment of the effect increases 25% of the damage reduction of [[The Iron Widow]]...and provides to it bonuses to the outgoing damage.
   - **Note**: Not according to the state-effecs it looks like the MT has to guide [[The Iron Widow]] on and off its magnetic platform to enable damage again. Must be verified...
1. Destroy wall at  by clicking on it. As it explodes get some distance to the wall...
1. Defeat [[Novinctus the Unleashed (Epic)]] at {{waypoint -37, -34, -106}} (2nd encounter)
   - Effects:
     - [[Obsidian Guard I (Epic)]] (Resolve 3740 etc)
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil I (Epic)]] (Deathcount 30 etc.): Starts with the beginning of the encounter.
     - [[Horned Frill]] (every 4 sec Tank-Debuff etc.)
   - Detrimentals etc.
     - [[Unyielding Onslaught I (Epic)]] (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
     - GUI-Massage (Narrative) "The weight of Novictus's charge cause large chunks of the cavern to collapse around you!": During the fights "red circel areas" appear on the ground (around a random raid-member). If you stand to long in that "red circle area" you will be hit by **Crumpling Cavern** (slow, mana-drain, DOT). Leave that "red circle area" to prevent the effect.
   - During the fight [[Novinctus the Unleashed]] starts sometimes to "travel on a rampage". Do not stand in its way...that becomes deadly. You can range-attack during its "journy".
1. Defeat [[Dread Lady Vezarra (Epic)]] at  (3rd encounter)
   - Speaks Sathirian language
   - Effects:
     - [[Obsidian Guard I (Epic)]] (Resolve 3740 etc)
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil I (Epic)]] (Deathcount 30 etc.): Starts with the beginning of the encounter.
   - Detrimantals etc.
     - [[Unyielding Onslaught I (Epic)]] (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
     - **Undead Prison** (Stun, Powerdrain-DOT, Crushing-DOT): If you get caught by a bone-claw ([[Unearthed bones]]).
   - Adds: [[Septic salive]] (purpose [[Need]])
   - Before a bone-claw tries to cache you a white target-circle appears on the ground.![Named is aiming by multiple white target-circles on the ground for the next bown-claw attacks.](images/WhiteCircleOnTheGround.jpg)
   - If you get cought in a bone-claw ([[Unearthed bones]]), **don't move**. If you move you will die. Attack the bone-claw to get out again or wait.
   - While you are encaged in the bone-claw ([[Unearthed bones]]) your casts have no effect.
   - When this bown-claw disappears [[A dread revenant]] spawns (GUI-Text " [[A dread revenant]] will rise form the corpse.") at that location and joins the fight.
1. As you have defeated the first named mobs, you can use the elevator at {{waypoint -320, -40, -151}} to go further down into the mine.
1. Defeat [[Chief Badagoosh (Epic)]] at {{waypoint -241, 239, -32}} (4th encounter)<br>**WARNING**: It looks like [[Chief Badagoosh (Epic)|Chief Badagoosh]] steals shinies out of your bags!<br>During the encounter [[Chief Badagoosh (Epic)|Chief Badagoosh]] says "Gimme gimme gimme!" and you get the GUI-Massage "[[Chief Badagoosh (Epic)|Chief Badagoosh]] wants yer shiny! (If you have one.)". So keep your bag clear!
   - Effects:
     - [[Obsidian Guard I (Epic)]] (Resolve 3740 etc)
     - [[Obsidian Defense (Epic)]]  (first 30 attacks ignored etc.)
     - [[Mortal Coil I (Epic)]] (Deathcount 30 etc.): Starts with the beginning of the encounter.
   - Detrimentals etc.
     - [[Unyielding Onslaught I (Epic)]]  (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
     - **Spelunker's Union**: every increment will increase for every add spelunker shiner. So kill the [[A spelunking shiner]] asap.
     - GUI-Massage (Narrative) "ARMED treasured chests spring up from the ground around the chief!": This chests will be exploding (AE damage) after a while.<br>When the treasured chest explodes it makes AE magic damage based on distance.<br>You can open it and then [[A shiny thingamajig]] (a shiny) will be spred over the ground. You can pick up [[A shiny thingamajig]] temporary items and use for . During the encounter [[Chief Badagoosh (Epic)|Chief Badagoosh]] will take it from you back and say "Stay back shiny thieves". Then a spelunking shiner graps the shiny and attacks.
1. Defeat [[Evisceraptor (Epic)]] and [[Sickleclaw (Epic)]] around {{waypoint 4, -248, 23}}. (5th encounter)
   - Effects:
     - [[Obsidian Guard I (Epic)]] (Resolve 3740 etc)
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil I (Epic)]] (Deathcount 30 etc.): Starts with the beginning of the encounter.
     - **Brood Bond** (increased offensive, defensive abilities, DD-AE): Triggers only IF health is seperated more then 5%.![Brood Bond effect](images/Effect_BroodBond.jpg)
     - **Predatory Proximity** (increased power based on range to eachother): Splitt both at more then 30m (maximum range of this effect).![Predatory Proximity effect](images/Effect_PredatoryProximity.jpg)
   - Detrimentals etc.
     - [[Unyielding Onslaught I (Epic)]]  (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
   - During the fight eggs spawn. Destroy it.
   - During the fight party-members get a curable cures. Cure it asap or one of the Named will port to the pary-member and instant kill him/her.
   - First defeat [[Evisceraptor]] and then [[Sickleclaw]]

### Walkthrough - Section 2 (Resolve 3865)

1. Defeat [[Korvisaur (Epic)]], [[Beastmaster Xerin (Epic)]] & [[Lord Commander Izeroth (Epic)]] at {{waypoint 56, -359, 174}} (6th encounter)
   - Effects:
     - [[Obsidian Guard II (Epic)]] (Resolve 3865 etc) all of them
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.) all of them
     - [[Mortal Coil II (Epic)]]  (Deathcount 24 etc.): Starts with the beginning of the encounter.
     - [[War Sokokar]] at [[Lord Commander Izeroth (Epic)]]
     - [[Dense Hide]] at [[Korvisaur (Epic)]]
   - Detrimentals
     - [[Unyielding Onslaught II (Epic)]]  (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
     - **Earsplitting Roar** (piercing-DD; piercing-AE; max. Range 30; etc.)![Earsplitting Roar effect](images/Effect_EarsplittingRoar.jpg)
   - Defeat first [[Korvisaur]], then [[Beastmaster Xerin]] and last [[Lord Commander Izeroth]].
   - When the fight starts [[Lord Commander Izeroth]] will fly to the ceiling and throws bombs which will - beside damage - also kick everbody who is standing in the white target-circles on the groud.
   - As long as [[Korvisaur]] stands the effect [[Dense Hide]] gives it a 99% damage reduction. To increase the damage you do to [[Korvisaur]] you can/should drag it into that white target-circles of [[Lord Commander Izeroth]] bombs. Then [[Korvisaur]] will lay down on the floor for a moment and you can make much more damage in that time.
1. Defeat [[Pyreduke Surtaug (Epic)]] at {{waypoint -29.49, -336.82, 5.06}} (7th encounter), the first "more demanding" encounter (but can also - as usual - be done flawless) ![Pryreduke Surtaug](images/Pyreduke_Surtaug_%28Heroic%29.jpg)
   - Effects:
     - [[Obsidian Guard II (Epic)]] (Resolve 3865 etc)
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil II (Epic)]] (Deathcount 24 etc.): Starts with the beginning of the encounter.
     - **Dominating Presence** (less then 24 raidmembers increases per increment the offensive power of the named)
   - Detrimentals etc.
     - [[Unyielding Onslaught II (Epic)]]  (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
     - [[Blinding Heat]] (Mitigation - 1.000.000 etc.) ![Blinding Heat effect](images/Effect_BlindingHeat.jpg)
     - [[Pyre Starter]] (heat DD, Heat-DOT; not cured will kill you and up to 6 in range of 10m; etc.)![Pyre Starte (part of effect)](images/Effect_PyreStarter.jpg)
   - Note: Compared to heroic-version [[Pyreduke Surtaug (Epic)]] does NOT have the effect [[Volcanic Armor]]. So it is NOT required to defeat the [[A vulcanic fragmentation]] to decrease that buff.
   - Note: To prevent "that millions" of spawning [[A blezing fragment|blezing fragments]] to become agro, single-focus-fight and NO AE Spell usage!
   - During the fight more and more add [[A vulcanic fragmentation]] (non-agro, non-targetable) are coming out of the lave and then become agro.<br>If you defeat [[A vulcanic fragmentation]] it splitts into 2 [[A blezing fragment|blezing fragments]] (non-agro!).<br>Note: To be able to see and tag the correct barbecue skewer "a Spit On The Barbican" it is suggested that the OffTank pulls the [[A vulcanic fragmentation]] aways.
   - The encounter has two phases:
     - 1. Phase "Roosted Members":<br>During the fight random raid-members (first 1, then 2 and - at last - 3 raid-members will be roosted) are ported on the rooster and will be killed over time. If one roosting raid-member dies the raid wipes.<br>Only the raid-members on the rooster can see which of the barbecue skewer "a Spit On The Barbican" (see picture![a Spit On The Barbican](images/ASpitOnTheBarbican.jpg)) the non-roosting-raid-members have to destroy. For each destroyed "a Spit On The Barbican" one roosting-raid-members is safed and ported back...<br>Suggestion: The roosting raid-members tag the according barbecue skewer. Also possible useing "assist target" over the roosting raid-member...as long as that have a barbecue skewer in targeted.
     - 2. Phase [[Searing Storm|Searing Storms]]:<br>Raid-members are not ported anymore anymore.<br>[[Searing Storm]] is casted by spawning [[Twisted flames]]. Defeat the asap to reduce damage output of the [[Searing Storm]] effects...and don't forget to permacure the MT and - maybe - the ohter incorrigible melee-fighters, too...<br>Suggested Range-fight as only tank must stand at the named and permacured cause of the [[Searing Storm]]. The other party-members stand more then 10m away if they can not prevent area-effects.
1. Defeat [[Onakoome (Epic)]] at {{waypoint -175, -369, -297}} (8th encounter)
   - Effects:
     - [[Obsidian Guard II (Epic)]] (Resolve 3865 etc)
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil II (Epic)]] (Deathcount 24 etc.): Starts with the beginning of the encounter.
     - [[Dominating Presence]] (less then 24 raidmembers increases per increment the offensive power of the named): Starts with the beginning of the encounter.
   - Detrimentals
     - [[Unyielding Onslaught II (Epic)]] (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
     - **Shreed Needles** (-20.000% pot; piercing DOT, DOT-damage based on distance to [[Onakoome (Epic)]]; DOT-damage increasing over time): If the raid is cursed the farest away player must be cured to cure the whole (!) raid.![Shred Needles effect](images/Effect_ShredNeedles.jpg)
     - **Ascension Deflection** (specific ascension damage immunity): As long as adds (plural!) are spawnd/not defeated [[Onakoome (Epic)]] will have the for each [[Ascension]]-Class the according effect: [[Onakoome (Epic)]] become immune to spells of that according [[Ascension]]-Classes and makes AE-damage to that according [[Ascension]]-Classes.![Ascension Delection here geomancer-version) effect](images/Effect_AscensionDeflection_geomancer.jpg)
   - That Ascension-Adds spawn during the fight at {{waypoint -147, -368, -287}} inside that pavilion.![Pavilion inside which the the asendension adds will spawn.](images/Onakoome_pavilion.jpg)
   - If 4 Ascension-Adds are there, the raids is wiped.
   - Every type of [[Ascension]]-Class is required for this fight in your raidforce as peridically an add spawns at {{waypoint -147, -368, -287}} with the effect [[Ascension Shield]] on it. Because of this effect ONLY players of one [[Ascension]]-Class can see and attack it. The add does not move. You must hit this add -times with the according [[Ascension]]-Class sothat the add will become visible and attackable for all raid-members. Then it also starts to move.<br>**Note**: One of each class is enough as the count of hits makes the add visible.
1. Defeat [[Galadoon (Epic)]] at  (9th encounter)

- Hp: 200.9 trillion     Mitigation: 142,982

- Effects:
  - [[Obsidian Guard II (Epic)]] (Resolve 3740 etc)
  - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
  - [[Mortal Coil II (Epic)]] (Deathcount 24 etc.): Starts with the beginning of the encounter.
- Detrimentals etc.
  - [[Unyielding Onslaught II]] (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
  - [[Between a Rock and a Hot Place]] (DOT & Powerdrain): This detriment is applied to someone in the raid, who will get a Narrative message saying "You start to heat up!". The damage and power drain increases every four seconds until a tick instantly kills you. Dying doesn't remove the detriment, but does reset the amount of damage it is doing. Removing this detriment requires doing a set of steps related to the groups of three "a magma rocks" that spawn during the fight.  They will all have a "<cooled>" buff/state on them when they spawn, which can be removed using a dispel that can affect elemental buffs (druid/shaman dispel, or use a [[Veilwalker's Energy Inverter]]). After this has been dispelled, attack the rocks with heat damage attacks until the rocks get a "Heated" buff on them - you can use [[Flames of Yore]] to change your non-melee attacks to heat damage to make more of your raid force able to do this. Once all three rocks are heated, the person with the "Between a Rock and a Hot Place" detriment on them can walk in the middle of the three rocks and the detriment will be removed. Note that the individual rocks will start cooling down on a 20s timer after they are heated, but doing any further heat damage to them will reset the timer back to 20s. Pro tip: Someone with AoE spells they can cast every 5-15s while having the [[Flames of Yore]] buff can keep the rocks constantly heated, making this part of the fight much easier to handle.
- **Slag Driving** (damage immunity; AE crushing DOT and AE Powerdrain etc.): During the fight [[Galadoon (Epic)]] can start rotating his chest and gets the effect [[Slag Driving]] and becomes rooted. To interupt it you have to defeat one add [[A slag fiend]] next to [[Galadoon (Epic)]].
- During the fight [[Galdoon (Epic)]] casts [[Slag Driving]], becomes rooted, immune to damage and starts to rotate his chest. This is accompanied by a message from the boss of "Spin! Right round! Round! Round!". To interupt it you have to
  1. bring add  down to 30% health and then
  1. charm it and then
  1. send it to [[Galdoon (Epic)]] and then
  1. defeat it next to [[Galdoon (Epic)]].
- During the fight one of your group is ported into one of the cages. An other person of your group becomes cursed and get the massage "you are the key". That person has to stand very near to the cage in which the other groupmember is caught. Then you cure the curse and both are freeed...one of the curse, the other of the cage.<br>**Warning**: Cured not next to the cage or last to long to find the correct cage: both dead...

1. By now the trash-mobs have the effect **Unified Force III**. 2 Groups of trash can wipe the raidforce. So slow down your "move" to the next named a little.
1. At {{waypoint -53, -380, -74}} you can find [[Lady Nadjena]].<br>*If you are on the quest  she gives you the next questupdate.*
1. Use the elevator-disk a t to go further deeper into the instance.

### Walkthrough - Section 3 (Resolve 4030)

<br>**[[Unified Forces III (Epic)]] "Solusek's Eye's invaders and inhabitans alike gain strength in numbers"**![Epic version of Unified Force III each trahmob has bejond this point.](images/Effect_UnifiedForce_III_%28Epic%29.jpg):<br>From this point {{waypoint -163, -548, 156}} mobs have the "expert-buff". As you have more mobs at the same time fighting, you will have much more damage-output of all mobs...<br>**You can reduce this detrimental by fear, mesz or stun the trashmobs!** So a disciplined advance can help...would this then be a miracle?

1. Defeat [[Hortu the Scorched (Epic)]] at {{waypoint -202, -557, 222}}  (10th encounter)
   - **WARNING**: Do not cure the noxios detrimantal  during the fight. Curing will kill you and your raid-member immidiatly.
   - Effects
     - [[Obsidian Guard IV (Epic)]] (Resolve 4030)
     - [[Mortal Coil III (Epic)]] (Deathcount 18 etc.): Starts with the beginning of the encounter.
     - [[Dominating Presence]] (each missing party-member to 24 will increase offensive power)
     - **Fist of Ro** (heat DD-AE; heat DOT-AE; Area of Effects becomes bigger and smaller over time)
     - **Scion's Song** (enpowers [[Hortu the Scorched (Epic)]]; 10th increment wipes party): Each add [[A singeing scion]] will increase the increments of this effect.
   - Detrimentals
     - [[Unyielding Onslaught IV (Epic)]] (DOTs & Powerdrain over time): Uncureable curse every raid-member gets with start of the encounter.
     - **Singed Skin** (Heat DD; Heat DOT; 5th increment kills):  For each living [[A singeing scion]] everybody in the raid will get the detremental [[Singed Skin]] with the according increments.
     - **Nothing to Fear** (no effect ... beside kills you if it is cured) ![Epic version of Nothing to Fear effect](images/Effect_NothingToFear_%28Epic%29.jpg): **Do not cure this noxiose detrimental.** It will kill the person who has the detrimental.
   - The fight has two phases.
     - 1. Phase:
       - During the fight based on the Health of [[Hortu the Scorched (Epic)]] three waves of 4x[[A singeing scion|a singeing scions]] ("red" monster, remember [[Unified Forces III (Epic)|Unified Forces III (Epic) effect]]) will be incoming.
       - For each living [[A singeing scion]] everybody in the raid will get the detremental [[Singed Skin]] with the according increments. This will kill at the 5th increment everybody. So you have to defeat the "first" wave of [[A singeing scion|a singeing scions]] before the next is incomming.
       - After you have defeated one [[A singeing scion]] one red circle will apear on the ground.<br>Note: Further in fight in every red circle one person has to stand to make the flying carpets visible and usable (see also 2.phase)
     - 2. Phase starts round about 40% of health of [[Hort the Scorched]] with the GUI-Massage "Hortus calls the forth elements of song that only bards can see!"![GUI Massage of Hortus starting the 2.phase of the encounter](images/GuiMsg_CallsForthElementsOfSong.jpg):
       - "Blue" add(s) will be spawn increasing the increments of [[Scion's Song]] of [[Hortu the Scorched (Epic)]]![Epic version of Scion's Song](images/Effect_ScionsSong_%28Epic%29.jpg)
       - Each must be melee-attacked once, sothat it can move and also everybody can attack it.
       - To reach this adds all the carpets have to be visiable by standing in the red rings of the 1. phase.
       - At least one has to jump to this blue add.
       - At the same time a greate manadrain starts, damageoutput of the named is increased...
1. Use the next half-disk-elevator at {{waypoint -315, -594, 193}} **up(!)** to go further deeper into the instance.<br>**Warning**: As in the heroic-version of this zone behind the next door, there a a lot of mob-groups. Because of the expert-buff ([[Unified Forces III (Epic)]]) this can become very critial. So be carefull...don't use open-AE-Abilities/-spells...discipline, discipline is the key...
1. Defeat [[Ayquini the Firemind (Epic)]] {{waypoint -279, -516, -96}} and it's sidekick [[Scorion]]  (11th encounter)![Ayquini and it's sidekick Scorion](images/11_AyquiniTheFiremind_%28Epic%29_and_Scorion_%28Epic%29.jpg)
   - Effects:
     - [[Obsidian Guard IV (Epic)]] (Resolve 4030 etc)
     - [[Obsidian Defence (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil III (Epic)]] (Deathcount 18 etc.): Starts with the beginning of the encounter.
   - Detrimentals etc.
     - [[Unyielding Onslaught IV (Epic)]]: Uncureable curse every raid-member gets with start of the encounter.
   - [[Ayquini the Firemind (Epic)]] has a periodically mem-wipe for ALL tanks/fighter...
   - GUI-Massage (Narrative) "{Player 1}} and {Player 2} are under the control of Ayquini's Mind Games, and must be reconnect when it expires or die!": During the fight 2 raid-members get cursed (one with an arcane-curse "**Linked Fate**" and someone else with "") AND one of them is randomly teleported to a nearby location (so standing on one spot doesn't help...) AND the GUI-view is switched but not your GUI-controll. To "cure" this curse both characters must stand next to eachother/meet and wait until the detrimental ends. So both have to WAIT!<br>If it last to long to meet, both die...<br>Suggestion: one stands, the other is moved. Mark both characters as not always you can see in the raid-crowed eachother better.<br>**Note**: If someone else is curing the arcane-curse, that party-member will die imidiatly too...
   - During the fight 1 raid-member get cursed and an other get the message, that only you can cure your raid-buddy. At the moment it looks like, that anybody can cure the cursed without any impact...
   - During the fight [[Scorion]] creates at least two doupleganger. While there are doupleganger you can not damage [[Ayquini the Firemind]].<br>Each doupleganger has an according raid-member, between both there is a red beam. This beams must crossed sothat the doupleganger become attackable.
     - **WARNING**: If you can not see the "red beam" you have to adapt your Displaysetting  (in (Advanced) Options\Display\Particle Effects):
       - Set "Max Spell Reuslts per Character" at least to 1.
       - Turn up your "Maximum Particle Size". The larger you make the maximum size, the larger the cow faces will appear.
1. Defeat [[Lord Kargurak (Epic)]] at {{waypoint 145, -494, 296}} (12th encounter)![Lord Kargurat at it's location beside the pedestals](images/12_LordKargurak_incl_the_pedestals.jpg)
   - Effects:
     - [[Obsidian Guard IV (Epic)]] (Resolve 4030 etc.)
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil III]] (Deathcounter 18)
     - [[Dominating Presence]] (each missing party-member to 24 will increase offensive power)
   - Detrimentals etc.:
     - [[Unyielding Onslaught IV (Epic)]]: Uncureable curse every raid-member gets with start of the encounter.
     - [[Ro Call]] (countdown timer): When counted down to 0 the next wave of Usurper's guards will income.
     - [[Class Struggle]] (divine-DOT, Powerdrain-DOT-AE, Dazes etc.): Cases by adds [[The Usurper's Guard]] as a kind of welcome-gift for the party. Can "cured" by fear, mesz or stun the caster-mob ([[The Usurper's Guard]]).
     - [[Divine Attention]] (increases offense and defense [[Lord Kargurak (Epic)]]): Can be dispeled, increases by 1 per every few seconds. Increases as long as adds are not defeated.
   - Strategies:
     - Position Lord Kargurak in the middle between the 12 blocks. In his buff window is a timer that counts down to zero to summon guards throughout the fight (Ro Call). They must be killed or the fight will fail. At 75%, 50% & 25% he will say "Time for roll call". Random party members (2 to 4) will have their clone appear on one of the 12 blocks. That person must click the red crystal on his/her block and type their name (sign in). Everyone go back to boss and continue DPS.
1. Defeat [[Qaaron the Usurper (Epic)]] at  (13th encounter)
   - Effects:
     - [[Obsidian Guard IV (Epic)]] (Resolve 4030 etc.)
     - [[Obsidian Defense (Epic)]] (first 30 attacks ignored etc.)
     - [[Mortal Coil IV (Epic)]] (Deathcounter 18)
     - **Conduits of Power (Epic)**![Conduits of Power effect in the epic-version](images/Effect_ConduitsOfPower_%28Epic%29.jpg)  (Power-Rain for [[Qaaron the Usurper (Epic)|Qaaron the Usurper]]): For each spawned efreeti lamp not "used" by a party-member this effect gets an increment.![one of the efreeti Lamps floating over the fire abyss](images/13_QuaaronTheUsurper%28Epic%29_item_anEfreetiLamp.jpg)<br>Note: It looks like, that the last bulletpoint of the effect-descriptions is an error, as the epic-version does not have any healing effects...in contrast to the heroic-version of [[Conduits of Power (Heroic)]].
     - **Dominating Presence** (less then 24 raidmembers increases per increment the power of the named)
   - Detrimentals etc.:
     - [[Unyielding Onslaught IV (Epic)]]: Uncureable curse every raid-member gets with start of the encounter.
     - **Ignite Mana** (Spell, Combat-arts, ascensions now cost health etc.): GUI-Massage (emote) "[[Qaaron the Usurper (Epic)|Qaaron the Usurper]] finds another target in {name} to Ignite Mana".To "cure" this effect [[Qaaron the Usurper (Epic)|Qaaron the Usurper]] must curse you again...and also dying "curse" it...<br>**Warning**: The incomming "damage" will also hit everybody of your raid in 5m range of you.
     - [[Controlled Conflagration notLikeTheOthers|Controlled Conflagration]] (Crit & CritBonus reduction and kill all curesed if not cured correctly and in time): A group of the raid-pary (healers or fighters or scouts or mages) BUT one is not of that type, that member is "sepcial". You can also examine your detremantal to "find out" if you are the special one. Have a makro telling the raid who must be cured in time.
       1. [[Controlled Conflagration (Epic) others|"One of you is not like the others..."]]: If you are cured, only you will be killed...at the moment.
       1. [[Controlled Conflagration (Epic) notLikeTheOthers|"...you are not like the others..."]] : If you are cured, all of the cursed-group is cured.
     - **Spit Fire** (cureable; AE Heat-DD; AE Heat-DOT; AE decreases Pot etc.): AE attack of the adds [[The Usurper's fireguard]] will curse you if you are hit. Increases Power with each increment.
     - **Thermal Interference (Epic)** ("uncureable"; AE DPS reduction; +50% incomming heat-damage etc.): AE attack of of the adds [[The Usurper's fireguard]] will curse you if you are hit.<br>Fear, mesmerize or stun the add to "cure" this detrimental.
     - **Note**: A lot of increments of the combination of **Thermal Interference** and **Spit Fire** and "not cure efreeti lamp-users" (by group-cures) can become a problem (no damage-output, increased incomming damage).<br>So single cure pary-members and stun/fear/mezz the according adds to get ride of both effects.
   - When a efreeti Lamp is summoned you will get GUI-Massage "[[Qaaron the Usurper (Epic)|Qaaron the Usurper]] summons another lamp!".
   - During the figth more and more [[The Usurper's fireguard]] with **Burning Manifestation** (hast; autoattack-heal; summons pet [[A burning manifestation]]) will add the encounter.
   - You have to defeat [[A burning manifestation]] next to a firepit![one of the Firepits you have to enlight](images/13_QaaronTheUsurper_Firepit.jpg) to lite the firepit. Then your get the accoriding bridges to - if already summoned - a efreeti lamps...Now you are able to reach the lamp.<br>**Note**:You get an accoridngn GUI-Massage (Narrative) "The coals from the nearby firepit ignite from the burning manifestation's blazing explosion!".
   - **Power Conduit (Epic)** (-85% incomming damag; increased range of all abilities/spells etc.): If you click the efreeti lamp you will disrupt the [[Conduits of Power]]![Conduits of Power effect in the epic-version](images/Effect_ConduitsOfPower_%28Epic%29.jpg) of [[Qaaron the Usurper (Epic)|Qaaron the Usurper]]) (reducing it by 1 increment) as long as you stand in range < 20m to the efreeti lamp. <br>**Note**: This effect is classified as a detrimental and can be cured. As it is a "negativ detrimental" you do not want to have it cured...If the lamp-"curse" is cured by e.g. a groupcure, instantly re-klick the lamp to disrupt it and get the effects again.<br>**Note**: If you are stund at "your" lamp, some GUI tells you that you can not use every ability. Thats a bug. You can use every ability/spell even the GUI shows "gray"/"red" the hotkey.
   - **Warning**:[[Qaaron the Usurper (Heroic)]] can destroy firebridges by turn off the fire in the according pit. The groupmember standing on the bridge will then fall and die (Revive in the chamber and rejoin the fight!). As long as it is not bypassable, tank [[Qaaron the Usurper]] as far as possible from the firepits.
   - Strategies
     - Tank'n spank "ignoring" bridges
     - burn adds when they spawn to reduce incomming damage
     - Cure the deadly [[Controlled Conflagration notLikeTheOthers|Controlled Conflagration]]
     - Pull: Hide behind one of that firepots, set all of your pets to passiv sothat the named jumps directly to your MT.
     - At 10% HP, start max. powerburn/drains, sothat the named does not heal up again.
     - DO NOT USE VERDICT!
1. Use the red glowing portal at {{waypoint 10, -601, -268}} to the Gong of Ro.
1. Use the Gong of Ro at {{waypoint -414, -589, -160}} to port into [[Scald (Solusek's Eye: The Calling (Raid))|Scald]] lare.

### Walkthrough - Section 4 (Resolve 4135)

1. Defeat [[Scald (Solusek's Eye: The Calling (Raid))|Scald]] at  (14th encounter)
   - Buff for all memebers of the raidforce:
     - **Flow Like Lava** (casting/using while moving, ranges of all type increased etc.)
   - Effects:
     - **Obsidian Guard VI** (Resolve 4135 etc.)
     - **Perched** (roots [[Scald (Solusek's Eye: The Calling (Raid))|Scald]])
     - **Obsidian Defense** (first 30 attacks ignored etc.)
     - [[Mortal Coil IV]] (Deathcount 12 etc.): Starts with the beginning of the encounter.![Mortal Coil IV effect](images/14_Scald_effect_MortalCoil_IV.jpg)
     - [[Nagafen's Favor]] starts with the beginning of the encounter. <br>It has two states, depending on how many [[Icon of Flames]], distirbute around the platform on which Scald is rooted, are "active".![two Icon of Flames not "active"](images/14_Scald_TwoIconOfFlames.jpg)
       1. [[Nagafen's Favor withoutIncrements|Nagafen's Favor]] without any increment adapts damage done vs Scald:![Nagafen's Fevor effect with no increment active](images/14_Scald_effect_NagafensFavor_0Increments.jpg)
          - +50% for cold-damage
          - -25% for pysical, noxious and arcane damage
          - -100% for heat damage
       1. [[Nagafen's Favor withIncrements|Nagafen's Favor]] with at least one Increment increases Scald's power per increment and at 8th increment will wipe the raidforce.![Nagaven's Favor effect with at least 1 Icon of Flames is active](images/14_Scald_effect_NagafensFavor.jpg)
   - Detrimentals etc.
     - [[A molten chrysalis]] spawn. Destroy it asap, as after a while  will replace that "egg" and attack the raidforce.
   - Strategies:
     1. If you have enough DPS
        - Ignore everything and
        - burn [[Scald (Solusek's Eye: The Calling (Raid))|Scald]] within 6 minutes.
     1. Handle only [[Icon of Flames]] and [[A molten chrysalis]]
        1. Focus damage [[Scald (Solusek's Eye: The Calling (Raid))|Scald]]
        1. By 70% one group starts destroying the [[Icon of Flames]]
        1. By 50% at least 2 players mezzes the [[A molten chrysalis]]<br>**WARNING**: NO AREA-ATTACK/EFFECTs ON the [[A molten chrysalis]]...this is missioncritical
   - Loot: Beside a master-cheast everybody gets 5x [[Firebrand Pearl]] as a revard for defeating [[Scald (Solusek's Eye: The Calling (Raid))|Scald]]
1. To leave the Zone click on the Dragon-scrached Lava Stone![Exit to the Blinding](images/13_Scald_Exit_Dragon-scratchedLavaStone.jpg) at {{waypoint 0, 1170, -17}}
