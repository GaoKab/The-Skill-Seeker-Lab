# Motion + Next.js Integration Guide

## Quick Start

**Pages Router** (Next.js 12): Works out of the box
```tsx
import { motion } from "motion/react"
```

**App Router** (Next.js 13+): MUST add "use client" directive
```tsx
"use client"
import { motion } from "motion/react-client"
```

## App Router Patterns

### Pattern 1: Direct Client Component (Simplest)
```tsx
"use client"
import { motion } from "motion/react-client"

export default function Page() {
  return (
    <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
      Welcome
    </motion.div>
  )
}
```

### Pattern 2: Wrapper Component (Recommended)
```tsx
// src/components/motion-client.tsx
"use client"
import * as motion from "motion/react-client"
export { motion }
export { AnimatePresence, MotionConfig, LazyMotion, LayoutGroup,
  useMotionValue, useTransform, useScroll, useSpring, useAnimate, useInView
} from "motion/react-client"
```

### Pattern 3: Server Data + Client Animation
Fetch data in Server Component, animate in Client Component.

### Pattern 4: MotionConfig Provider
```tsx
"use client"
import { MotionConfig } from "motion/react-client"

export function MotionProvider({ children }) {
  return <MotionConfig reducedMotion="user">{children}</MotionConfig>
}
```

## Known Issues

1. **AnimatePresence with Soft Navigation**: Exit animations don't work with App Router navigation. Use component-level AnimatePresence instead.
2. **Reorder Component**: Doesn't work with Next.js routing. Use `@dnd-kit/core` instead.
3. **Bundle Size**: Use LazyMotion to reduce from 34 KB → 4.6 KB.
4. **Reduced Motion + AnimatePresence**: Manual `prefers-reduced-motion` check needed.

## Performance

- Use `motion/react-client` import (excludes server-side code)
- Use LazyMotion for smaller bundles
- Use dynamic imports for animations not needed on initial load
- Target: Motion < 5 KB with LazyMotion, Lighthouse > 90
