import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import { ArrowRight, Star } from "lucide-react"

function Hero() {
  return (
    <section className="relative min-h-screen flex items-center bg-[#fffbf5] overflow-hidden">
      <div className="absolute top-20 right-[8%] w-16 h-16 rounded-full bg-[#fde68a]" />
      <div className="absolute top-36 right-[22%] w-8 h-8 rounded-full bg-[#c4b5fd]" />
      <div className="absolute top-[55%] right-[6%] w-12 h-12 rounded-xl bg-[#a7f3d0] -rotate-12" />
      <div className="absolute bottom-32 right-[18%] w-10 h-10 rounded-full bg-[#fca5a5]" />
      <div className="absolute bottom-24 left-[4%] w-14 h-14 rounded-full bg-[#93c5fd] rotate-6" />
      <div className="absolute top-32 left-[14%] w-6 h-6 rounded-full bg-[#fdba74]" />
      <div className="absolute top-44 left-[7%] text-5xl text-[#fbbf24]/30 font-black rotate-12 select-none">+</div>
      <div className="absolute bottom-44 right-[12%] text-4xl text-[#a78bfa]/30 font-black -rotate-12 select-none">+</div>
      <div className="absolute top-28 right-[38%] text-3xl text-[#34d399]/30 font-black rotate-45 select-none">✦</div>
      <div className="absolute bottom-36 left-[20%] text-2xl text-[#fb923c]/30 font-black select-none">✦</div>

      <div className="max-w-7xl mx-auto px-6 pt-28 pb-20 relative z-10">
        <div className="max-w-4xl">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
            <span className="inline-block bg-[#fde68a] text-gray-800 font-black text-sm px-4 py-2 rounded-full -rotate-2 shadow-sm">
              🎤 Now enrolling in Gaborone!
            </span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.1 }}
            className="text-5xl md:text-7xl lg:text-[5.5rem] font-black text-gray-900 leading-[1.05] mt-8"
            style={{ fontFamily: "Nunito, sans-serif" }}
          >
            Every child has a voice.{" "}
            <span className="marker-yellow">We help them find it!</span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.25 }}
            className="mt-8 text-xl text-gray-500 leading-relaxed max-w-2xl"
          >
            Botswana's youth communication academy. We train children ages 6–18
            to speak with clarity, think critically, and lead with confidence —
            through fun, structured programs that actually work.
          </motion.p>

          <motion.div
            initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.4 }}
            className="mt-8 flex flex-wrap gap-3"
          >
            {[
              { label: "👧 Ages 6–18", bg: "bg-[#dbeafe]", text: "text-[#1e40af]", tilt: "rotate-1" },
              { label: "👥 Small Groups", bg: "bg-[#dcfce7]", text: "text-[#166534]", tilt: "-rotate-1" },
              { label: "💻 In-Person & Online", bg: "bg-[#fef3c7]", text: "text-[#92400e]", tilt: "rotate-2" },
              { label: "📅 6-Month Programs", bg: "bg-[#ede9fe]", text: "text-[#5b21b6]", tilt: "-rotate-2" },
            ].map((badge) => (
              <span key={badge.label} className={`inline-block ${badge.bg} ${badge.text} font-bold text-sm px-4 py-2 rounded-full ${badge.tilt} shadow-sm`}>
                {badge.label}
              </span>
            ))}
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.5 }}
            className="mt-10 flex flex-col sm:flex-row gap-4"
          >
            <Link to="/contact">
              <motion.button
                className="bg-[#f97316] hover:bg-[#ea580c] text-white font-black px-8 py-4 rounded-full text-lg flex items-center gap-2 shadow-lg shadow-orange-200 transition-colors w-full sm:w-auto justify-center"
                style={{ fontFamily: "Nunito, sans-serif" }}
                whileHover={{ scale: 1.05, rotate: 1 }}
                whileTap={{ scale: 0.95 }}
              >
                Enroll Your Child <ArrowRight size={20} />
              </motion.button>
            </Link>
            <Link to="/programs">
              <motion.button
                className="bg-white hover:bg-gray-50 text-gray-800 font-bold px-8 py-4 rounded-full text-lg border-2 border-gray-200 transition-colors w-full sm:w-auto justify-center"
                style={{ fontFamily: "Nunito, sans-serif" }}
                whileHover={{ scale: 1.05, rotate: -1 }}
                whileTap={{ scale: 0.95 }}
              >
                Explore Programs
              </motion.button>
            </Link>
          </motion.div>
        </div>
      </div>
    </section>
  )
}

