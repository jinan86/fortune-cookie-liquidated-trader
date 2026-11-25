# Fortune Cookie for the Liquidated Trader

[![make.fun](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/jinan86/fortune-cookie-liquidated-trader/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/jinan86/fortune-cookie-liquidated-trader/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

One fortune cookie line for a crypto trader who was just liquidated —
written for the [make.fun](https://make.fun) competition
**Fortune Cookie for the Liquidated Trader**.

## The fortune

> Your lucky numbers are 0.00, 0.00, 0.00, and the friend who texts back at 3am.

The classic fortune-cookie line — "Your lucky numbers are ..." — kept
intact, the numbers all zero (the empty balance), and the punchline
landing on the one thing the liquidation could not take: the friend
who texts back at 3am.

## How it works

`main.py` writes the fortune, deterministically, to `/output/entry.txt`
(one line, 15 words, 78 characters, plain UTF-8 text):

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
