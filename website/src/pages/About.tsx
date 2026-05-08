import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import {
  ArrowRight, BookOpen, Search, Target,
  TrendingUp, Heart, Globe, Quote,
} from "lucide-react"

const bounce = { type: "spring" as const, stiffness: 300, damping: 15 }

function PageHero() {
  return (
    <section className="relative bg-[#FEF3C7] pt-32 pb-20 px-6 overflow-hidden">
      <div className="absolute top-20 right-[10%] w-14 h-14 rounded-2xl bg-[#FBCFE8] border-2 border-[#F9A8D4] clay rotate-6 opacity-50" />
      <div className="absolute bottom-16 left-[6%] w-12 h-12 rounded-2xl bg-[#DDD6FE] border-2 border-[#C4B5FD] clay -rotate-12 opacity-50" />
      <div className="absolute top-36 left-[18%] w-10 h-10 rounded-xl bg-[#BBF7D0] border-2 border-[#86EFAC] clay rotate-12 opacity-40" />
      <div className="max-w-4xl mx-auto relative z-10">
        <motion.span
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="inline-flex items-center gap-2 bg-white border-2 border-gray-200 text-gray-800 font-black text-sm px-4 py-2 rounded-2xl clay-sm mb-6"
        >
          <BookOpen className="w-4 h-4 text-[#4F46E5]" />
          Our story
        </motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight"
        >
          We're building the academy{" "}
          <span className="marker-yellow">Botswana's children deserve</span>.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-gray-600 max-w-2xl leading-relaxed"
        >
          Find Your Voice isn't a workshop or a one-day event. It's a structured
          communication training academy that develops confident, articulate, and
          thoughtful young people — one cohort at a time.
        </motion.p>
      </div>
    </section>
  )
}

