# Houndstooth

Bite-shaped geometry.

## What It Is

Houndstooth is a **duotone broken check pattern** created by twill weave, featuring pointed shapes that resemble a hound's tooth. It's a classic menswear and luxury fabric pattern.

## Construction

- **Twill-based**: Usually 2×2 twill creating the characteristic broken check
- **Two colors**: Traditionally black and white, or two contrasting tones
- **Pointed shapes**: The twill break creates jagged, tooth-like edges
- **Scale variation**: From micro-houndstooth (tiny) to large windowpane houndstooth

## Visual DNA

- **Jagged checks**: Pointed rather than squared corners
- **Two-tone contrast**: Light and dark creating strong graphic effect
- **Directional bias**: The twill gives a subtle diagonal energy
- **Luxury association**: Tweed houndstooth = classic British tailoring
- **Common uses**: Suiting, coats, scarves, accessories, upholstery

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `tooth_size` | 0.01–0.1 | Size of each houndstooth unit |
| `color_1` | RGB | Dark color (traditionally black) |
| `color_2` | RGB | Light color (traditionally white) |
| `twill_angle` | 22°–45° | Underlying twill direction |

## GLSL Snippet

```glsl
float houndstooth(vec2 uv, float size) {
    vec2 grid = uv / size;
    float x = fract(grid.x);
    float y = fract(grid.y);
    float tooth = step(0.5, x + y);
    return tooth;
}
```

## Prompt Template

> "Classic black and white houndstooth wool suiting fabric, broken check pattern with pointed tooth-shaped edges from 2×2 twill weave, luxury British tailoring textile, close-up detail"

## Anti-Drift

- **Not shepherd's check**: Shepherd's check is simpler and rounder; houndstooth is jagged
- **Not glen plaid**: Glen plaid is a larger pattern combining houndstooth with other elements
- **Scale matters**: "Puppytooth" = very small; "windowpane" = very large

---

*Broken check, pointed edges. The tooth is the signature.*
