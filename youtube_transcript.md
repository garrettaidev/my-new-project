# YouTube Transcript: NZ1mKAWJPr4

Video URL: https://youtu.be/NZ1mKAWJPr4

---

Most OpenClaw videos right now
are either first-week impressions,

or set up tutorials, or showing use
cases after three days of usage.

Nobody can tell you what happens
after the first month, because

they haven't been there yet.

I have.

Every single day. For over
50 days. Through every single

iteration of this tool:

when it was ClawdBot, when it
was MoltBot (which I refused

to call it that) and when it
is now OpenClaw. I made the

setup video that ended up in the
official OpenClaw documentation.

I built Clawdiverse, the community
directory of use cases, and the

most common post on Reddit is still:

"I set up OpenClaw, but I
don't know what to use it for."

This video is the answer: 20 real use
cases from my daily life, plus the

honest truth about what breaks, how
it breaks, and how to deal with it.

Quick context for anyone new.

OpenClaw is an always-on AI agent
that runs on your server, your VPS, a

Mac Mini or even a Raspberry Pi, 24/7.

It connects to your messaging
apps that you already have

on your phone, like Telegram,
WhatsApp, Discord, iMessage.

If you need the full setup,
I have a video for that

(link in the description)

This video is about what you
*do* with it once it's running.

And a super important thing:

Every single prompt for every
use case I'm about to show

you is in this document

(also link in the description)

It's ready for copy-pasting
and using with your own agent.

Let's go see how it all works.

Before the use cases, let
me walk you through what

50 days actually look like.

Because the way you use
this thing in week one is

nothing like in week seven.

Week one is novelty.

You're asking it random questions,
testing what it can do, kind

of using it like a ChatGPT.

But one decision I made from day
one saved me over and over in

coming weeks markdown-first.

A lot of people build their workflows
around SQLite, databases,

vector stores, custom schemas.

I put everything in Obsidian from
the start in plain text files.

Any person can read
them, I can read them.

Any program can work with them.

It's just plain text when the next
thing after OpenClaw or the next

iteration of OpenClaw comes along.

My data moves with me in five seconds.

No lock-in, just files.

I can do anything with them.

By week three, you start
building automations, warning

briefings, background checks.

It starts being more useful and
you can feel it in week five when

you start using it more and more.

You hit a wall, everything
is in one conversation and

everything is mixed together.

Research, bookmarks, analytics,
daily tasks, and there's more and

more context pollution, and that's
when I learned to separate contexts.

I now have one Discord
channel per workflow.

This way, research doesn't
bleed into analytics.

Bookmarks don't pollute daily
assistant tasks, and I'll show you the

full architecture later in week seven.

Another lesson.

Not every channel
needs the same brain.

You need to match the
model to the task.

So Opus is for deep thinking and
cheap models are good enough for

routine work, and that's when
costs stop being scary and crazy.

And by week eight and onwards, it
stops being a chatbot and becomes

a system and lesson from this.

Is three important principles after 50
days that I would recommend everyone

is to have everything in markdown
from the beginning to separate context

and to match the model to the task.

Here's what we are covering, 20
use cases across six categories,

and I'm going to move fast, real
screenshots, real conversations,

real results, and if you only steal
three ideas from this entire video.

I'll tell you exactly which
three closer to the end of

the video, so stick around.

It's gonna be worth it.

Most of my setup runs in Discord
now, which wasn't the case from

the beginning, and I'll show the
channel architecture and model

routing later for now, starting with
the things that run every single

day without me touching anything.

Every morning at 7:00 AM my
agent scans a bunch of tweets

from accounts they follow.

Picks the top 10, writes
them to my Obsidian notes.

Appends any video ideas to my shipping
backlog and sends me a summary.

I wake up and I don't need
to scroll through the feed

to know what happened.

The most important and interesting
part is already waiting for me

and it's tailored to my interests
or what I'm currently working on.

So today's stories are about
Anthropic and OpenClaw,

new Gemini model dropping.

And this is already saved in
Obsidian, and a couple video

