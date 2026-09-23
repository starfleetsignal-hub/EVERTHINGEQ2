---
title: Categorization
type: page
categories:
- Planning
source:
  title: Categorization
  url: https://eq2.fandom.com/wiki/Categorization
  history: https://eq2.fandom.com/wiki/Categorization?action=history
  revision: 34863
  revised: '2006-10-30T02:24:56Z'
  license: CC BY-SA 3.0
---

In this article I am concerened with Categories (and Subcategories): Why, and How to use them.

First, I would like to point you to an article on Wikipedia, [Categorization](http://en.wikipedia.org/wiki/Wikipedia:Categorization). It is very in-depth but a little hard to dig through.

## Why?

Why should we use Categories?

Because we love our users and want them to be able to find what they are looking for as quickly as possible. Sometimes, this means using multiple Categories for the same article to ensure that no matter how they approach the question they can get there from here.

Likewise, Subcategories can allow us to group similar or related articles together, making it easier to browse around until the user finds just the information they were looking for.

I know that all this categorization adds an extra load on the contributors but, and as a database programmer I assure you, the trick to any database design, and all a wiki is is a database, is to link your information in as many ways as you possibly can. It is more difficult to do it later, and the more ways the data is linked the more useful it becomes.

## How?

Categories are simple to add to any article. At the top, in the middle, or at the bottom, the Wiki parser finds the category markup when it parses the article after you hit "Save page". Some categories, like NPC, can be added by a template. In the case of NPC, the template NPCInformation automatically adds your article to Category:NPC.

To manually add your article to one or more categories, use the following:

<tt>&#91;&#91;Category:CategoryName]]</tt>

You can include as many or as few categories to any single article as are required to fully link it in a meaningful way. For example, consider the following block of code form the bottom of [[Find Gingus]], a quest form the Bonemire Soloing Timeline.

<tt>&#91;&#91;Category:Quest]]&#91;&#91;Category:Faction Quests]]&#91;&#91;Category:Drednever Expedition (Faction)]]&#91;&#91;Category:Drednever Expedition (Good Faction)]]</tt>

I added this one article to 4 different but related levels of Categories. It will be listed under all 4 Categories, but as you tunnel down from Quest to Faction Quest to Drednever Expedition (Faction) to Drednever Expedition (Good Faction], at each level the number of articles displayed will get closer and closer to just the one type of quest you are looking for. If you knew the exact name you could have found it in any of the 4 lists.

## Subcategories

This is only slightly trickier to setup, but all you need to remember is that a subcategory is just a category list that is, in turn, a member of a higher category.

For [[Find Gingus]] I clicked on the red link for Drednever Expedition (Bad Faction) which brough up the edit page. I added some text from the in-game faction description and a Category link to Drednever Expedition (Faction)!!! Then I repeated this operation to add Drednever Expedition (Faction) to Faction Quests. I could have also linked any of these levels to Bonemire Quests, or any such. The more ways the user can list it, the more useful it is.

## Subcategory Structure

We need to try to maintain categorization that reduces the number of choices at each layer as much as possible. Consider quests as a good example. A quest automatically links to several categories: the zone it is in, the difficulty of the quest, the update it was introduced in, the journal category it appears under in the journal and, of course, Category:Quests.

In order to reduce confusion and a plethora of level-jumping links, we need to keep each layer to as few upward links as possible. For instance, since each quest is already linked to Quests there is NO need to link each layer above it to quests. A quest in Commonlands does NOT need a link from Category:Commonlands Quests to Category:Quests because the quest itself is already linked there. All Commonlands Quests should be linked to is Quests by Zone. Likewise, Epic Quests does not need a link to Quests, just to Quests by Difficulty. ONLY the TOP layer in the structure should be linked to Quests. For instance, Quests by Zone and Quests by Difficulty ARE linked to Quests.
