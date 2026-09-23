---
title: Agent of Disgust
type: named
expansion: Rage of Cthurath
level: '143'
difficulty: Epic x4 ^^^
zone: '[[The Oogothl Sprawl: Unseen Horrors (Raid)]]'
location: Forbidden Forest {{waypoint -787.54, 192.21, -351.80}}
primary_damage: Crushing, Cold
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Oogothl Sprawl: Unseen Horrors (Raid) Named Monsters'
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
source:
  title: Agent of Disgust
  url: https://eq2.fandom.com/wiki/Agent_of_Disgust
  history: https://eq2.fandom.com/wiki/Agent_of_Disgust?action=history
  revision: 2019197
  revised: '2026-07-24T01:52:55Z'
  license: CC BY-SA 3.0
---

Agent of Disgust is a Tier 2 raid boss. He gains an additive advantage for each player below 18 and has a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Conscription of Disease**
- A buff that gives a chance to trigger Splash of Putrescence on an attacker, which deals disease damage.
- **Surging Purges**
- An incurable trauma that deals increasing crushing damage to health and magic damage to power over time.
- **Overbearing Influence II**
- An incurable trauma that makes power usage also cost health based on the amount of power used.
- **Poisonous Pummeling**
- A curable noxious that deals poison damage and increases incoming physical damage from all sources.
- **Poisonous Burst II**
- A curable noxious that deals increasing poison damage. This ability can be blocked by Area Effect blockers, and the reuse time is 60 seconds.
- **Explosion of Disgust**
- A curable noxious that deals increasing disease damage. When removed, it triggers Disgusting Spray to all allies within 25 meters, which deals much faster disease damage and slows movement speed. Receiving a second Disgusting Spray kills the target.
- **Mental Disgust**
- An incurable noxious that marks the target. If the same target receives Mental Disgust a second time, the target's group is killed.
- **Confounding Disgust**
- A curable curse that has 4 increments. The curse holds the target at the bottom of the Agent's hatelist. If it expires, or the target dies, the entire raid is killed.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

If the Agent of Disgust and [[A malglare aberration]] are both targeting the same player, that player dies.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Disgust)[0-9A-F]{6}(?&amp;lt;Player&amp;gt;\w+) senses a feeling of disgust&quot; SD=&quot;get away ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Unseen Horrors [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "get away <Player>" when the Agent casts Explosion of Disgust.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Disgust)joins the fight&quot; SD=&quot;kill add&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Unseen Horrors [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "kill add" when [[A malglare aberration]] joins the fight.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Disgust)peers deep into the mind of (?&amp;lt;Player&amp;gt;\w+)&quot; SD=&quot;tank swap ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Unseen Horrors [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap <Player>" when the Agent casts Mental Disgust.
