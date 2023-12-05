# oweightlifting_eda
EDA examining Olympic Weightlifting Medals earned by country from 1973 to the modern era

Weightlifting is fascinating for a number of reasons but particularly due to it history with doping. The sport as we know it (snatch + clean&jerk) became a part of the Olympics in 1976. From around this time to 1992 was considered the “Golden Age” of weightlifting — heavy, world-record weights were being moved on a regular basis. This was definitely helped by the rigorous, state-sanctioned doping regimes coupled with incredibly inadequate doping regulations. In 1992, there was a change of weight-classes and renewed focus on anti-doping due to an increase in doping violations. Then in 2017 it was found that there had been extensive doping since the sport went “clean” in 1992 as evidenced by retroactive testing, whistleblowing, and more. For instance, retroactive testing in 2016 led to the disqualification of 8 lifters in the 94kg weightclass at the 2012 Summer Olympics - including all three original medalists. This story is one of heavy-handed corruption and it leads me to believe that there is an interesting story to be told by the numbers. Specifically, I am looking to track total Olympic medal counts per country from 1976 to 2020. I believe that examining the distribution of medals over the modern era of weightlifting (1976-2020) and seeing how the counts fluctuated will offer insights into weightlifting and deeply-rooted corruption that has been rampant since 1976. 

Data will be scraped from Wikipedia, namely the [Weightlifting at the 1976 Summer Olympics](https://en.wikipedia.org/wiki/Weightlifting_at_the_1976_Summer_Olympics) page. This one page has all the necessary url information for the other pertinent Summer Olympic years.

I will be employing:
BeautifulSoup --> to scrape data from HTTP files
requests --> to send HTTP requests
Pandas --> to manipulate and analyze data 



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
