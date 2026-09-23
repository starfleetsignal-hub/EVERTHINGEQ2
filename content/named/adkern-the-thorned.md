---
title: Adkern, the Thorned
type: named
expansion: Rage of Cthurath
race: Grathok
level: '143'
difficulty: Epic x4 ^^^
zone: '[[The Oogothl Sprawl: Adkern''s Pools (Raid)]]'
location: Gardens of Industry {{waypoint 154.61, 48.37, -297.28}}
primary_damage: Crushing, Disease
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
  title: Adkern, the Thorned
  url: https://eq2.fandom.com/wiki/Adkern,_the_Thorned
  history: https://eq2.fandom.com/wiki/Adkern,_the_Thorned?action=history
  revision: 2018820
  revised: '2026-07-23T02:27:41Z'
  license: CC BY-SA 3.0
---

Adkern, the Thorned is a Tier 2 raid boss. He gains an additive advantage for each player below 18 and has a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Bob and Weave**
- A buff that increases strength and agility.
- **Void-Cloaked**
- A buff that gives a chance of triggering "Negative Static" on an attacker, which deals magic damage and reduces fervor.
- **Surging Thorns**
- An incurable elemental deals increasing physical and elemental damage to health and power over time.
- **Overbearing Influence II**
- An incurable trauma that makes power usage also cost health based on the amount of power used.
- **Beatdown**
- A curable arcane that
- **Crashing Waves**
- A curable trauma that deals crushing damage and increases noxious and elemental damage from all sources.
- **Noxious Waves**
- A curable noxious that deals disease damage and increases physical and elemental damage from all sources.
- **Elemental Waves**
- A curable elemental that deals heat damage and increases physical and noxious damage from all sources.
- **Strategic Targeting**
- A curable trauma that deals high health and power damage to scouts within 30 meters and mages outside 15 meters. This damage cannot be warded.
- **Weighted Slam**
- A curable trauma that deals high health and power damage to those further from Adkern.
- **Void Lift**
- A curable trauma that deals slashing damage over time and knocks the target back. Damage from this effect has 100% bleedthrough.
- **Tortured Animosity**
- A curse that deals increasing physical damage for each other player within 8 meters. It can only be cured if there are no other players within 8 meters. The first and second times this curse expires, it kills the target. The third failure additionally kills the target's group. The fourth failure additionally kills the entire raid.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

At 15%, a water spout appears in the nearby pool. At 10%, Adkern splashes a potion on himself to protect from death. Dragging Adkern through the water spout removes these protections.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Thorned)&amp;quot;Tortured Animosity&amp;quot; curse targeting (?&amp;lt;Player&amp;gt;\w+)&quot; SD=&quot;${Player} joust 9&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Adkern&amp;apos;s Pools [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "<Player> joust 9" when Adkern casts Tortured Animosity.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Thorned)begins to gather void energy&quot; SD=&quot;scouts joust 30&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Adkern&amp;apos;s Pools [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "scouts joust 30" when Adkern casts Strategic Targeting.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Thorned)joins the fight&quot; SD=&quot;kill add&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Adkern&amp;apos;s Pools [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "kill add" when [[Adkern's Loyal Voidpet]] joins the fight.
