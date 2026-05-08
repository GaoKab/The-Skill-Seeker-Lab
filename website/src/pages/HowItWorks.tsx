import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import {
  ClipboardList,
  Users,
  Mic,
  MessageSquare,
  TrendingUp,
  Trophy,
  RefreshCw,
  Target,
  Shield,
  BarChart3,
  Sprout,
  Lightbulb,
  Flame,
  Sparkles,
  ArrowRight,
  Clock,
} from "lucide-react"

const springBounce = { type: "spring" as const, stiffness: 300, damping: 15 }

function PageHero() {
  return (
    <section className="relative bg-[#EDE9FE] pt-32 pb-20 px-6 overflow-hidden">
      <div className="absolute top-20 right-[10%] w-14 h-14 rounded-full bg-[#a78bfa]/20" />
      <div className="absolute bottom-16 left-[6%] w-10 h-10 rounded-xl bg-[#fbbf24]/20 rotate-12" />
      <div className="absolute top-32 right-[30%] w-6 h-6 rounded-full bg-[#c4b5fd]/40" />
      <div className="max-w-4xl mx-auto relative z-10">
        <motion.span
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="inline-flex items-center gap-2 bg-white text-gray-800 font-black text-sm px-4 py-2 rounded-full border-2 border-[#C4B5FD] clay-sm mb-6"
        >
          <ClipboardList size={16} className="text-[#4F46E5]" />
          The journey
        </motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight"
        >
          Simple to start. <span className="marker-purple">Structured to transform</span>.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
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
    {
      icon: ClipboardList,
      iconColor: "text-[#3B82F6]",
      title: "Choose Your Program",
      desc: "Pick the right age group — Young Speakers (6–10), Rising Voices (11–14), or Future Leaders (15–18). Then choose your format: group classes, one-on-one coaching, or online sessions.",
      bg: "bg-[#BFDBFE]",
      border: "border-[#93C5FD]",
    },
    {
      icon: Users,
      iconColor: "text-[#22C55E]",
      title: "Join a Small Cohort",
      desc: "Your child is placed in a small group of peers at a similar level. Groups are kept small — every child gets personal attention, time at the front, and direct feedback.",
      bg: "bg-[#BBF7D0]",
      border: "border-[#86EFAC]",
    },
    {
      icon: Mic,
      iconColor: "text-[#EAB308]",
      title: "Learn by Doing — Every Session",
      desc: "No lectures. No workbooks. Every weekly session is built around active participation — speeches, debates, impromptu challenges, role plays, and group discussions.",
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
    },
    {
      icon: MessageSquare,
      iconColor: "text-[#8B5CF6]",
      title: "Get Real Feedback",
      desc: "After every speech or exercise, children receive structured feedback — what worked, what to improve, and how. They also learn to give feedback to peers.",
      bg: "bg-[#DDD6FE]",
      border: "border-[#C4B5FD]",
    },
    {
      icon: TrendingUp,
      iconColor: "text-[#F97316]",
      title: "Progress Through Phases",
      desc: "The 6-month program is divided into three phases: Foundation (months 1–2), Development (months 3–4), and Mastery (months 5–6). You'll get progress updates at every milestone.",
      bg: "bg-[#FED7AA]",
      border: "border-[#FDBA74]",
    },
    {
      icon: Trophy,
      iconColor: "text-[#EC4899]",
      title: "Showcase & Certificate",
      desc: "At the end, children deliver a final presentation to parents and peers. They receive a certificate and a detailed growth report. Many continue into the next track!",
      bg: "bg-[#FBCFE8]",
      border: "border-[#F9A8D4]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#7c3aed] uppercase tracking-widest mb-4 text-center">
            Step by step
          </p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14">
            Six steps from enrollment to <span className="marker-purple">transformation</span>
          </h2>
        </FadeIn>

        <div className="space-y-5">
          {steps.map((s, i) => {
            const Icon = s.icon
            return (
              <FadeIn key={s.title} delay={i * 0.08}>
                <motion.div
                  className={`flex gap-5 items-start ${s.bg} p-6 rounded-2xl border-2 ${s.border} clay`}
                  whileHover={{ scale: 1.02, y: -2 }}
                  transition={springBounce}
                >
                  <div className="flex flex-col items-center shrink-0 gap-1">
                    <div className="w-14 h-14 rounded-2xl bg-white border-2 border-white/60 clay-sm flex items-center justify-center">
                      <Icon size={26} className={s.iconColor} />
                    </div>
                  </div>
                  <div>
                    <span className="text-xs font-black text-gray-400 uppercase tracking-widest">
                      Step {String(i + 1).padStart(2, "0")}
                    </span>
                    <h3 className="text-xl font-black text-gray-900 mt-0.5 mb-2">
                      {s.title}
                    </h3>
                    <p className="text-gray-600 leading-relaxed">{s.desc}</p>
                  </div>
                </motion.div>
              </FadeIn>
            )
          })}
        </div>
      </div>
    </section>
  )
}

function Method() {
  const principles = [
    {
      icon: RefreshCw,
      iconColor: "text-[#3B82F6]",
      title: "Repetition builds reflex",
      desc: "Confidence isn't a feeling — it's a habit. By speaking every session, presenting becomes natural instead of terrifying.",
      bg: "bg-[#BFDBFE]",
      border: "border-[#93C5FD]",
    },
    {
      icon: Target,
      iconColor: "text-[#22C55E]",
      title: "Feedback accelerates growth",
      desc: "Children don't improve by speaking into a void. Structured feedback teaches them to self-correct and continuously improve.",
      bg: "bg-[#BBF7D0]",
      border: "border-[#86EFAC]",
    },
    {
      icon: Shield,
      iconColor: "text-[#EAB308]",
      title: "Small groups create safety",
      desc: "Large audiences intimidate. Small cohorts of peers create a safe space to fail, try again, and eventually thrive.",
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
    },
    {
      icon: BarChart3,
      iconColor: "text-[#8B5CF6]",
      title: "Progressive challenge prevents plateaus",
      desc: "Each phase introduces harder formats — impromptu speaking, debates, panel discussions. The difficulty curve keeps growth consistent.",
      bg: "bg-[#DDD6FE]",
      border: "border-[#C4B5FD]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#0ea5e9] uppercase tracking-widest mb-4 text-center">
            Our method
          </p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14">
            Why it <span className="marker-blue">actually works</span>.
          </h2>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6">
          {principles.map((p, i) => {
            const Icon = p.icon
            return (
              <FadeIn key={p.title} delay={i * 0.1}>
                <motion.div
                  className={`${p.bg} p-7 rounded-3xl border-2 ${p.border} clay`}
                  whileHover={{ scale: 1.03, y: -3 }}
                  transition={springBounce}
                >
                  <div className="w-12 h-12 rounded-2xl bg-white border-2 border-white/60 clay-sm flex items-center justify-center mb-4">
                    <Icon size={24} className={p.iconColor} />
                  </div>
                  <h3 className="font-black text-lg text-gray-900 mb-2">
                    {p.title}
                  </h3>
                  <p className="text-gray-600 leading-relaxed">{p.desc}</p>
                </motion.div>
              </FadeIn>
            )
          })}
        </div>
      </div>
    </section>
  )
}

function Timeline() {
  const items = [
    {
      time: "Week 1–2",
      icon: Sprout,
      iconColor: "text-[#34d399]",
      title: "The quiet start",
      desc: "Most children are nervous. They speak softly, avoid eye contact, and rely on notes. This is normal. The safe environment begins to do its work.",
      color: "border-l-[#34d399]",
      bg: "bg-[#BBF7D0]",
      border: "border-[#86EFAC]",
    },
    {
      time: "Month 1",
      icon: Lightbulb,
      iconColor: "text-[#fbbf24]",
      title: "Small breakthroughs",
      desc: "Your child starts volunteering to go first. Their voice gets steadier. They begin making eye contact. At home, you notice them expressing opinions more clearly.",
      color: "border-l-[#fbbf24]",
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
    },
    {
      time: "Month 3",
      icon: Flame,
      iconColor: "text-[#f97316]",
      title: "Visible confidence",
      desc: "They're handling impromptu challenges. They disagree respectfully in debates. Teachers start noticing. Other parents ask what happened.",
      color: "border-l-[#f97316]",
      bg: "bg-[#FED7AA]",
      border: "border-[#FDBA74]",
    },
    {
      time: "Month 6",
      icon: Sparkles,
      iconColor: "text-[#a78bfa]",
      title: "A different communicator",
      desc: "Your child delivers a polished presentation to an audience. They hold the room. They handle questions. This isn't the same child who started.",
      color: "border-l-[#a78bfa]",
      bg: "bg-[#DDD6FE]",
      border: "border-[#C4B5FD]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#d97706] uppercase tracking-widest mb-4 text-center">
            What to expect
          </p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14">
            The transformation <span className="marker-yellow">timeline</span>
          </h2>
        </FadeIn>

        <div className="space-y-5">
          {items.map((item, i) => {
            const Icon = item.icon
            return (
              <FadeIn key={item.time} delay={i * 0.1}>
                <motion.div
                  className={`${item.bg} border-l-4 ${item.color} border-2 ${item.border} rounded-2xl p-6 clay`}
                  whileHover={{ scale: 1.02, x: 4 }}
                  transition={springBounce}
                >
                  <div className="flex items-center gap-3 mb-2">
                    <div className="w-10 h-10 rounded-xl bg-white border-2 border-white/60 clay-sm flex items-center justify-center">
                      <Icon size={20} className={item.iconColor} />
                    </div>
                    <span className="text-xs font-black text-gray-400 uppercase tracking-widest">
                      {item.time}
                    </span>
                  </div>
                  <h3 className="font-black text-gray-900 mb-1">{item.title}</h3>
                  <p className="text-gray-600 leading-relaxed">{item.desc}</p>
                </motion.div>
              </FadeIn>
            )
          })}
        </div>
      </div>
    </section>
  )
}

function CTA() {
  return (
    <section className="py-20 px-6 bg-[#EDE9FE] relative overflow-hidden">
      <div className="absolute top-10 right-[12%] w-12 h-12 rounded-full bg-[#a78bfa]/15" />
      <div className="absolute bottom-10 left-[10%] w-10 h-10 rounded-xl bg-[#fbbf24]/15 rotate-12" />
      <div className="text-center max-w-3xl mx-auto relative z-10">
        <FadeIn>
          <div className="w-16 h-16 rounded-2xl bg-white border-2 border-[#C4B5FD] clay-sm flex items-center justify-center mx-auto mb-6">
            <Clock size={32} className="text-[#4F46E5]" />
          </div>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 leading-tight">
            The longer you wait, the more <span className="marker-purple">confidence they lose</span>.
          </h2>
          <p className="mt-5 text-lg text-gray-600">
            Start this quarter. By the end of the year, your child will be a completely different communicator.
          </p>
          <Link to="/contact">
            <motion.button
              className="mt-8 bg-[#F97316] text-white font-black px-8 py-4 rounded-2xl border-2 border-[#EA580C] clay-sm text-lg inline-flex items-center gap-2 transition-colors hover:bg-[#ea580c]"
              whileHover={{ scale: 1.05, rotate: 1 }}
              whileTap={{ scale: 0.95 }}
              transition={springBounce}
            >
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