ideas are also added to a note in
Obsidian, and the value compounds

with time because it doesn't just
summarize, it connects the dots.

Like, Hey, this tweet about
model pricing connects to

your video idea about cost
optimization, that kind of thing.

But briefings are the gateway drug.

Everyone starts there.

Let me show you what comes after.

This is my favorite use case.

Every morning my agent fetches
Wikipedia's 'On This Day' events,

picks the most impactful historical
event and then generates a woodcut

style image showing 10 seconds
before that event happened, like the

iceberg approaching the Titanic or
the apple, about to fall on Newton's

head, this kind of stuff, and then it
pushes to my TRMNL e-ink display.

In a mystery mode, it only
shows the date and location,

and I need to guess the event.

Sometimes it's obvious,
sometimes it's a lesson for me.

So for example, this is
February 1st, 2003 over Texas.

This is seconds before
shuttle Columbia Disaster.

Where it blew up, and these are the
kind of images that it produces.

For example, this is just before
the last public appearance of

the Beatles on the rooftop.

And this is the beheading of Mary
Queen of Scots, which changed

the course of Europe's history.

And this is part of my daily ritual.

Now I walk past the display, look at
the new picture, try to guess what it

is, learn something new about history.

Every single day a new
one is waiting for me.

This is maybe less of a use case and
more like part of my daily routine and

also an important part of the routine.

So I have two cron jobs that I now
never think about every day at 4:00

AM when I'm sleeping, my agent updates
its own skills from ClawHub updates.

The OpenClaw package itself
restarts the gateway, and

then reports the results.

When something breaks during an
update, it tells me and every day,

half an hour later, a separate
cron job backs up everything

important, all configuration
files, workflow directory, crown

schedules, SOUL file, MEMORY files,
skills, everything that defines how

my agent works or who he even is.

So if my server dies tomorrow,
I'm back up in half an hour, not

rebuilding from scratch, not trying
to remember how I configured things.

Just restore and go, and
that's the whole point.

It just runs.

And if something goes
wrong, I can recover easily.

And just as a reminder, all of
the prompts to achieve all these

tasks and use cases are in this.

Just on GitHub, so you can
just go there, copy paste to

your agent, and be good to go.

Always on checks, like for
example, background health checks.

This used to feel like the headline
feature, but now I think of it as

background guardrails useful, but
it's only one piece of the system.

My agent runs routine heartbeat
checks every 30 minutes.

And I can define what it
does every 30 minutes.

For example, it scans my emails,
checks my calendar, monitors

my services, and it catches
things I would have missed.

For example, one time it just sent
me this message out of the blue

about a Netflix payment failure,
and I had no idea about it.

It found it during a
routine email scan.

I paid it five minutes later so I
could safely watch more TV shows.

Or rather, I don't
really watch TV shows.

I don't have time.

Rather, my kids could safely watch
more hunters and catches a lot of

other things like domain renewal
coming up, or a meeting I was about

to miss, or a relevant newsletter
article that it found during a Sunday

heartbeat scan that connected to a
video that I was currently working on.

And none of these were
tasks that I assigned.

My agent just found them.

It knew what I'm working on and
the things that would normally

fall through the cracks.

That's exactly what gets
caught by the agent.

And an important piece of setup
here is that the agent is in

a draft only mode for email.

It can read my inbox.

It can flag what's important.

It can even draft responses,
but it cannot send it.

I need to review and send the email.

And, and it doesn't happen
without my approval.

For now, there's no robust
general solution yet for

prompt injection via email.

So I treat inbox content as
potentially hostile research

and content creation.

And I love the research part
of working with OpenClaw.

It just appeals to me to do
it on the go when I have ideas

and I want to discuss it.

For example, for this video, I told
my agents to research what people

are doing with OpenClaw, and then
it spawned five parallel sub-agents.

One Search Twitter, one crawled
Reddit, one hit Hacker News.

One analyzed YouTube competition and
one scraped multiple different forums.

They all ran simultaneously
and produced massive

structured research files.

Each one of them with competitive
analysis ranked video ideas, full

