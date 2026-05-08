import { useState } from "react"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import { MessageCircle, Send } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-[#dbeafe] pt-32 pb-20 px-6 overflow-hidden">
      <div className="absolute top-20 right-[12%] w-14 h-14 rounded-full bg-[#93c5fd]/30" />
      <div className="absolute bottom-14 left-[8%] w-10 h-10 rounded-xl bg-[#fbbf24]/20 rotate-12" />
      <div className="absolute top-32 right-[28%] text-3xl text-[#bfdbfe]/50 font-black rotate-45 select-none">✦</div>
      <div className="max-w-4xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="inline-block bg-white text-gray-800 font-black text-sm px-4 py-2 rounded-full rotate-1 shadow-sm mb-6">👋 Get in touch</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}
        >
          Enroll your child or <span className="marker-blue">ask us anything</span>.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-gray-600 max-w-2xl leading-relaxed"
        >
          Whether you're ready to enroll or just have questions — we're here. Fill out the form, WhatsApp us, or call. We respond within 24 hours.
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
            <span className="text-6xl block mb-4">🎉</span>
            <h2 className="text-3xl font-black text-gray-900 mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>We've received your message!</h2>
            <p className="text-gray-500 text-lg">Thank you for reaching out. A member of our team will get back to you within 24 hours. If it's urgent, WhatsApp us directly.</p>
          </FadeIn>
        </div>
      </section>
    )
  }

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-6xl mx-auto grid lg:grid-cols-5 gap-12">
        <FadeIn className="lg:col-span-3">
          <h2 className="text-2xl font-black text-gray-900 mb-8" style={{ fontFamily: "Nunito, sans-serif" }}>Send us a message 📩</h2>
          <form onSubmit={(e) => { e.preventDefault(); setSubmitted(true) }} className="space-y-5">
            <div className="grid sm:grid-cols-2 gap-5">
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-1.5">Your Name</label>
                <input type="text" required placeholder="e.g. Mpho Kabelo" className="w-full border-[3px] border-dashed border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#f97316] bg-white transition-colors" />
              </div>
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-1.5">Phone Number</label>
                <input type="tel" required placeholder="+267 71 234 567" className="w-full border-[3px] border-dashed border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#f97316] bg-white transition-colors" />
              </div>
            </div>
            <div>
              <label className="block text-sm font-bold text-gray-700 mb-1.5">Email Address</label>
              <input type="email" required placeholder="your@email.com" className="w-full border-[3px] border-dashed border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#f97316] bg-white transition-colors" />
            </div>
            <div>
              <label className="block text-sm font-bold text-gray-700 mb-1.5">I'm interested in</label>
              <select required className="w-full border-[3px] border-dashed border-gray-200 rounded-xl px-4 py-3 text-gray-900 focus:outline-none focus:border-[#f97316] bg-white transition-colors">
                <option value="">Select an option</option>
                <option value="young-speakers">🌱 Young Speakers (Ages 6–10)</option>
                <option value="rising-voices">🔥 Rising Voices (Ages 11–14)</option>
                <option value="future-leaders">👑 Future Leaders (Ages 15–18)</option>
                <option value="one-on-one">🎯 One-on-One Coaching</option>
                <option value="online">💻 Online Sessions</option>
                <option value="school">🏫 School Partnership</option>
                <option value="other">💬 General Inquiry</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-bold text-gray-700 mb-1.5">Child's Age (if enrolling)</label>
              <input type="text" placeholder="e.g. 12" className="w-full border-[3px] border-dashed border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#f97316] bg-white transition-colors" />
            </div>
            <div>
              <label className="block text-sm font-bold text-gray-700 mb-1.5">Your Message</label>
              <textarea rows={4} placeholder="Tell us about your child, your goals, or any questions you have..." className="w-full border-[3px] border-dashed border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder:text-gray-400 focus:outline-none focus:border-[#f97316] resize-none bg-white transition-colors" />
            </div>
            <motion.button
              type="submit"
              className="w-full bg-[#f97316] hover:bg-[#ea580c] text-white font-black py-4 rounded-full text-lg flex items-center justify-center gap-2 shadow-lg shadow-orange-200 transition-colors"
              style={{ fontFamily: "Nunito, sans-serif" }}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              Send Message <Send size={18} />
            </motion.button>
          </form>
        </FadeIn>

        <FadeIn className="lg:col-span-2" delay={0.15}>
          <div className="bg-white rounded-3xl border-[3px] border-dashed border-gray-200/60 p-8 space-y-8">
            <div>
              <h3 className="font-black text-lg text-gray-900 mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>Contact Information</h3>
              <ul className="space-y-4">
                <li className="flex items-start gap-3">
                  <span className="text-xl">📍</span>
                  <div><p className="text-gray-700 font-bold">Location</p><p className="text-gray-500 text-sm">Gaborone, Botswana</p></div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-xl">📞</span>
                  <div><p className="text-gray-700 font-bold">Phone</p><p className="text-gray-500 text-sm">+267 71 234 567</p></div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-xl">✉️</span>
                  <div><p className="text-gray-700 font-bold">Email</p><p className="text-gray-500 text-sm">hello@findyourvoice.co.bw</p></div>
                </li>
              </ul>
            </div>
            <div className="border-t-2 border-dashed border-gray-100 pt-6">
              <h3 className="font-black text-lg text-gray-900 mb-3" style={{ fontFamily: "Nunito, sans-serif" }}>Prefer WhatsApp? 💬</h3>
              <p className="text-gray-500 text-sm mb-4">Most parents find it easiest to reach us on WhatsApp. Tap below to start a conversation.</p>
              <motion.a
                href="https://wa.me/26771234567?text=Hi%2C%20I'm%20interested%20in%20Find%20Your%20Voice%20for%20my%20child."
                target="_blank" rel="noopener noreferrer"
                className="flex items-center justify-center gap-2 bg-[#25D366] hover:bg-[#20bd5a] text-white font-black py-3 px-6 rounded-full transition-colors w-full shadow-md shadow-green-200"
                style={{ fontFamily: "Nunito, sans-serif" }}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                <MessageCircle size={18} />
                Chat on WhatsApp
              </motion.a>
            </div>
            <div className="border-t-2 border-dashed border-gray-100 pt-6">
              <h3 className="font-black text-lg text-gray-900 mb-3" style={{ fontFamily: "Nunito, sans-serif" }}>Response Time ⚡</h3>
              <p className="text-gray-500 text-sm">We respond to all inquiries within 24 hours. WhatsApp messages are usually answered within a few hours during business days.</p>
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

