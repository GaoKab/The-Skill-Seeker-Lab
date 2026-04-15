import { Link } from "react-router-dom"
import { MapPin, Phone, Mail, Heart } from "lucide-react"

export default function Footer() {
  return (
    <footer className="bg-gray-900 text-gray-300">
      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="grid md:grid-cols-4 gap-10">
          {/* Brand */}
          <div className="md:col-span-1">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-2xl bg-[#0ea5e9] flex items-center justify-center">
                <span className="text-white font-black text-xl" style={{ fontFamily: "Nunito, sans-serif" }}>F</span>
              </div>
              <span className="font-black text-xl text-white" style={{ fontFamily: "Nunito, sans-serif" }}>
                Find Your Voice
              </span>
            </div>
            <p className="text-sm leading-relaxed text-gray-400">
              Building Botswana's next generation of confident communicators,
              critical thinkers, and young leaders. 🇧🇼
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-black text-white mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>Quick Links</h4>
            <ul className="space-y-2.5 text-sm">
              <li><Link to="/about" className="hover:text-[#38bdf8] transition-colors">About Us</Link></li>
              <li><Link to="/programs" className="hover:text-[#38bdf8] transition-colors">Programs</Link></li>
              <li><Link to="/how-it-works" className="hover:text-[#38bdf8] transition-colors">How It Works</Link></li>
              <li><Link to="/for-schools" className="hover:text-[#38bdf8] transition-colors">For Schools</Link></li>
              <li><Link to="/contact" className="hover:text-[#38bdf8] transition-colors">Enroll</Link></li>
            </ul>
          </div>

          {/* Programs */}
          <div>
            <h4 className="font-black text-white mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>Programs</h4>
            <ul className="space-y-2.5 text-sm">
              <li><Link to="/programs" className="hover:text-[#38bdf8] transition-colors">🌱 Young Speakers (6–10)</Link></li>
              <li><Link to="/programs" className="hover:text-[#38bdf8] transition-colors">🔥 Rising Voices (11–14)</Link></li>
              <li><Link to="/programs" className="hover:text-[#38bdf8] transition-colors">👑 Future Leaders (15–18)</Link></li>
              <li><Link to="/programs" className="hover:text-[#38bdf8] transition-colors">🏫 School Partnerships</Link></li>
              <li><Link to="/programs" className="hover:text-[#38bdf8] transition-colors">🎯 One-on-One Coaching</Link></li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="font-black text-white mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>Get In Touch</h4>
            <ul className="space-y-3 text-sm">
              <li className="flex items-start gap-2">
                <MapPin size={16} className="mt-0.5 shrink-0 text-[#38bdf8]" />
                <span>Gaborone, Botswana</span>
              </li>
              <li className="flex items-center gap-2">
                <Phone size={16} className="shrink-0 text-[#38bdf8]" />
                <span>+267 71 234 567</span>
              </li>
              <li className="flex items-center gap-2">
                <Mail size={16} className="shrink-0 text-[#38bdf8]" />
                <span>hello@findyourvoice.co.bw</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-sm text-gray-500 flex items-center gap-1">
            &copy; {new Date().getFullYear()} Find Your Voice Academy. Made with <Heart size={12} className="text-red-400 fill-red-400" /> in Botswana.
          </p>
          <p className="text-sm text-gray-500">
            Founded by Mpho Kabelo
          </p>
        </div>
      </div>
    </footer>
  )
}
