# NAC_Bot

This is the official bot for the NISER (National Institute of Science Education and Research) Astronomy Club's Discord server.
The primary intention for the development of this bot is to provide a collection of resources and tools that could be utilised by club members before, during, and after the conduction of skywatching sessions.
For v0.1 of NAC_Bot, The following features are currently being added to the repository:
1. Weather updates for the following 7 days (by default, for Jatni), posted every 3 hours, and additionally updated at any given time upon command
2. Satellite cloud images, on command, at any given moment over Eastern India
3. Displaying sky charts at any given time for the part of the sky above the horizon, on command
4. Constellation and object recognition for night sky images (need to choose catalogues)

The golden target, for now:
Producing an observation session success probability (takes into account the weather, equipment condition, number of days left before next midsem/endsem) based on previously collected weather data and member surveys. ML can be applied to achieve this (maybe something something simple like TuriCreate to get ML models).