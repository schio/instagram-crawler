# instagram-crawler

[![HitCount](http://hits.dwyl.io/schio/https://github.com/schio/instagram-crawler.svg)](http://hits.dwyl.io/schio/https://github.com/schio/instagram-crawler)

Instagram crawler using Python for research data collection 

# Installation


```sh
$ git clone https://github.com/schio/instagram-crawler.git
$ pip install -r requirements.txt
```



# Usage


**How to use**

``` sh
$ python crawler.py seoul seoul100_4.json 120 4
```

**Print**

```sh
--------해시태그 검색 시작--------
스크롤 다운 횟수 : 1 피드 수 : 33
스크롤 다운 횟수 : 2 피드 수 : 45
스크롤 다운 횟수 : 3 피드 수 : 57
스크롤 다운 횟수 : 4 피드 수 : 69
스크롤 다운 횟수 : 5 피드 수 : 81
스크롤 다운 횟수 : 6 피드 수 : 81
스크롤 다운 횟수 : 7 피드 수 : 81
스크롤 다운 횟수 : 8 피드 수 : 117
스크롤 다운 횟수 : 9 피드 수 : 117
스크롤 다운 횟수 : 10 피드 수 : 129
#seoul에 대한 피드129개를 찾았습니다.
19 seconds | Num of feed : 129
---------------------------------
you can see result at < output_seoul100_4.json >. go to check!
total runtime is 51.16804623603821
```



**Two files are created.**


**First, Format of output_outer [filename]**

```python
resultJson = {
	fullyinfofeed[Url][Tag],    # <class 'numpy.ndarray'> 링크와 대표 이미지에 대한 설명문이 써있음
	runTime,                    # <class 'float'> 크롤링 소요 시간
	lenFullyInfoFeed            # <class 'int'> 크롤링 한 피드 총 개수
}
```

**Ex>**

```python
{
	"urlAndTagOfFeeds": [
		[
			"https://www.instagram.com/p/7CAPH5MUDh/",
			"No photo description available."
		],
		[
			"https://www.instagram.com/p/BlX06k-le92",
			"Image may contain: one or more people and closeup"
		],
		...
		[
			"https://www.instagram.com/p/BuQXqM-HRNH",
			"Image may contain: food"
		]
	],
	"runTime": 19.991328239440918,
	"lenFullyInfoFeed": 129
}
```



**The second, output_ [filename]**

```python
meta = {
	'id',                   # <class 'str'>
	'numOfLikes',           # <class 'int'>
	'numOfComments',        # <class 'int'>
	'hashtags',             # <class 'list'>
	'emptyHashtags',        # <class 'bool'>
	'url',                  # <class 'numpy.str_'>
	'tag',                  # <class 'numpy.str_'>
	'uploadDatetime',       # <class 'str'>
	'commentUsernames',     # <class 'list'>
	'imageUrl',             # <class 'str'>
	'errorFlag'             # <class 'bool'>    
}
```

**Ex**>

```python
[
    "{\"id\": \"ray.photobyfilm\", \"numOfLikes\": 4, \"numOfComments\": 1, \"hashtags\": [\"children\", \"girl\", \"filmphotography\", \"seoul\", \"film\", \"rollei35\", \"streetphotography\", \"ray\", \"filmcamera\", \"travel\", \"street\"], \"emptyHashtags\": true, \"url\": \"https://www.instagram.com/p/7CAPH5MUDh/\", \"tag\": \"No photo description available.\", \"uploadDatetime\": \"2015-08-31T02:39:49\", \"commentUsernames\": [\"ray.photobyfilm\", \"_miguel_420\"], \"imageUrl\": \"https://scontent-hkg3-1.cdninstagram.com/vp/5b4c372112efc1a3ff6815337692fd90/5D27E0EF/t51.2885-15/e35/11881680_163985320601649_974477186_n.jpg?_nc_ht=scontent-hkg3-1.cdninstagram.com\", \"errorFlag\": false}",

    "{\"id\": \"ray.photobyfilm\", \"numOfLikes\": 5, \"numOfComments\": 2, \"hashtags\": [\"film\", \"seoul\", \"filmcamera\", \"street\", \"singing\", \"아이\", \"streetfinder\", \"rollei35\", \"골목길\", \"ray\", \"노래\", \"children\", \"streetphotography\", \"filmphotography\"], \"emptyHashtags\": true, \"url\": \"https://www.instagram.com/p/7DAkq_sUKk/\", \"tag\": \"No photo description available.\", \"uploadDatetime\": \"2015-08-31T12:02:00\", \"commentUsernames\": [\"ray.photobyfilm\", \"fujiodesign_\", \"ray.photobyfilm\"], \"imageUrl\": \"https://scontent-hkg3-1.cdninstagram.com/vp/be135b457fa23e4c4de8c7f06e8428d9/5D0DB7B3/t51.2885-15/e35/11820601_856984724397280_777690103_n.jpg?_nc_ht=scontent-hkg3-1.cdninstagram.com\", \"errorFlag\": false}",
    
    ...
    
    "{\"id\": \"lovessta\", \"numOfLikes\": 0, \"numOfComments\": 0, \"hashtags\": [\"seoul\", \"korea\"], \"emptyHashtags\": true, \"url\": \"https://www.instagram.com/p/BuQXoNRnNU7\", \"tag\": \"Image may contain: 1 person\", \"uploadDatetime\": \"2019-02-24T07:14:41\", \"commentUsernames\": [\"lovessta\"], \"imageUrl\": \"https://scontent-hkg3-1.cdninstagram.com/vp/81d099125f4e637c8b2492498cd3ce42/5CEF2381/t51.2885-15/e35/51861377_2302688359977180_302083639506343340_n.jpg?_nc_ht=scontent-hkg3-1.cdninstagram.com\", \"errorFlag\": false}",

    "{\"id\": \"wabi_sabi_vibes\", \"numOfLikes\": 1, \"numOfComments\": 1, \"hashtags\": [\"korea\", \"goodvibes\", \"生活日常\", \"ペルー人\", \"인스타푸드\", \"hyggelifestyle\", \"sundaybrunch\", \"hafu\", \"먹스타그램\", \"seoul\", \"ホットケーキ\", \"hyggemoment\", \"おしゃれ\", \"회덮밥\", \"おいしい\", \"hapagirl\", \"ハーフ\", \"라이프\", \"맛스타그램\", \"instatravel\"], \"emptyHashtags\": true, \"url\": \"https://www.instagram.com/p/BuQXqM-HRNH\", \"tag\": \"Image may contain: food\", \"uploadDatetime\": \"2019-02-24T07:14:58\", \"commentUsernames\": [\"wabi_sabi_vibes\", \"orasao143\"], \"imageUrl\": \"https://scontent-hkg3-1.cdninstagram.com/vp/9e0e11b7348249df5248bd028ce692e1/5D05A773/t51.2885-15/e35/51665988_384959455388511_4795837889885352232_n.jpg?_nc_ht=scontent-hkg3-1.cdninstagram.com\", \"errorFlag\": false}"
]
```



# Help


```sh
$ python crawler.py -h
usage: crawler.py [-h] Hashtag Filename maxNumOfFeed numOfProcess

For Instagram Crawler

positional arguments:
  Hashtag       Hashtag you want to search
  Filename      File name to be saved
  maxNumOfFeed  How many feeds will you search for
  numOfProcess  Number of processes to use for multiprocessing

optional arguments:
  -h, --help    show this help message and exit
```