outlines, with source links, and
it took them minutes, not hours.

The research files for this
video alone produced by these

agents are over 50 pages.

And it gave me a clear understanding
of what people are doing.

And more importantly, not yet doing
with OpenClaw and what I need to

focus on to give the most value.

And it's not just for video research,
it's for any kind of research.

You can define how broad it should go.

How fresh the data needs to be.

Is it the last seven days?

Is it the last three months?

And then let it run and come
back with results so you don't

start from scratch and you have
a solid base to start with.

And speaking about YouTube, I have
two dedicated Discord channels

related to YouTube creation.

The first is my YouTube
analytics channel.

It has access to all my stats via
the API, and I can query anything in.

Natural language, like how did my last
five videos compare on retention or

which topics get the most engagement?

Or compare my OpenClaw videos
to my Claude Code videos, and

then it slices and dices the
data anyway I want on demand.

It's like much more flexible than
YouTube studios built in dashboards,

and it also synthesizes the numbers.

And gives ideas and
advice based on that.

You're not getting this
from any kind of analytics.

For example, this was just a random
question how my last two weeks went,

and then it gave me the view numbers.

It showed me when I published the
videos to understand where was the

spike, how it goes down, where is the
uptick, what were the key insights?

What was the watch time, which
I didn't even ask about, and

what was the bottom line?

So everything related to what I
care about, which I didn't even ask.

It just knows and
gives me the details.

As granular as I want them to
be, and the second channel is

my video idea research channel.

Throughout the week, I drop links,
articles, tweets, half warm thoughts,

what I want to include or what I don't
want to include in the next video.

And then the agent goes and
enriches those snippets.

It connects the dots across different
sources and builds context over time.

And by the time I sit down to work on
the video, I don't start from scratch.

I have weeks of accumulated
organized research waiting for

me, and this exact video is
a great meta example of it.

The research for this video
accumulated over probably like

three weeks, maybe even more.

Links from Reddit, insights
from Discord, competitive

analysis, audience pay
points, all fed over time.

As ideas came to me as I got
some data, as I got some numbers.

And then everything got organized
and connected by the agent so that I

have a solid baseline to start with.

And having those two different
channels for YouTube are important

because the separation matters,
analytics context, stays isolated,

and then research builds over weeks
without polluting other conversations.

Next is summarizing
practically anything.

Throw any URL at it, like an article,
a YouTube video, a research paper,

A PDF, and you get a summary back
and I use it multiple times a day.

For example, let's
summarize my last video.

/summarize and a URL and it goes
to work, and a few seconds

later I get the summary.

What's the video about?

What's the core message?

What are the key numbers?

What are the practical steps?

And from there, I can tell it to
either expand or this is good enough,

or maybe save it to an Obsidian note.

I can do anything.

Infrastructure and DevOps.

My agent migrated me from the alt
ClawdBot package to OpenClaw.

It found both packages
running at the same time.

It killed a zombie process
running at 160% of CPU.

It deleted the old system services
fixed seven days of silently broken

cron jobs that went unnoticed and all
from one message, go fix everything.

It's also connected to my VPS server
via API, and I host everything there.

And the first time I connected
it, it reviewed more than 20 apps.

Running there, flagged
some unhealthy services.

Did some fixes and right now
I can do anything with it.

I don't need to SSH to my server.

I can check the health of the whole
server or specific apps and it can

fix the apps, restart the apps.

I have basically like a remote
control to my whole server just in my

Discord, and again, about security.

There is an allow list of commands
that it can do, and there's

also a deny list of commands
that it cannot do by itself.

It has to ask my permission first.

Works pretty well and I
haven't had any issues so far.

It allows me also to
code from my phone.

I can tell my agents to go fix a bug.

Build a feature, create a PR, all
from my phone while I'm away from my

desk, and you don't need your laptop
because your AI has your laptop.

But to be completely honest,
I do not use it for production

as my main way of programming.

I only use it for some quick fixes
or simple ideas that come to my mind,

and I wanted to test them on the go.

