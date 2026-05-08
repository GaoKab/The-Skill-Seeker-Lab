import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import { ArrowRight } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-[#ede9fe] pt-32 pb-20 px-6 overflow-hidden">
      <div className="absolute top-20 right-[10%] w-14 h-14 rounded-full bg-[#a78bfa]/20" />
      <div className="absolute bottom-16 left-[6%] w-10 h-10 rounded-xl bg-[#fbbf24]/20 rotate-12" />
      <div className="absolute top-32 right-[30%] text-3xl text-[#c4b5fd]/40 font-black rotate-45 select-none">✦</div>
      <div className="max-w-4xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="inline-block bg-white text-gray-800 font-black text-sm px-4 py-2 rounded-full rotate-1 shadow-sm mb-6">🗺️ The journey</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}
        >
          Simple to start. <span className="marker-purple">Structured to transform</span>.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-gray-600 max-w-2xl leading-relaxed"
        >
          From the moment you enroll to the moment your child delivers their first confident speech — here's exactly what the journey looks like.
        </motion.p>
      </div>
    </section>
  )
}

function Steps() {
  const steps = [
    { emoji: "📋", title: "Choose Your Program", desc: "Pick the right age group — Young Speakers (6–10), Rising Voices (11–14), or Future Leaders (15–18). Then choose your format: group classes, one-on-one coaching, or online sessions.", bg: "bg-[#dbeafe]" },
    { emoji: "👥", title: "Join a Small Cohort", desc: "Your child is placed in a small group of peers at a similar level. Groups are kept small — every child gets personal attention, time at the front, and direct feedback.", bg: "bg-[#dcfce7]" },
    { emoji: "🎤", title: "Learn by Doing — Every Session", desc: "No lectures. No workbooks. Every weekly session is built around active participation — speeches, debates, impromptu challenges, role plays, and group discussions.", bg: "bg-[#fef3c7]" },
    { emoji: "💬", title: "Get Real Feedback", desc: "After every speech or exercise, children receive structured feedback — what worked, what to improve, and how. They also learn to give feedback to peers.", bg: "bg-[#ede9fe]" },
    { emoji: "📈", title: "Progress Through Phases", desc: "The 6-month program is divided into three phases: Foundation (months 1–2), Development (months 3–4), and Mastery (months 5–6). You'll get progress updates at every milestone.", bg: "bg-[#ffedd5]" },
    { emoji: "🏆", title: "Showcase & Certificate", desc: "At the end, children deliver a final presentation to parents and peers. They receive a certificate and a detailed growth report. Many continue into the next track!", bg: "bg-[#fce7f3]" },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#7c3aed] uppercase tracking-widest mb-4 text-center">Step by step</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Six steps from enrollment to <span className="marker-purple">transformation</span> 🦋
          </h2>
        </FadeIn>

        <div className="space-y-4">
          {steps.map((s, i) => (
            <FadeIn key={s.title} delay={i * 0.08}>
              <div className={`flex gap-5 items-start ${s.bg} p-6 rounded-2xl border-[3px] border-dashed border-gray-200/60`}>
                <div className="flex flex-col items-center shrink-0">
                  <motion.div
                    className="w-14 h-14 rounded-2xl bg-white flex items-center justify-center text-3xl shadow-sm"
                    whileHover={{ rotate: [0, -8, 8, 0], scale: 1.1 }}
                  >
                    {s.emoji}
                  </motion.div>
                </div>
                <div>
                  <span className="text-xs font-black text-gray-400 uppercase tracking-widest">Step {String(i + 1).padStart(2, "0")}</span>
                  <h3 className="text-xl font-black text-gray-900 mt-0.5 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{s.title}</h3>
                  <p className="text-gray-500 leading-relaxed">{s.desc}</p>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function Method() {
  const principles = [
    { emoji: "🔄", title: "Repetition builds reflex", desc: "Confidence isn't a feeling — it's a habit. By speaking every session, presenting becomes natural instead of terrifying.", bg: "bg-[#dbeafe]", tilt: "-rotate-1" },
    { emoji: "🎯", title: "Feedback accelerates growth", desc: "Children don't improve by speaking into a void. Structured feedback teaches them to self-correct and continuously improve.", bg: "bg-[#dcfce7]", tilt: "rotate-1" },
    { emoji: "🛡️", title: "Small groups create safety", desc: "Large audiences intimidate. Small cohorts of peers create a safe space to fail, try again, and eventually thrive.", bg: "bg-[#fef3c7]", tilt: "-rotate-2" },
    { emoji: "📊", title: "Progressive challenge prevents plateaus", desc: "Each phase introduces harder formats — impromptu speaking, debates, panel discussions. The difficulty curve keeps growth consistent.", bg: "bg-[#ede9fe]", tilt: "rotate-2" },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#0ea5e9] uppercase tracking-widest mb-4 text-center">Our method</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Why it <span className="marker-blue">actually works</span>.
          </h2>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6">
          {principles.map((p, i) => (
            <FadeIn key={p.title} delay={i * 0.1}>
              <motion.div
                className={`${p.bg} p-7 rounded-3xl ${p.tilt} border-[3px] border-dashed border-gray-200/60`}
                whileHover={{ rotate: 0, scale: 1.02 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                <span className="text-4xl block mb-3">{p.emoji}</span>
                <h3 className="font-black text-lg text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{p.title}</h3>
                <p className="text-gray-500 leading-relaxed">{p.desc}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function Timeline() {
  const items = [
    { time: "Week 1–2", emoji: "🌱", title: "The quiet start", desc: "Most children are nervous. They speak softly, avoid eye contact, and rely on notes. This is normal. The safe environment begins to do its work.", color: "border-l-[#34d399]" },
    { time: "Month 1", emoji: "💡", title: "Small breakthroughs", desc: "Your child starts volunteering to go first. Their voice gets steadier. They begin making eye contact. At home, you notice them expressing opinions more clearly.", color: "border-l-[#fbbf24]" },
    { time: "Month 3", emoji: "🔥", title: "Visible confidence", desc: "They're handling impromptu challenges. They disagree respectfully in debates. Teachers start noticing. Other parents ask what happened.", color: "border-l-[#f97316]" },
    { time: "Month 6", emoji: "🦋", title: "A different communicator", desc: "Your child delivers a polished presentation to an audience. They hold the room. They handle questions. This isn't the same child who started.", color: "border-l-[#a78bfa]" },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#d97706] uppercase tracking-widest mb-4 text-center">What to expect</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            The transformation <span className="marker-yellow">timeline</span> ⏱️
          </h2>
        </FadeIn>

        <div className="space-y-5">
          {items.map((item, i) => (
            <FadeIn key={item.time} delay={i * 0.1}>
              <div className={`bg-white border-l-4 ${item.color} rounded-r-2xl p-6 shadow-sm`}>
                <div className="flex items-center gap-3 mb-2">
                  <span className="text-2xl">{item.emoji}</span>
                  <span className="text-xs font-black text-gray-400 uppercase tracking-widest">{item.time}</span>
                </div>
                <h3 className="font-black text-gray-900 mb-1" style={{ fontFamily: "Nunito, sans-serif" }}>{item.title}</h3>
                <p className="text-gray-500 leading-relaxed">{item.desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function CTA() {
  return (
    <section className="py-20 px-6 bg-[#ede9fe] relative overflow-hidden">
      <div className="absolute top-10 right-[12%] w-12 h-12 rounded-full bg-[#a78bfa]/15" />
      <div className="absolute bottom-10 left-[10%] w-10 h-10 rounded-xl bg-[#fbbf24]/15 rotate-12" />
      <div className="text-center max-w-3xl mx-auto relative z-10">
        <FadeIn>
          <span className="text-5xl block mb-6">⏰</span>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}>
            The longer you wait, the more <span className="marker-purple">confidence they lose</span>.
          </h2>
          <p className="mt-5 text-lg text-gray-600">Start this quarter. By the end of the year, your child will be a completely different communicator.</p>
          <Link to="/contact">
            <motion.button className="mt-8 bg-[#f97316] hover:bg-[#ea580c] text-white font-black px-8 py-4 rounded-full text-lg inline-flex items-center gap-2 shadow-lg shadow-orange-200 transition-colors" style={{ fontFamily: "Nunito, sans-serif" }} whileHover={{ scale: 1.05, rotate: 1 }} whileTap={{ scale: 0.95 }}>
              Enroll Your Child <ArrowRight size={20} />
            </motion.button>
          </Link>
        </FadeIn>
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
