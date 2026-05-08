import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import {
  ArrowRight, Star, Mic, Brain, Trophy, Rocket,
  Users, BookOpen, Target, Sparkles, ClipboardList,
  Hand, Eye, Award, Handshake, Briefcase, MessageCircle,
  ChevronRight,
} from "lucide-react"

const bounce = { type: "spring" as const, stiffness: 300, damping: 15 }

function ClayIcon({ icon: Icon, bg, border, color, size = "w-14 h-14" }: { icon: React.ElementType; bg: string; border: string; color: string; size?: string }) {
  return (
    <motion.div
      className={`${size} rounded-2xl ${bg} border-2 ${border} flex items-center justify-center clay-sm shrink-0`}
      whileHover={{ scale: 1.1, rotate: [-2, 2, 0] }}
      transition={bounce}
    >
      <Icon className={`w-6 h-6 ${color}`} />
    </motion.div>
  )
}

function Hero() {
  return (
    <section className="relative min-h-screen flex items-center bg-[#fffbf5] overflow-hidden">
      <div className="absolute top-24 right-[8%] w-20 h-20 rounded-3xl bg-[#FDE68A] border-2 border-[#FCD34D] clay rotate-6 opacity-60" />
      <div className="absolute top-[50%] right-[5%] w-14 h-14 rounded-2xl bg-[#BBF7D0] border-2 border-[#86EFAC] clay -rotate-12 opacity-50" />
      <div className="absolute bottom-28 left-[4%] w-16 h-16 rounded-2xl bg-[#BFDBFE] border-2 border-[#93C5FD] clay rotate-6 opacity-50" />
      <div className="absolute top-36 left-[12%] w-10 h-10 rounded-xl bg-[#DDD6FE] border-2 border-[#C4B5FD] clay -rotate-6 opacity-40" />
      <div className="absolute bottom-40 right-[22%] w-12 h-12 rounded-xl bg-[#FBCFE8] border-2 border-[#F9A8D4] clay rotate-12 opacity-40" />

      <div className="max-w-7xl mx-auto px-6 pt-28 pb-20 relative z-10">
        <div className="max-w-4xl">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
            <span className="inline-flex items-center gap-2 bg-[#EEF2FF] border-2 border-[#C7D2FE] rounded-2xl px-4 py-2 clay-sm">
              <Mic className="w-4 h-4 text-[#6366F1]" />
              <span className="text-[#4F46E5] font-semibold text-sm">Now enrolling in Gaborone!</span>
            </span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.1 }}
            className="text-5xl md:text-7xl lg:text-[5.5rem] font-bold text-gray-900 leading-[1.05] mt-8"
          >
            Every child has a voice.{" "}
            <span className="text-[#F97316]">We help them find it.</span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.25 }}
            className="mt-8 text-xl text-gray-500 leading-relaxed max-w-2xl"
          >
            Botswana's youth communication academy. We train children ages 6–18
            to speak with clarity, think critically, and lead with confidence —
            through fun, structured programs that actually work.
          </motion.p>

          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.4 }} className="mt-8 flex flex-wrap gap-3">
            {[
              { icon: Users, label: "Ages 6–18", bg: "bg-[#BFDBFE]", border: "border-[#93C5FD]", color: "text-[#2563EB]" },
              { icon: Users, label: "Small Groups", bg: "bg-[#BBF7D0]", border: "border-[#86EFAC]", color: "text-[#059669]" },
              { icon: BookOpen, label: "In-Person & Online", bg: "bg-[#FDE68A]", border: "border-[#FCD34D]", color: "text-[#92400E]" },
              { icon: Target, label: "6-Month Programs", bg: "bg-[#DDD6FE]", border: "border-[#C4B5FD]", color: "text-[#6D28D9]" },
            ].map((b) => (
              <span key={b.label} className={`inline-flex items-center gap-2 ${b.bg} ${b.color} border-2 ${b.border} font-semibold text-sm px-4 py-2 rounded-2xl clay-sm`}>
                <b.icon className="w-4 h-4" />
                {b.label}
              </span>
            ))}
          </motion.div>

          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.5 }} className="mt-10 flex flex-col sm:flex-row gap-4">
            <Link to="/contact">
              <motion.button
                className="bg-[#F97316] text-white font-bold px-8 py-4 rounded-2xl text-lg flex items-center gap-2 border-2 border-[#EA580C] clay-sm transition-all w-full sm:w-auto justify-center"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                Enroll Your Child <ArrowRight size={20} />
              </motion.button>
            </Link>
            <Link to="/programs">
              <motion.button
                className="bg-white text-gray-700 font-bold px-8 py-4 rounded-2xl text-lg border-2 border-gray-200 clay-sm transition-all w-full sm:w-auto justify-center"
                whileHover={{ scale: 1.05, y: -2 }}
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
  const problems = [
    { icon: Eye, text: "Your child struggles to speak up in class or around adults", bg: "bg-[#FED7AA]", border: "border-[#FDBA74]", color: "text-[#C2410C]" },
    { icon: MessageCircle, text: "They avoid eye contact and mumble through conversations", bg: "bg-[#DDD6FE]", border: "border-[#C4B5FD]", color: "text-[#6D28D9]" },
    { icon: Brain, text: "They have great ideas but can't express them clearly", bg: "bg-[#BFDBFE]", border: "border-[#93C5FD]", color: "text-[#1D4ED8]" },
    { icon: Users, text: "They freeze during presentations or group activities", bg: "bg-[#FBCFE8]", border: "border-[#F9A8D4]", color: "text-[#BE185D]" },
  ]

  return (
    <section className="py-20 px-6 bg-[#FEF3C7]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-semibold text-[#D97706] uppercase tracking-widest mb-4">Sound familiar?</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 leading-tight mb-12">
            You've noticed it. <span className="marker-yellow">So have they.</span>
          </h2>
        </FadeIn>
        <div className="space-y-4">
          {problems.map((p, i) => (
            <FadeIn key={p.text} delay={i * 0.1}>
              <motion.div
                className="flex items-center gap-4 bg-white/80 p-5 rounded-2xl border-2 border-[#FDE68A] clay-sm"
                whileHover={{ x: 4 }}
                transition={bounce}
              >
                <ClayIcon icon={p.icon} bg={p.bg} border={p.border} color={p.color} size="w-12 h-12" />
                <p className="text-gray-700 text-lg font-medium">{p.text}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
        <FadeIn delay={0.4}>
          <p className="mt-10 text-center text-gray-500 text-lg">
            It's not a character flaw. It's a <span className="font-bold text-gray-800">skill gap</span>. And skills can be taught.
          </p>
        </FadeIn>
      </div>
    </section>
  )
}

function Solution() {
  const pillars = [
    { icon: Mic, title: "Communication", desc: "Articulate ideas with structure, clarity, and conviction — in any setting.", bg: "bg-[#BFDBFE]", border: "border-[#93C5FD]", color: "text-[#1D4ED8]" },
    { icon: Brain, title: "Critical Thinking", desc: "Analyze, question, and form opinions independently — not just repeat what they're told.", bg: "bg-[#DDD6FE]", border: "border-[#C4B5FD]", color: "text-[#6D28D9]" },
    { icon: Trophy, title: "Confidence", desc: "Stand in front of any room and own the moment — without fear or hesitation.", bg: "bg-[#FDE68A]", border: "border-[#FCD34D]", color: "text-[#92400E]" },
    { icon: Rocket, title: "Leadership", desc: "Influence, collaborate, and inspire — skills that compound for a lifetime.", bg: "bg-[#BBF7D0]", border: "border-[#86EFAC]", color: "text-[#047857]" },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-semibold text-[#4F46E5] uppercase tracking-widest mb-4 text-center">What we build</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 text-center mb-4">
            Way more than <span className="marker-blue">public speaking</span>.
          </h2>
          <p className="text-gray-500 text-center text-lg max-w-2xl mx-auto mb-14">Four superpowers. One program. A lifetime of impact.</p>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6">
          {pillars.map((p, i) => (
            <FadeIn key={p.title} delay={i * 0.1}>
              <motion.div
                className={`${p.bg} p-8 rounded-3xl border-3 ${p.border} clay`}
                whileHover={{ y: -4, scale: 1.02 }}
                transition={bounce}
              >
                <ClayIcon icon={p.icon} bg="bg-white/60" border="border-white/40" color={p.color} />
                <h3 className="text-2xl font-bold text-gray-900 mt-4 mb-2">{p.title}</h3>
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
    { icon: BookOpen, age: "Ages 6–10", name: "Young Speakers", desc: "Foundational skills through storytelling, show-and-tell, and structured play.", bg: "bg-[#BBF7D0]", border: "border-[#86EFAC]", color: "text-[#047857]", accent: "text-[#059669]" },
    { icon: Target, age: "Ages 11–14", name: "Rising Voices", desc: "Intermediate training in debate, persuasive speaking, and group discussion.", bg: "bg-[#FDE68A]", border: "border-[#FCD34D]", color: "text-[#92400E]", accent: "text-[#D97706]" },
    { icon: Award, age: "Ages 15–18", name: "Future Leaders", desc: "Advanced leadership communication — presentations, panels, and real-world speaking.", bg: "bg-[#DDD6FE]", border: "border-[#C4B5FD]", color: "text-[#6D28D9]", accent: "text-[#7C3AED]" },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-semibold text-[#059669] uppercase tracking-widest mb-4 text-center">Programs</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 text-center mb-14">
            Three tracks. Every age <span className="marker-green">covered</span>.
          </h2>
        </FadeIn>
        <div className="space-y-6">
          {programs.map((p, i) => (
            <FadeIn key={p.name} delay={i * 0.15}>
              <motion.div
                className={`${p.bg} border-3 ${p.border} rounded-3xl p-8 md:p-10 flex flex-col md:flex-row items-start gap-6 clay`}
                whileHover={{ x: 6 }}
                transition={bounce}
              >
                <ClayIcon icon={p.icon} bg="bg-white/60" border="border-white/40" color={p.color} />
                <div>
                  <span className={`text-xs font-bold uppercase tracking-widest ${p.accent}`}>{p.age}</span>
                  <h3 className="text-2xl font-bold text-gray-900 mt-1 mb-2">{p.name}</h3>
                  <p className="text-gray-600 leading-relaxed">{p.desc}</p>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>
        <FadeIn delay={0.5}>
          <div className="text-center mt-10">
            <Link to="/programs" className="inline-flex items-center gap-2 text-[#4F46E5] font-bold hover:underline text-lg">
              See full program details <ChevronRight size={18} />
            </Link>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

function Benefits() {
  const benefits = [
    { icon: Hand, text: "Your child raises their hand in class — without being asked" },
    { icon: Eye, text: "They introduce themselves to adults with eye contact and a firm voice" },
    { icon: Trophy, text: "They win debates — not because they're loud, because they're clear" },
    { icon: Star, text: "They lead group projects instead of hiding behind them" },
    { icon: Handshake, text: "They handle disagreements with words, not silence" },
    { icon: Briefcase, text: "They walk into interviews and new schools with presence" },
  ]

  return (
    <section className="py-20 px-6 bg-[#DCFCE7]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-semibold text-[#059669] uppercase tracking-widest mb-4 text-center">The outcome</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 text-center mb-4">
            What parents <span className="marker-green">actually notice</span>.
          </h2>
          <p className="text-gray-500 text-center text-lg max-w-2xl mx-auto mb-14">
            This isn't about raising a child who gives speeches. It's about raising a child who doesn't shrink.
          </p>
        </FadeIn>
        <div className="space-y-3">
          {benefits.map((b, i) => (
            <FadeIn key={b.text} delay={i * 0.08}>
              <motion.div
                className="flex items-center gap-4 bg-white/70 p-5 rounded-2xl border-2 border-[#86EFAC] clay-sm"
                whileHover={{ x: 4 }}
                transition={bounce}
              >
                <ClayIcon icon={b.icon} bg="bg-[#BBF7D0]" border="border-[#86EFAC]" color="text-[#047857]" size="w-10 h-10" />
                <p className="text-gray-700 leading-relaxed font-medium">{b.text}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function HowItWorksPreview() {
  const steps = [
    { icon: ClipboardList, title: "Choose a Program", desc: "Select the right age group and format — group, one-on-one, or online.", bg: "bg-[#BFDBFE]", border: "border-[#93C5FD]", color: "text-[#1D4ED8]" },
    { icon: Users, title: "Join a Cohort", desc: "Your child joins a small group of peers and begins the 6-month journey.", bg: "bg-[#BBF7D0]", border: "border-[#86EFAC]", color: "text-[#047857]" },
    { icon: Target, title: "Learn by Doing", desc: "Weekly sessions with speeches, debates, and feedback — not lectures.", bg: "bg-[#FDE68A]", border: "border-[#FCD34D]", color: "text-[#92400E]" },
    { icon: Sparkles, title: "Watch Them Transform", desc: "Within weeks you'll notice the difference. By month 6, a new communicator.", bg: "bg-[#DDD6FE]", border: "border-[#C4B5FD]", color: "text-[#6D28D9]" },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-semibold text-[#7C3AED] uppercase tracking-widest mb-4 text-center">The process</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 text-center mb-14">
            How it <span className="marker-purple">works</span>.
          </h2>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6">
          {steps.map((s, i) => (
            <FadeIn key={s.title} delay={i * 0.12}>
              <motion.div
                className={`${s.bg} p-7 rounded-3xl border-3 ${s.border} clay text-center`}
                whileHover={{ y: -4, scale: 1.02 }}
                transition={bounce}
              >
                <div className="flex justify-center mb-4">
                  <ClayIcon icon={s.icon} bg="bg-white/60" border="border-white/40" color={s.color} size="w-16 h-16" />
                </div>
                <span className="text-xs font-bold text-gray-400 uppercase tracking-widest">Step {i + 1}</span>
                <h3 className="text-xl font-bold text-gray-900 mt-1 mb-2">{s.title}</h3>
                <p className="text-gray-600 leading-relaxed text-sm">{s.desc}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
        <FadeIn delay={0.5}>
          <div className="text-center mt-10">
            <Link to="/how-it-works" className="inline-flex items-center gap-2 text-[#7C3AED] font-bold hover:underline text-lg">
              Learn more about our method <ChevronRight size={18} />
            </Link>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

function Founder() {
  return (
    <section className="py-20 px-6 bg-[#FEF3C7]">
      <div className="max-w-4xl mx-auto grid md:grid-cols-5 gap-12 items-center">
        <FadeIn className="md:col-span-2">
          <div className="aspect-[4/5] rounded-3xl bg-[#FDE68A] border-3 border-[#FCD34D] clay flex items-center justify-center">
            <div className="text-center">
              <div className="w-28 h-28 rounded-full bg-[#F97316] border-3 border-[#EA580C] flex items-center justify-center mx-auto mb-4 clay">
                <span className="text-white text-4xl font-bold">MK</span>
              </div>
              <p className="text-gray-800 font-bold text-lg">Mpho Kabelo</p>
              <p className="text-[#D97706] text-sm font-semibold">Founder & Lead Facilitator</p>
            </div>
          </div>
        </FadeIn>
        <FadeIn className="md:col-span-3" delay={0.15}>
          <span className="inline-flex items-center gap-2 bg-white/60 border-2 border-[#FDE68A] rounded-2xl px-4 py-2 clay-sm mb-6">
            <Star className="w-4 h-4 text-[#D97706]" />
            <span className="text-[#92400E] font-semibold text-sm">Meet the founder</span>
          </span>
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6 leading-tight">
            "I started this because I watched too many <span className="marker-coral">brilliant kids go quiet</span>."
          </h2>
          <p className="text-gray-500 leading-relaxed mb-4">
            Mpho Kabelo founded Find Your Voice after years of watching talented young people in Botswana hold back — not because they lacked ideas, but because no one taught them how to express those ideas with power.
          </p>
          <p className="text-gray-500 leading-relaxed">
            The academy is based in Gaborone and growing across Botswana — with plans for online delivery and school partnerships nationwide.
          </p>
        </FadeIn>
      </div>
    </section>
  )
}

function Testimonials() {
  const quotes = [
    { quote: "My daughter used to freeze when her teacher called on her. After three months, she volunteered to lead morning assembly.", name: "Parent — Gaborone", bg: "bg-[#BFDBFE]", border: "border-[#93C5FD]" },
    { quote: "This isn't tutoring. It's something deeper. My son doesn't just speak better — he thinks better.", name: "Parent — Gaborone", bg: "bg-[#BBF7D0]", border: "border-[#86EFAC]" },
    { quote: "We partnered with Find Your Voice for our Grade 7 class. Within a term, students were presenting with confidence we hadn't seen before.", name: "School Administrator", bg: "bg-[#DDD6FE]", border: "border-[#C4B5FD]" },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-semibold text-[#D97706] uppercase tracking-widest mb-4 text-center">What people say</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 text-center mb-14">
            The results speak for themselves.
          </h2>
        </FadeIn>
        <div className="grid md:grid-cols-3 gap-6">
          {quotes.map((q, i) => (
            <FadeIn key={i} delay={i * 0.12}>
              <motion.div
                className={`${q.bg} p-7 rounded-3xl border-3 ${q.border} clay h-full flex flex-col`}
                whileHover={{ y: -4 }}
                transition={bounce}
              >
                <div className="flex gap-1 mb-4">
                  {[...Array(5)].map((_, j) => (
                    <Star key={j} size={16} className="fill-[#F97316] text-[#F97316]" />
                  ))}
                </div>
                <p className="text-gray-700 leading-relaxed italic flex-1">"{q.quote}"</p>
                <p className="mt-4 text-sm font-bold text-gray-600">{q.name}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function FinalCTA() {
  return (
    <section className="py-20 px-6 bg-[#EEF2FF] relative overflow-hidden">
      <div className="absolute top-8 right-[10%] w-16 h-16 rounded-2xl bg-[#BFDBFE] border-2 border-[#93C5FD] clay rotate-12 opacity-40" />
      <div className="absolute bottom-12 left-[8%] w-12 h-12 rounded-2xl bg-[#FDE68A] border-2 border-[#FCD34D] clay -rotate-6 opacity-40" />
      <div className="text-center max-w-3xl mx-auto relative z-10">
        <FadeIn>
          <div className="flex justify-center mb-6">
            <ClayIcon icon={Rocket} bg="bg-[#DDD6FE]" border="border-[#C4B5FD]" color="text-[#6D28D9]" size="w-16 h-16" />
          </div>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 leading-tight">
            The best time to start was years ago. <span className="text-[#F97316]">The next best time is now.</span>
          </h2>
          <p className="mt-6 text-lg text-gray-500 max-w-2xl mx-auto">
            Every term your child waits is another term they practice being quiet. Give them the tools to speak, think, and lead.
          </p>
          <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/contact">
              <motion.button
                className="bg-[#F97316] text-white font-bold px-8 py-4 rounded-2xl text-lg flex items-center gap-2 border-2 border-[#EA580C] clay-sm transition-all w-full sm:w-auto justify-center"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                Enroll Your Child Today <ArrowRight size={20} />
              </motion.button>
            </Link>
            <a href="https://wa.me/26771234567?text=Hi%2C%20I'm%20interested%20in%20Find%20Your%20Voice%20for%20my%20child." target="_blank" rel="noopener noreferrer">
              <motion.button
                className="bg-white text-gray-700 font-bold px-8 py-4 rounded-2xl text-lg border-2 border-gray-200 clay-sm transition-all w-full sm:w-auto justify-center flex items-center gap-2"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                <MessageCircle size={18} /> Chat on WhatsApp
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
