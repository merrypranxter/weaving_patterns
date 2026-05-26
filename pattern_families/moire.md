# Moiré

Optical interference in silk.

## What It Is

Moiré ("watered") fabric is created by **pressing a ribbed fabric against itself at a slight angle**, producing an interference pattern of wavy lines. It's an optical effect, not a woven pattern.

## Construction

- **Ribbed base**: Usually silk or rayon with fine cord/rib structure
- **Calendering**: Two layers pressed together under heat and pressure
- **Angle offset**: Slight rotation between layers creates interference
- **Permanent effect**: The rib structure is permanently altered

## Visual DNA

- **Watery waves**: Undulating lines resembling rippling water
- **Iridescent quality**: Light plays across the waves
- **No actual pattern**: The effect is purely optical interference
- **Luxury association**: Classic for evening wear, ribbons, formal accessories
- **Common uses**: Evening gowns, ribbons, tuxedo lapels, formal accessories

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `rib_frequency` | 50–500 | Fine rib threads per unit |
| `moire_angle` | 0.1°–5° | Offset angle between layers |
| `wave_amplitude` | 0.0–0.1 | Strength of interference pattern |
| `sheen` | 0.5–1.0 | Silk reflectivity |

## GLSL Snippet

```glsl
float moire(vec2 uv, float rib_freq, float angle) {
    float grid1 = sin(uv.x * rib_freq);
    float grid2 = sin((uv.x * cos(angle) + uv.y * sin(angle)) * rib_freq);
    float pattern = grid1 * grid2; // Interference = multiplication
    return pattern;
}
```

## Prompt Template

> "Black silk moiré taffeta with watered wave pattern, optical interference from ribbed structure pressed at slight angle, liquid light rippling across surface, formal evening wear textile"

## Anti-Drift

- **Not a woven pattern**: Moiré is a surface treatment on ribbed fabric
- **Not digital moiré**: Screen moiré is unwanted; fabric moiré is deliberate
- **Silk or rayon only**: Requires fine rib structure; won't work on plain weave
- **Permanent**: The rib is crushed into the interference pattern permanently

---

*Optical interference. The wave is the light, not the thread.*
