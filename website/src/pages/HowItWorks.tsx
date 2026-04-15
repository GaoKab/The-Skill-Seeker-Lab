import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import { ArrowRight } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] pt-32 pb-24 px-6 overflow-hidden">
      <div className="absolute bottom-20 left-[5%] w-28 h-28 bg-[#fbbf24]/20 rounded-full blur-sm" />
      <div className="max-w-7xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-2xl">🗺️</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-white mt-4 max-w-3xl leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}
        >
          Simple to start. Structured to transform.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-white/90 max-w-2xl leading-relaxed"
        >
          From the moment you enroll to the moment your child delivers their first confident speech — here's exactly what the journey looks like.
        </motion.p>
      </div>
      <div className="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 60" fill="none" className="w-full"><path d="M0,30 C360,60 720,0 1440,30 L1440,60 L0,60 Z" fill="#fffbf5" /></svg></div>
    </section>
  )
}

function Steps() {
  const steps = [
    { emoji: "📋", title: "Choose Your Program", desc: "Pick the right age group — Young Speakers (6–10), Rising Voices (11–14), or Future Leaders (15–18). Then choose your format: group classes, one-on-one coaching, or online sessions." },
    { emoji: "👥", title: "Join a Small Cohort", desc: "Your child is placed in a small group of peers at a similar level. Groups are kept small — every child gets personal attention, time at the front, and direct feedback." },
    { emoji: "🎤", title: "Learn by Doing — Every Session", desc: "No lectures. No workbooks. Every weekly session is built around active participation — speeches, debates, impromptu challenges, role plays, and group discussions." },
    { emoji: "💬", title: "Get Real Feedback", desc: "After every speech or exercise, children receive structured feedback — what worked, what to improve, and how. They also learn to give feedback to peers." },
    { emoji: "📈", title: "Progress Through Phases", desc: "The 6-month program is divided into three phases: Foundation (months 1–2), Development (months 3–4), and Mastery (months 5–6). You'll get progress updates at every milestone." },
    { emoji: "🏆", title: "Showcase & Certificate", desc: "At the end, children deliver a final presentation to parents and peers. They receive a certificate and a detailed growth report. Many continue into the next track!" },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader label="The journey" title="Six steps from enrollment to transformation. 🦋" />
      <div className="max-w-3xl mx-auto space-y-6">
        {steps.map((s, i) => (
          <FadeIn key={s.title} delay={i * 0.08}>
            <div className="flex gap-5">
              <div className="flex flex-col items-center">
                <motion.div
                  className="w-16 h-16 rounded-3xl bg-[#e0f2fe] flex items-center justify-center shrink-0 text-3xl border-2 border-[#bae6fd]"
                  whileHover={{ rotate: [0, -5, 5, 0], scale: 1.1 }}
                >
                  {s.emoji}
                </motion.div>
                {i < steps.length - 1 && <div className="w-0.5 h-full bg-[#bae6fd] mt-3" />}
              </div>
              <div className="pb-6">
                <span className="text-xs font-black text-[#0ea5e9] uppercase tracking-widest">Step {String(i + 1).padStart(2, "0")}</span>
                <h3 className="text-xl font-black text-gray-900 mt-1 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{s.title}</h3>
                <p className="text-gray-500 leading-relaxed">{s.desc}</p>
              </div>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function Method() {
  const principles = [
    { emoji: "🔄", title: "Repetition builds reflex", desc: "Confidence isn't a feeling — it's a habit. By speaking every session, presenting becomes natural instead of terrifying." },
    { emoji: "🎯", title: "Feedback accelerates growth", desc: "Children don't improve by speaking into a void. Structured feedback teaches them to self-correct and continuously improve." },
    { emoji: "🛡️", title: "Small groups create safety", desc: "Large audiences intimidate. Small cohorts of peers create a safe space to fail, try again, and eventually thrive." },
    { emoji: "📊", title: "Progressive challenge prevents plateaus", desc: "Each phase introduces harder formats — impromptu speaking, debates, panel discussions. The difficulty curve keeps growth consistent." },
  ]

  return (
    <Section className="bg-white">
      <SectionHeader label="Our method" title="Why it actually works." subtitle="Every element of our training is designed around four principles." />
      <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {principles.map((p, i) => (
          <FadeIn key={p.title} delay={i * 0.1}>
            <motion.div className="bg-[#fffbf5] p-7 rounded-3xl border border-gray-100" whileHover={{ y: -3 }}>
              <span className="text-3xl">{p.emoji}</span>
              <h3 className="font-black text-lg text-gray-900 mt-3 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{p.title}</h3>
              <p className="text-gray-500 leading-relaxed">{p.desc}</p>
            </motion.div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function Timeline() {
  const items = [
    { time: "Week 1–2", emoji: "🌱", title: "The quiet start", desc: "Most children are nervous. They speak softly, avoid eye contact, and rely on notes. This is normal. The safe environment begins to do its work." },
    { time: "Month 1", emoji: "💡", title: "Small breakthroughs", desc: "Your child starts volunteering to go first. Their voice gets steadier. They begin making eye contact. At home, you notice them expressing opinions more clearly." },
    { time: "Month 3", emoji: "🔥", title: "Visible confidence", desc: "They're handling impromptu challenges. They disagree respectfully in debates. Teachers start noticing. Other parents ask what happened." },
    { time: "Month 6", emoji: "🦋", title: "A different communicator", desc: "Your child delivers a polished presentation to an audience. They hold the room. They handle questions. This isn't the same child who started." },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader label="What to expect" title="The transformation timeline. ⏱️" subtitle="Here's what parents typically notice at each stage." />
      <div className="max-w-3xl mx-auto">
        {items.map((item, i) => (
          <FadeIn key={item.time} delay={i * 0.1}>
            <div className="flex gap-6 mb-8">
              <div className="w-20 shrink-0 text-center">
                <span className="text-2xl block mb-1">{item.emoji}</span>
                <span className="text-xs font-black text-[#0ea5e9]">{item.time}</span>
              </div>
              <div className="border-l-3 border-[#bae6fd] pl-6 pb-4">
                <h3 className="font-black text-gray-900 mb-1" style={{ fontFamily: "Nunito, sans-serif" }}>{item.title}</h3>
                <p className="text-gray-500 leading-relaxed">{item.desc}</p>
              </div>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function CTA() {
  return (
    <section className="relative overflow-hidden">
      <div className="bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] py-20 md:py-28 px-6">
        <div className="absolute top-0 left-0 right-0"><svg viewBox="0 0 1440 60" fill="none" className="w-full"><path d="M0,0 L1440,0 L1440,30 C1080,60 360,0 0,30 Z" fill="#fffbf5" /></svg></div>
        <div className="text-center max-w-3xl mx-auto relative z-10">
          <FadeIn>
            <span className="text-5xl block mb-4">⏰</span>
            <h2 className="text-3xl md:text-4xl font-black text-white" style={{ fontFamily: "Nunito, sans-serif" }}>The longer you wait, the more confidence they lose.</h2>
            <p className="mt-5 text-lg text-white/90">Start this quarter. By the end of the year, your child will be a completely different communicator.</p>
            <Link to="/contact">
              <motion.button className="mt-8 bg-[#fbbf24] hover:bg-[#f59e0b] text-gray-900 font-black px-8 py-4 rounded-full text-lg inline-flex items-center gap-2 shadow-lg shadow-amber-300/30 transition-colors" style={{ fontFamily: "Nunito, sans-serif" }} whileHover={{ scale: 1.05, y: -2 }} whileTap={{ scale: 0.95 }}>
                Enroll Your Child ✨ <ArrowRight size={20} />
              </motion.button>
            </Link>
          </FadeIn>
        </div>
      </div>
    </section>
  )
}

export default function HowItWorks() {
  return (
    <>
      <PageHero />
      <Steps />
      <Method />
      <Timeline />
      <CTA />
    </>
  )
}