function Story() {
  const paragraphs = [
    "Mpho Kabelo didn't set out to start an academy. It started with a simple observation: brilliant children in Botswana were going quiet. Not because they had nothing to say — but because no one had ever shown them how to say it.",
    "In classrooms, the same three kids would raise their hands. In family gatherings, teenagers would sit in silence while adults spoke. At school presentations, children would read from notes without ever looking up. The pattern was everywhere — and it wasn't about talent. It was about training.",
    "Find Your Voice was created to fill that gap. Not with motivational talks or weekend workshops that fade by Monday, but with a structured system that builds real communication skills over months — through practice, feedback, and repetition.",
    "Based in Gaborone and expanding across Botswana, the academy now trains children ages 6–18 through group classes, school partnerships, one-on-one coaching, and online sessions.",
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#4F46E5] uppercase tracking-widest mb-4">
            Our Origin
          </p>
          <h2 className="text-3xl md:text-4xl font-black text-gray-900 mb-10">
            The story behind{" "}
            <span className="marker-green">Find Your Voice</span>
          </h2>
        </FadeIn>
        {paragraphs.map((text, i) => (
          <FadeIn key={i} delay={0.1 + i * 0.05}>
            <p className="text-gray-500 text-lg leading-relaxed mb-5">{text}</p>
          </FadeIn>
        ))}
        <FadeIn delay={0.3}>
          <div className="bg-[#FDE68A]/40 border-3 border-[#FCD34D] rounded-3xl p-8 mt-8 clay">
            <div className="flex items-start gap-4">
              <div className="w-12 h-12 rounded-2xl bg-[#FDE68A] border-2 border-[#FCD34D] flex items-center justify-center clay-sm shrink-0">
                <Quote className="w-5 h-5 text-[#B45309]" />
              </div>
              <p className="text-gray-800 font-bold text-lg italic leading-relaxed">
                "Communication is a skill, and like any skill, it can be taught."
              </p>
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

function Values() {
  const values = [
    {
      icon: Search,
      title: "Clarity Over Volume",
      desc: "We don't teach children to be loud. We teach them to be clear. The child who can organize their thoughts will always outperform the one who shouts.",
      bg: "bg-[#BFDBFE]",
      border: "border-[#93C5FD]",
      iconColor: "text-[#1D4ED8]",
    },
    {
      icon: Target,
      title: "Practice, Not Theory",
      desc: "Every session is built around doing — speeches, debates, group discussions, impromptu challenges. Children learn by speaking, not by watching.",
      bg: "bg-[#BBF7D0]",
      border: "border-[#86EFAC]",
      iconColor: "text-[#15803D]",
    },
    {
      icon: TrendingUp,
      title: "Long-Term Development",
      desc: "Our programs run 6 to 12 months because confidence doesn't happen in a day. We build skills progressively, so each phase deepens what came before.",
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
      iconColor: "text-[#B45309]",
    },
    {
      icon: Heart,
      title: "Every Voice Matters",
      desc: "We keep groups small. Every child gets time at the front of the room, personal feedback, and the space to grow at their own pace.",
      bg: "bg-[#DDD6FE]",
      border: "border-[#C4B5FD]",
      iconColor: "text-[#6D28D9]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#F97316] uppercase tracking-widest mb-4 text-center">
            Our principles
          </p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14">
            What guides{" "}
            <span className="marker-coral">everything we do</span>.
          </h2>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6">
          {values.map((v, i) => (
            <FadeIn key={v.title} delay={i * 0.1}>
              <motion.div
                className={`${v.bg} p-8 rounded-3xl border-3 ${v.border} clay`}
                whileHover={{ scale: 1.02, y: -4 }}
                transition={bounce}
              >
                <motion.div
                  className={`w-14 h-14 rounded-2xl bg-white/60 border-2 ${v.border} flex items-center justify-center clay-sm mb-4`}
                  whileHover={{ scale: 1.1, rotate: [-2, 2, 0] }}
                  transition={bounce}
                >
                  <v.icon className={`w-6 h-6 ${v.iconColor}`} />
                </motion.div>
                <h3 className="text-xl font-black text-gray-900 mb-2">
                  {v.title}
                </h3>
                <p className="text-gray-600 leading-relaxed">{v.desc}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function Vision() {
  return (
    <section className="py-20 px-6 bg-[#fef9e7] relative overflow-hidden">
      <div className="absolute top-8 right-[10%] w-16 h-16 rounded-2xl bg-[#BFDBFE] border-2 border-[#93C5FD] clay rotate-12 opacity-40" />
      <div className="absolute bottom-12 left-[8%] w-12 h-12 rounded-2xl bg-[#FDE68A] border-2 border-[#FCD34D] clay -rotate-6 opacity-40" />
      <div className="absolute top-[45%] right-[4%] w-10 h-10 rounded-xl bg-[#BBF7D0] border-2 border-[#86EFAC] clay rotate-6 opacity-30" />
      <div className="max-w-3xl mx-auto text-center relative z-10">
        <FadeIn>
          <motion.div
            className="w-16 h-16 rounded-2xl bg-[#FED7AA] border-2 border-[#FDBA74] flex items-center justify-center clay-sm mx-auto mb-6"
            whileHover={{ scale: 1.1, rotate: [-2, 2, 0] }}
            transition={bounce}
          >
            <Globe className="w-7 h-7 text-[#C2410C]" />
          </motion.div>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 mb-6 leading-tight">
            A Botswana where no young person holds back because they were{" "}
            <span className="marker-yellow">never taught how to speak up</span>.
          </h2>
          <p className="text-gray-500 text-lg leading-relaxed mb-10">
            We're starting in Gaborone. But the plan is bigger — school
            partnerships nationwide, online programs for children everywhere in
            Botswana, and eventually a model that can be replicated across
            Southern Africa. Every child deserves the tools to be heard.
          </p>
          <Link to="/contact">
            <motion.button
              className="bg-[#F97316] text-white font-bold px-8 py-4 rounded-2xl text-lg inline-flex items-center gap-2 border-2 border-[#EA580C] clay-sm transition-all"
              whileHover={{ scale: 1.05, rotate: 1 }}
              whileTap={{ scale: 0.95 }}
              transition={bounce}
            >
              Join the Movement <ArrowRight className="w-5 h-5" />
            </motion.button>
          </Link>
        </FadeIn>
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
