# oweightlifting_eda
EDA examining Olympic Weightlifting Medals earned by country from 1973 to the modern era

Weightlifting is fascinating for a number of reasons but particularly due to it history with doping. The sport as we know it (snatch + clean&jerk) became a part of the Olympics in 1976. From around this time to 1992 was considered the “Golden Age” of weightlifting — heavy, world-record weights were being moved on a regular basis. This was definitely helped by the rigorous, state-sanctioned doping regimes coupled with incredibly inadequate doping regulations. In 1992, there was a change of weight-classes and renewed focus on anti-doping due to an increase in doping violations. Then in 2017 it was found that there had been extensive doping since the sport went “clean” in 1992 as evidenced by retroactive testing, whistleblowing, and more. For instance, retroactive testing in 2016 led to the disqualification of 8 lifters in the 94kg weightclass at the 2012 Summer Olympics - including all three original medalists. This story is one of heavy-handed corruption and leads me to believe that there is an interesting story to be told by the numbers.

Do the numbers tell us anything? Any abnormalities that could show us that something was amiss?

the  This story is one of heavy-handed corruption and it is just so impressive that I wanted to perform an exploratory data analysis on Olympic medal counts per country - surely there is an interesting story to be told by the numbers.


## General Approach 
**A .)** Compile list of URLs from Wikipedia of “Weightlifting at the [insert year here] Summer Olympics” from 1976 to 2021

**B.)** Loop through the list of URLs and do the following:

- Make a request to the selected URL (with requests)

- Scrape + Parse URL (with BeautifulSoup)

- Extract the medal table

- Store the data in a dataframe to be explored later on

**C.)** EDA time >:)

#### Medium Project Logs:
[[12/2/22]](https://medium.com/@junyoungdchun/project-diary-weightlifting-medal-counts-and-doping-intro-start-f692dc6be6ed)  
[[3/2/23]](https://medium.com/@junyoungdchun/project-diary-wl-medal-counts-and-doping-compiling-our-list-of-urls-2-415a47e2d12d)