For my main workflow, I still
use Claude Code and Codex on my

desktop Daily Life assistant.

And to start with, what everybody's
doing is email, triage and draft

replies beyond the proactive
catches that I already showed you.

The day-to-day email workflow is
simple that it reads my inbox.

Flags what's important
and drafts responses.

I review and send.

This way I can easily reply to
an email the same day rather than

during the weekend when I have
more time to go through my inbox.

This one is useful.

Calendar and family
management, not just for

myself but for family as well.

For example, I have a group
chat on WhatsApp this time.

Because my wife doesn't use
Telegram or Discord, and in

WhatsApp group, I can drop
messages like Schedule Dentist

Thursday at 3:00 PM and it's done.

And my wife can add events,
check the schedule, get

reminders all through that same
group chat and chat interface.

It is simple, but it
is helpful as well.

And once it works, you start
asking like, what else can you do?

Voice note transcription.

This is something that I always
thought I would be using on my phone

because I can dictate stuff and it's
there, but when I tried it, I never

went back to listen to those messages.

Now it can actually
be done automatically.

So for example, I send a voice
message on WhatsApp, telegram or

Discord, and it transcribes it
with Whisper model and responds in

text, quick thoughts while driving.

Shopping lists, while walking,
meeting notes on the go.

I just talk and then
it handles the rest.

And if it's something important, it
puts it in maybe a file in Obsidian.

Or sends a message or drafts
an email so that I don't even

need to go back to those notes.

They are already taken care of
and more small stuff from daily

life, like find me a good coffee
shop within walking distance.

It uses Google Places API, so it
has access to ratings reviews.

Walking distances from my home, what
people like or dislike in that place.

What are the prices?

So it can do much more in seconds
than I would do myself, and it's

helpful for one of searches as well.

I was searching for snowboard
boots to go snowboarding, and

I have a large foot, so it's
an issue to find my size.

So it serves multiple shops.

Where I could buy one, it
checked online whether they had

my size and it gave me three
options where I could go and buy.

So I went to the first one, bought
one, which were not available anywhere

else in the city or almost, and.

Took me 20 minutes
for weather forecast.

It doesn't tell me just like
tomorrow is gonna be sunny.

I have it on my watch, but it
did warn me once, for example,

about minus 19 degrees cold snap
coming up, which is like minus

two, minus three Fahrenheit.

And that was quite helpful.

And then there are reminders
about maybe rehab exercises

with snooze capability meeting
reminders before my weekly calls.

These are all small things on their
own, but they do add up and they are.

Genuinely helpful in everyday
life, helping friends with their

technical issues and problems.

And this one is personal.

So my friend wanted to set up his own
OpenClaw after watching my videos,

and I added him to a WhatsApp group
with my own agent, and myself and my

agent spent three and a half hours.

Guiding him step by step through
the entire setup in a non-English

language, NPM permissions, WhatsApp
linking daemon configuration, cloud

authorization, debugging like the
whole saga, and it was all done

either via asking questions or
posting screenshots in the group chat.

And my friend would take
a screenshot of an error.

My agent would read it and explain
the fix, tell what the next

step is, and that's how it went.

Well, previously, I would have
had to answer everything myself.

Now my agent answered 90% of
the questions, and I just added

context from my own experience
to some of the answers.

After a few days when my friend
installed his own instance, the

questions become more rare, and
then they stopped because he

switched to asking his own agent,
and I didn't have any technical

questions from him in weeks.

And I only hear updates from
time to time as to what kind

of automations he's able to do.

And for a non-technical user
who runs an accounting company,

I'm genuinely amazed how quickly
and how far he has gone already.

I also have a group chat
with my wife and my agent.

And it adds fun to our conversation,
some jokes or second opinion on

things that we are discussing.

And once my wife texted in
that channel to tell Rad to

play with me when I was too
busy talking to my agent and.

I left what I was doing and we played.

And the last part is about
my evolution of how I am

using OpenClaw today.

So migrating to Discord, building the
knowledge base and some fun projects.

