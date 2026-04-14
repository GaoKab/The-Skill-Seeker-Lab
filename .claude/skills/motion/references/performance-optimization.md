# Motion Performance Optimization Guide

## Bundle Size Optimization

### LazyMotion (Recommended: 34 KB → 4.6 KB)
```tsx
import { LazyMotion, domAnimation, m } from "motion/react"

<LazyMotion features={domAnimation}>
  <m.div animate={{ opacity: 1 }}>Only 4.6 KB!</m.div>
</LazyMotion>
```

### useAnimate Mini (2.3 KB)
```tsx
import { useAnimate } from "motion/mini"

const [scope, animate] = useAnimate()
animate(scope.current, { opacity: 1 })
```

## Runtime Performance

- Use `willChange` CSS property for optimized transforms
- Prioritize GPU-accelerated properties: `transform`, `opacity`
- Use `layout` prop for FLIP-based animations
- Use native ScrollTimeline API for scroll animations
- Debounce complex calculations in transform hooks
- Choose tween transitions over springs for predictable timing

## Large Lists (50+ items)

- Use virtualization: `react-window` or `react-virtuoso`
- Stagger animations with `delayChildren` for moderate lists
- Use `whileInView` for lazy-loading animations
- Simplify animations for very large datasets

## Production Checklist

- [ ] LazyMotion enabled (bundle < 5 KB)
- [ ] GPU-accelerated properties only (transform, opacity)
- [ ] Virtualization for 50+ animated items
- [ ] prefers-reduced-motion respected
- [ ] 60 FPS minimum on target devices