function Problem() {
  return (
    <section className="py-20 px-6 bg-[#fef9e7]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#d97706] uppercase tracking-widest mb-4">Sound familiar?</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 leading-tight mb-12" style={{ fontFamily: "Nunito, sans-serif" }}>
            You've noticed it. <span className="marker-yellow">So have they.</span>
          </h2>
        </FadeIn>

        <div className="space-y-4">
          {[
            { emoji: "🤫", text: "Your child struggles to speak up in class or around adults", color: "border-l-[#f97316]" },
            { emoji: "😔", text: "They avoid eye contact and mumble through conversations", color: "border-l-[#a78bfa]" },
            { emoji: "💭", text: "They have great ideas but can't express them clearly", color: "border-l-[#0ea5e9]" },
            { emoji: "😰", text: "They freeze during presentations or group activities", color: "border-l-[#f43f5e]" },
          ].map((p, i) => (
            <FadeIn key={p.text} delay={i * 0.1}>
              <div className={`flex items-center gap-4 bg-white p-5 rounded-2xl border-l-4 ${p.color} shadow-sm`}>
                <span className="text-3xl">{p.emoji}</span>
                <p className="text-gray-700 text-lg font-medium">{p.text}</p>
              </div>
            </FadeIn>
          ))}
        </div>

        <FadeIn delay={0.4}>
          <p className="mt-10 text-center text-gray-500 text-lg">
            It's not a character flaw. It's a <span className="font-black text-gray-800">skill gap</span>. And skills can be taught. 💪
          </p>
        </FadeIn>
      </div>
    </section>
  )
}

