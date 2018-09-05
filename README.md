# PythonStuff

# Google News Scraper

Takes the headlines from Google news and can print them out. Also prints out the most common keywords. Not too useful right now but might improve in the future.

Sample output:

```
[('found', 8), ('.', 7), ('dead', 7), ('years', 6), ('Battlefield', 6), ('Reef', 6), ('Morrison', 6), ('Amazon', 5), ('Wizard', 5), ('elephants', 5), ('murder', 5), ('Typhoon', 5), ('slippers', 5), ('Jebi', 5), ('reward', 5), ('Labor', 5), ('Great', 5), ('Oz', 5), ('Trump', 5), ('Bali', 5)]
```

# Imageboard Scrapers

Ever wanted to archive or analyse the deep conversations on imageboards? Me either. But here's some code to do that. I have code for 4chan, 8chan and Lainchan. Might be useful for some kind of cyberpunk project in the future or something, idk.

Sample output:

```
  [Simple Security Questions Hong, Guil Dong 2018-03-20 09:54:44]

Last one reached reply limit.

This is the Simple Security Questions thread for simple questions.

If you have a simple question and a suitable thread doesn't already exist, just post it here and someone will probably try to answer it for you.

Remember to do some research before asking your question. No one wants to answer a question that a simple search can already resolve.


  [Anamika 2018-03-20 09:55:42]

And now my question! I got the portal page working. Just one thing left.

How can I block access to all IP addresses except those in the 192.168.0.0/24 and fc00::/7 range with iptables?


  [SHODAN 2018-03-20 18:39:29]

>>4229
iptables -F INPUT # warning - this will delete ALL of your existing rules
iptables -I INPUT -s 127.0.0.1 -j ACCEPT # technically you didn't ask for this but you need it
iptables -I INPUT -s 192.168.0.0/24 -j ACCEPT
iptables -A INPUT -j DROP

I'll let you figure out the ipv6 one yourself
```
