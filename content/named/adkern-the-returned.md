---
title: Adkern, the Returned
type: named
expansion: Rage of Cthurath
race: Grathok
level: '143'
difficulty: Epic x4 ^^^
zone: '[[The Oogothl Sprawl: Adkern''s Pools (Raid)]]'
location: Gardens of Industry {{waypoint 264.61, 32.66, -104.90}}
primary_damage: Crushing
drops:
- '[[Adkern''s Boots of the Returned]]'
- '[[Adkern''s Chain Boots of the Returned]]'
- '[[Adkern''s Earring of Damnation]]'
- '[[Adkern''s Sabatons of the Returned]]'
- '[[Adkern''s Sandals of the Returned]]'
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Grathok
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Oogothl Sprawl: Adkern''s Pools (Raid) Named Monsters'
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
source:
  title: Adkern, the Returned
  url: https://eq2.fandom.com/wiki/Adkern,_the_Returned
  history: https://eq2.fandom.com/wiki/Adkern,_the_Returned?action=history
  revision: 2018821
  revised: '2026-07-23T03:16:57Z'
  license: CC BY-SA 3.0
---

Adkern, the Returned is a Tier 2 raid boss. He gains an additive advantage for each player below 18 and has a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Bob and Weave**
- A buff that increases strength and agility.
- **Void-Cloaked**
- A buff that gives a chance to trigger Negative Static on an attacker.
- **Negative Static**
- A curable arcane that interrupts the target, deals magic damage over time, decreases fervor, and decreases accuracy.
- **Beatdown**
- **Surging Fumes**
- An incurable elemental that deals increasing noxious and elemental damage to health and power over time.
- **Mindwracking Influence II**
- An incurable arcane that causes all abilities to cost additional power.
- **Returning Noxious Waves**
- A curable noxious that deals disease damage and increases incoming physical and elemental damage from all sources.
- **Returning Elemental Waves**
- A curable elemental that deals heat damage and increases incoming physical and noxious damage from all sources.
- **Returning Crashing Waves**
- A curable trauma that deals crushing damage and increases noxious and elemental damage from all sources.
- **Weighted Slam**
- A curable trauma that deals high health and power damage to those further from Adkern.
- **Electrical Zap**
- A curable curse that lands on players standing in the water. It deals heat damage to the target and all other targets in the water.
- **Electrify**
- An incurable elemental that deals heat damage to the target followed by additional attacks to allies.
- **Drunken Fumes**
- An incurable curse that deals crushing damage and debuffs offensive ability. This effect is applied if the target falls below 10% power.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

While out of the water, Adkern hardens his skin and regenerates his wounds. Holding him in the pool allows him to be damaged.

If two of [[Adkern's Loyal Voidpet|Adkern's Loyal Voidpets]] are up simultaneously, the entire raid is killed.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Returned)collects surrounding energy as he prepares&quot; SD=&quot;Out of water&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Adkern&amp;apos;s Pools [Raid]&quot; T=&quot;T&quot; TN=&quot;pool joust&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "out of water" when Adkern casts Electrical Zap.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Returned)joins the fight&quot; SD=&quot;kill add&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Adkern&amp;apos;s Pools [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "kill add" when [[Adkern's Loyal Voidpet]] joins the fight.
