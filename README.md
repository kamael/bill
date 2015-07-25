
Usage
--

```
bill.py SomeOne out SomeMoney
支出记录

bill.py SomeOne1 to SomeOne2 SomeMoney
1 向 2 支付 SomeMoney

bill.py show
输出相互欠钱情况
```

bill.log
--

```
{
    pay_person: 'SomeOne',
    recv_person: 'SomeOne or NoOne',
    money: "Money"
},

...
```

result.log
--

```
{
SomeOne: money,
SomeOne: money,
SomeOne: money
}
```

