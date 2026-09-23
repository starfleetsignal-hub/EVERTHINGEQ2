---
title: Irid Pangionug
type: named
expansion: Rage of Cthurath
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Zon Zobboz: Gaze of the Oglth (Raid)]]'
location: Hatchery of Horrors {{waypoint 742.88, 38.88, 125.97}}
primary_damage: Poison
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Zon Zobboz: Gaze of the Oglth (Raid) Named Monsters'
source:
  title: Irid Pangionug
  url: https://eq2.fandom.com/wiki/Irid_Pangionug
  history: https://eq2.fandom.com/wiki/Irid_Pangionug?action=history
  revision: 1993522
  revised: '2026-04-03T20:05:31Z'
  license: CC BY-SA 3.0
---

Irid Pangionug is a Tier 1 raid boss. It gains an additive advantage for each player below 12 in the raid and beyond a soft time limit of 60 minutes.

## Statistics

- Flurry Avoidance 250.0
- Ability Doublecast Avoidance 700.0
- Resolve 13,230.0

## Abilities

- **Overbearing Influence I**
- An incurable detriment that causes power usage to also cost health based on the amount of power used.
- **Bumbling Will**
- A buff that increases offensive ability for each [[A Bumbling Bonder|Bumbling Bonder]] active in the encounter.
- **Surging Bludgeon**
- An incurable detriment that deals increasing crushing and poison damage over time.
- **Forceful Lance**
- A incurable trauma that deals crushing and poison damage as well as debuffing crit bonus.
- **Crushing Voidstrike**
- A curable trauma that deals high crushing and poison damage and increases piercing and cold damage from all sources.
- **Side-Eyed**
- An incurable curse that increases incoming cold and piercing damage types. If it expires or the target dies, it triggers a failure in the encounter. The first failure summons a [[Shadowed Gaze of Pangionug]]. The second failure additionally kills the target. The third failure additionally kills the target's group. The fourth failure additionally kills the entire raid. The curse is removed if, during the next check, no players are standing between Irid and Fera.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]]. Irid and Fera have separate Barrage abilities.

## Strategy

If Irid and Fera are too close to each other, they both begin healing until separated. If Irid and Fera are both targeting the same player, they combine their strength to instantly kill that player.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Irid)forms from the shadows&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: Gaze of the Oglth [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up" when a Bumbling Bonder joins the fight.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Irid)prepare to identify new targets&quot; SD=&quot;back out&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: Gaze of the Oglth [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "back out" when Irid and Fera begin casting their Side-Eyed Curse.
