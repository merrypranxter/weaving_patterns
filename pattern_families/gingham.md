# Gingham

Checked simplicity.

## What It Is

Gingham is a **dyed cotton fabric woven in a checked pattern** using colored warp and white weft (or vice versa), creating a simple even check. It's the quintessential picnic tablecloth fabric.

## Construction

- **Yarn-dyed**: Threads are dyed before weaving
- **Balanced check**: Equal-width colored and white stripes in both directions
- **No pattern weft**: The check comes from warp/weft color arrangement
- **Light to medium weight**: Usually cotton or cotton blend

## Visual DNA

- **Even check**: Equal-width colored and white squares
- **Yarn-dyed clarity**: Color goes through the thread, not on surface
- **Simple geometry**: Usually two colors max (one color + white)
- **Crisp hand**: Cotton gingham is firm, not drapey
- **Common uses**: Shirts, dresses, tablecloths, curtains, summer wear

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `check_size` | 0.01–0.1 | Size of each square |
| `color_1` | RGB | Main color |
| `color_2` | RGB | Usually white or second color |
| `color_3` | RGB | Intersection blend color |

## GLSL Snippet

```glsl
vec3 gingham(vec2 uv, float size, vec3 c1, vec3 c2) {
    vec2 grid = floor(uv / size);
    float check = mod(grid.x + grid.y, 2.0);
    vec3 stripe_x = mix(c1, c2, mod(grid.x, 2.0));
    vec3 stripe_y = mix(c1, c2, mod(grid.y, 2.0));
    return (stripe_x + stripe_y) * 0.5; // Intersection blend
}
```

## Prompt Template

> "Classic red and white gingham check cotton fabric, yarn-dyed even check pattern with equal-sized squares, crisp cotton hand, picnic tablecloth textile, flat lay"

## Anti-Drift

- **Not printed check**: Gingham is yarn-dyed; printed check sits on surface
- **Usually two colors**: One color + white; multicolor gingham exists but is less common
- **Not plaid**: Plaid has multiple colors and stripe widths; gingham is simple even check
- **Not tablecloth only**: Despite reputation, gingham is also shirts, dresses, etc.

---

*Yarn-dyed check. The grid is the color.*