function FAQ() {
  const faqs = [
    { emoji: "👧", q: "What age groups do you accept?", a: "We train children ages 6–18, divided into three programs: Young Speakers (6–10), Rising Voices (11–14), and Future Leaders (15–18)." },
    { emoji: "📅", q: "How long is the program?", a: "Each program runs for 6 months, divided into three phases: Foundation, Development, and Mastery. Many students continue into the next age track after completing." },
    { emoji: "🎟️", q: "Do you offer trial sessions?", a: "Yes! We offer a single trial session so your child can experience the format before committing. Contact us to book one." },
    { emoji: "🤫", q: "What if my child is extremely shy?", a: "That's exactly who we're designed for. Our groups are small and supportive. We start with low-pressure exercises and build gradually. The shy ones often show the most dramatic transformation." },
    { emoji: "💻", q: "Do you offer online sessions?", a: "Yes. We run online sessions via Zoom for families outside Gaborone. Same structure, same facilitators, same results — just delivered remotely." },
    { emoji: "💰", q: "How much does it cost?", a: "Pricing depends on the program and format (group, one-on-one, or online). Contact us for current pricing and payment plan options." },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#7c3aed] uppercase tracking-widest mb-4 text-center">FAQ</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Frequently Asked <span className="marker-purple">Questions</span> 🤔
          </h2>
        </FadeIn>
        <div className="space-y-4">
          {faqs.map((faq, i) => (
            <FadeIn key={faq.q} delay={i * 0.06}>
              <div className="bg-[#fffbf5] p-6 rounded-2xl border-[3px] border-dashed border-gray-200/60">
                <h3 className="font-black text-gray-900 mb-2 flex items-center gap-2" style={{ fontFamily: "Nunito, sans-serif" }}>
                  <span>{faq.emoji}</span> {faq.q}
                </h3>
                <p className="text-gray-500 leading-relaxed">{faq.a}</p>
              </div>
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
