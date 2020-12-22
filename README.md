# thou-decimal

"千字文" baseed 1000-decimal decoder

verse is copied from [here](https://ja.wikisource.org/w/index.php?title=%E5%8D%83%E5%AD%97%E6%96%87&uselang=ja)

```bash
$ python thoudecimal.py 天
天 => 1
$ python thoudecimal.py 地
地 => 2
$ python thoudecimal.py 宇宙
宇宙 => 5006
$ python thoudecimal.py 天地人
天地人 => 1002079
$ python thoudecimal.py 二千五百
二千五百 => 415503151613
```

## Usage

```
python thoudecimal.py <words>
```
