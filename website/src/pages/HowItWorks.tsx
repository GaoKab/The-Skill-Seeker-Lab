import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import {
  ArrowRight,
  ClipboardList,
  Users,
  Mic,
  TrendingUp,
  MessageSquare,
  RotateCcw,
  Award,
} from "lucide-react"

function PageHero() {
  return (
    <section className="bg-gradient-to-br from-slate-900 via-teal-950 to-slate-900 pt-32 pb-20 px-6">
      <div className="max-w-7xl mx-auto">
        <motion.span
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="text-teal-400 font-semibold text-sm uppercase tracking-wide"
        >
          How It Works
        </motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-bold text-white mt-4 max-w-3xl tracking-tight"
        >
          Simple to start. Structured to transform.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-slate-300 max-w-2xl leading-relaxed"
        >
          From the moment you enroll to the moment your child delivers their
          first confident speech — here's exactly what the journey looks
          like.
        </motion.p>
      </div>
    </section>
  )
}

function Steps() {
  const steps = [
    {
      icon: ClipboardList,
      num: "01",
      title: "Choose Your Program",
      desc: "Pick the right age group — Young Speakers (6–10), Rising Voices (11–14), or Future Leaders (15–18). Then choose your format: group classes, one-on-one coaching, or online sessions. Not sure? We'll help you decide.",
    },
    {
      icon: Users,
      num: "02",
      title: "Join a Small Cohort",
      desc: "Your child is placed in a small group of peers at a similar level. Groups are kept small intentionally — every child gets personal attention, time at the front of the room, and direct feedback from facilitators.",
    },
    {
      icon: Mic,
      num: "03",
      title: "Learn by Doing — Every Session",
      desc: "No lectures. No workbooks. Every weekly session is built around active participation — speeches, debates, impromptu challenges, role plays, and group discussions. Your child speaks every single session.",
    },
    {
      icon: MessageSquare,
      num: "04",
      title: "Get Real Feedback",
      desc: "After every speech or exercise, children receive structured feedback — what worked, what to improve, and how. They also learn to give feedback to peers, which deepens their own understanding.",
    },
    {
      icon: RotateCcw,
      num: "05",
      title: "Progress Through Phases",
      desc: "The 6-month program is divided into three phases: Foundation (months 1–2), Development (months 3–4), and Mastery (months 5–6). Each phase builds on the last. You'll get progress updates at every milestone.",
    },
    {
      icon: Award,
      num: "06",
      title: "Showcase & Certificate",
      desc: "At the end of each program, children deliver a final presentation to an audience of parents and peers. They receive a certificate and a detailed report on their growth. Many choose to continue into the next track.",
    },
  ]

  return (
    <Section>
      <SectionHeader
        label="The journey"
        title="Six steps from enrollment to transformation."
      />
      <div className="max-w-3xl mx-auto space-y-10">
        {steps.map((s, i) => (
          <FadeIn key={s.num} delay={i * 0.08}>
            <div className="flex gap-6">
              <div className="flex flex-col items-center">
                <div className="w-14 h-14 rounded-2xl bg-teal-50 flex items-center justify-center shrink-0">
                  <s.icon size={24} className="text-teal-600" />
                </div>
                {i < steps.length - 1 && (
                  <div className="w-px h-full bg-teal-100 mt-3" />
                )}
              </div>
              <div className="pb-8">
                <span className="text-xs font-bold text-teal-500 uppercase tracking-wider">
                  Step {s.num}
                </span>
                <h3 className="text-xl font-bold text-slate-900 mt-1 mb-3">
                  {s.title}
                </h3>
                <p className="text-slate-500 leading-relaxed">{s.desc}</p>
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
    {
      title: "Repetition builds reflex",
      desc: "Confidence isn't a feeling — it's a habit. By speaking every session, the act of presenting becomes natural instead of terrifying.",
    },
    {
      title: "Feedback accelerates growth",
      desc: "Children don't improve by speaking into a void. Structured feedback after every exercise teaches them to self-correct and continuously improve.",
    },
    {
      title: "Small groups create safety",
      desc: "Large audiences intimidate. Small cohorts of peers create a safe space to fail, try again, and eventually thrive.",
    },
    {
      title: "Progressive challenge prevents plateaus",
      desc: "Each phase introduces harder formats — impromptu speaking, debates, panel discussions. The difficulty curve keeps growth consistent.",
    },
  ]

  return (
    <Section className="bg-slate-50">
      <SectionHeader
        label="Our method"
        title="Why it actually works."
        subtitle="The approach isn't complicated. But it is intentional. Every element of our training is designed around four principles."
      />
      <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
        {principles.map((p, i) => (
          <FadeIn key={p.title} delay={i * 0.1}>
            <div className="bg-white p-7 rounded-xl border border-slate-200">
              <h3 className="font-bold text-lg text-slate-900 mb-2">
                {p.title}
              </h3>
              <p className="text-slate-500 leading-relaxed">{p.desc}</p>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function Timeline() {
  return (
    <Section>
      <SectionHeader
        label="What to expect"
        title="The transformation timeline."
        subtitle="Here's what parents typically notice at each stage of the program."
      />
      <div className="max-w-3xl mx-auto">
        {[
          {
            time: "Week 1–2",
            title: "The quiet start",
            desc: "Most children are nervous. They speak softly, avoid eye contact, and rely on notes. This is normal. The safe environment begins to do its work.",
          },
          {
            time: "Month 1",
            title: "Small breakthroughs",
            desc: "Your child starts volunteering to go first. Their voice gets steadier. They begin making eye contact. At home, you notice them expressing opinions more clearly.",
          },
          {
            time: "Month 3",
            title: "Visible confidence",
            desc: "They're handling impromptu challenges. They disagree respectfully in debates. Teachers start noticing changes at school. Other parents ask what happened.",
          },
          {
            time: "Month 6",
            title: "A different communicator",
            desc: "Your child delivers a polished presentation to an audience. They hold the room. They handle questions. You realize this isn't the same child who started 6 months ago.",
          },
        ].map((item, i) => (
          <FadeIn key={item.time} delay={i * 0.1}>
            <div className="flex gap-6 mb-8">
              <div className="w-20 shrink-0">
                <span className="text-sm font-bold text-teal-600">
                  {item.time}
                </span>
              </div>
              <div className="border-l-2 border-teal-200 pl-6 pb-4">
                <h3 className="font-bold text-slate-900 mb-1">
                  {item.title}
                </h3>
                <p className="text-slate-500 leading-relaxed">{item.desc}</p>
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
    <Section className="bg-gradient-to-br from-slate-900 via-teal-950 to-slate-900">
      <div className="text-center max-w-3xl mx-auto">
        <FadeIn>
          <TrendingUp className="text-teal-400 mx-auto mb-4" size={32} />
          <h2 className="text-3xl md:text-4xl font-bold text-white">
            The longer you wait, the more confidence they lose.
          </h2>
          <p className="mt-5 text-lg text-slate-300">
            Start this quarter. By the end of the year, your child will be a
            completely different communicator.
          </p>
          <Link to="/contact">
            <motion.button
              className="mt-8 bg-teal-500 hover:bg-teal-400 text-slate-900 font-bold px-8 py-4 rounded-xl text-lg inline-flex items-center gap-2 transition-colors"
              whileHover={{ scale: 1.03 }}
              whileTap={{ scale: 0.97 }}
            >
              Enroll Your Child
              <ArrowRight size={20} />
            </motion.button>
          </Link>
        </FadeIn>
      </div>
    </Section>
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
