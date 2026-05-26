# Jacquard

The programmable loom.

## What It Is

Jacquard weaving uses a **mechanized (now digital) control system** to lift individual warp threads independently, allowing any pixel-like pattern to be woven. It's the ancestor of computer-controlled manufacturing.

## Construction

- **Individual warp control**: Every thread can be raised/lowered independently
- **Pixel = thread intersection**: Design maps directly to loom control
- **No repeat limit**: Patterns can be extremely large and non-repeating
- **Brocade adjacent**: Jacquard is the mechanism; brocade is the effect

## Visual DNA

- **Photographic complexity**: Can reproduce detailed images
- **Float management**: Long floats on back (often cut for cleaner reverse)
- **Rich color layering**: Multiple weft colors in complex arrangements
- **Weight**: Usually heavy due to dense patterning
- **Common uses**: Ties, tapestries, brocade, elaborate upholstery

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `pattern_resolution` | 50–1000 | Threads per pattern width |
| `color_layer_count` | 2–16 | Number of weft colors |
| `float_length_max` | 4–50 | Longest float on back |
| `loom_control_type` | 0–1 | 0 = mechanical, 1 = digital |

## GLSL Snippet

```glsl
float jacquard(vec2 uv, sampler2D pattern_map) {
    return texture(pattern_map, uv).r; // Pattern determines over/under
}
```

## Prompt Template

> "Elaborate jacquard woven fabric with [COMPLEX MOTIF] pattern in [COLOR PALETTE], individual thread control creating photographic detail, rich color layering, slight sheen from satin-float areas, luxury upholstery textile"

## Anti-Drift

- **Jacquard is a mechanism, not a pattern**: The pattern can be anything
- **Not dobby**: Dobby controls groups of threads; jacquard controls individual threads
- **Modern jacquard = digital**: Computer files directly control the loom
- **Back side is messy**: Long floats visible on reverse unless cut

---

*Individual thread control. The loom is the computer. The fabric is the output.*
