import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import { ArrowRight, Star } from "lucide-react"

/* ─── Decorative floating shapes ─── */
function FloatingShape({ className, delay = 0 }: { className: string; delay?: number }) {
  return (
    <motion.div
      className={`absolute rounded-full ${className}`}
      animate={{ y: [0, -12, 0], rotate: [0, 5, 0] }}
      transition={{ duration: 4, repeat: Infinity, delay, ease: "easeInOut" }}
    />
  )
}

/* ─── Hero ─── */
function Hero() {
  return (
    <section className="relative min-h-screen flex items-center overflow-hidden bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc]">
      {/* Decorative blobs */}
      <FloatingShape className="w-32 h-32 bg-[#fbbf24]/30 top-24 right-[10%] blur-sm" delay={0} />
      <FloatingShape className="w-24 h-24 bg-white/20 top-[60%] right-[20%] blur-sm" delay={1} />
      <FloatingShape className="w-40 h-40 bg-[#a78bfa]/20 bottom-20 left-[5%] blur-sm" delay={0.5} />
      <FloatingShape className="w-16 h-16 bg-[#fb923c]/30 top-[30%] left-[15%]" delay={1.5} />

      {/* Big speech bubble shapes */}
      <div className="absolute top-20 right-[8%] w-48 h-48 bg-white/10 rounded-[2rem] rotate-6" />
      <div className="absolute bottom-28 left-[3%] w-36 h-36 bg-white/10 rounded-[2rem] -rotate-12" />

      <div className="max-w-7xl mx-auto px-6 pt-28 pb-20 relative z-10">
        <div className="max-w-3xl">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5 }}
            className="inline-flex items-center gap-2 bg-white/20 backdrop-blur-sm rounded-full px-5 py-2 mb-8"
          >
            <span className="text-2xl">🎤</span>
            <span className="text-white font-bold text-sm">
              Now enrolling in Gaborone!
            </span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.1 }}
            className="text-4xl md:text-6xl lg:text-7xl font-black text-white leading-[1.1]"
            style={{ fontFamily: "Nunito, sans-serif" }}
          >
            Every child has a voice.{" "}
            <span className="text-[#fbbf24] drop-shadow-sm">
              We help them use it!
            </span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.25 }}
            className="mt-7 text-lg md:text-xl text-white/90 leading-relaxed max-w-2xl"
          >
            Find Your Voice is Botswana's youth communication academy.
            We train children ages 6–18 to speak with clarity, think
            critically, and lead with confidence — through fun, structured
            programs that build real skills.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="mt-10 flex flex-col sm:flex-row gap-4"
          >
            <Link to="/contact">
              <motion.button
                className="bg-[#fbbf24] hover:bg-[#f59e0b] text-gray-900 font-black px-8 py-4 rounded-full text-lg flex items-center gap-2 shadow-lg shadow-amber-300/40 transition-colors w-full sm:w-auto justify-center"
                style={{ fontFamily: "Nunito, sans-serif" }}
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                Enroll Your Child ✨
                <ArrowRight size={20} />
              </motion.button>
            </Link>
            <Link to="/programs">
              <motion.button
                className="bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white font-bold px-8 py-4 rounded-full text-lg border-2 border-white/40 transition-colors w-full sm:w-auto justify-center"
                style={{ fontFamily: "Nunito, sans-serif" }}
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                Explore Programs
              </motion.button>
            </Link>
          </motion.div>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6, delay: 0.6 }}
            className="mt-12 flex flex-wrap gap-6 text-sm text-white/80 font-semibold"
          >
            {[
              { emoji: "👧", text: "Ages 6–18" },
              { emoji: "👥", text: "Group & 1-on-1" },
              { emoji: "💻", text: "In-Person & Online" },
              { emoji: "📅", text: "6-Month Program" },
            ].map((item) => (
              <span key={item.text} className="flex items-center gap-2 bg-white/10 rounded-full px-4 py-1.5">
                <span>{item.emoji}</span>
                {item.text}
              </span>
            ))}
          </motion.div>
        </div>
      </div>

      {/* Wave bottom */}
      <div className="absolute bottom-0 left-0 right-0">
        <svg viewBox="0 0 1440 100" fill="none" className="w-full">
          <path d="M0,60 C360,100 720,0 1440,60 L1440,100 L0,100 Z" fill="#fffbf5" />
        </svg>
      </div>
    </section>
  )
}