Migrating to Discord is one of
the biggest changes in my setup

over the last 50 days, and I
think it's the most important

thing that I can share with you.

So first I started on WhatsApp
and then quickly moved to

Telegram because it just had more
features and was just better.

And most people started
on Telegram too.

But around week five, I
started hitting a wall.

Everything was in one conversation.

My YouTube stats were
mixed with my bookmarks.

My research was mixed with
my daily assistant tasks.

And context was getting polluted
and it was hard to start finding

things or getting back to
something that I saw previously.

So I migrated to Discord and now
it's night and day difference.

Instead of one conversation or
multiple separate agents like I had

before, I now have channels and each
channel is a dedicated workspace.

With its own context, there's a
channel for YouTube analytics, a

channel for video idea research, and
inbox channel for bookmarks, a general

channel for daily assistant stuff.

And each one stays focused on
just that one task and area.

And the important part is that I can
set different models per channel.

For example, my YouTube stats
channel can use a cheaper model

because it's mostly data retrieval.

My research channel uses Opus because
I need deep thinking during research.

My inbox channel uses a fast
cheap model because it's just.

Processing links, summarizing
and categorizing, and that's

how we keep costs down.

Matching the model to the task,
not the other way around, and not

overpaying for expensive models
for tasks that can very well be

done by a cheaper, smaller model.

And switching to Discord
wasn't about the app itself.

It was about the architecture.

I would prefer staying on Telegram
or WhatsApp, but this works better.

It separates contexts.

It has cleaner conversations, it
has better formatting, and you

have per channel models, and you
have lower costs because of that,

and with this setup of channels, I
always know where to go for what.

And I'm careful about
adding more channels.

I'll probably have more with time,
but I only add a new one as and

when I really, really need it.

And that's what 50 days looks like.

You stop using the tool and start
designing how you interact with it and

start getting more value out of it.

Bookmarks, bookmark is a fun.

I used to use Raindrop for bookmarks.

I had a paid subscription.

A separate app, manual tagging,
putting everything into folders.

And as I was using that, I
even built a system that was

regularly pulling the bookmarks
from Raindrop using the API

and putting them in my Obsidian.

What's more, I even built a
skill for OpenClaw to manage.

Bookmarks from Raindrop and to
enrich them and to create tags

automatically and to pull to
Obsidian, just the whole thing.

But at some point I realized
that I don't need an

intermediary, which is Raindrop.

I can do it myself directly.

So now I just drop any link into
my Discord inbox channel, uh,

and the agent does the rest.

It summarizes the content.

It extracts key information.

It creates text for every bookmark,
and over time builds a knowledge

graph, connecting related links,
all in markdown, all searchable,

all building context over time,
all in Obsidian, and it runs on a

cheaper model because link processing
doesn't need Opus and I canceled

Raindrop and I don't miss it.

Obsidian and knowledge base.

As you might have noticed already,
most of the things that I do with

my agent in some way or in another
end up in Obsidian, and here's where

the markdown first thing pays off.

I have almost 3000 notes in Obsidian,
and my agent indexes all of them every

night using QMD for semantic search.

Semantic search means that
I can ask questions like,

what did I decide about?

Thumbnail design last month, and
then it finds the exact note.

It's not keyword matching,
it's semantic understanding

what I'm asking about.

So for example, what's the overarching
theme in my last five videos?

It lists the five videos and
says that the overarching

theme is making AI coding tools
actually useful in practice.

It's not something that can be
found by searching for keywords.

And as I work more and more with
my agent, as I forward random

things, random thoughts, random
links, ideas throughout the day,

they go into Obsidian as markdown
files and the agent organizes them,

and then every night at 3:00 AM.

The entire index rebuilds,
and then I have this nice

semantic search available to me.

When I first set this up, it
took a few minutes to build the

initial embedding index because
it was about 3000 or then two and

a half thousand nodes, and now it
updates automatically every night,

and it takes about 10 seconds.

People call this second brain stuff.

Mine is always on, does all the
organizing for me and everything is in

plain text files that I own forever.

