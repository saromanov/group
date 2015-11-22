# group

Working with [groups](https://en.wikipedia.org/wiki/Group_%28mathematics%29). Basic operations, and information. Now suports only [cyclic](https://en.wikipedia.org/wiki/Cyclic_group) and [symmetric](https://en.wikipedia.org/wiki/Symmetric_group) groups

 [![Build Status](https://travis-ci.org/saromanov/group.svg?branch=master)](https://travis-ci.org/saromanov/group) [![Coverage Status](https://coveralls.io/repos/saromanov/group/badge.svg?branch=master&service=github)](https://coveralls.io/github/saromanov/group?branch=master)

## Why?
This is mostly for better understanding Group theory.

## Usage

```python
import groups
gr1 = groups.Sn(4) # Create symmetric group
gr2 = groups.Zn(4) # Create cyclic group
# Check is groups is Abelian
gr1.isAbelian()
gr2.isAbelian()
```

## API
### group.setBinOp
Set binary operation to the group. By default is is modulo operation
```python
import groups
gr = groups.Zn(4)
gr.setBinOp(lambda (x,y): x + y)
```

### group.isAbelian
Return True if group is abelian and False otherwise

### group.inverse
Return inverse element if exist

### group.elements
Return elements of the group

