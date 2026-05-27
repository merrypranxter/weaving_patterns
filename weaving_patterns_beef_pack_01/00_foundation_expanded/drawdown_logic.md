# Drawdown Logic

The drawdown shows which thread is visible at each intersection.

A drawdown can be represented as a 2D array:

```text
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
```

This is plain weave. It is also a checkerboard shader, a binary mask, and a textile truth table.

## Read it as

- `1` = warp visible
- `0` = weft visible

For colored yarns, the visible cell chooses from the warp color array or the weft color array.
