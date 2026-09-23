---
title: Benelith, Consumed Heart
type: named
expansion: Rage of Cthurath
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Gerion: Captive Audience (Raid)]]'
location: near Dismal Stage {{waypoint 0.51, 0.51, -521.34}}
primary_damage: Crushing, Magic
drops:
- '[[Benelith''s Heartsworn Barbute]]'
- '[[Benelith''s Heartsworn Earring]]'
- '[[Benelith''s Heartsworn Helmet]]'
- '[[Benelith''s Heartsworn Hood]]'
- '[[Benelith''s Heartsworn Skullcap]]'
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- 'Gerion: Captive Audience (Raid) Named Monsters'
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
source:
  title: Benelith, Consumed Heart
  url: https://eq2.fandom.com/wiki/Benelith,_Consumed_Heart
  history: https://eq2.fandom.com/wiki/Benelith,_Consumed_Heart?action=history
  revision: 1996262
  revised: '2026-04-17T02:12:49Z'
  license: CC BY-SA 3.0
---

Benelith, Consumed Heart is a Tier 1 raid boss. She gains an additive advantage for each player below 12 in the raid and beyond a soft time limit of 60 minutes.

## Statistics

- Flurry Avoidance: 250.0
- Ability Doublecast Avoidance: 700.0
- Resolve: 13,230.0

## Abilities

- **Mindwracking Influence I**
- An incurable arcane that causes all abilities to cost additional power.
- **Surging Heartbeats**
- An incurable elemental that deals increasing magic and cold damage to health and power over time.
- **Consume Spirits**
- An incurable arcane that deals increasing divine damage to all targets. While applied, this effect increases all incoming mental and magic damage. The detriment is curable while Benelith is standing inside the northern red bubble. If a player dies while this effect is active, Benelith heals slightly.
- **Consume Minds**
- An incurable arcane that deals increasing mental damage to all targets. While applied, this effect increases all incoming divine and magic damage. The detriment is curable while Benelith is standing inside the eastern purple bubble. If a player dies while this effect is active, Benelith heals slightly.
- **Consume Power**
- An incurable arcane that deals magic damage to all targets. While applied, this effect increases all incoming divine and mental damage. The detriment is curable while Benelith is standing inside the western green bubble. If a player dies while this effect is active, Benelith heals slightly.
- **Consume Will**
- ![The variation of Consume Will that is removed via the central crystal.](images/Consume_Will_curse_center_variant.png)An incurable curse that prevents interruption due to movement and reduces incoming damage. It can only be removed by clicking on the appropriate crystal (central, western, or eastern), as indicated in the curse text. Each of the three variations has a distinct icon. If it expires, or if the player clicks on the wrong crystal, Benelith heals significantly, and a [[Manifested Protector]] joins the fight. Benelith is immune to damage while the Protector is alive. A second failure additionally kills the cursed player. A third failure additionally kills the cursed player's group. A fourth failure additionally kills the entire raid.
- **Barrage**
- An incurable curse that can be blocked with [[Bulwark of Order]].
- **Bolstered Will**
- Increases Melee Multiplier, Haste, and DPS multiplied by the number of [[Summoned Willbreaker|Summoned Willbreakers]] active in the fight.
- **Heartbreaking Wail**
- A curable elemental that deals heat and piercing damage every 3 seconds. If the target drops below 10% power while this effect is active, the target has the curse Heartbroken applied. This curse roots the target, increases all incoming damage by 50%, and prevents the casting of hostile and beneficial abilities.

## Strategy

Benelith continuously summons a [[Summoned Willbreaker]] into the fight. If this add is not controlled by a fighter, it switches to a random target.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;is called forth by the consumed will&quot; SD=&quot;immune, kill protector&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Captive Audience [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "immune, kill protector" when a [[Manifested Protector]] joins the fight.
- **<code>&lt;Trigger R=&quot;is manifested to join the fight&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Captive Audience [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up" when a [[Summoned Willbreaker]] joins the fight.
