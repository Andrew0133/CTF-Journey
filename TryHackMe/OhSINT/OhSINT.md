# OhSINT

## Room Info

Room: [Here](https://tryhackme.com/room/ohsint)

Difficulty: **Easy**

## Description

Are you able to use open source intelligence to solve this challenge?

## Task 1 - OhSINT

### Context

What information can you possible get with just one photo?

### Question 1 - *What is this user's avatar of?*

#### Hint: exiftool is your friend. Who is the author of the image? Do they have any social media accounts?

The first thing I did was use **ExifTool** to read metadata in the image. I discovered something interesting: the '**Copyright**' property, as shown in the image below:

![Alt text](./imgs/exiftool-output.png?raw=true "exiftool output")

Since the question mentioned a 'user avatar,' I searched for the value of the property on Google to find a social media page that matches the 'author' of the image. I discovered an entry on a Twitter page:

![Alt text](./imgs/author-twitter-page.png?raw=true "author twitter page")

As we can see from the image, by examining the avatar, we obtain the information we need.

The answer is: ```cat```

### Question 2 - *What city is this person in?*

#### Hint: BSSID + Wigle.net

For this question, I continued to explore posts on the Twitter profile and came across an interesting one:

![Alt text](./imgs/bssid-information.png?raw=true "bssid twitter post")

The **BSSID** is a unique identifier for a specific wireless access point in a Wi-Fi network.

I searched on Google "BSSID finder" and I discovered an interesting site called [Wigle.net](https://wigle.net/)

The "FAQ" label in the "Info" tab provides information about this web application: "*We consolidate location and information of wireless networks world-wide to a central database, and have user-friendly desktop and web applications that can map, query and update the database via the web.*"

I filtered the results using the BSSID we found and obtained a circle indicating the London area. This is the type of information we were looking for:

![Alt text](./imgs/wigle-dot-net-search.png?raw=true "wigle.net bssid search")

The answer is: ```London```

### Question 3 - *What is the SSID of the WAP he connected to?*

For this question, the result is in the search we conducted in the previous question. However, to access this information, we need to register on the site. Once registered, the information can be viewed by clicking on the marker on the map.

![Alt text](./imgs/wigle-advanced-search.png?raw=true "wigle.net advanced search")

As we can see from the image, by examining the popup, we obtain the information we need.

The answer is: ```UnileverWiFi```.

### Question 4 - *What is his personal email address?*

For this question, I searched on Twitter to check if the email was provided, but unfortunately, it was not. So, I conducted a Google search using the Twitter username to see if the person might have other social media accounts or a blog where we could find the information.

In my first search, I came across a WordPress site for "Oliver Woodflint Blog", unfortunately this blog has been archived or suspended, as we can see from the image below:

![Alt text](./imgs/oliverwoodflint-wordpress-page.png?raw=true "oliverwoodflint wordpress page")

I continued to search and I found a GitHub repository called **people_finder**.

Within the repository, in the ```README.md``` file we can see the email that we are looking for!

![Alt text](./imgs/people-finder-repository.png?raw=true "people finder repository")

The answer is: ```OWoodflint@gmail.com```

### Question 5 - *What site did you find his email address on?*

We got the answer from the previous question!

The answer is: ```GitHub```

### Question 6 - *Where has he gone on holiday?*

For this question I searched on google and I found something interesting:

![Alt text](./imgs/google-search.png?raw=true "google search for owoodflint")

Since the blog is closed we can use the [Wayback Machine](https://web.archive.org/)

We can see that there are severals URLs, and the second one caught my interest:

![Alt text](./imgs/wayback-machine-urls.png?raw=true "waybback machine matching urls")

The second one caught my interest because it mentioned a "journey", so it could be a sort of holiday.

![Alt text](./imgs/blog-post.png?raw=true "waybback machine matching urls")

In the blog post, I discovered a mention of New York, so this could be the answer we are looking for!

The answer is: ```New York```

### Question 7 - *What is the person's password?*

#### Hint: Check the Source code

For this question, based on the previous Google search, I noticed the following under the description of the blog post about the journey:

![Alt text](./imgs/google-search-two.png?raw=true "google search for owoodflint")

The interesting thing is that, one the blog post I didn't find this sentence.

I decided to revisit the recovered blog post and tried using CTRL+A to select all the text, hoping to uncover any hidden content

![Alt text](./imgs/blog-post-secret.png?raw=true "waybback machine matching urls")

Here we can see the hidden text!

I then took it a step further and pressed ```F12``` to inspect that element on the page:

![Alt text](./imgs/blog-post-secret-analyze.png?raw=true "waybback machine matching urls")

From the source code we can see that the color text is #ffffff (white), explaining why it wasn't visible. This must to be the "password"!

The answer is: ```pennYDr0pper.!```