# Duplicate Content

##A. Description of the approach

* Use a web scraper to retrieve all the `<a>` tags from Viki homepage.

* If the `href` property in an `<a>` tag contains one of the `/tv/`, `/videos/`, `/celebrities/` keywords, split it into two parts using that keyword as a delimiter.

* The latter part will be used as an identifier for each channel/video/celebrity. Three hash tables of each content type will be initialized to map the identifiers to their frequency.

* As observed in the HTML source file of Viki homepage, celebrity and channel links appear in pairs - one for image and the other for text. Hence if any celebrity/channel link appears more than twice, we assume it is a duplicate.

* For video links, they only appear once as text link. Hence we assume a video link is a duplicate if they appear more than once.

## B: Why the implemented solution is the best possible solution

There can be other ways to implement the solution. One way is to check for duplicates in text or images. However, given a text for example, we do not know which content type it is. It could be a text describing a channel or a video, but we don't know for sure unless we have prior knowledge.

Upon observation, channel/video/celebrity links are RESTful, meaning they encode the collection type in the URL path. A general form of such links is shown below:

`/content_type/item`

Since all the info is encoded in the URL path, therefore it becomes straightforward to retrieve the `content_type` as well as `item`, and use a hash table of `content_type` to map `item` to its occurrence count.

After going through all the links and inserting their item to hash tables, one may assume checking for duplicates is a matter of checking which item occurs more than once. But there's a caveat:

* Celebrity and channel links appear in pairs.
* Video links are standalone.

Hence we apply a simple heuristic to detect if any of them is duplicate by setting a threshold on their frequency.

## C: Instructions to execute the script

`pip install -r requirements.txt`

`python find_duplicates.py`

### Duplicates found as of 01/11/2016

`Likely duplicate video: 1113035v-customize-happiness-episode-12`
`Likely duplicate channel: 33458c-customize-happiness`