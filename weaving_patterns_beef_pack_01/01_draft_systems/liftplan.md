# Liftplan

This file documents **liftplan**: direct row-by-row shaft lifting logic, useful for dobby and digital translation.

## Structural role

In the full weaving program, this controls one layer of the cloth's logic. It either determines which warp threads are available, which shafts are raised, how picks repeat, or how the final drawdown resolves.

## Shader translation

Represent this as an array, matrix, or lookup function. A shader can sample `cell = ivec2(floor(uv * thread_count))`, then look up whether the warp or weft is visible.

## Prompt language

Use phrases like:

- visible draft logic
- over-under drawdown grid
- woven binary matrix
- structured interlacement repeat
- thread-level pattern grammar

## Anti-drift

Do not reduce this to a decorative grid. The point is that structure creates surface.
