import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import {
  MessageCircle,
  Brain,
  Users,
  Trophy,
  ArrowRight,
  CheckCircle2,
  Sparkles,
  Target,
  GraduationCap,
  Lightbulb,
  Star,
  Mic,
} from "lucide-react"

/* ─── Hero ─── */
function Hero() {
  return (
    <section className="relative min-h-screen flex items-center bg-gradient-to-br from-slate-900 via-teal-950 to-slate-900 overflow-hidden">
      {/* Decorative circles */}
      <div className="absolute top-20 right-10 w-72 h-72 bg-teal-500/10 rounded-full blur-3xl" />
      <div className="absolute bottom-20 left-10 w-96 h-96 bg-teal-600/5 rounded-full blur-3xl" />

      <div className="max-w-7xl mx-auto px-6 pt-28 pb-20 relative z-10">
        <div className="max-w-3xl">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="inline-flex items-center gap-2 bg-teal-500/10 border border-teal-500/20 rounded-full px-4 py-1.5 mb-8"
          >
            <Sparkles size={14} className="text-teal-400" />
            <span className="text-teal-300 text-sm font-medium">
              Now enrolling in Gaborone
            </span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.1 }}
            className="text-4xl md:text-6xl lg:text-7xl font-bold text-white tracking-tight leading-[1.1]"
          >
            Every child has a voice.{" "}
            <span className="text-teal-400">We help them use it.</span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.25 }}
            className="mt-7 text-lg md:text-xl text-slate-300 leading-relaxed max-w-2xl"
          >
            Find Your Voice is Botswana's premier youth communication academy.
            We train children ages 6–18 to speak with clarity, think critically,
            and lead with confidence — through structured programs that build
            real skills, not just stage presence.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.4 }}
            className="mt-10 flex flex-col sm:flex-row gap-4"
          >
            <Link to="/contact">
              <motion.button
                className="bg-teal-500 hover:bg-teal-400 text-slate-900 font-bold px-8 py-4 rounded-xl text-lg flex items-center gap-2 transition-colors w-full sm:w-auto justify-center"
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
              >
                Enroll Your Child
                <ArrowRight size={20} />
              </motion.button>
            </Link>
            <Link to="/programs">
              <motion.button
                className="border border-slate-500 hover:border-teal-400 text-white font-semibold px-8 py-4 rounded-xl text-lg transition-colors w-full sm:w-auto justify-center"
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
              >
                Explore Programs
              </motion.button>
            </Link>
          </motion.div>

          {/* Quick proof */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.7, delay: 0.6 }}
            className="mt-14 flex flex-wrap gap-8 text-sm text-slate-400"
          >
            {[
              "Ages 6–18",
              "Group & 1-on-1 Sessions",
              "In-Person & Online",
              "6-Month Structured Program",
            ].map((item) => (
              <span key={item} className="flex items-center gap-2">
                <CheckCircle2 size={14} className="text-teal-500" />
                {item}
              </span>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  )
}

/* ─── Problem ─── */
function Problem() {
  const problems = [
    {
      text: "Struggles to speak up in class or around adults",
      icon: MessageCircle,
    },
    {
      text: "Avoids eye contact and mumbles through conversations",
      icon: Users,
    },
    {
      text: "Has great ideas but can't express them clearly",
      icon: Lightbulb,
    },
    {
      text: "Freezes during presentations or group activities",
      icon: Target,
    },
  ]

  return (
    <Section className="bg-slate-50">
      <SectionHeader
        label="The reality"
        title="You've noticed it. So have they."
        subtitle="Most children aren't taught how to communicate with confidence. They're expected to just figure it out. Some do. Most don't."
      />
      <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {problems.map((p, i) => (
          <FadeIn key={p.text} delay={i * 0.1}>
            <div className="flex items-start gap-4 bg-white p-6 rounded-xl border border-slate-200">
              <div className="w-10 h-10 rounded-lg bg-red-50 flex items-center justify-center shrink-0">
                <p.icon size={20} className="text-red-400" />
              </div>
              <p className="text-slate-700 leading-relaxed">{p.text}</p>
            </div>
          </FadeIn>
        ))}
      </div>
      <FadeIn delay={0.4}>
        <p className="text-center mt-10 text-slate-500 text-lg max-w-2xl mx-auto">
          It's not a character flaw. It's a skill gap. And skills can be
          taught.
        </p>
      </FadeIn>
    </Section>
  )
}

/* ─── Solution ─── */
function Solution() {
  const pillars = [
    {
      icon: Mic,
      title: "Communication",
      desc: "Articulate ideas with structure, clarity, and conviction — in any setting.",
    },
    {
      icon: Brain,
      title: "Critical Thinking",
      desc: "Analyze, question, and form opinions independently — not just repeat what they're told.",
    },
    {
      icon: Trophy,
      title: "Confidence",
      desc: "Stand in front of any room and own the moment — without fear or hesitation.",
    },
    {
      icon: Users,
      title: "Leadership",
      desc: "Influence, collaborate, and inspire — skills that compound for a lifetime.",
    },
  ]

  return (
    <Section>
      <SectionHeader
        label="What we build"
        title="This is not just public speaking."
        subtitle="Find Your Voice is a structured training system that develops four core capabilities in every child who comes through our program."
      />
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        {pillars.map((p, i) => (
          <FadeIn key={p.title} delay={i * 0.1}>
            <motion.div
              className="text-center p-6"
              whileHover={{ y: -4 }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <div className="w-14 h-14 rounded-2xl bg-teal-50 flex items-center justify-center mx-auto mb-5">
                <p.icon size={26} className="text-teal-600" />
              </div>
              <h3 className="font-bold text-lg text-slate-900 mb-2">
                {p.title}
              </h3>
              <p className="text-slate-500 text-sm leading-relaxed">
                {p.desc}
              </p>
            </motion.div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

/* ─── Program Overview ─── */
function ProgramOverview() {
  const programs = [
    {
      age: "Ages 6–10",
      name: "Young Speakers",
      desc: "Foundational communication skills through storytelling, show-and-tell, and structured play. Children learn to organize thoughts and speak in front of small groups.",
      color: "bg-teal-50 border-teal-200",
      accent: "text-teal-700",
    },
    {
      age: "Ages 11–14",
      name: "Rising Voices",
      desc: "Intermediate training in debate, persuasive speaking, and group discussion. Students develop critical thinking and learn to defend ideas under pressure.",
      color: "bg-amber-50 border-amber-200",
      accent: "text-amber-700",
    },
    {
      age: "Ages 15–18",
      name: "Future Leaders",
      desc: "Advanced leadership communication — presentations, panel discussions, interview preparation, and real-world speaking opportunities that build a portfolio.",
      color: "bg-slate-50 border-slate-200",
      accent: "text-slate-700",
    },
  ]

  return (
    <Section className="bg-teal-950">
      <SectionHeader
        light
        label="Programs"
        title="Structured training for every stage."
        subtitle="Three age-specific programs designed to meet children exactly where they are — and take them further than they thought possible."
      />
      <div className="grid md:grid-cols-3 gap-8">
        {programs.map((p, i) => (
          <FadeIn key={p.name} delay={i * 0.12}>
            <motion.div
              className={`rounded-2xl border p-8 ${p.color} h-full`}
              whileHover={{ y: -6 }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <span
                className={`text-xs font-bold uppercase tracking-wider ${p.accent}`}
              >
                {p.age}
              </span>
              <h3 className="text-2xl font-bold text-slate-900 mt-2 mb-4">
                {p.name}
              </h3>
              <p className="text-slate-600 leading-relaxed">{p.desc}</p>
            </motion.div>
          </FadeIn>
        ))}
      </div>
      <FadeIn delay={0.4}>
        <div className="text-center mt-12">
          <Link
            to="/programs"
            className="inline-flex items-center gap-2 text-teal-400 font-semibold hover:text-teal-300 transition-colors"
          >
            See full program details
            <ArrowRight size={18} />
          </Link>
        </div>
      </FadeIn>
    </Section>
  )
}

/* ─── Benefits ─── */
function Benefits() {
  const benefits = [
    "Your child raises their hand in class — without being asked.",
    "They introduce themselves to adults with eye contact and a firm voice.",
    "They win debates, not because they're loud — because they're clear.",
    "They lead group projects instead of hiding behind them.",
    "They handle disagreements with words, not silence.",
    "They walk into interviews, auditions, and new schools with presence.",
  ]

  return (
    <Section>
      <SectionHeader
        label="The outcome"
        title="What parents actually see."
        subtitle="This isn't about raising a child who gives speeches. It's about raising a child who doesn't shrink."
      />
      <div className="max-w-3xl mx-auto grid sm:grid-cols-2 gap-5">
        {benefits.map((b, i) => (
          <FadeIn key={b} delay={i * 0.08}>
            <div className="flex items-start gap-3">
              <CheckCircle2
                size={20}
                className="text-teal-500 shrink-0 mt-0.5"
              />
              <p className="text-slate-700 leading-relaxed">{b}</p>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

/* ─── How It Works ─── */
function HowItWorksPreview() {
  const steps = [
    {
      num: "01",
      title: "Choose a Program",
      desc: "Select the right age group and format — group classes, one-on-one, or online sessions.",
    },
    {
      num: "02",
      title: "Join a Cohort",
      desc: "Your child joins a small group of peers and begins the structured 6-month training journey.",
    },
    {
      num: "03",
      title: "Learn by Doing",
      desc: "Weekly sessions with speeches, debates, feedback, and real speaking opportunities — not lectures.",
    },
    {
      num: "04",
      title: "See the Transformation",
      desc: "Within weeks, you'll notice the difference. By month 6, they'll be a different communicator.",
    },
  ]

  return (
    <Section className="bg-slate-50">
      <SectionHeader
        label="The process"
        title="How it works."
        subtitle="A simple, structured path from enrollment to transformation."
      />
      <div className="grid md:grid-cols-4 gap-8 max-w-5xl mx-auto">
        {steps.map((s, i) => (
          <FadeIn key={s.num} delay={i * 0.12}>
            <div className="text-center">
              <span className="text-4xl font-bold text-teal-200">
                {s.num}
              </span>
              <h3 className="font-bold text-slate-900 mt-3 mb-2">
                {s.title}
              </h3>
              <p className="text-sm text-slate-500 leading-relaxed">
                {s.desc}
              </p>
            </div>
          </FadeIn>
        ))}
      </div>
      <FadeIn delay={0.5}>
        <div className="text-center mt-12">
          <Link
            to="/how-it-works"
            className="inline-flex items-center gap-2 text-teal-600 font-semibold hover:text-teal-700 transition-colors"
          >
            Learn more about our method
            <ArrowRight size={18} />
          </Link>
        </div>
      </FadeIn>
    </Section>
  )
}

/* ─── Founder / Trust ─── */
function Founder() {
  return (
    <Section>
      <div className="max-w-4xl mx-auto grid md:grid-cols-5 gap-12 items-center">
        <FadeIn className="md:col-span-2">
          <div className="aspect-[4/5] rounded-2xl bg-gradient-to-br from-teal-100 to-teal-200 flex items-center justify-center">
            <div className="text-center">
              <div className="w-24 h-24 rounded-full bg-teal-600 flex items-center justify-center mx-auto mb-4">
                <span className="text-white text-3xl font-bold">MK</span>
              </div>
              <p className="text-teal-800 font-semibold">Mpho Kabelo</p>
              <p className="text-teal-600 text-sm">Founder & Lead Facilitator</p>
            </div>
          </div>
        </FadeIn>
        <FadeIn className="md:col-span-3" delay={0.15}>
          <span className="text-teal-600 font-semibold text-sm uppercase tracking-wide">
            Meet the founder
          </span>
          <h2 className="text-3xl md:text-4xl font-bold text-slate-900 mt-3 mb-6">
            "I started this because I watched too many brilliant kids go
            quiet."
          </h2>
          <p className="text-slate-600 leading-relaxed mb-4">
            Mpho Kabelo founded Find Your Voice after years of watching
            talented young people in Botswana hold back — not because they
            lacked ideas, but because no one taught them how to express those
            ideas with power.
          </p>
          <p className="text-slate-600 leading-relaxed mb-4">
            Find Your Voice was created to fix that gap. Not with one-off
            workshops that children forget by Monday, but with a structured
            training system that builds lasting communication skills over
            time.
          </p>
          <p className="text-slate-600 leading-relaxed">
            The academy is based in Gaborone and is growing across Botswana —
            with plans for online delivery and school partnerships
            nationwide.
          </p>
        </FadeIn>
      </div>
    </Section>
  )
}

/* ─── Testimonials placeholder ─── */
function SocialProof() {
  const stats = [
    { value: "6-Month", label: "Structured Program" },
    { value: "6–18", label: "Age Range" },
    { value: "3", label: "Training Tracks" },
    { value: "100%", label: "Learn-by-Doing" },
  ]

  return (
    <Section className="bg-teal-600">
      <div className="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-4xl mx-auto">
        {stats.map((s, i) => (
          <FadeIn key={s.label} delay={i * 0.1}>
            <div className="text-center">
              <p className="text-3xl md:text-4xl font-bold text-white">
                {s.value}
              </p>
              <p className="text-teal-100 text-sm mt-1">{s.label}</p>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

/* ─── Testimonials ─── */
function Testimonials() {
  const quotes = [
    {
      quote:
        "My daughter used to freeze when her teacher called on her. After three months, she volunteered to lead morning assembly. I couldn't believe it was the same child.",
      name: "Parent — Gaborone",
      icon: Star,
    },
    {
      quote:
        "This isn't tutoring. It's something deeper. My son doesn't just speak better — he thinks better. He listens, he reasons, he challenges ideas respectfully.",
      name: "Parent — Gaborone",
      icon: Star,
    },
    {
      quote:
        "We partnered with Find Your Voice for our Grade 7 class. Within a term, students were presenting research with structure and confidence we hadn't seen before.",
      name: "School Administrator",
      icon: GraduationCap,
    },
  ]

  return (
    <Section className="bg-slate-50">
      <SectionHeader
        label="What people say"
        title="The results speak for themselves."
      />
      <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        {quotes.map((q, i) => (
          <FadeIn key={i} delay={i * 0.12}>
            <div className="bg-white p-8 rounded-2xl border border-slate-200 h-full flex flex-col">
              <div className="flex gap-1 mb-4">
                {[...Array(5)].map((_, j) => (
                  <Star
                    key={j}
                    size={16}
                    className="fill-amber-400 text-amber-400"
                  />
                ))}
              </div>
              <p className="text-slate-600 leading-relaxed italic flex-1">
                "{q.quote}"
              </p>
              <div className="mt-6 flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-teal-100 flex items-center justify-center">
                  <q.icon size={18} className="text-teal-600" />
                </div>
                <span className="text-sm font-medium text-slate-700">
                  {q.name}
                </span>
              </div>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

/* ─── Final CTA ─── */
function FinalCTA() {
  return (
    <Section className="bg-gradient-to-br from-slate-900 via-teal-950 to-slate-900">
      <div className="text-center max-w-3xl mx-auto">
        <FadeIn>
          <h2 className="text-3xl md:text-5xl font-bold text-white tracking-tight">
            The best time to start was years ago.
            <br />
            <span className="text-teal-400">The next best time is now.</span>
          </h2>
          <p className="mt-6 text-lg text-slate-300 max-w-2xl mx-auto">
            Every term your child waits is another term they practice being
            quiet. Give them the tools to speak, think, and lead — starting
            this quarter.
          </p>
          <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/contact">
              <motion.button
                className="bg-teal-500 hover:bg-teal-400 text-slate-900 font-bold px-8 py-4 rounded-xl text-lg flex items-center gap-2 transition-colors w-full sm:w-auto justify-center"
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
              >
                Enroll Your Child Today
                <ArrowRight size={20} />
              </motion.button>
            </Link>
            <Link to="/contact">
              <motion.button
                className="border border-slate-500 hover:border-teal-400 text-white font-semibold px-8 py-4 rounded-xl text-lg transition-colors w-full sm:w-auto justify-center"
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
              >
                Talk to Us on WhatsApp
              </motion.button>
            </Link>
          </div>
        </FadeIn>
      </div>
    </Section>
  )
}

/* ─── Page ─── */
export default function Home() {
  return (
    <>
      <Hero />
      <Problem />
      <Solution />
      <ProgramOverview />
      <Benefits />
      <HowItWorksPreview />
      <Founder />
      <SocialProof />
      <Testimonials />
      <FinalCTA />
    </>
  )
}
