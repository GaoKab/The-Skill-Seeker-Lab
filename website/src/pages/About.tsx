import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import { ArrowRight } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] pt-32 pb-24 px-6 overflow-hidden">
      <div className="absolute top-16 right-[10%] w-32 h-32 bg-white/10 rounded-full blur-sm" />
      <div className="absolute bottom-16 left-[5%] w-24 h-24 bg-[#fbbf24]/20 rounded-full blur-sm" />
      <div className="max-w-7xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-2xl">📖</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-white mt-4 max-w-3xl leading-tight"
          style={{ fontFamily: "Nunito, sans-serif" }}
        >
          We're building the academy Botswana's children deserve.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-white/90 max-w-2xl leading-relaxed"
        >
          Find Your Voice isn't a workshop. It isn't a one-day event. It's a
          structured communication training academy that develops confident,
          articulate, and thoughtful young people — one cohort at a time.
        </motion.p>
      </div>
      <div className="absolute bottom-0 left-0 right-0">
        <svg viewBox="0 0 1440 60" fill="none" className="w-full"><path d="M0,30 C360,60 720,0 1440,30 L1440,60 L0,60 Z" fill="#fffbf5" /></svg>
      </div>
    </section>
  )
}

function Story() {
  return (
    <Section className="bg-[#fffbf5]">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <h2 className="text-3xl md:text-4xl font-black text-gray-900 mb-8" style={{ fontFamily: "Nunito, sans-serif" }}>
            The story behind Find Your Voice 💬
          </h2>
        </FadeIn>
        {[
          "Mpho Kabelo didn't set out to start an academy. It started with a simple observation: brilliant children in Botswana were going quiet. Not because they had nothing to say — but because no one had ever shown them *how* to say it.",
          "In classrooms, the same three kids would raise their hands. In family gatherings, teenagers would sit in silence while adults spoke. At school presentations, children would read from notes without ever looking up. The pattern was everywhere — and it wasn't about talent. It was about training.",
          "Find Your Voice was created to fill that gap. Not with motivational talks or weekend workshops that fade by Monday, but with a structured system that builds real communication skills over months — through practice, feedback, and repetition.",
          "Based in Gaborone and expanding across Botswana, the academy now trains children ages 6–18 through group classes, school partnerships, one-on-one coaching, and online sessions. Every program is built around the same principle: **communication is a skill, and like any skill, it can be taught.**",
        ].map((text, i) => (
          <FadeIn key={i} delay={0.1 + i * 0.05}>
            <p className="text-gray-500 text-lg leading-relaxed mb-5">{text}</p>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function Values() {
  const values = [
    { emoji: "🔍", title: "Clarity Over Volume", desc: "We don't teach children to be loud. We teach them to be clear. The child who can organize their thoughts and express them simply will always outperform the one who shouts." },
    { emoji: "🎯", title: "Practice, Not Theory", desc: "Every session is built around doing — speeches, debates, group discussions, impromptu challenges. Children learn by speaking, not by watching someone else do it." },
    { emoji: "📈", title: "Long-Term Development", desc: "Our programs run 6 to 12 months because confidence doesn't happen in a day. We build skills progressively, so each phase deepens what came before." },
    { emoji: "💛", title: "Every Voice Matters", desc: "We keep groups small. Every child gets time at the front of the room, personal feedback, and the space to grow at their own pace. No one gets lost in the crowd." },
  ]

  return (
    <Section className="bg-white">
      <SectionHeader label="Our principles" title="What guides everything we do." />
      <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {values.map((v, i) => (
          <FadeIn key={v.title} delay={i * 0.1}>
            <motion.div
              className="flex items-start gap-5 bg-[#fffbf5] p-7 rounded-3xl border border-gray-100"
              whileHover={{ y: -3 }}
            >
              <span className="text-3xl">{v.emoji}</span>
              <div>
                <h3 className="font-black text-lg text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{v.title}</h3>
                <p className="text-gray-500 leading-relaxed">{v.desc}</p>
              </div>
            </motion.div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function Vision() {
  return (
    <section className="relative overflow-hidden">
      <div className="bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] py-20 md:py-28 px-6">
        <div className="absolute top-0 left-0 right-0">
          <svg viewBox="0 0 1440 60" fill="none" className="w-full"><path d="M0,0 L1440,0 L1440,30 C1080,60 360,0 0,30 Z" fill="white" /></svg>
        </div>
        <div className="max-w-3xl mx-auto text-center relative z-10">
          <FadeIn>
            <span className="text-5xl block mb-4">🌍</span>
            <h2 className="text-3xl md:text-4xl font-black text-white mb-6" style={{ fontFamily: "Nunito, sans-serif" }}>
              A Botswana where no young person holds back because they were never taught how to speak up.
            </h2>
            <p className="text-white/90 text-lg leading-relaxed mb-10">
              We're starting in Gaborone. But the plan is bigger — school
              partnerships nationwide, online programs for children everywhere
              in Botswana, and eventually a model that can be replicated across
              Southern Africa. Every child deserves the tools to be heard.
            </p>
            <Link to="/contact">
              <motion.button
                className="bg-[#fbbf24] hover:bg-[#f59e0b] text-gray-900 font-black px-8 py-4 rounded-full text-lg inline-flex items-center gap-2 shadow-lg shadow-amber-300/30 transition-colors"
                style={{ fontFamily: "Nunito, sans-serif" }}
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                Join the Movement ✨
                <ArrowRight size={20} />
              </motion.button>
            </Link>
          </FadeIn>
        </div>
      </div>
    </section>
  )
}

export default function About() {
  return (
    <>
      <PageHero />
      <Story />
      <Values />
      <Vision />
    </>
  )
}
