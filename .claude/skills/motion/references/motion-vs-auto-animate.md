# Motion vs AutoAnimate - Decision Guide

## TL;DR - Quick Decision

**Use AutoAnimate when:**
- Animating list add/remove/sort operations
- Simple accordion expand/collapse
- Toast notifications fade in/out
- Bundle size is critical (3.28 KB)
- Want zero configuration

**Use Motion when:**
- Need gesture controls (drag, hover, tap with fine control)
- Need scroll-based animations or parallax
- Need layout/shared element transitions
- Need SVG path morphing or line drawing
- Need spring physics customization
- Need complex orchestrated animations

**Rule of Thumb**: AutoAnimate for 90% of cases, Motion for 10%

## Bundle Size Comparison

| Package | Minified + Gzipped | Use Case |
|---------|-------------------|----------|
| AutoAnimate | 3.28 KB | Simple list animations |
| Motion useAnimate mini | 2.3 KB | Smallest React animation |
| Motion with LazyMotion | 4.6 KB | Optimized declarative |
| Motion full component | 34 KB | Full feature set |

## Decision Flowchart

```
Do you need gestures (drag, hover with fine control)? → Yes → Motion
Do you need scroll-based animations or parallax? → Yes → Motion
Do you need shared element transitions? → Yes → Motion
Do you need SVG path morphing? → Yes → Motion
Is it just list add/remove/sort? → Yes → AutoAnimate
Is it accordion/collapse/expand? → Yes → AutoAnimate
Do you want zero configuration? → Yes → AutoAnimate
Otherwise → Motion
```

## Can You Use Both?

Yes! Use AutoAnimate for simple list animations and Motion for complex gestures and scroll effects.
