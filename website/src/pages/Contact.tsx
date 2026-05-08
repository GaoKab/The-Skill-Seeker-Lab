import { useState } from "react"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import {
  Mail, Send, MessageCircle, MapPin, Phone, Zap,
  Users, Monitor,
  MessageSquare, Calendar, Ticket,
  DollarSign, CheckCircle2,
} from "lucide-react"

const bounce = { type: "spring" as const, stiffness: 300, damping: 15 }

function ClayIcon({
  icon: Icon,
  bg,
  border,
  color,
  size = "w-14 h-14",
}: {
  icon: React.ElementType
  bg: string
  border: string
  color: string
  size?: string
}) {
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

function PageHero() {
  return (
    <section className="relative bg-[#BFDBFE] pt-32 pb-20 px-6 overflow-hidden">
      {/* Decorative clay shapes */}
      <div className="absolute top-20 right-[12%] w-16 h-16 rounded-2xl bg-[#DDD6FE] border-2 border-[#C4B5FD] clay rotate-6 opacity-50" />
      <div className="absolute bottom-14 left-[8%] w-12 h-12 rounded-2xl bg-[#FDE68A] border-2 border-[#FCD34D] clay -rotate-12 opacity-50" />
      <div className="absolute top-40 left-[18%] w-10 h-10 rounded-xl bg-[#BBF7D0] border-2 border-[#86EFAC] clay rotate-12 opacity-40" />
      <div className="absolute bottom-24 right-[25%] w-14 h-14 rounded-2xl bg-[#FED7AA] border-2 border-[#FDBA74] clay -rotate-6 opacity-40" />

      <div className="max-w-4xl mx-auto relative z-10">
        <motion.span
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          className="inline-flex items-center gap-2 bg-white border-2 border-[#C7D2FE] rounded-2xl px-4 py-2 clay-sm mb-6"
        >
          <Mail className="w-4 h-4 text-[#4F46E5]" />
          <span className="text-gray-800 font-bold text-sm">Get in touch</span>
        </motion.span>

        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight"
        >
          Enroll your child or <span className="marker-blue">ask us anything</span>.
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-gray-700 max-w-2xl leading-relaxed"
        >
          Whether you're ready to enroll or just have questions — we're here. Fill out the form,
          WhatsApp us, or call. We respond within 24 hours.
        </motion.p>
      </div>
    </section>
  )
}

function ContactForm() {
  const [submitted, setSubmitted] = useState(false)

  if (submitted) {
    return (
      <section className="py-20 px-6 bg-[#fffbf5]">
        <div className="max-w-2xl mx-auto text-center">
          <FadeIn>
            <div className="bg-[#BBF7D0] border-3 border-[#86EFAC] rounded-3xl p-12 clay">
              <motion.div
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={bounce}
                className="w-24 h-24 rounded-3xl bg-[#BFDBFE] border-2 border-[#93C5FD] flex items-center justify-center clay-sm mx-auto mb-6"
              >
                <CheckCircle2 className="w-12 h-12 text-[#4F46E5]" />
              </motion.div>
              <h2 className="text-3xl font-black text-gray-900 mb-4">
                We've received your message!
              </h2>
              <p className="text-gray-600 text-lg leading-relaxed">
                Thank you for reaching out. A member of our team will get back to you within
                24 hours. If it's urgent, WhatsApp us directly.
              </p>
            </div>
          </FadeIn>
        </div>
      </section>
    )
  }

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-6xl mx-auto grid lg:grid-cols-5 gap-12">
        {/* Form */}
        <FadeIn className="lg:col-span-3">
          <div className="flex items-center gap-3 mb-8">
            <ClayIcon
              icon={Send}
              bg="bg-[#BFDBFE]"
              border="border-[#93C5FD]"
              color="text-[#4F46E5]"
              size="w-10 h-10"
            />
            <h2 className="text-2xl font-black text-gray-900">Send us a message</h2>
          </div>

          <form
            onSubmit={(e) => {
              e.preventDefault()
              setSubmitted(true)
            }}
            className="space-y-5"
          >
            <div className="grid sm:grid-cols-2 gap-5">
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-1.5">Your Name</label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Mpho Kabelo"
                  className="w-full border-2 border-[#C7D2FE] rounded-2xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#6366F1] bg-white clay-sm transition-colors"
                />
              </div>
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-1.5">Phone Number</label>
                <input
                  type="tel"
                  required
                  placeholder="+267 71 234 567"
                  className="w-full border-2 border-[#C7D2FE] rounded-2xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#6366F1] bg-white clay-sm transition-colors"
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-bold text-gray-700 mb-1.5">Email Address</label>
              <input
                type="email"
                required
                placeholder="your@email.com"
                className="w-full border-2 border-[#C7D2FE] rounded-2xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#6366F1] bg-white clay-sm transition-colors"
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-gray-700 mb-1.5">I'm interested in</label>
              <select
                required
                className="w-full border-2 border-[#C7D2FE] rounded-2xl px-4 py-3 text-gray-900 focus:outline-none focus:border-[#6366F1] bg-white clay-sm transition-colors"
              >
                <option value="">Select an option</option>
                <option value="young-speakers">🌱 Young Speakers (Ages 6-10)</option>
                <option value="rising-voices">🔥 Rising Voices (Ages 11-14)</option>
                <option value="future-leaders">👑 Future Leaders (Ages 15-18)</option>
                <option value="one-on-one">🎯 One-on-One Coaching</option>
                <option value="online">💻 Online Sessions</option>
                <option value="school">🏫 School Partnership</option>
                <option value="other">💬 General Inquiry</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-bold text-gray-700 mb-1.5">
                Child's Age (if enrolling)
              </label>
              <input
                type="text"
                placeholder="e.g. 12"
                className="w-full border-2 border-[#C7D2FE] rounded-2xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#6366F1] bg-white clay-sm transition-colors"
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-gray-700 mb-1.5">Your Message</label>
              <textarea
                rows={4}
                placeholder="Tell us about your child, your goals, or any questions you have..."
                className="w-full border-2 border-[#C7D2FE] rounded-2xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#6366F1] resize-none bg-white clay-sm transition-colors"
              />
            </div>

            <motion.button
              type="submit"
              className="w-full bg-[#F97316] text-white font-black py-4 rounded-2xl text-lg flex items-center justify-center gap-2 border-2 border-[#EA580C] clay-sm transition-colors"
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              transition={bounce}
            >
              Send Message <Send size={18} />
            </motion.button>
          </form>
        </FadeIn>

        {/* Sidebar */}
        <FadeIn className="lg:col-span-2" delay={0.15}>
          <div className="bg-white rounded-3xl border-2 border-[#C7D2FE] p-8 space-y-8 clay">
            {/* Contact Info */}
            <div>
              <h3 className="font-black text-lg text-gray-900 mb-4">Contact Information</h3>
              <ul className="space-y-4">
                <li className="flex items-start gap-3">
                  <ClayIcon
                    icon={MapPin}
                    bg="bg-[#FED7AA]"
                    border="border-[#FDBA74]"
                    color="text-[#EA580C]"
                    size="w-10 h-10"
                  />
                  <div>
                    <p className="text-gray-700 font-bold">Location</p>
                    <p className="text-gray-500 text-sm">Gaborone, Botswana</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <ClayIcon
                    icon={Phone}
                    bg="bg-[#BBF7D0]"
                    border="border-[#86EFAC]"
                    color="text-[#16a34a]"
                    size="w-10 h-10"
                  />
                  <div>
                    <p className="text-gray-700 font-bold">Phone</p>
                    <p className="text-gray-500 text-sm">+267 71 234 567</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <ClayIcon
                    icon={Mail}
                    bg="bg-[#BFDBFE]"
                    border="border-[#93C5FD]"
                    color="text-[#4F46E5]"
                    size="w-10 h-10"
                  />
                  <div>
                    <p className="text-gray-700 font-bold">Email</p>
                    <p className="text-gray-500 text-sm">hello@findyourvoice.co.bw</p>
                  </div>
                </li>
              </ul>
            </div>

            {/* WhatsApp */}
            <div className="border-t-2 border-[#E5E7EB] pt-6">
              <div className="flex items-center gap-2 mb-3">
                <MessageCircle className="w-5 h-5 text-[#25D366]" />
                <h3 className="font-black text-lg text-gray-900">Prefer WhatsApp?</h3>
              </div>
              <p className="text-gray-500 text-sm mb-4">
                Most parents find it easiest to reach us on WhatsApp. Tap below to start a
                conversation.
              </p>
              <motion.a
                href="https://wa.me/26771234567?text=Hi%2C%20I'm%20interested%20in%20Find%20Your%20Voice%20for%20my%20child."
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-center gap-2 bg-[#25D366] text-white font-black py-3 px-6 rounded-2xl transition-colors w-full border-2 border-[#20BD5A] clay-sm"
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                transition={bounce}
              >
                <MessageCircle size={18} />
                Chat on WhatsApp
              </motion.a>
            </div>

            {/* Response Time */}
            <div className="border-t-2 border-[#E5E7EB] pt-6">
              <div className="flex items-center gap-2 mb-3">
                <Zap className="w-5 h-5 text-[#F97316]" />
                <h3 className="font-black text-lg text-gray-900">Response Time</h3>
              </div>
              <p className="text-gray-500 text-sm">
                We respond to all inquiries within 24 hours. WhatsApp messages are usually answered
                within a few hours during business days.
              </p>
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

function FAQ() {
  const faqs: {
    icon: React.ElementType
    iconBg: string
    iconBorder: string
    iconColor: string
    cardBg: string
    cardBorder: string
    q: string
    a: string
  }[] = [
    {
      icon: Users,
      iconBg: "bg-[#BFDBFE]",
      iconBorder: "border-[#93C5FD]",
      iconColor: "text-[#4F46E5]",
      cardBg: "bg-[#BFDBFE]/30",
      cardBorder: "border-[#93C5FD]",
      q: "What age groups do you accept?",
      a: "We train children ages 6-18, divided into three programs: Young Speakers (6-10), Rising Voices (11-14), and Future Leaders (15-18).",
    },
    {
      icon: Calendar,
      iconBg: "bg-[#BBF7D0]",
      iconBorder: "border-[#86EFAC]",
      iconColor: "text-[#16a34a]",
      cardBg: "bg-[#BBF7D0]/30",
      cardBorder: "border-[#86EFAC]",
      q: "How long is the program?",
      a: "Each program runs for 6 months, divided into three phases: Foundation, Development, and Mastery. Many students continue into the next age track after completing.",
    },
    {
      icon: Ticket,
      iconBg: "bg-[#FDE68A]",
      iconBorder: "border-[#FCD34D]",
      iconColor: "text-[#b45309]",
      cardBg: "bg-[#FDE68A]/30",
      cardBorder: "border-[#FCD34D]",
      q: "Do you offer trial sessions?",
      a: "Yes! We offer a single trial session so your child can experience the format before committing. Contact us to book one.",
    },
    {
      icon: MessageSquare,
      iconBg: "bg-[#DDD6FE]",
      iconBorder: "border-[#C4B5FD]",
      iconColor: "text-[#7c3aed]",
      cardBg: "bg-[#DDD6FE]/30",
      cardBorder: "border-[#C4B5FD]",
      q: "What if my child is extremely shy?",
      a: "That's exactly who we're designed for. Our groups are small and supportive. We start with low-pressure exercises and build gradually. The shy ones often show the most dramatic transformation.",
    },
    {
      icon: Monitor,
      iconBg: "bg-[#FED7AA]",
      iconBorder: "border-[#FDBA74]",
      iconColor: "text-[#EA580C]",
      cardBg: "bg-[#FED7AA]/30",
      cardBorder: "border-[#FDBA74]",
      q: "Do you offer online sessions?",
      a: "Yes. We run online sessions via Zoom for families outside Gaborone. Same structure, same facilitators, same results — just delivered remotely.",
    },
    {
      icon: DollarSign,
      iconBg: "bg-[#BBF7D0]",
      iconBorder: "border-[#86EFAC]",
      iconColor: "text-[#16a34a]",
      cardBg: "bg-[#BBF7D0]/30",
      cardBorder: "border-[#86EFAC]",
      q: "How much does it cost?",
      a: "Pricing depends on the program and format (group, one-on-one, or online). Contact us for current pricing and payment plan options.",
    },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#7c3aed] uppercase tracking-widest mb-4 text-center">
            FAQ
          </p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14">
            Frequently Asked <span className="marker-purple">Questions</span>
          </h2>
        </FadeIn>

        <div className="space-y-4">
          {faqs.map((faq, i) => (
            <FadeIn key={faq.q} delay={i * 0.06}>
              <motion.div
                className={`${faq.cardBg} p-6 rounded-2xl border-2 ${faq.cardBorder} clay-sm`}
                whileHover={{ scale: 1.01, y: -2 }}
                transition={bounce}
              >
                <h3 className="font-black text-gray-900 mb-2 flex items-center gap-3">
                  <div
                    className={`w-9 h-9 rounded-xl ${faq.iconBg} border-2 ${faq.iconBorder} flex items-center justify-center clay-sm shrink-0`}
                  >
                    <faq.icon className={`w-4 h-4 ${faq.iconColor}`} />
                  </div>
                  {faq.q}
                </h3>
                <p className="text-gray-500 leading-relaxed pl-12">{faq.a}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

export default function Contact() {
  return (
    <>
      <PageHero />
      <ContactForm />
      <FAQ />
    </>
  )
}