/* ─── Problem ─── */
function Problem() {
  const problems = [
    { emoji: "🤫", text: "Struggles to speak up in class or around adults" },
    { emoji: "😔", text: "Avoids eye contact and mumbles through conversations" },
    { emoji: "💭", text: "Has great ideas but can't express them clearly" },
    { emoji: "😰", text: "Freezes during presentations or group activities" },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader
        label="Sound familiar?"
        title="You've noticed it. So have they."
        subtitle="Most children aren't taught how to communicate with confidence. They're expected to just figure it out. Some do. Most don't."
      />
      <div className="grid md:grid-cols-2 gap-5 max-w-4xl mx-auto">
        {problems.map((p, i) => (
          <FadeIn key={p.text} delay={i * 0.1}>
            <motion.div
              className="flex items-start gap-4 bg-white p-6 rounded-2xl shadow-sm border border-gray-100"
              whileHover={{ y: -3, boxShadow: "0 8px 30px rgba(0,0,0,0.08)" }}
            >
              <span className="text-3xl">{p.emoji}</span>
              <p className="text-gray-700 leading-relaxed font-medium">{p.text}</p>
            </motion.div>
          </FadeIn>
        ))}
      </div>
      <FadeIn delay={0.4}>
        <p className="text-center mt-10 text-gray-400 text-lg max-w-2xl mx-auto font-medium">
          It's not a character flaw. It's a skill gap. And skills can be taught. 💪
        </p>
      </FadeIn>
    </Section>
  )
}