No database, just markdown files
and semantic search on top of it.

This one is funny.

Like one day I was checking out
my analytics on my website, velvet

shark.com, and I noticed that
there were many hits to a WordPress

logging page, but my website is not
on WordPress, so I asked my agent

to set up a honeypot on my website,
like a fake WordPress logging page.

That re rolls anyone who tries to log
in and it built the page, created a

full pull request and deployed it.

And when I went to this page, it's
not a WordPress page, it's a fake

page that you can enter anything
you want in here and try to log in.

Yeah, you get the idea.

To be clear, this is purely on
my own domain, catching bots that

scan for WordPress admin pages and
try to hack into WordPress, uh,

websites Don't use this pattern
to impersonate any real services.

I'll probably have it for a few days
or a couple weeks, and then I'll

get bored of it and I'll remove it.

But it was fun to just think
of something like type a few

sentences on my phone and have
this fun, just like party trick.

Live on my website, so one
minute the agent is managing your

infrastructure and the next, it's
setting up some like fun pranks,

and that's the fun part of it.

My agent also can create diagrams
and graphs automatically through

the Excalidraw MCP integration,
like architecture diagrams,

flow charts, concept maps,
it generates them on the fly.

During conversations, and then
I only need to change a few

things, maybe move stuff around
and maybe add a few words.

Like for example, this chart
that was presented earlier, it

was done completely by my open
cloud instance for this one.

I didn't have to
change anything at all.

Oh, maybe I changed the
colors of the models here.

Nothing else.

So if you need more than just
creating text or some copy and you

need to visualize a workflow, you
just ask and it draws for you home

automation, this one is in progress
for me currently and I'm showing

it because it's where my setup is
heading next as I'm setting up home

assistance for smart home control.

I have two home assistant
voice preview edition

devices for voice control.

So full home automation can be
managed through OpenClaw, like

light control climates, routines,
all through chat or voice, not even

having to write anything, and it's
closer to what Siri should have been.

Than anything that Apple
has shipped so far.

So that's 20 use cases from my daily
life, but I'm not the only one.

The community is doing
like incredible things.

People are running like actual
businesses through their agents.

Customer quoting, invoicing, lead
generation deal, closing, SEO, and

people are managing smart homes with
home assistant controlling 3D printers

connecting their cars even like their
Teslas, and they're making phone

calls through their voice agents.

Connecting robots with cameras,
fact checking conference speakers

in real time, and even deploying
code from the Apple Watch.

I haven't done that yet,
but sounds interesting.

And I built Clawdiverse.com.

To catalog all of it, link in
the description and the range

is wider than I expected.

And if 20 use cases that you
already saw is not enough, you can

find many more on Clawdiverse.com.

But this video is about
my own experience.

So let me tell you
what nobody else will.

But before going to the honest part.

If you installed OpenClaw today
and you are overwhelmed, start with

these three things, one draft only.

Email triage With urgent alerts,
it catches things that you miss.

Two, a daily briefing that
writes to a markdown file.

Morning context, organized
automatically for you

as you start the day.

And three one Discord inbox.

Channel four bookmarks.

Drop links.

Agent enriches them, replaces a
paid app immediately and builds

your knowledge base over time,
which is more and more valuable as

you go do these three things for a
week and you'll start getting it.

Everything else grows from there.

Okay.

What doesn't work well?

No sugar coating.

Number one, memory loss and context.

Compaction, my agent forgets
things sometimes mid conversation.

No warning, like it just
drifts away for a second.

It's not there for a while.

Then replies to something
from three sentences back and

then says it's still there.

Everything is fine.

And this is the number one
technical frustration that

people mention everywhere.

Silent compaction.

The context window fills up.

The agent compresses the conversation
and important details disappear.

The mitigation is to
write everything to files.

Use QMD for semantic search.

Use compact manually before the
system does it automatically.

But it's still rough chat.

GPT at least warns you.

When context is getting long
OpenClaw just silently

compresses and moves on.

You can at least type a status
command to see how much context

is left, but that's not ideal.

