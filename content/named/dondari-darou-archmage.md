---
title: Dondari, Darou Archmage
type: named
expansion: Rage of Cthurath
race: Gruengach
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Yon Gorroth: The Infinite Abyss (Raid)]]'
location: Bog'ta Beach {{waypoint -248.31, -1.32, -617.03}}
primary_damage: Poison
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Gruengach
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Yon Gorroth: The Infinite Abyss (Raid) Named Monsters'
source:
  title: Dondari, Darou Archmage
  url: https://eq2.fandom.com/wiki/Dondari,_Darou_Archmage
  history: https://eq2.fandom.com/wiki/Dondari,_Darou_Archmage?action=history
  revision: 1997620
  revised: '2026-04-24T03:34:28Z'
  license: CC BY-SA 3.0
---

Dondari, Darou Archmage is a Tier 2 raid boss. He gains an additive advantage for each player below 18 in the raid and beyond a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Overbearing Influence II**
- An incurable trauma that causes power usage to also cost health based on the amount of power used.
- **Spellsurge**
- An incuralbe elemental that deals increasing mental, cold, and poison damage to health and power over time.
- **Conscription of Light II**
- A buff that gives a chance of triggering Flash of Brilliant Light on the attacker, which deals divine damage.
- **Darou Support**
- A buff that increases Melee Multiplier, Haste, and DPS for each increment. If at least 5 increments are present, it increases Resolve for each increment. It also decreases damage taken from all sources for each increment. Each Supporting Defender in the encounter increases the increments by one.
- **Powerful Boom**
- A curable trauma that deals slashing damage over time and knocks back all targets within 15 meters. This damage has 100% bleedthrough.
- **Repair Robes**
- A curable arcane that drains health over time. The closer to Dondari, the more health is drained.
- **Maelstrom of Ice**
- A curable elemental that deals increasing cold damage and increases physical and noxious damage from all sources.
- **Spellflurry Splash I**
- An incurable arcane that deals multiple strikes of high magic damage. This effect can be lessened with [[Raid Rune: Aegis of the Monarch I|Monarch's Blessed Aegis]]
- **Forced Procrastination**
- A curable curse that wounds health and power by 50%. When cured, it heals Dondari based on the amount of time remaining on the curse. If allowed to expire, it triggers additional failure effects. [The mentioned failure appears to do nothing at all.] Dying with the curse counts as curing it (but without any fail text).
- **Flashfreezing Bones**
- An incurable curse that lands on players within 12 meters. If a cursed target dies, all cursed targets die.
- **Spotted Weakness**
- An incurable noxious cast on Dondari's primary target. If the spell lands on the same person twice, that person and their group is instantly killed.
- **Barrage**
- An incurable curse that can only be blocked by [[Bulwark of Order]].

## Strategy

Dondari summons [[Archmage's Chosen]] into the fight, which increment Darou Support. These supporters do not move.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Dondari)a potential weakness in (?&amp;lt;Player&amp;gt;\w+)&quot; SD=&quot;tank swap ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap <player>" when Dondari casts Spotted Weakness.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Dondari)Chosen&amp;#92;&amp;#92;/a is summoned&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up" when an [[Archmage's Chosen]] joins the fight.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Dondari)leans back for a headbutt&quot; SD=&quot;kick soon&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "kick soon" when Dondari casts Powerful Boom.
