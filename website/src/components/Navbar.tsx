import { useState, useEffect } from "react"
import { Link, useLocation } from "react-router-dom"
import { motion, AnimatePresence } from "motion/react"
import { Menu, X } from "lucide-react"

const links = [
  { to: "/", label: "Home" },
  { to: "/about", label: "About" },
  { to: "/programs", label: "Programs" },
  { to: "/how-it-works", label: "How It Works" },
  { to: "/for-schools", label: "For Schools" },
]

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  const { pathname } = useLocation()

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20)
    window.addEventListener("scroll", onScroll)
    return () => window.removeEventListener("scroll", onScroll)
  }, [])

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled ? "bg-white shadow-md" : "bg-[#fffbf5]"
      }`}
    >
      <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        {/* Logo */}
        <Link to="/" className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-[#0ea5e9] flex items-center justify-center shadow-md">
            <span className="text-white font-black text-xl" style={{ fontFamily: "Nunito, sans-serif" }}>F</span>
          </div>
          <div>
            <span className="font-black text-xl text-gray-900 leading-none" style={{ fontFamily: "Nunito, sans-serif" }}>
              Find Your Voice
            </span>
            <p className="text-[10px] text-[#0ea5e9] font-bold uppercase tracking-widest leading-none mt-0.5">
              Youth Academy
            </p>
          </div>
        </Link>

        {/* Desktop links */}
        <div className="hidden md:flex items-center gap-6">
          {links.map((link) => (
            <Link
              key={link.to}
              to={link.to}
              className={`text-sm font-bold transition-colors rounded-full px-3 py-1.5 ${
                pathname === link.to
                  ? "bg-[#e0f2fe] text-[#0284c7]"
                  : "text-gray-600 hover:text-gray-900 hover:bg-gray-100"
              }`}
              style={{ fontFamily: "Nunito, sans-serif" }}
            >
              {link.label}
            </Link>
          ))}
          <Link to="/contact">
            <motion.button
              className="bg-[#0ea5e9] text-white px-6 py-2.5 rounded-full text-sm font-black shadow-lg shadow-sky-200 hover:bg-[#0284c7] transition-colors"
              style={{ fontFamily: "Nunito, sans-serif" }}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              Enroll Now ✨
            </motion.button>
          </Link>
        </div>

        {/* Mobile toggle */}
        <button
          className="md:hidden text-gray-700 w-10 h-10 flex items-center justify-center rounded-xl hover:bg-gray-100"
          onClick={() => setOpen(!open)}
        >
          {open ? <X size={22} /> : <Menu size={22} />}
        </button>
      </div>

      {/* Mobile menu */}
      <AnimatePresence>
        {open && (
          <motion.div
            key="mobile-menu"
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden bg-white border-t border-gray-100 overflow-hidden"
          >
            <div className="px-6 py-5 flex flex-col gap-2">
              {links.map((link) => (
                <Link
                  key={link.to}
                  to={link.to}
                  onClick={() => setOpen(false)}
                  className={`text-base font-bold py-2.5 px-4 rounded-xl ${
                    pathname === link.to
                      ? "bg-[#e0f2fe] text-[#0284c7]"
                      : "text-gray-600"
                  }`}
                  style={{ fontFamily: "Nunito, sans-serif" }}
                >
                  {link.label}
                </Link>
              ))}
              <Link
                to="/contact"
                onClick={() => setOpen(false)}
                className="bg-[#0ea5e9] text-white px-6 py-3 rounded-full text-base font-black text-center mt-2 shadow-lg shadow-sky-200"
                style={{ fontFamily: "Nunito, sans-serif" }}
              >
                Enroll Now ✨
              </Link>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  )
}
