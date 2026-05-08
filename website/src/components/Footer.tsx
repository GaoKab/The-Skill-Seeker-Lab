import { Link } from "react-router-dom"
import { Mic, MapPin, Phone, Mail, Heart } from "lucide-react"

export default function Footer() {
  return (
    <footer className="bg-[#EEF2FF] border-t-3 border-[#C7D2FE]">
      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="grid md:grid-cols-4 gap-10">
          <div className="md:col-span-1">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-2xl bg-[#818CF8] border-2 border-[#6366F1] flex items-center justify-center clay-sm">
                <Mic className="w-5 h-5 text-white" />
              </div>
              <span className="font-bold text-xl text-gray-900">Find Your Voice</span>
            </div>
            <p className="text-sm leading-relaxed text-gray-500">
              Building Botswana's next generation of confident communicators, critical thinkers, and young leaders.
            </p>
          </div>

          <div>
            <h4 className="font-bold text-gray-900 mb-4">Quick Links</h4>
            <ul className="space-y-2.5 text-sm">
              {[
                { to: "/about", label: "About Us" },
                { to: "/programs", label: "Programs" },
                { to: "/how-it-works", label: "How It Works" },
                { to: "/for-schools", label: "For Schools" },
                { to: "/contact", label: "Enroll" },
              ].map((l) => (
                <li key={l.to}><Link to={l.to} className="text-gray-500 hover:text-[#4F46E5] transition-colors">{l.label}</Link></li>
              ))}
            </ul>
          </div>

          <div>
            <h4 className="font-bold text-gray-900 mb-4">Programs</h4>
            <ul className="space-y-2.5 text-sm">
              {[
                "Young Speakers (6–10)",
                "Rising Voices (11–14)",
                "Future Leaders (15–18)",
                "School Partnerships",
                "One-on-One Coaching",
              ].map((p) => (
                <li key={p}><Link to="/programs" className="text-gray-500 hover:text-[#4F46E5] transition-colors">{p}</Link></li>
              ))}
            </ul>
          </div>

          <div>
            <h4 className="font-bold text-gray-900 mb-4">Get In Touch</h4>
            <ul className="space-y-3 text-sm text-gray-500">
              <li className="flex items-start gap-2"><MapPin size={16} className="mt-0.5 shrink-0 text-[#818CF8]" /><span>Gaborone, Botswana</span></li>
              <li className="flex items-center gap-2"><Phone size={16} className="shrink-0 text-[#818CF8]" /><span>+267 71 234 567</span></li>
              <li className="flex items-center gap-2"><Mail size={16} className="shrink-0 text-[#818CF8]" /><span>hello@findyourvoice.co.bw</span></li>
            </ul>
          </div>
        </div>

        <div className="border-t-2 border-[#C7D2FE] mt-12 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-sm text-gray-400 flex items-center gap-1">
            &copy; {new Date().getFullYear()} Find Your Voice Academy. Made with <Heart size={12} className="text-red-400 fill-red-400" /> in Botswana.
          </p>
          <p className="text-sm text-gray-400">Founded by Mpho Kabelo</p>
        </div>
      </div>
    </footer>
  )
}
