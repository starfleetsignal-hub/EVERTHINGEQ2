---
title: Oogiloi Eye
type: named
expansion: Rage of Cthurath
race: Gazer
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Zon Zobboz: The Outer Swarmyard (Raid)]]'
location: Ichor Grounds {{waypoint -488.62, 9.43, 821.25}}
primary_damage: Crushing, Divine
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Gazer
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Zon Zobboz: The Outer Swarmyard (Raid) Named Monsters'
source:
  title: Oogiloi Eye
  url: https://eq2.fandom.com/wiki/Oogiloi_Eye
  history: https://eq2.fandom.com/wiki/Oogiloi_Eye?action=history
  revision: 1997616
  revised: '2026-04-24T01:43:59Z'
  license: CC BY-SA 3.0
---

Oogiloi Eye is a Tier 1 raid boss. It gains an additive advantage for each player below 12 in the raid and beyond a soft time limit of 60 minutes.

## Statistics

- Flurry Avoidance 250.0
- Ability Doublecast Avoidance 700.0
- Resolve 13,230.0

## Abilities

- **Surging Wonderment**
- An incurable trauma that deals increasing crushing and divine damage to health and power over time.
- **Mindwracking Influence I**
- An incurable detriment that increases the power cost of all abilities.
- **Distorted Perspective I**
- A curable arcane that deals fast-growing damage over time.
- **Constant Glare**
- A curable noxious that fears targets within 25 meters, deals fast ticking increasing poison damage, and increases physical damage from all sources. This effect can be blocked by area effect immunities.
- **Forceful Strike**
- A curable trauma that deals slashing damage over time and knocks back all targets within 18 meters. This damage has 100% bleedthrough.
- **Volley of Strikes**
- A curable trauma that deals multiple strikes of crushing damage and deals fast-ticking increasing piercing damage. The piercing damage has increased bleedthrough.
- **Conscription of Blight**
- A buff that gives a chance of triggering Ocular Blight on an attacker, which interrupts, deals disease damage, and debuffs offensive ability.
- **Void Bubble of Protection**
- A buff that covers the island in a large yellow dome and prevents all incoming damage. If this ability is left on for too long, the entire raid is killed instantly.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].
- **Gaze of Oogiloi**
- An incurable curse that lands on players with less than 5% power. It deals crushing damage over time and debuffs offensive ability. The effect cannot be dispelled and persists through death.
- **Watchful Eye of Oogiloi**
- An incurable curse that applies on the caster of a [[Voidborne Spear]]. It reduces maximum health and power by 25% and debuffs offensive and defensive ability for 5 minutes. If somehow removed prematurely, it is reapplied at a new full duration.

## Strategy

![The spear looted from Oogiloi Lancers that dispells protections from Oogiloi Eye.](images/Voidborne_Spear.png)
Oogiloi Eye summons an [[Oogiloi Lancer]] which drops a [[Voidborne Spear]]. The spear can be used to dispell Void Bubble of Protection, which also places an incurable curse Watchful Eye of Oogiloi on the caster. This curse prevents using another spear until the curse expires.

Oogiloi Eye locks his attention to a particular tank for 15 seconds, immediately switching its current target to that tank. During this time, any other player who takes aggro is immediately killed.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Oogiloi)Lancer&amp;#92;&amp;#92;/a joins the fight&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Outer Swarmyard [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up" when an [[Oogiloi Lancer]] joins the fight.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Oogiloi)locks his attention to (?&amp;lt;Player&amp;gt;\w+)&quot; SD=&quot;tank lock on ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Outer Swarmyard [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank lock on <player>" when Oogiloi Eye locks his attention on a particular tank.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Oogiloi)protects himself with a void bubble&quot; SD=&quot;void bubble&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Outer Swarmyard [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "void bubble" when Oogiloi Eye casts Void Bubble of Protection.
