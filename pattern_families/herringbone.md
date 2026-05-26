# Herringbone

Chevron's sophisticated cousin.

## What It Is

Herringbone is a **broken twill** where the diagonal direction reverses at regular intervals, creating a zigzag or V-shaped pattern resembling a fish skeleton (hence the name).

## Construction

- **Twill base**: Over-2, under-1 or similar twill progression
- **Direction reversal**: The diagonal changes direction at set points
- **Symmetry**: Mirror-image halves meeting at a center line
- **Common counts**: 2×2 herringbone, 3×3 herringbone

## Visual DNA

- **V-shaped ribs**: Diagonal lines meeting at points
- **Directional alternation**: Left-leaning then right-leaning sections
- **Textured surface**: The break creates slight ridges at reversal points
- **Classic colors**: Tweed herringbone in browns/greys; formal in black/white
- **Common uses**: Suiting, overcoating, upholstery, scarves

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `zigzag_freq` | 2–20 | Number of V peaks per unit |
| `twill_angle` | 22°–45° | Steepness of diagonal |
| `reversal_width` | 0.05–0.5 | Width of each V segment |
| `ridge_depth` | 0.0–0.1 | Normal displacement at break point |

## GLSL Snippet

```glsl
float herringbone(vec2 uv, float freq, float angle) {
    float zigzag = abs(fract(uv.x * freq) - 0.5) * 2.0;
    float diagonal = uv.y + zigzag * angle;
    float pattern = fract(diagonal);
    return pattern;
}
```

## Prompt Template

> "[COLOR] herringbone tweed suiting fabric, classic V-shaped broken twill pattern with diagonal ribs alternating direction, slight textural ridge at reversal points, wool overcoat material"

## Anti-Drift

- **Not chevron**: Chevron is point-to-point continuous; herringbone has a visible break/reversal
- **Twill underneath**: The diagonal is still twill structure; the break just reverses it
- **Named after fish bones**: The V-shape resembles a herring fish skeleton

---

*Broken twill. The V is the signature.*