/* ─── Solution / Pillars ─── */
function Solution() {
  const pillars = [
    {
      emoji: "🎤",
      color: "bg-[#e0f2fe]",
      borderColor: "border-[#0ea5e9]/20",
      title: "Communication",
      desc: "Articulate ideas with structure, clarity, and conviction — in any setting.",
    },
    {
      emoji: "🧠",
      color: "bg-[#ede9fe]",
      borderColor: "border-[#a78bfa]/20",
      title: "Critical Thinking",
      desc: "Analyze, question, and form opinions independently — not just repeat what they're told.",
    },
    {
      emoji: "⭐",
      color: "bg-[#fef3c7]",
      borderColor: "border-[#fbbf24]/20",
      title: "Confidence",
      desc: "Stand in front of any room and own the moment — without fear or hesitation.",
    },
    {
      emoji: "🚀",
      color: "bg-[#ffedd5]",
      borderColor: "border-[#fb923c]/20",
      title: "Leadership",
      desc: "Influence, collaborate, and inspire — skills that compound for a lifetime.",
    },
  ]

  return (
    <Section className="bg-white">
      <SectionHeader
        label="What we build"
        title="This is way more than public speaking."
        subtitle="Find Your Voice develops four core superpowers in every child who comes through our program."
      />
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        {pillars.map((p, i) => (
          <FadeIn key={p.title} delay={i * 0.1}>
            <motion.div
              className={`text-center p-7 rounded-3xl ${p.color} border ${p.borderColor}`}
              whileHover={{ y: -6, scale: 1.02 }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <span className="text-5xl block mb-4">{p.emoji}</span>
              <h3 className="font-black text-lg text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>
                {p.title}
              </h3>
              <p className="text-gray-500 text-sm leading-relaxed">{p.desc}</p>
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
      emoji: "🌱",
      age: "Ages 6–10",
      name: "Young Speakers",
      desc: "Foundational skills through storytelling, show-and-tell, and structured play. Children learn to organize thoughts and speak in front of small groups.",
      color: "bg-[#d1fae5]",
      border: "border-[#34d399]",
      text: "text-[#059669]",
    },
    {
      emoji: "🔥",
      age: "Ages 11–14",
      name: "Rising Voices",
      desc: "Intermediate training in debate, persuasive speaking, and group discussion. Students develop critical thinking and defend ideas under pressure.",
      color: "bg-[#fef3c7]",
      border: "border-[#fbbf24]",
      text: "text-[#d97706]",
    },
    {
      emoji: "👑",
      age: "Ages 15–18",
      name: "Future Leaders",
      desc: "Advanced leadership communication — presentations, panel discussions, interview prep, and real-world speaking opportunities.",
      color: "bg-[#ede9fe]",
      border: "border-[#a78bfa]",
      text: "text-[#7c3aed]",
    },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader
        label="Programs"
        title="Three tracks. Every age covered."
        subtitle="Age-specific programs designed to meet children exactly where they are — and take them further than they thought possible."
      />
      <div className="grid md:grid-cols-3 gap-6">
        {programs.map((p, i) => (
          <FadeIn key={p.name} delay={i * 0.12}>
            <motion.div
              className={`rounded-3xl border-2 ${p.border} ${p.color} p-8 h-full`}
              whileHover={{ y: -6, scale: 1.02 }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <span className="text-4xl">{p.emoji}</span>
              <span className={`block text-xs font-black uppercase tracking-widest ${p.text} mt-4`}>
                {p.age}
              </span>
              <h3 className="text-2xl font-black text-gray-900 mt-1 mb-3" style={{ fontFamily: "Nunito, sans-serif" }}>
                {p.name}
              </h3>
              <p className="text-gray-600 leading-relaxed">{p.desc}</p>
            </motion.div>
          </FadeIn>
        ))}
      </div>
      <FadeIn delay={0.4}>
        <div className="text-center mt-10">
          <Link
            to="/programs"
            className="inline-flex items-center gap-2 text-[#0ea5e9] font-black hover:underline transition-colors text-lg"
            style={{ fontFamily: "Nunito, sans-serif" }}
          >
            See full program details →
          </Link>
        </div>
      </FadeIn>
    </Section>
  )
}

/* ─── Benefits ─── */
function Benefits() {
  const benefits = [
    { emoji: "✋", text: "Your child raises their hand in class — without being asked." },
    { emoji: "👋", text: "They introduce themselves to adults with eye contact and a firm voice." },
    { emoji: "🏆", text: "They win debates — not because they're loud, because they're clear." },
    { emoji: "🌟", text: "They lead group projects instead of hiding behind them." },
    { emoji: "🤝", text: "They handle disagreements with words, not silence." },
    { emoji: "💼", text: "They walk into interviews and new schools with presence." },
  ]

  return (
    <Section className="bg-white">
      <SectionHeader
        label="The outcome"
        title="What parents actually notice."
        subtitle="This isn't about raising a child who gives speeches. It's about raising a child who doesn't shrink."
      />
      <div className="max-w-3xl mx-auto grid sm:grid-cols-2 gap-4">
        {benefits.map((b, i) => (
          <FadeIn key={b.text} delay={i * 0.08}>
            <div className="flex items-start gap-3 bg-[#f0fdf4] p-5 rounded-2xl border border-[#bbf7d0]">
              <span className="text-xl">{b.emoji}</span>
              <p className="text-gray-700 leading-relaxed font-medium">{b.text}</p>
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
    { num: "1", emoji: "📋", title: "Choose a Program", desc: "Select the right age group and format — group, one-on-one, or online." },
    { num: "2", emoji: "👥", title: "Join a Cohort", desc: "Your child joins a small group of peers and begins the 6-month journey." },
    { num: "3", emoji: "🎯", title: "Learn by Doing", desc: "Weekly sessions with speeches, debates, feedback — not lectures." },
    { num: "4", emoji: "🦋", title: "Watch Them Transform", desc: "Within weeks you'll notice the difference. By month 6, a new communicator." },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader
        label="The process"
        title="How it works."
        subtitle="A simple path from enrollment to transformation."
      />
      <div className="grid md:grid-cols-4 gap-6 max-w-5xl mx-auto">
        {steps.map((s, i) => (
          <FadeIn key={s.num} delay={i * 0.12}>
            <div className="text-center">
              <motion.div
                className="w-20 h-20 rounded-3xl bg-[#e0f2fe] flex items-center justify-center mx-auto mb-4 text-4xl"
                whileHover={{ rotate: [0, -5, 5, 0], scale: 1.1 }}
                transition={{ duration: 0.5 }}
              >
                {s.emoji}
              </motion.div>
              <h3 className="font-black text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>
                {s.title}
              </h3>
              <p className="text-sm text-gray-500 leading-relaxed">{s.desc}</p>
            </div>
          </FadeIn>
        ))}
      </div>
      <FadeIn delay={0.5}>
        <div className="text-center mt-10">
          <Link
            to="/how-it-works"
            className="inline-flex items-center gap-2 text-[#0ea5e9] font-black hover:underline transition-colors"
            style={{ fontFamily: "Nunito, sans-serif" }}
          >
            Learn more about our method →
          </Link>
        </div>
      </FadeIn>
    </Section>
  )
}

/* ─── Founder ─── */
function Founder() {
  return (
    <Section className="bg-white">
      <div className="max-w-4xl mx-auto grid md:grid-cols-5 gap-12 items-center">
        <FadeIn className="md:col-span-2">
          <div className="aspect-[4/5] rounded-3xl bg-gradient-to-br from-[#e0f2fe] to-[#bae6fd] flex items-center justify-center">
            <div className="text-center">
              <div className="w-28 h-28 rounded-full bg-[#0ea5e9] flex items-center justify-center mx-auto mb-4 shadow-lg shadow-sky-200">
                <span className="text-white text-4xl font-black" style={{ fontFamily: "Nunito, sans-serif" }}>MK</span>
              </div>
              <p className="text-gray-800 font-black text-lg" style={{ fontFamily: "Nunito, sans-serif" }}>Mpho Kabelo</p>
              <p className="text-[#0ea5e9] text-sm font-bold">Founder & Lead Facilitator</p>
            </div>
          </div>
        </FadeIn>
        <FadeIn className="md:col-span-3" delay={0.15}>
          <span className="inline-block bg-[#fef3c7] text-[#d97706] font-black text-xs tracking-widest uppercase px-4 py-1.5 rounded-full mb-4">
            Meet the founder
          </span>
          <h2 className="text-3xl md:text-4xl font-black text-gray-900 mb-6" style={{ fontFamily: "Nunito, sans-serif" }}>
            "I started this because I watched too many brilliant kids go quiet."
          </h2>
          <p className="text-gray-500 leading-relaxed mb-4">
            Mpho Kabelo founded Find Your Voice after years of watching
            talented young people in Botswana hold back — not because they
            lacked ideas, but because no one taught them how to express
            those ideas with power.
          </p>
          <p className="text-gray-500 leading-relaxed mb-4">
            Find Your Voice was built to fix that. Not with one-off workshops
            that kids forget by Monday, but with a structured training
            system that builds lasting communication skills over time.
          </p>
          <p className="text-gray-500 leading-relaxed">
            The academy is based in Gaborone and growing across Botswana —
            with plans for online delivery and school partnerships
            nationwide. 🇧🇼
          </p>
        </FadeIn>
      </div>
    </Section>
  )
}

/* ─── Stats ─── */
function SocialProof() {
  const stats = [
    { emoji: "📅", value: "6-Month", label: "Structured Program" },
    { emoji: "👧", value: "6–18", label: "Age Range" },
    { emoji: "🎯", value: "3", label: "Training Tracks" },
    { emoji: "💯", value: "100%", label: "Learn-by-Doing" },
  ]

  return (
    <Section className="bg-gradient-to-r from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] relative">
      <div className="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-4xl mx-auto">
        {stats.map((s, i) => (
          <FadeIn key={s.label} delay={i * 0.1}>
            <div className="text-center">
              <span className="text-3xl block mb-2">{s.emoji}</span>
              <p className="text-3xl md:text-4xl font-black text-white" style={{ fontFamily: "Nunito, sans-serif" }}>
                {s.value}
              </p>
              <p className="text-sky-100 text-sm font-semibold mt-1">{s.label}</p>
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
      quote: "My daughter used to freeze when her teacher called on her. After three months, she volunteered to lead morning assembly. I couldn't believe it.",
      name: "Parent — Gaborone",
      emoji: "💝",
    },
    {
      quote: "This isn't tutoring. It's something deeper. My son doesn't just speak better — he thinks better. He listens, he reasons, he challenges ideas respectfully.",
      name: "Parent — Gaborone",
      emoji: "🧠",
    },
    {
      quote: "We partnered with Find Your Voice for our Grade 7 class. Within a term, students were presenting with structure and confidence we hadn't seen before.",
      name: "School Administrator",
      emoji: "🏫",
    },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader
        label="What people say"
        title="The results speak for themselves. 🗣️"
      />
      <div className="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
        {quotes.map((q, i) => (
          <FadeIn key={i} delay={i * 0.12}>
            <motion.div
              className="bg-white p-8 rounded-3xl border border-gray-100 shadow-sm h-full flex flex-col"
              whileHover={{ y: -4 }}
            >
              <div className="flex gap-1 mb-4">
                {[...Array(5)].map((_, j) => (
                  <Star key={j} size={16} className="fill-[#fbbf24] text-[#fbbf24]" />
                ))}
              </div>
              <p className="text-gray-600 leading-relaxed italic flex-1">
                "{q.quote}"
              </p>
              <div className="mt-6 flex items-center gap-3">
                <span className="text-2xl">{q.emoji}</span>
                <span className="text-sm font-bold text-gray-700">{q.name}</span>
              </div>
            </motion.div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

/* ─── Final CTA ─── */
function FinalCTA() {
  return (
    <section className="relative overflow-hidden">
      <div className="bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] py-20 md:py-28 px-6">
        {/* Top wave */}
        <div className="absolute top-0 left-0 right-0">
          <svg viewBox="0 0 1440 60" fill="none" className="w-full">
            <path d="M0,0 L1440,0 L1440,30 C1080,60 360,0 0,30 Z" fill="#fffbf5" />
          </svg>
        </div>

        <FloatingShape className="w-24 h-24 bg-white/10 top-20 right-[15%]" />
        <FloatingShape className="w-16 h-16 bg-[#fbbf24]/20 bottom-20 left-[10%]" delay={1} />

        <div className="text-center max-w-3xl mx-auto relative z-10">
          <FadeIn>
            <span className="text-5xl block mb-6">🚀</span>
            <h2 className="text-3xl md:text-5xl font-black text-white leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}>
              The best time to start was years ago.{" "}
              <span className="text-[#fbbf24]">The next best time is now!</span>
            </h2>
            <p className="mt-6 text-lg text-white/90 max-w-2xl mx-auto">
              Every term your child waits is another term they practice being
              quiet. Give them the tools to speak, think, and lead — starting
              this quarter.
            </p>
            <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/contact">
                <motion.button
                  className="bg-[#fbbf24] hover:bg-[#f59e0b] text-gray-900 font-black px-8 py-4 rounded-full text-lg flex items-center gap-2 shadow-lg shadow-amber-400/30 transition-colors w-full sm:w-auto justify-center"
                  style={{ fontFamily: "Nunito, sans-serif" }}
                  whileHover={{ scale: 1.05, y: -2 }}
                  whileTap={{ scale: 0.95 }}
                >
                  Enroll Your Child Today ✨
                  <ArrowRight size={20} />
                </motion.button>
              </Link>
              <Link to="/contact">
                <motion.button
                  className="bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white font-bold px-8 py-4 rounded-full text-lg border-2 border-white/40 transition-colors w-full sm:w-auto justify-center"
                  style={{ fontFamily: "Nunito, sans-serif" }}
                  whileHover={{ scale: 1.05, y: -2 }}
                  whileTap={{ scale: 0.95 }}
                >
                  💬 Chat on WhatsApp
                </motion.button>
              </Link>
            </div>
          </FadeIn>
        </div>
      </div>
    </section>
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