function Solution() {
  const pillars = [
    { emoji: "🎤", title: "Communication", desc: "Articulate ideas with structure, clarity, and conviction — in any setting.", bg: "bg-[#dbeafe]", tilt: "rotate-1" },
    { emoji: "🧠", title: "Critical Thinking", desc: "Analyze, question, and form opinions independently — not just repeat what they're told.", bg: "bg-[#ede9fe]", tilt: "-rotate-1" },
    { emoji: "⭐", title: "Confidence", desc: "Stand in front of any room and own the moment — without fear or hesitation.", bg: "bg-[#fef3c7]", tilt: "rotate-2" },
    { emoji: "🚀", title: "Leadership", desc: "Influence, collaborate, and inspire — skills that compound for a lifetime.", bg: "bg-[#dcfce7]", tilt: "-rotate-2" },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#0ea5e9] uppercase tracking-widest mb-4 text-center">What we build</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>
            Way more than <span className="marker-blue">public speaking</span>.
          </h2>
          <p className="text-gray-500 text-center text-lg max-w-2xl mx-auto mb-14">
            Four superpowers. One program. A lifetime of impact.
          </p>
        </FadeIn>

        <div className="grid md:grid-cols-2 gap-6">
          {pillars.map((p, i) => (
            <FadeIn key={p.title} delay={i * 0.1}>
              <motion.div
                className={`${p.bg} p-8 rounded-3xl ${p.tilt} border-[3px] border-dashed border-gray-200/60`}
                whileHover={{ rotate: 0, scale: 1.02 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                <span className="text-5xl block mb-4">{p.emoji}</span>
                <h3 className="text-2xl font-black text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{p.title}</h3>
                <p className="text-gray-600 leading-relaxed">{p.desc}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function ProgramOverview() {
  const programs = [
    { emoji: "🌱", age: "Ages 6–10", name: "Young Speakers", desc: "Foundational skills through storytelling, show-and-tell, and structured play. Children learn to organize thoughts and speak in front of small groups.", bg: "bg-[#dcfce7]", border: "border-[#86efac]" },
    { emoji: "🔥", age: "Ages 11–14", name: "Rising Voices", desc: "Intermediate training in debate, persuasive speaking, and group discussion. Students develop critical thinking and defend ideas under pressure.", bg: "bg-[#fef3c7]", border: "border-[#fde68a]" },
    { emoji: "👑", age: "Ages 15–18", name: "Future Leaders", desc: "Advanced leadership communication — presentations, panel discussions, interview prep, and real-world speaking opportunities.", bg: "bg-[#ede9fe]", border: "border-[#c4b5fd]" },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#059669] uppercase tracking-widest mb-4 text-center">Programs</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Three tracks. Every age <span className="marker-green">covered</span>.
          </h2>
        </FadeIn>

        <div className="space-y-6">
          {programs.map((p, i) => (
            <FadeIn key={p.name} delay={i * 0.15}>
              <motion.div
                className={`${p.bg} border-2 ${p.border} rounded-3xl p-8 md:p-10 flex flex-col md:flex-row items-start gap-6`}
                whileHover={{ scale: 1.01, x: 4 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                <span className="text-6xl shrink-0">{p.emoji}</span>
                <div>
                  <span className="text-xs font-black uppercase tracking-widest text-gray-500">{p.age}</span>
                  <h3 className="text-2xl font-black text-gray-900 mt-1 mb-3" style={{ fontFamily: "Nunito, sans-serif" }}>{p.name}</h3>
                  <p className="text-gray-600 leading-relaxed">{p.desc}</p>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>

        <FadeIn delay={0.5}>
          <div className="text-center mt-10">
            <Link to="/programs" className="text-[#059669] font-black hover:underline text-lg" style={{ fontFamily: "Nunito, sans-serif" }}>
              See full program details →
            </Link>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

function Benefits() {
  const benefits = [
    { emoji: "✋", text: "Your child raises their hand in class — without being asked" },
    { emoji: "👋", text: "They introduce themselves to adults with eye contact and a firm voice" },
    { emoji: "🏆", text: "They win debates — not because they're loud, because they're clear" },
    { emoji: "🌟", text: "They lead group projects instead of hiding behind them" },
    { emoji: "🤝", text: "They handle disagreements with words, not silence" },
    { emoji: "💼", text: "They walk into interviews and new schools with presence" },
  ]

  return (
    <section className="py-20 px-6 bg-[#f0fdf4]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#059669] uppercase tracking-widest mb-4 text-center">The outcome</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>
            What parents <span className="marker-green">actually notice</span>.
          </h2>
          <p className="text-gray-500 text-center text-lg max-w-2xl mx-auto mb-14">
            This isn't about raising a child who gives speeches. It's about raising a child who doesn't shrink.
          </p>
        </FadeIn>

        <div className="space-y-3">
          {benefits.map((b, i) => (
            <FadeIn key={b.text} delay={i * 0.08}>
              <div className="flex items-center gap-4 bg-white p-5 rounded-2xl border-2 border-dashed border-[#bbf7d0] shadow-sm">
                <span className="text-2xl">{b.emoji}</span>
                <p className="text-gray-700 leading-relaxed font-medium">{b.text}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function HowItWorksPreview() {
  const steps = [
    { emoji: "📋", title: "Choose a Program", desc: "Select the right age group and format — group, one-on-one, or online.", color: "bg-[#dbeafe]" },
    { emoji: "👥", title: "Join a Cohort", desc: "Your child joins a small group of peers and begins the 6-month journey.", color: "bg-[#dcfce7]" },
    { emoji: "🎯", title: "Learn by Doing", desc: "Weekly sessions with speeches, debates, and feedback — not lectures.", color: "bg-[#fef3c7]" },
    { emoji: "🦋", title: "Watch Them Transform", desc: "Within weeks you'll notice the difference. By month 6, a new communicator.", color: "bg-[#ede9fe]" },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#7c3aed] uppercase tracking-widest mb-4 text-center">The process</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            How it <span className="marker-purple">works</span>.
          </h2>
        </FadeIn>

        <div className="space-y-6">
          {steps.map((s, i) => (
            <FadeIn key={s.title} delay={i * 0.12}>
              <div className={`flex items-start gap-5 ${i % 2 === 1 ? "md:flex-row-reverse md:text-right" : ""}`}>
                <motion.div
                  className={`w-16 h-16 ${s.color} rounded-2xl flex items-center justify-center shrink-0 text-3xl border-2 border-dashed border-gray-200/60`}
                  whileHover={{ rotate: [0, -8, 8, 0], scale: 1.1 }}
                  transition={{ duration: 0.4 }}
                >
                  {s.emoji}
                </motion.div>
                <div className="pt-1">
                  <span className="text-xs font-black text-gray-400 uppercase tracking-widest">Step {i + 1}</span>
                  <h3 className="text-xl font-black text-gray-900 mt-0.5 mb-1" style={{ fontFamily: "Nunito, sans-serif" }}>{s.title}</h3>
                  <p className="text-gray-500 leading-relaxed">{s.desc}</p>
                </div>
              </div>
              {i < steps.length - 1 && (
                <div className={`border-l-2 border-dashed border-gray-200 h-6 ${i % 2 === 1 ? "md:ml-auto md:mr-8" : "ml-8"}`} />
              )}
            </FadeIn>
          ))}
        </div>

        <FadeIn delay={0.5}>
          <div className="text-center mt-10">
            <Link to="/how-it-works" className="text-[#7c3aed] font-black hover:underline text-lg" style={{ fontFamily: "Nunito, sans-serif" }}>
              Learn more about our method →
            </Link>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

function Founder() {
  return (
    <section className="py-20 px-6 bg-[#fff7ed]">
      <div className="max-w-4xl mx-auto grid md:grid-cols-5 gap-12 items-center">
        <FadeIn className="md:col-span-2">
          <div className="aspect-[4/5] rounded-3xl bg-[#fef3c7] border-[3px] border-dashed border-[#fbbf24]/40 flex items-center justify-center -rotate-2">
            <div className="text-center rotate-2">
              <div className="w-28 h-28 rounded-full bg-[#f97316] flex items-center justify-center mx-auto mb-4 shadow-lg shadow-orange-200">
                <span className="text-white text-4xl font-black" style={{ fontFamily: "Nunito, sans-serif" }}>MK</span>
              </div>
              <p className="text-gray-800 font-black text-lg" style={{ fontFamily: "Nunito, sans-serif" }}>Mpho Kabelo</p>
              <p className="text-[#f97316] text-sm font-bold">Founder & Lead Facilitator</p>
            </div>
          </div>
        </FadeIn>
        <FadeIn className="md:col-span-3" delay={0.15}>
          <span className="inline-block bg-[#fde68a] text-gray-800 font-black text-xs tracking-widest uppercase px-4 py-2 rounded-full -rotate-1 mb-6">
            Meet the founder
          </span>
          <h2 className="text-3xl md:text-4xl font-black text-gray-900 mb-6 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}>
            "I started this because I watched too many <span className="marker-coral">brilliant kids go quiet</span>."
          </h2>
          <p className="text-gray-500 leading-relaxed mb-4">
            Mpho Kabelo founded Find Your Voice after years of watching talented young people in Botswana hold back — not because they lacked ideas, but because no one taught them how to express those ideas with power.
          </p>
          <p className="text-gray-500 leading-relaxed mb-4">
            Find Your Voice was built to fix that. Not with one-off workshops that kids forget by Monday, but with a structured training system that builds lasting communication skills over time.
          </p>
          <p className="text-gray-500 leading-relaxed">
            The academy is based in Gaborone and growing across Botswana — with plans for online delivery and school partnerships nationwide. 🇧🇼
          </p>
        </FadeIn>
      </div>
    </section>
  )
}

function Testimonials() {
  const quotes = [
    { quote: "My daughter used to freeze when her teacher called on her. After three months, she volunteered to lead morning assembly. I couldn't believe it.", name: "Parent — Gaborone", emoji: "💝" },
    { quote: "This isn't tutoring. It's something deeper. My son doesn't just speak better — he thinks better. He listens, he reasons, he challenges ideas respectfully.", name: "Parent — Gaborone", emoji: "🧠" },
    { quote: "We partnered with Find Your Voice for our Grade 7 class. Within a term, students were presenting with structure and confidence we hadn't seen before.", name: "School Administrator", emoji: "🏫" },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#d97706] uppercase tracking-widest mb-4 text-center">What people say</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Don't take our word for it 🗣️
          </h2>
        </FadeIn>

        <div className="space-y-10">
          {quotes.map((q, i) => (
            <FadeIn key={i} delay={i * 0.15}>
              <div className={`${i % 2 === 0 ? "md:mr-16" : "md:ml-16"}`}>
                <div className="relative bg-white p-7 rounded-2xl shadow-sm border-[3px] border-dashed border-gray-200/60">
                  <div className="flex gap-1 mb-3">
                    {[...Array(5)].map((_, j) => (
                      <Star key={j} size={14} className="fill-[#fbbf24] text-[#fbbf24]" />
                    ))}
                  </div>
                  <p className="text-gray-600 text-lg leading-relaxed italic">"{q.quote}"</p>
                  <div className="absolute -bottom-3 left-10 w-6 h-6 bg-white border-r-[3px] border-b-[3px] border-dashed border-gray-200/60 rotate-45" />
                </div>
                <div className="mt-5 ml-6 flex items-center gap-3">
                  <span className="text-2xl">{q.emoji}</span>
                  <span className="font-bold text-gray-700">{q.name}</span>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function FinalCTA() {
  return (
    <section className="py-20 px-6 bg-[#fef3c7] relative overflow-hidden">
      <div className="absolute top-10 right-[10%] w-14 h-14 rounded-full bg-[#fb923c]/20" />
      <div className="absolute bottom-12 left-[8%] w-18 h-18 rounded-xl bg-[#a78bfa]/15 -rotate-12" />
      <div className="absolute top-20 left-[22%] w-8 h-8 rounded-full bg-[#34d399]/20" />
      <div className="absolute bottom-20 right-[25%] text-3xl text-[#fbbf24]/30 font-black rotate-12 select-none">✦</div>

      <div className="text-center max-w-3xl mx-auto relative z-10">
        <FadeIn>
          <span className="text-5xl block mb-6">🚀</span>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}>
            The best time to start was years ago. <span className="marker-yellow">The next best time is now!</span>
          </h2>
          <p className="mt-6 text-lg text-gray-600 max-w-2xl mx-auto">
            Every term your child waits is another term they practice being quiet. Give them the tools to speak, think, and lead — starting this quarter.
          </p>
          <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/contact">
              <motion.button
                className="bg-[#f97316] hover:bg-[#ea580c] text-white font-black px-8 py-4 rounded-full text-lg flex items-center gap-2 shadow-lg shadow-orange-200 transition-colors w-full sm:w-auto justify-center"
                style={{ fontFamily: "Nunito, sans-serif" }}
                whileHover={{ scale: 1.05, rotate: 1 }}
                whileTap={{ scale: 0.95 }}
              >
                Enroll Your Child Today <ArrowRight size={20} />
              </motion.button>
            </Link>
            <a href="https://wa.me/26771234567?text=Hi%2C%20I'm%20interested%20in%20Find%20Your%20Voice%20for%20my%20child." target="_blank" rel="noopener noreferrer">
              <motion.button
                className="bg-white hover:bg-gray-50 text-gray-800 font-bold px-8 py-4 rounded-full text-lg border-2 border-gray-200 transition-colors w-full sm:w-auto justify-center"
                style={{ fontFamily: "Nunito, sans-serif" }}
                whileHover={{ scale: 1.05, rotate: -1 }}
                whileTap={{ scale: 0.95 }}
              >
                💬 Chat on WhatsApp
              </motion.button>
            </a>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

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
      <Testimonials />
      <FinalCTA />
    </>
  )
}