For example, here it
shows that I have.

35% of context used up and no
compactions yet in this session.

If I see that context is filling up
and it's more than 50%, I can start

a new session and then it starts
with a fresh context from zero.

Next, the cost reality, I covered
this in depth in my cost optimization

video linking the description.

The quick summary is that Opus
is amazing, but expensive, and

the answer is multi-model routing.

Use opus for the real thinking
and cheaper models for

heartbeats or sub agents.

And my Discord channel setup
is built around this.

Each channel uses the model that.

Matches its task.

And you can also set different models
for heartbeats or other simple tasks.

And my cost calculator, where
you choose different models for

different primary model or heartbeat
model or sub-agent model shows how

much you can save and it's real
money and you need to plan for it.

Another problem is,
what do I use it for?

Problem.

This is the most common
post on subreddit.

It's what people ask in Discord.

It's what people post on Twitter.

And the harsh truth is that
you need to realize one thing.

If you don't have workflows
to automate, OpenClaw won't

invent them for you if you
don't manage your calendar.

And AI calendar manager won't
help if you don't check email ai.

Email triage is pointless.

So.

It can help you if you have what to
help with, and the people getting

the most value already had systems
OpenClaw made their systems

easier, faster, and automatic.

But the systems were there
that said, this video is the

answer to, what do I use it for?

I just showed you 20
ideas plus a starter pack.

Pick three, start
there, grow from there.

Next is tasks that need babysitting,
like complex, multi-step tasks,

still fail or need pushing.

Browser automation is still flaky.

Sessions, extensions drop.

The agents sometimes go silent
mid-task, and you have to

ask like, Hey, how's it going?

It works better as an assistant than
an autonomous agent, at least for now.

The simpler the task, the more
reliable it is, and the more complex,

the more you need to check in and
to give more detailed instructions

for losing context and for
compactions, it helps when you

explicitly tell to launch subagent.

This tweet from Matt shows it nicely.

So this is the main agent, the
orchestrator, and it is launching

subagent, and each subagent
gets its own context window.

So while doing research
or performing tasks.

Those sub-agents do not into your
main context window, and your

main agent only does coordination
instead of all the work.

And this works wonderfully.

And this is also how I do all,
almost all my research where the

orchestrator launches subagents
and then just like gathers.

All the content, all the research,
and then synthesizes the results

and gives the final output.

Next, and I will never
stop highlighting this.

Security is real.

There is no full proof general
solution for prompting injection yet.

So I treat inbox content as
hostile or potentially hostile.

And if your agent
reads untrusted emails.

Someone could craft a message
that makes your agent do

something that you didn't want to.

The way I solve it is not exposing
anything to the outside world in

terms of connectivity and having
all my machines on Tailscale.

Then draft only email mode approval
needed for destructive actions.

And running security audit
regularly for security audit.

Either use this from ClawHub, ClawdBot security check, or just point

your agent to this security page
in OpenClaw documentation and.

Tell it to implement and verify
everything on this page and if

something is not done on your end to
implement these security measures.

And lastly, my own failures.

I want to be specific about
things that went wrong for me.

And to be honest, most of these were
closer to week one than week seven.

Because the whole system is
evolving and improving rapidly.

But for example, daily update.

CR job was using the old ClawdBot
commands after the migration to

OpenClaw failed silently for days.

I didn't notice and missed
a few updates because of

just a simple package.

rename. Authentication,
debugging with my friend.

Three plus hours of false
starts, credential comparisons,

complete reinstalls.

The setup is sometimes genuinely
hard, but luckily, my own agent

was doing 90% of debugging,
so at least that helped.

Context.

Compaction hit me a few times in the
middle of a complex research task.

Now I'm more aware of that.

I'm mitigating that, so I'm
getting it less and less.

The Discord migration itself took
also some iteration, getting the

right channel structure, figuring
out which models work best,

where, how to set up different
models to different channels.

Migrating context from
Telegram conversations.

All of that wasn't like
super easy or instant.

It took about a week of tweaking
to get everything right and none of

