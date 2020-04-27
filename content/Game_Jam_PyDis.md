Title: GameJam: 3 keys on the Run
Date: 2020-04-27
Category: Project
Tags: Python, Game, GameJam, arcade

This week, I participated in Python Discord's 2020 GameJam. GameJams are sort of hackathon for games, often video games.
In limited time and from scratch, you have to build a video game alone or with a small team, in a limited 
time, from a few hours to several days!

The aim of this game jam was to use the arcade game framework with Python. I already told you about arcade and how clear
and simple it is, in my [last article]({filename}/MineSweeper_Sunday.md). Loving the framework, being stuck in lockdown, 
and at the end of a contract, this was the best time for me to join and have fun. 

## Brainstorming
The theme of this year game jam was "3 of a Kind", a rather obscure theme! I had a project in my head, but it was not 
fitting the theme at all! The first thing that came to mind with the theme was 
["Lost Viking"](https://en.wikipedia.org/wiki/The_Lost_Vikings) an old Blizzard video game, where you control 3 characters,
with their own power. To be able to progress in the level, you had to use all of the characters. This required some brainstorming.

 
![Lost Viking is a game where you control 3 characters](https://main.judgehype.com/images/froala/2019/04/1554232974_6.jpg)

However, as rich inspiration it was, a game like this would require a lot of assets, the ability to create clever levels,
and more coding than I had time. I decided to reduce the scope as much as possible. After all, a tiny finished game is
better than a grandiose prototype.

After iterating on numerous ideas, I decided that a runner type of game would be perfect. In this kind of game, you have
 only one or two buttons,your character runs automatically and you have to avoid hazards by pressing buttons at
the right time. Below are some example of such games:
- Canabalt ([link](http://canabalt.com/))
- Temple Run ([link](https://play.google.com/store/apps/details?id=com.imangi.templerun&hl=en))
- Google Dino Easter egg ([link](https://www.omgchrome.com/list-google-chrome-easter-eggs/)) 

I wanted my game to be playable with just one button. One button would control the character and it would avoid obstacles.
Instead of controlling one character and look after the obstacles, you would control 3 characters, with 3 buttons, 
on 3 different locations! I had my game idea. 

## First iterations
Thanks to arcade simple and efficient API, I was able to do a prototype really quickly. A quick and dirty pixel art later, 
i had a guy running and jumping, with obstacles coming forward.

![Work of art]({filename}/image/GameDev1.gif)

To do this I only needed a couple of methods!


[`arcade.PhysicsEnginePlatformer`](https://arcade.academy/_modules/arcade/physics_engines.html) takes a Sprite, 
(here, my character)and check collision with a list of Sprite (here the floor, the black bar on the screenshot above).
It handles gravity, and jump mechanics! 90% of the hard work was already done. 

###Parallax
Then, I needed to give a feeling of movement to my character. He stays standing still after all. One trick I could use 
was [parallax scrolling effect](https://en.wikipedia.org/wiki/Parallax_scrolling). Basically you have a moving background,
giving the feeling your character is moving across the scenery. I didn't have time to draw really long background, 
so I decided to cycle the same background with a little trick. Whenever one copy of the background would quit the screen, 
I would teleport it at the left, so it can be reused again.
 

![schema]({filename}/image/GameDev2.png)
  

It was working well with one background, but it's even better two, at different distances!
 

![parallax finished]({filename}/image/GameDev3.gif)


### Pixel art and animation
I spent a lot of time creating the background, but it would not be the most difficult task. The most difficult task was
to draw animation. Pixel art is really difficult despite its apparent simplicity. However, armed with 
[Pixel Studio](https://store.steampowered.com/app/1204050/Pixel_Studio_for_pixel_art/)
(free on Steam), their tutorials, and a few pieces of advice from a [friend](https://twitter.com/Fe_nris) way more skilled
than me, I was able to produce an animation that made me proud! 
 

![Sprites used for animation]({filename}/image/GameDev4.gif)


###Endgame
During the development of the game, I deviated slightly from my original idea and decided that it would be more akin to 
a rhythm game, where correct input is determined if you hit them at the right time, shown on the screen as a little window.
I added code to generate different patterns of notes/obstacles to hit. I kept the jumping to have a little animation of 
input and disable repeated inputs in a short period of time. I then focused on the finishing touches, adding music, 
a life system, a high score board, better-looking score and window, and resolving minor bugs. You can see the full game
in the gif below.

![Full Game Gif]({filename}/image/GameDev5.gif)

##Last words and links
Overall, I really enjoyed this experience. The time and theme constraint surprisingly boost creativity and it was my 
first attempt at a game jam and pixel art. I enjoyed the most, the iterative content creation, bouncing from idea to idea, 
adding a frame of animation, a little functionality. Having a deadline forces you to focus on the important thing, and 
make you actually finish a project. It left me hungry for more, especially after seeing other participant
creations! 

If you have python 3, you can clone [my repo](https://github.com/Elesh-Norn/game-jam-2020) and play the game,
by following the instructions. 

If you wish to see other participants' creations and take over the theme, go check the
[python discord](https://github.com/python-discord/game-jam-2020) repo! If you wish to join the discord, you can find
their website [here](https://pythondiscord.com/).

Arcade site is [here](https://arcade.academy/) and the arcade discord [here](https://discord.gg/fceAXdY).