this made me stop using OpenClaw.

But nobody else is telling
you about this stuff.

Everything seems rosy, which
is not always the case.

Okay, so let's do some scoring.

Let me put a number of it from
a few different perspectives.

In terms of setup difficulty, it's
about seven out of 10, which is

intentional because it's still a work
in progress and it might be dangerous

if someone doesn't know what to do.

So it's intentionally
not being done easier.

So if you know how to go
through, set a process, you are

at least somewhat technical and
you are aware of the dangers.

Daily value once running and once
you have your own setup tailored to

your needs, easily nine out of 10.

Reliability for simple workflows.

Eight out of 10.

Very good.

Four complex, especially
browser tasks.

Still hit or miss five out of 10, and
there is a lot still to improve there.

Best feature, at least for today for
me, is Discord channel architecture.

With per channel models, the biggest
unlock is file-based memory with

markdown-first files with nightly
semantic indexing and retrieval.

And I'm building up my knowledge
base day after day, and it's more

and more useful for me with time
and it's only getting better.

Most quietly useful is
background, heartbeat checks.

You can start simple and as you think
what else you might be checking.

Every once in a while you can
add more to your heartbeat.

And the biggest pain for now is
still memory and context compaction.

What surprised me is first
that it gets better over time.

The more context it has in its cell
file and in its memory file and

folder, the better it understands you.

And after 50 days it anticipates what
I need, but even internalized like

tiny style preferences over time.

The shark emoji, the language
switching between dms and groups, it

learns you over time and it can easily
surprise you how well it learns you.

So when you start in week one with
what seems like a simple tool,

by week three, it feels almost
like an infrastructure already.

And by week seven, you reorganize
your workflow around it.

And that's when it stopped being a
chatbot for me and became a system.

Another surprise for me was that
it replaced more than expected.

I expected it to replace ChatGPT,
but it also replaced parts of Zapier,

raindrop parts of YouTube, studio
analytics, parts of web analytics,

and half of my Apple shortcuts.

And for personal use, I'm not
paying for Zapier anymore.

I'm not paying for Raindrop anymore,
and I don't miss either of them.

And the ecosystem is not
just growing, it's exploding.

There are thousands
of skills on ClawHub.

There are hosted services launching
for non-technical users, which

still might not be the best idea,
but it's there and the tooling and

security is maturing very fast.

And when the security will be much
harder and when the setup gets

eventually easier, everyone will
be running some version of this and

the capability is already there.

The onboarding isn't
by design for now.

So would I recommend OpenClaw?

Yes.

But with some conditions, yes.

If you have workflows to automate.

And you are comfortable with
a terminal and you understand

the cost implications not yet.

If you want something that just works
out of the box, you are not technical

or you expect fully autonomous AI
that never needs babysitting and

does stuff for you start to finish.

I feel like we are currently using
maybe 5% of what this can do.

And the ceiling is like
absurdly high, but the floor

still has some holes in it.

And if you are okay with
this trade off, if you like

building towards something.

Then this is the most fun like I've
had with technology in years, and I,

I keep having fun every day with it.

So that's my journey.

50 plus days every day through
ClawdBot to MoltBot, to

OpenClaw, rebrand saga.

Now OpenAI and Foundation Shift.

I've seen the community grow from
a few hundred to tens of thousands.

And I've seen my bot fail.

I've seen my bot kill itself.

I've seen it forget what
it was doing, but I've also

seen it migrate my server.

Research the entire video with
parallel agents, help my friends set

up for three hours, or generate art
that makes me smile every morning.

So for me, I'm not going
back and that's the strongest

endorsement I can give.

As always, all links
are in the description.

There are always all the
prompts for all the use cases,

some bonus security tips, cost
optimization tips, my setup video.

If you want to get started, the
cost calculator, the official

documentation, and once you
watch it and start doing and

using those prompts, drop your
favorite use cases in the comments.

I want to hear what you're
building, what you are trying

or maybe failing, and subscribe.

If you want more practical ways to
use AI and now go build yourself

a system and have fun doing it.